# director / loop_12.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`b97cbce126491ce9c98d.json`](../../sessions/b9/b97cbce126491ce9c98d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-21T01:38:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5, westd-19828 cuda:0-1。不得使用白名单外 GPU
- westd-19828 网络不可达，模型必须用本地路径（如 `/root/autodl-tmp/.hf_cache/pythia-1b-local`），不能依赖 HF Hub 下载
- 6.9B+ 模型在单 A100-96GB 上只能用 bf16 + gradient_checkpointing，fp32 会 OOM（M053 教训）
- westd-17855 磁盘紧张（~30GB free），scale_69b_bf16 checkpoint rotation 峰值 ~26GB。已派 Agent 清理 52GB 旧 scale_check 目录——确认清理完成前不要启动新的大模型实验
- CSV compile_dose_response.py 必须应用 D111 direction filter (peak_lag < 0)，否则 NaiveXCorr/DiffXCorr K≥3 会系统性高估（M052）
- a065 分析 worker 写入了旧字段格式（ty_granger/K3_3sigma），需要修正为标准字段名（ty_forward_sig/robust_pairs_K3）

### 2. 🖥️ 基础设施快照
- **westd-17855**: connect.westd.seetacloud.com, root, `/root/autodl-tmp/distrib_canary_collapse`
  - 6 GPU (A100-96GB), conda base env (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)
  - HF cache: `/root/autodl-tmp/.hf_cache`
  - 活跃实验: cuda:0 a048, cuda:1 t20_a025, cuda:2 a070, cuda:3 scale_69b_bf16, cuda:4 gen_gpt2m_s43, cuda:5 a010_bf16
- **westd-19828**: connect.westd.seetacloud.com, root, `/root/autodl-tmp/distrib_canary_collapse`
  - 2 GPU, 网络隔离（TRANSFORMERS_OFFLINE=1 必须）
  - 活跃: cuda:0 scale_14b_a050_s42_bf16, cuda:1 generalize_pythia1b_c4_a100_s43_v2 (retry_count=1)
- **论文目录**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/`
- **审稿群 (C群)**: `oc_21bf8254f3677799a62db5ed920cc0b3`

### 3. 📊 当前状态
**刚完成**：Round 5 论文全部修改（Phase 1: 13 structural changes + Phase 2: 4 statistical items + J2 Non-Stationarity Robustness patch）。编译通过：8 页主文, 23 页总, 0 undefined refs。

**Round 5 审稿已提交**（`apr_20260520T223036_9zbf`），pending 用户批准审稿卡。推荐 continue 模式。用户 Directive 36 目标 4.5，Round 4 = 3.0。

**8 个实验 RUNNING**：
- alpha_sweep_a048_s42_fp32 (~3h, transition midpoint)
- alpha_sweep_a070_s42_fp32 (~3h, sync dip recovery boundary)
- t20_a025_s42_fp32 (~8h 预估已超，应快完成)
- scale_69b_a100_s43_bf16 (~20h, 刚重提交)
- gen_gpt2m_a100_s43 (~4h, GPT-2-medium cross-seed)
- alpha_sweep_a010_s42_bf16 (~3h)
- scale_14b_a050_s42_bf16 (~6h, 19828)
- generalize_pythia1b_c4_a100_s43_v2 (~4h, 19828, retry)

**等待**：磁盘清理 Agent 回调；Round 5 审稿批准；8 个实验的 on_complete 回调。

### 4. 📋 待办（条件触发式）
- Round 5 审稿报告到达 → 按 `review-report-action.skill.md` 协议处理：Holistic Pass → Per-Comment Action Matrix → post_to_reviewer 反审 → 定稿分派
- Round 5 ≥ 3.5 → 走 Round 6 polish + 强化 claim 路线
- Round 5 < 3.5 → 分析最大扣分项，集中突破单一最大 reviewer 抱怨
- a048 完成 → 如果 >0/8 则 α_c 进一步左移，更新 paper sigmoid fit 和 CI；如果 0/8 则 blind zone 确认到 0.48
- a070 完成 → 如果 0/8 则 sync dip 扩到 [0.55, 0.70]，如果 >0/8 则恢复在 (0.65, 0.70]，更新 dose-response framing
- scale_69b_bf16 完成 → cross-seed 验证 6.9B 结果（s42 PermG=7/8），更新 Table 2
- gen_gpt2m_s43 完成 → 验证 GPT-2-medium 检测失败是 architecture-specific 还是 seed-specific，更新 11/15 数字
- 磁盘清理回调 → 确认 52GB 已回收，scale_69b 安全继续
- a065 registry 旧字段 → 修正为标准格式（ty_forward_sig/robust_pairs_K3）

### 5. 🎯 战略上下文
**核心 story**: Token entropy Granger-precedes diversity collapse，sharp onset at α_c≈0.50。三大贡献：(1) detection onset boundary mapping, (2) Cascade Ordering Theory (Theorem 1, 15/15 validated at α≥0.30), (3) intervention PoC (58% PPL reduction)。

**Round 4→5 关键转变**: Cascade Theory 在 Round 4 完全未被 reviewer 提到（可见度 = 0）。Round 5 升级为独立 §3 section（在 method 之前），Theorem box + empirical validation subsection。这是 3.0→3.5+ 的核心杠杆。

**决策链**: D154 (t20_a045 Model B confirmed) → D155 (Round 4 Action Plan: 贡献重组 + 统计修复)。155 条决策记录在 decisions.yaml。

**易错点**:
- PermG FPR 不能 claim "theoretically robust to non-stationarity"——仿真显示 φ≥0.95 下 FPR 膨胀到 ~10%。正确表述是 "empirically maintains size control in our setting"（三层防线：null φ=-0.51 / d1 差分 φ<0.44 / 经验 0/24）
- S×R 是 z-test power formula 的 reparameterization，不是独立理论贡献。只能作为 interpretive lens
- MMCT 是 sensitivity analysis，不是 method ranking tool。Equal-weight 下 PermG 仍排第一但 margin 窄（0.015）
- 11/15 (73%) cross-architecture，不是 13/15。GPT-2-medium 0/8 + SmolLM3-3B 3/8 + Pythia-1.4B non-monotonic + C4 preliminary
- Sync dip 区间已扩到 [0.55, 0.65]（不是之前的 [0.55, 0.60]），a070 结果将确定右边界
- Deadline: EMNLP 2026 ARR 2026-05-25（4 天），用户要求留 Round 6 buffer


---
