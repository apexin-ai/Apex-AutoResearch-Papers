# director / loop_4.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`97197af6ffaff1463b0e.json`](../../sessions/97/97197af6ffaff1463b0e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T14:24:37+00:00'
---

## ratekv Director Handoff — 2026-05-14

### 当前状态
项目处于 **Paper Writing + 审稿阶段**，投稿目标 EMNLP 2026 Main（ARR May 25, 距今 11 天）。全章节初稿已完成（refinement round 2），Paper Agent 正在 Step 5 迭代精修。审稿团队（Group C）已在独立审稿。

### 实验完成度
- P0 (8/8) ✅ 全部完成
- P1 (7/7) ✅ 全部完成
- P2 (1/1) ⏸ Deferred（plan_013 70B/72B profiling，D039/D043 决定 defer，磁盘空间不足 + 仅增一个数据点）
- 总计 57 个实验，30 成功，10 负向，6 失败，1 运行中（gemma2_9b_full_pipeline），5 待处理

### 三个核心 Claims 全部有证据支撑
1. **Heterogeneity-dependent**: 3 模型 Top-5% concentration，multi-seed std=0.06
2. **Constraint is THE contribution**: Solver Δ=0.0000，oracle 0/28 改进，greedy=MCKP
3. **Practical diagnostic**: Top-5% > 0.50 rule，C4 agreement 96.4%

### 运行中 / 待处理
- **gemma2_9b_full_pipeline** — 正在运行（扩展到第四个模型家族）
- **待处理队列**：multi_seed_lowres（等审批）、yi15_9b_full_pipeline（等提交）、qwen72b_profiling（已 defer D043）、greedy_constrained_ablation、cross_domain_calibration_v2

### 论文 Patch 队列 (D040)
- [ ] Multi-seed error bars (±0.06) → Table 1 + §4.2
- [ ] Oracle comparison (0/28) → §3.5 or §4.2
- [ ] C4 cross-dataset (96.4% agreement) → 解冻 §4.5
- [x] KV separation ablation → §5.5 已写入
- ❌ Runtime latency 不放入正文 (D038)

### 关键决策历史
- D043: 72B profiling 正式 defer（磁盘）
- D042/D041: Table 4 heuristic baselines 必须用 per-model optimal k，校正后 gap 缩小但 MCKP 仍优
- D040: Patch 批次定义
- D039: 70B profiling defer（论文是关键路径）
- D038: Runtime benchmark 不入正文（simulated quantization 无优化 kernel）
- D037: Table 1 使用 per-model optimal k

### GPU 资源
westd-37397: 2× RTX PRO 6000 96GB。gemma2_9b_full_pipeline 占用中。Agent 队列当前空闲。

### 接手后优先事项
1. 检查 gemma2_9b_full_pipeline 运行状态——这是扩展到第四个模型的关键实验
2. 确认 Paper Agent Step 5 精修进展，确保 D040 patch 批次已经/正在被处理
3. multi_seed_lowres 在等审批，评估是否还需要（可能已被 multi_seed_error_bars 覆盖）
4. 距 ARR DDL 11 天，论文精修和审稿反馈处理是关键路径
5. yi15_9b_full_pipeline 脚本已写好（`run_yi15_full_pipeline.py`），等 GPU 空出可提交

### 注意事项
- 论文 §5.3-5.5 已移到 appendix（commit 9b16d41）
- paper_provenance 覆盖率 38/38，所有 claim 有实验溯源
- 审稿阶段 GPU 不能空——gemma2 跑完后立即安排下一个（yi15 或其他）
- memory.md 有详细的经验教训，特别是关于 eval pipeline 一致性、bf16 vs fp16、per-model optimal k 等


---
