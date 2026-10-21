# director / loop_9.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`30511b509bf67b5a8b77.json`](../../sessions/30/30511b509bf67b5a8b77.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-19T10:30:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- gpu-6000pro-2 GPU 白名单: cuda:0, cuda:1（仅此 2 张）。当前被 14B 实验占满，不可抢占
- westd-48862 GPU 白名单: cuda:0, cuda:1。当前被 accumulation v3 占满
- 论文真源在**本地** workspace `projects/recursive_gen_depth_est/docs/paper/`，远程 gpu-6000pro-2 只是编译环境。Paper Agent 无 SSH 权限（M007），所有 rsync+编译必须由 Agent 执行
- ARR 正文 ≤ 8 页硬约束（D047 已卡到恰好 8 页，任何新增必须等量压缩）
- Accumulation 实验必须是 LoRA 训练+文本生成（M008/M009 教训：Agent 两次做成特征空间混合，已纠正到 v3）
- 不要信 Paper Agent 的"编译通过"报告——它没有 SSH 权限，编译必须 Agent 做

### 2. 🖥️ 基础设施快照
- **gpu-6000pro-2**: 2× RTX PRO 6000, SSH alias `autodl-rtx6000`（实际是 westb 端口 52439）
  - 论文编译目录: 远程 paper/ (需从本地 rsync)
  - 14B 实验目录: `/root/autodl-tmp/recursive_gen_depth_est/`
  - 活跃: qwen25_14b_temp09 (cuda:0), qwen25_14b_topk50 (cuda:1)
- **westd-48862**: 2× RTX PRO 6000 Blackwell (98GB/卡), SSH alias `westd-48862`
  - 项目目录: `/root/autodl-tmp/recursive_gen_depth_est/`
  - 根分区仅 5.9GB，所有输出必须写 `/root/autodl-tmp/`
  - 活跃: accum_v3_mix50 (cuda:0, PID 114330), accum_v3_mix25 (cuda:1, PID 114471)
  - GPT-2 XL + Pythia-1.4B 权重已缓存
  - rsync 注意: `docs/paper/figures` 是符号链接，用 `-L` 或排除 figures/
- **本地**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`

### 3. 📊 当前状态
**刚做完**:
- D044: Round 13 写作修复 8/8 完成（Reviewer 验证），D047 编译通过
- Introduction 叙事修复 3 处（cross-scale 范围、instruction-tuned 泛化、d4v5 scope）
- 14B 场景模板清理（84.75% 错误数字、quantization confound、QLoRA qualifier）
- Binoculars ordinal baseline 代码就绪（`artifacts/binoculars_baseline/`），等 GPU
- Rebuttal 模板 4 条（W10/W11/W14/W15）已修正事实错误
- MDD 计算完成: MDD=EDD 全部 12 profiles，改为 1 句 empirical validation caveat

**RUNNING 实验**:
- `qwen25_14b_temp09`: gpu-6000pro-2 cuda:0, ETA May 20 ~05:00-06:00 UTC
- `qwen25_14b_topk50`: gpu-6000pro-2 cuda:1, ETA May 20 ~06:00 UTC
- `accum_v3_mix50`: westd-48862 cuda:0, 50% human mix, ETA May 19 ~14:30 UTC
- `accum_v3_mix25`: westd-48862 cuda:1, 25% human mix, ETA May 19 ~14:30 UTC

**刚刚启动**:
- D045: CORAL ordinal regression 升级为主分类器（用户批准）。Agent Worker 正在 CPU 跑 Phase 1 (9-cell CORAL vs RF 对比)，~15-20min 完成

**Invalidated**: accum_mix50/accum_mix25 (feature-level mixing, M008/M009)

### 4. 📋 待办（条件触发式）
- CORAL Phase 1 结果回来 → 审查 CORAL vs RF 差距；若 CORAL ≥ RF 则确认升级为主分类器并派 Paper Agent 改写 Method §3；若 CORAL < RF 则改为"complementary ordinal perspective"而非替代
- CORAL Phase 1 通过 → 派 Agent 做 Phase 2 (cross-strategy CORAL) + Phase 3 (等 14B 数据)
- accum_v3 完成 (ETA 今晚) → Reviewer 验证结果 → 若 accumulation < full-replacement 则写入 Discussion §6（替换预测语言为实际数据）+ Appendix table；若 ≈ full-replacement 则改 framing 为 "different regime"
- accum_v3 完成后 westd-48862 空出 → 立即跑 Binoculars ordinal baseline (<1 GPU-h)
- 14B temp09/topk50 完成 (ETA 明天) → 选用三场景模板 (`docs/paper/drafts/14b_scenarios.tex`) patch §5.4 + Abstract → CORAL Phase 3
- 所有实验完成 + 论文 patch 完毕 → 最终编译 → 提交 Round 14 审稿
- Discussion accumulation 段落目前是纯预测语言 → accum_v3 结果出来前**不要 finalize** Discussion §6

### 5. 🎯 战略上下文
**核心决策链**: D038(Strong Accept冲刺) → D043(Round 12修复) → D044(Round 13修复8/8) → D045(CORAL method升级)

**当前评分**: Round 13 = 3.0 (R1: 3.5, R2: 3.0)。目标 4.0 (Conference Accept)。

**D045 是关键转折**: 用户批准将 CORAL ordinal regression 升级为主分类器。这是从 3.5 冲 4.0 的核心手段——给论文增加方法贡献。之前两轮审稿一致指出"标准 RF 无算法贡献"。CORAL 天然适配 depth estimation（有序分类）。已有初步数据: baseline_battery 显示 CORAL ≈ RF (78.07% vs ~78-79%)，差距不大。如果 9-cell 系统评估后 CORAL 仍 ≈ RF，framing 改为"CORAL provides ordinal consistency guarantee that RF lacks"而非"CORAL beats RF"。

**易错点**:
- Accumulation 实验: Agent 已两次做错（特征空间混合而非 LoRA 训练）。v3 已修复（Reviewer 代码审查通过），正在运行。如果结果 <1h 完成或不用 GPU = 又做错了
- Paper Agent 编译报告不可信（无 SSH），必须 Agent rsync+remote compile
- 页数极紧（恰好 8 页），任何新增内容必须从别处压缩等量空间
- review_issues.yaml 在 `artifacts/review_issues.yaml`，22 个 issue 跨 Round 12-13 追踪
- Introduction "7-14B (54-70%)" 已修复为按模型系列分开报告，不要回退
- Claim 3 (downstream application) 覆盖率仅 33.3%，downstream 实际效果全部 negative/failed，不要 over-claim


---
