# reviewer / loop_2.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`b33929cd0ec68cf88e38.json`](../../sessions/b3/b33929cd0ec68cf88e38.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-15T14:07:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19183 上只能用 cuda:0 和 cuda:1（2×RTX PRO 6000）
- 所有大文件必须在 `/root/autodl-tmp/vla-ssd/`，根分区仅 ~30GB
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要创建 venv
- `vla_mean_rho` 在 `compute_judgment()` 中有 bug：用 `rho_vla_pt.max()` 不排除坍塌层（得 0.9562/L3 而非 0.9550/L4），当前不影响 verdict 但边界情况会出错
- DINO subtask AUC=0.9717 来自 auto-extracted labels（非 BDDL predicates），引用时要注意区分

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，代码 `/root/vla-ssd`，数据 `/root/autodl-tmp/vla-ssd/`
- Python：`/root/miniconda3/bin/python`（conda base env）
- Features：`/root/autodl-tmp/vla-ssd/features/{trained,untrained}/`（各 10 H5，~57GB/model，33层×4096dim fp16）
- Results：`/root/autodl-tmp/vla-ssd/results/{trained,untrained,dinov2,analysis}/temporal_distance/`
- Verdict：`/root/autodl-tmp/vla-ssd/results/analysis/summary.json`（clean verdict，时间戳 21:53 UTC）
- 活跃进程：mvp_controlb_trained (PID 608744/608749, tmux, cuda:0) + mvp_controlb_untrained (PID 608886/608891, tmux, cuda:1)——bash PID 与 python PID 差 5
- 无 wandb 配置，不检查 wandb

### 3. 📊 当前状态
**刚完成**：
- Clean verdict 审查 PASS（best_layer=4, Δρ=0.043, FAIL confirmed）
- Subtask predicate feasibility 审查（结论：不可行，LIBERO predicates 视觉可辨）
- D009 ROADMAP 审查（pivot to action prediction probe，标了两个遗漏攻击面）

**RUNNING**：
- `mvp_controlb_trained`：Control B label permutation on trained features，~33 层，约 21:50 开始，预计很快完成
- `mvp_controlb_untrained`：同上 on untrained features

**等待中**：
- Control B 完成回调 → 需审查（预期 ρ≈0 验证 probe 方法论）
- `worker_code_action-prediction-probe-prep` 已完成（status=done）但 find 未发现新 .py 文件——**可能只是设计文档而非代码提交，需要确认实际产出**
- 两个并行 research workers（文献调研 + 技术设计）可能随时完成
- Director 待决：action prediction probe 方向 go/no-go

### 4. 📋 待办
- Control B 完成通知 → 验证 ρ≈0（所有层 |ρ| < 0.05）→ 如有异常层 ρ > 0.1 则 CRITICAL
- Action prediction probe 代码提交 → 审查 train_probes.py 改动：(1) action regression 实现正确性 (2) key mismatch bug 是否修复（VLA features 用 `demo_X`，旧 subtask labels 用 `traj_X`）(3) LIBERO HDF5 action 格式（7-DoF）是否正确解析
- Action probe 实验启动 → GPU 合规检查 + 验证 features 复用（不应重新提取）
- 文献调研 worker 完成 → 审查"VLA probing"领域是否有直接竞争工作
- Director 要求 CoRL go/no-go 评估 → 基于 action probe 结果 + story 强度给出审查意见

### 5. 🎯 战略上下文
**决策链**：D001(标准校准) → D002(per-task mean) → D003(移除 subtask gate) → D004-D006(DINO 阈值修正 0.554→0.901) → D007(MVP FAIL) → D008(clean verdict) → D009(subtask terminated, pivot to action probe)

**核心结论**：temporal distance 信号由 SigLIP vision encoder 主导（untrained ρ=0.933 vs trained ρ=0.955），VLA LLM 训练仅贡献 Δρ≈0.04。LIBERO 作为 testbed 的结构性限制：tabletop manipulation 的 task progress 全部视觉可达。

**易错点**：
1. **不要把 DINO 旧 metrics 当真**——dinov2_baseline registry 的 temporal distance metrics（pooled ρ=0.833, per-task=0.554）已 invalidated，新值 per-task=0.901。但 subtask AUC=0.9717 仍有效（不同方法，不受 pair sampling 影响）
2. **registry 的 mvp_probe_trained 有两套数值混用历史**——早期 best_layer=3/collapsed=10 是 raw probe 值，现在已修正为 verdict 值（best_layer=4/collapsed=16）。如果看到旧值要警惕
3. **Action prediction probe 的两个审稿人攻击面**已发给 Director 但尚未得到回应：(a)"VLA 预测 action 是 trivial" (b)"为什么不直接用 VLA 的 action head"
4. **memory.md 中 DINO 旧值 0.554 标注**——已在 memory.md 中更新为 0.901，但如果看到其他文档残留旧值要标 warning


---
