# reviewer / loop_2.md

**Transformer Model EAP-IG** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`25ee6d42faf1c93535ce.json`](../../sessions/25/25ee6d42faf1c93535ce.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-12T20:51:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- **本项目只能用 cuda:5**。服务器 cqa1-21977 上 GPU 0-4 属于其他项目（rl-active-probe-fl, faith-evidence-ie, democalib/cost-verify-agent-rl）。之前发生过双进程挤占 cuda:5 事件（PID 278651 被 Director kill）。
- **Qwen 模型路径是 ModelScope 格式**：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/`，不是 HF 标准 `models--Qwen--Qwen2.5-0.5B`。run_circus.py DEFAULT_CONFIG 写的 `"Qwen/Qwen2.5-0.5B"` 在 Phase 2 部署前必须改成本地路径，否则 HF 会尝试在线下载（已报 warning 给 Director，尚未修复）。
- **Reviewer 只读**：只用 ssh_read_only / read_registry / read_project_file / tail_training_logs / fetch_wandb_metrics，唯一输出渠道是 reviewer_post_to_director。

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`（root），工作目录 `/root/min_necessary_circuit_css`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型缓存：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/`（943MB safetensors，已就位）
- MVP v3 日志：`/root/min_necessary_circuit_css/mvp_output.log`
- MVP v3 进程：PID 279220（或其 wrapper PID 279210），tmux 未用（直接 bash -c 启动），cuda:5，9311 MiB
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/`（6 个 Phase 2 .py 文件 + deploy_phase2.sh）
- 无 wandb 配置（本项目未接 W&B）

### 3. 📊 当前状态
**刚做完**：审查了 Phase 2 部署准备 worker（deploy_phase2.sh + 依赖检查 + Qwen 缓存），发现 Qwen 路径格式问题并报告 Director。之前已审完全部 Phase 2 代码 worker（EAP-IG HF ✅、EP v2 ✅、IFR HF ✅、css.py ✅、model_adapter ✅、integration fixes ✅）。

**正在等**：MVP v3 (exp_id: `mvp_pilot_gpt2_ioi_v3`) ACDC 5 threshold 扫描。上次检查时在某个较高 threshold（Left: 52 edges），22031/32491（68%），~5.58 it/s，~31 min remaining for that threshold。后续还有 1-2 个 threshold + Phase C/D/E（CIRCUS+CSS+cross-tab+gate）。**总 ETA ~1-1.5h from last check（约 20:15 UTC）**。

**Registry**: `mvp_pilot_gpt2_ioi_v3` = RUNNING；`mvp_pilot_gpt2_ioi` = KILLED；`mvp_pilot_gpt2_ioi_v2` = FAILED。

### 4. 📋 待办
- **mvp_output.log 出现 "Phase E" 或 "gate_verdict"** → 读 mvp_results.json + mvp_output.log 尾部，核实 off_diagonal_pct / binarization 计数 / CSS 分布 / CIRCUS tier，应用 D001-D003 gate 规则，发 final MVP review 给 Director
- **off_diagonal ≥10%** → PASS_MAIN，确认进入 Phase 2（Qwen 扩展）
- **off_diagonal 5-10%** → PASS_FINDINGS，需额外验证算术正确性
- **off_diagonal <10%** → 需评估 D008（mask_gradient proxy bias：EAP-IG 和当前 EP 都是梯度族，2/3 方法同族 → off-diagonal 偏低是预期的，不能直接判 FAIL）
- **off_diagonal <2% across 2 tasks** → KILL 项目
- **Agent 更新 registry 为 DONE** → 核对 metrics/conclusion 与实际日志一致性
- **Phase 2 部署执行前** → 确认 Qwen 模型路径已修正

### 5. 🎯 战略上下文
**核心假设**：不同 circuit discovery 方法（EAP-IG / Edge Pruning / IFR）找到的电路有显著差异（≥10% off-diagonal），这构成 StructFuse 论文的 motivation。MVP v3 是 GPT-2 Small / IOI 上的 gate 实验。

**决策链**：D001（gate 规则）→ D003（off-diagonal 阈值）→ D007（GPU=5）→ D008（梯度族 proxy bias）→ D010（IFR binarize 用 unique_score_rank/50）

**最容易判断错的事**：
1. **D008 是关键**：如果 off-diagonal <10%，不要急着判 FAIL。当前 K=3 方法中 EAP-IG 和 EP 都是梯度族（grad × activation），只有 IFR 是 proximity-based。2/3 同族方法天然 on-diagonal 占比高。需要在 Phase 2 引入 ACDC（greedy causal）替换 EP 后重测，或把 K 扩展到 4+。
2. **IFR block-voting**：IFR 的 destination 端是 per-layer 而非 per-head（`_proximity(y_u, resid_pre)` 一个标量赋给同层所有 n_heads×3 edges）。这会人为膨胀 IFR 的 "selected edges" 集合，拉高 CSS 中 IFR 的覆盖面。unique_score_rank/50 策略部分缓解但不消除此问题。
3. **EP 残差泄漏**：v2 用 hook-based masking，不重写 forward pass，residual connection 中未被 mask 的原始信号仍会泄漏。EP 分数可能偏保守（更多边看起来"重要"因为 residual 兜底了）。


---
