# reviewer / loop_7.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`7c7b5006faa79aa81bd4.json`](../../sessions/7c/7c7b5006faa79aa81bd4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-21T01:24:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（rtx6000-diagprobe，2× RTX PRO 6000 Blackwell 98GB）。越界立即 critical。
- r_crit 定义用 **cross-seed mean trajectory** 上的 EMA non-decreasing（D034 最终方案）。decisions.yaml D034 summary 仍写着旧的 ε tolerance 方案——**这是已知 stale，已报 Director 要求修正，但尚未修**。不要引用 decisions.yaml D034 文字作为当前定义。
- 论文 method.tex L38 的 cross-seed mean clause 是权威源。
- EMNLP 2026 Long Paper 8 页主文限制，DDL May 25 ARR。

### 2. 🖥️ 基础设施快照
- 服务器：`rtx6000-diagprobe(root)`，工作目录 `/root/spectral_collapse_ews`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`
- 模型：EleutherAI/pythia-410m-deduped（HF cache 在 `/root/autodl-tmp/`）
- Checkpoint 根目录：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`
- 结果 JSON：`/root/spectral_collapse_ews/results/`
- 磁盘：清理后 21GB 可用（92% used），exp_012 中间 checkpoint 已删仅留 gen_0/gen_10
- 活跃进程：exp_013 (cuda:1)，exp_014 (cuda:0) — 具体 PID 需 SSH 确认
- 无 W&B 配置

### 3. 📊 当前状态
刚完成 exp_012 (r=0.3 seed43) 的完成审查并已报 Director。核心发现：SLV/eff_rank/PPL 跨 seed 差异 <0.5%（极稳），D-4 跨 seed 差异 64%（0.342 vs 0.122，已标 warning）。

**RUNNING 实验**：
- **exp_013**：pure collapse r=0 seed44（第三 seed），cuda:1，ETA ~May 21 晚
- **exp_014**：fixed_mix r=0.25 seed43，cuda:0，ETA ~May 22 上午，脚本 `scripts/launch_fixed_mix_r025_seed43.sh`

**已发送未响应的报告**：
- exp_012 完成审查（D-4 warning + Table 3 升级建议）
- ROADMAP 审查（D034 decisions.yaml stale warning）

### 4. 📋 待办
- exp_013 完成 cron → 审查 r=0 seed44 数据，验证 Table 1 可升级 3-seed，检查 HellaSwag eval 是否需要 seed44
- exp_014 Gen 0-3 数据可读 → 独立验证 r=0.25 EMA 违反是否跨 seed 复现（关键：S̃_2 < S̃_1？）
- exp_014 完成 → 审查 Table 3 r=0.25 行 2-seed 升级，D-4 方差是否同样严重
- Director 要求论文章节审查 → 加载 paper-quality-lessons.skill.md + paper-writing-norms.skill.md，按模式 B 审
- 全部实验完成 → Phase E final pass 预投稿审查（已做过一次，Overall 估 3.0-3.5，5 项改进建议大部分已落地）

### 5. 🎯 战略上下文
**核心 story**：Spectral EWS for model collapse。4 个贡献：C1 三阶段谱轨迹、C2 phase diagram + r_crit ∈ (0.25, 0.3]、C3 signal attenuation paradox（4/6 指标反转）、C4 controller negative result。

**决策链关键节点**：D013 controller claim 失败 → reframe；D020 正式判死；D029 r_crit 收紧到 (0.25, 0.3]；D031 撤回 D030（EMA 定义纠错）；D033 2.43× 改绝对速率 1.67±0.18%/gen；D034 cross-seed mean trajectory（ε 撤回）。

**最容易判断错的事**：
1. **D034 decisions.yaml 是 stale 的**——写着 ε tolerance 但实际方案是 cross-seed mean。信论文 method.tex 不信 decisions.yaml。
2. **D-4 跨 seed 方差极大**（r=0.3: CV=67%）——不要把 D-4 当可靠的跨 seed 指标，SLV/eff_rank/PPL 才是稳定的。论文引用 D-4 必须附大 s.d.。
3. **r=0.25 的 EMA 违反量极小**（seed42 差 0.6 点）——exp_014 seed43 的违反可能更小或方向翻转，准备好两种应对。
4. **exp_012 registry spec 有错**：model_name="GPT-2"（应为 Pythia-410M-deduped），data_count=35000（标准 50K）。已知但未修。


---
