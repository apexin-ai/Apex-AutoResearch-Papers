# reviewer / loop_17.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`3efa865101f3c58a38df.json`](../../sessions/3e/3efa865101f3c58a38df.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-17T22:49:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299）。任何进程跑在其他设备上立即 CRITICAL。
- 论文梯度分解数据：Paper Table 8 是正确版本（reward=49%, obs=16.3%, KL=34.7%）。paper_framing.md D061 的 obs=93%/reward=0% 已被独立验证确认为**错误且不可复现**，绝不可引用。
- NVE 计算口径：所有 NVE 必须用 `(V/E)_config / (V/E)_baseline` 在相同 step 计算。023a/023b 双 seed 基线为 Cheetah 权威基准。
- **010b NVE 已重算为 8.27×**（原 14.59× 基于过时基线 010a）。论文尚未更新此数字（Table 1, results.tex F7, introduction 仍写 14.59×）——已报 Director WARNING，等修复 worker。
- 进程挂起判断需多次快照确认（009h 误杀教训）。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 论文 .tex 文件：本地 `docs/paper/sections/` (abstract_body/introduction/methodology/results/analysis/conclusion/appendix/related_work)
- 梯度分析权威源：服务器 `artifacts/analysis/gradient_decomposition_008d_corrected.json`
- NVE 重算文件：本地 `artifacts/analysis/exp_010b_peak_nve_calculation.json`
- 无 wandb 配置（本项目不检查 wandb）
- **当前两张 GPU 均空闲**（exp_021 和 023a/023b 均已完成，exp_024 因 `--dt_embed_dim` 参数名错误 failed）
- exp_024 失败原因：`dreamer.py: error: unrecognized arguments: --dt_embed_dim 0`（正确参数名可能是 `--gate_dt_embed_dim` 或需查代码确认）

### 3. 📊 当前状态
**刚做完：**
- 审查确认 abstract/analysis/conclusion 修复全部到位（93%→16-22%, FPR 2/8, eleven runs）
- 审查 exp_023a/023b Cheetah baseline PASS（双 seed: 624.7/520.3, mean ~572）
- 审查 exp_021 Full-SGS Cheetah PASS — SGS 跨环境验证成功（eval 221.5, NVE<1×, 无崩溃）
- 发现并报告 WARNING：010b peak NVE 论文值 14.59× 需更新为 8.27×（重算已完成）
- Table 1 精简审查通过（8 行，保留关键证据链）
- ROADMAP 审查通过（方向合理，GPU 预算充裕）

**RUNNING**: 无

**等待中**:
- Director 回应 010b NVE 更新（14.59→8.27×）
- exp_024 重试（需修正参数名）
- 可能的后续 Cheetah 实验（SGS seed 2、no-dt-emb 因果控制）

### 4. 📋 待办
- Director 确认 010b NVE 更新 → 审查论文修改：Table 1 (14.59→8.27)、results.tex F7、introduction
- exp_024 rerun 完成 → 核实：(1) GPU 合规 (2) NVE<1.5× 预期 (3) 与 010b 形成因果对比
- exp_021 分析 worker 完成 → 核对 Agent 结论与我的独立验证一致（eval 221.5, NVE<1×）
- 任何新 RUNNING 实验 → 检查 GPU 设备 + 参数合规
- 论文最终版提交前 → 全文数字一致性扫描（特别是 010b NVE 在所有出现位置统一为新值）

### 5. 🎯 战略上下文
- 核心结论链：trained dt_emb + multi-rate exposure → obs decoder gradient → RSSM fidelity gap (2.78×) → critic overestimation → CIVO collapse。因果控制铁三角（008d/008f/008a）+ AUROC=0.926 是最强证据。
- CoRL 2026 DDL 2026-05-29（12天），预估 borderline accept (40-50%)。最大风险：无有效 mitigation + 叙事过载。
- **易错点 1**：paper_framing.md D061 旧数据（obs=93%/reward=0%）绝不可用——用 Paper Table 8。
- **易错点 2**：010b NVE 论文现值 14.59× 是错的，正确值 8.27×（基于 023a/023b 双 seed 基线）。已报 Director 但论文尚未改。
- **易错点 3**：exp_024 failed 因为 `--dt_embed_dim` 不是有效参数。Agent 需查代码确认正确参数名后 resubmit。
- **易错点 4**：022b 的 baseline 比是 300.7/915.7=32.8%（Walker），不要与 Cheetah 数据混用。
- **易错点 5**：019b eval 26.64 是 final（@200K），NVE=3.78× 是 normalized against 019a_v2 baseline（不是 Walker baseline）。
- D086 决策：梯度数据统一为 Paper Table 8 版本。D083：019b 是 TN（detector 正确不触发）。
- exp_021 SGS Cheetah 成功但轨迹极度波动（4.6@45K→221.5@105K），论文引用时需注明不稳定性。


---
