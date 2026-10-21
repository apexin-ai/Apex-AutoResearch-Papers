# reviewer / loop_15.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`1ac27a4ccea3ec62d455.json`](../../sessions/1a/1ac27a4ccea3ec62d455.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-21T11:41:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- gpu-6000pro-2 项目 GPU 白名单：cuda:0, cuda:1。当前无 RUNNING 训练，但新实验（accum_pythia_nuc_001, accum_olmo_temp_001）如果启动训练必须在这两张卡上
- 用户此前明确说过"实验结束就收掉了"——R17 后 Director 决定加做补充实验（14b_cross_ref、fpr_coverage、conditional_pi、accumulation），但用户是否正式批准了这个变更我无法确认。如果用户再次表示不做实验，立即停止一切新实验审查，只做写作审查
- 14B 实验用 self-reference（Qwen2.5-14B 评自己），1-1.5B atlas 用 Pythia-1.4B cross-reference（Pythia 是 self-ref，OLMo/GPT-2 XL 是 cross-ref）。Table 1 的 Pythia 行标 † 表示 self-reference caveat。混淆这两个会导致数字对不上
- stat_only 数字必须用 main pipeline 值（temp09=50.5%, topk50=47.93%），不能用 ablation CV 值（51.83%, 48.84%）——方案A 已确认

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，远程代码根目录 /root/autodl-tmp/recursive_gen_depth_est
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/
- 论文路径：docs/paper/（main.tex 入口，25 页 PDF，8 页主文 + appendix）
- artifacts 路径：artifacts/（各实验报告）
- 无活跃 GPU 进程（上次 nvidia-smi：cuda:0 0MiB used, 100% util 可能是残留状态）
- 无 W&B 配置（项目不检查 W&B）
- 无 tmux/cron 活跃任务

### 3. 📊 当前状态
**刚完成**：R17 Action Matrix 审查 + 4 个补充实验的逐个审查

**Registry 状态**：
- `accum_pythia_nuc_001` — ANALYZING（Pythia nucleus accumulation，等 metrics 落地）
- `accum_olmo_temp_001` — ANALYZING（OLMo temp accumulation，等 metrics 落地）
- `conditional_pi_001` — ANALYZING（conditional permutation importance，VIF 补充）
- `14b_cross_ref_001` — DONE，**重大发现**：cross-ref 下 14B EDD 从 0 升到 2（nucleus/temp09）
- `fpr_coverage_001` — DONE，FPR-coverage 曲线数据完整

**等待中**：
- accum_pythia_nuc_001 和 accum_olmo_temp_001 的 metrics 落 registry（worker done 但 status=ANALYZING）
- conditional_pi_001 同上
- Director 整合所有补充实验结果后可能触发最终写作修改 + 终审请求

### 4. 📋 待办
- accum_pythia_nuc_001 + accum_olmo_temp_001 metrics 落地 → 审查：(a) 数字与 accum_v3 一致性（Pythia 应 ~70%/69%）；(b) OLMo temp 是新 cell，关注 attenuation 幅度是否与 Pythia 一致（-14 to -15pp）；(c) 论文 §6 accumulation 数字是否需要更新
- conditional_pi_001 完成 → 审查：group-level permutation importance 是否改变 §4.2 的 feature family dominance 结论（预期不会）
- Director 触发论文写作修改（整合 14b_cross_ref EDD=2 发现 + accum 多 cell 数据 + FPR curve + conditional PI）→ 做最终叙事一致性审查，重点检查 Abstract/§5.4/§6 的 14B EDD 叙事是否正确更新
- 编译后必查 8 页限制（R16 修改后 §6 扩展到 3 段，之前验证刚好 8 页，新增内容可能溢出）

### 5. 🎯 战略上下文
**项目核心结论**：recursive generation depth estimation 在 1-1.5B within-strategy 条件下 work（d1-d3 59-82%），cross-strategy/cross-scale 大幅衰减。四轮 Fresh Review 一致 3.0 Findings，目标投 EMNLP 2026 ARR Findings track。

**14b_cross_ref_001 是本 session 最重要的新发现**：self-ref EDD=0 → cross-ref EDD=2（nucleus/temp09）。这直接改变了 "14B is a dead end" 的叙事，变为 "14B signal exists but requires appropriate reference model"。论文中所有 "EDD₀.₇₀=0 at 14B" 的表述都需要 qualify。下一个"你"最容易犯的错是延续旧叙事（EDD=0），忽视 cross-ref 结果。

**易踩的坑**：
1. accum_v3（Pythia, DONE）vs accum_v2（killed）vs accum_pythia_nuc_001（新实验）——三套 accumulation 实验容易混淆。v3 是已有数据（70.1%/69.1%），新实验可能是重做或扩展
2. 排除 Pythia 算 "conservative estimate" 的陷阱——6-cell mean (80.3%) 比 9-cell mean (78.4%) 更高，因为 Pythia 是最弱模型。不要建议用 6-cell 作为 conservative number
3. 论文 §6 引用 "84.2% full-replacement" 是 accumulation baseline，不是 atlas 最佳 cell（85.9%）也不是 Pythia atlas（78.7%）——来源不同，读者可能困惑


---
