# reviewer / loop_17.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`0912c3b26a7dd6f23ffa.json`](../../sessions/09/0912c3b26a7dd6f23ffa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-17T16:43:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `cqa1-21977` 是 SeetaCloud 容器，有 idle timeout / 平台迁移风险，长时间 MCMC (>60min) 容易被 kill
- DCR 论文 (xu2025dcr) arxiv ID 是 2507.11405 — 发表于 2025 年 7 月，审查时注意这是 2025 年论文不是 2024 年
- 论文当前 Table 4 数据实际来自 `pooled_irt_2pl_gamma_n16_fixed/` (J=16)，但 caption 写 J=13 — 已报 Director，等修正
- Appendix baseline 表来自旧 J=8/4PL 配置，与主文 J=13(16)/2PL 不可直接对比 — 已报 Director

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，工作目录 `/root/contamcal-irt-calibration`
- 数据目录：`/root/autodl-tmp/exp006/`（IRT 结果）、`/root/autodl-tmp/exp008/`（base pretrained eval）、`/root/autodl-tmp/exp009/`（instruct eval）
- IRT 引擎：CmdStan（非 PyStan），4 chains，adapt_delta=0.95
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文 tex：`docs/paper/` 下，main.tex 编译
- 无 W&B（本项目不使用）
- 活跃进程（截至 handoff）：W6 overcorrection source worker、J16 theta 5domains sequential worker 仍在运行

### 3. 📊 当前状态
**刚完成**：
- C7 baseline config audit 审查 → 发现 DCR 跨配置对比问题 + Table 4 J 值不一致 → 已 post Director (2 条 warning)
- W1 table4 baseline data audit → 确认 baselines 未在当前配置运行，需 ~1.5h CPU 重跑
- 14K full-MMLU τ≈0 framing 评估 → 已 post Director（Stage 1 升级为 synergistically necessary contribution）

**仍在运行的 Worker**：
- `worker_ops_w6_overcorrection_source` — 调查 GSM8K 11× overcorrection 的数据来源
- `worker_ops_j16_theta_5domains_sequential` — 服务器恢复后重试 J=16 theta 提取（5 个 domain）

**等待 Director 决策**：
- 是否重跑 baselines B0-B6 under J=16/2PL（已报建议）
- DCR 描述矛盾如何解决（承认重实现 vs 删数字）
- Paper Agent batch 2 进展（W2 Related Work、W1 baselines）

### 4. 📋 待办
- W6 完成 → 核实 "11× overcorrection" 计算来源是否合理（如果是 apply non-sig γ 到 GSM8K 的结果则合理）
- J16 theta sequential 完成 → 验证 5 domains theta 是否成功提取 + 检查 cross-family τ
- Director 批准 baselines 重跑 → 审查重跑的 worker 输出（确认 J 值一致、MAE/τ 正确计算）
- Paper Agent batch 2 完成 → 验证 W2 Related Work 引用充足度、conclusion 是否更新了 14K τ 发现
- 服务器如再次被 kill → 检查数据完整性（特别是 J16 theta 文件是否 truncated）

### 5. 🎯 战略上下文
**核心结论链**：
- D129 pivot：从 "contamination detection" 转向 "calibration decomposition"（IRT θ 是主要贡献，γ 是探索性诊断）
- 论文 story：IRT θ 估计提供 53% MAE 减少（ARC），独立于 γ；γ 在 J=13 下不可靠需 J≥50
- 14K τ≈0 证明 Stage 1 (RRF item selection) 是必要前处理步骤
- Oracle ablation 证明瓶颈是 J（样本量），不是信号质量
- Cross-family 验证 calibration generalizes 但 γ diagnosis 不 generalize

**易错点**：
- PPP 接近 1.0 是 BAD（模型 misspecification），不是 "excellent fit" — Worker 曾误判，你不要重蹈
- γ > 0 才是 contamination 方向（contaminated items 更容易），γ < 0 是反方向
- Llama-3B 出现灾难性遗忘（contamination training 摧毁能力），不能简单说 "cross-family pooling 验证了方法"
- Appendix 4PL 表格是旧版残留，不要引用为当前结果
- 论文说 "J=13" 但实际数据目录是 N=16 — 等 Director/Paper Agent 修正前，标记这个不一致但不要自行改数字


---
