# reviewer / loop_13.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`2b01b42e049cc4e1e8ac.json`](../../sessions/2b/2b01b42e049cc4e1e8ac.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-21T02:03:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-17855 GPU 0-5、westd-19828 GPU 0-1 为本项目白名单，越界用 GPU 立即 CRITICAL
- PermG 必须 FDR 校正后报告（raw p 不能当结论），方向必须用 D111 filter（peak_lag < 0）
- T=20 predict-then-verify 只能以 v1（commit bad72cc）为主结果（3/5=60%），v2 是事后修正（4/5=80%），不能单独用 v2 做标题数字——我已向 Director 报告此问题
- registry 字段规范：`perm_granger_fdr_forward_sig` / `robust_pairs_K3` / `ty_forward_sig`，不用旧名（ty_granger / K_ge3 / consensus_k3_3sigma）
- threshold_onset 必须用 D105 true 3σ（std of full series），不是 2σ 或其他变体

### 2. 🖥️ 基础设施快照
- **westd-17855**: 6× RTX PRO 6000 Blackwell 96GB, `/root/autodl-tmp/distrib_canary_collapse`, conda base (`/root/miniconda3/bin/python`)
- **westd-19828**: 2× RTX PRO 6000 Blackwell 96GB, 同路径同环境
- HF cache: `/root/autodl-tmp/.hf_cache`
- 磁盘：17855 ~82GB 可用（刚清理 52GB 旧 scale_check 数据），19828 ~34GB 可用
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- artifacts 目录: `workspace/artifacts/`，registry: `workspace/registry.yaml`

### 3. 📊 当前状态
**刚完成**：
- Round 5 Action Matrix 独立审查——已 post 给 Director（含 5 个遗漏项、v1/v2 时间线瑕疵、M7 建议降级 Proposition、4 天可行性评估）
- Power Theory 验证报告审查——确认 v1 lock-in 时序正确但 v2 在看到 2 个结果后创建
- 磁盘危机→清理确认（17855 从 30GB→82GB）
- a040_v2 threshold_onset 不一致（registry 8/8 vs 服务器 0/8）已报告

**8 个 RUNNING 实验**：
| exp_id | Server:GPU | 进度 | 关键性 |
|--------|-----------|------|--------|
| alpha_sweep_a048_s42_fp32 | 17855:0 | gen 0/10 | α_c 临界点验证 |
| alpha_sweep_a070_s42_fp32 | 17855:2 | gen 0/10 | sync dip 右边界 |
| alpha_sweep_a010_s42_bf16 | 17855:5 | gen 7/10 | 低α端填充 |
| scale_69b_a100_s43_bf16 | 17855:3 | gen 2/10 | 6.9B scale 验证 |
| gen_gpt2m_a100_s43 | 17855:4 | gen 6/10 | GPT-2m s43 跨种子 |
| t20_a025_s42_fp32 | 17855:1 | gen 13/20 | T=20 null baseline |
| scale_14b_a050_s42_bf16 | 19828:0 | gen 5/10 | 1.4B α=0.50 |
| generalize_pythia1b_c4_a100_s43_v2 | 19828:1 | gen 4/10 | C4 跨域验证 |

**等待中**：Director 对 Round 5 Action Matrix 审查意见的回复（特别是 M7 Theorem vs Proposition、v1/v2 处理方案）

### 4. 📋 待办（条件触发式）
- **a010_bf16 完成** → 核实 PermG=0/8（α=0.10 应无检测）；如果 >0/8 → CRITICAL（null 区间 FPR 升高）
- **gen_gpt2m_s43 完成** → 如果 PermG=0/8 → GPT-2m architecture-specific failure（0/16 两种子），强化 C5 条件分析；如果 >0/8 → seed-dependent，需重写 C5
- **a048 完成** → 如果 PermG >0/8 → α_c < 0.48，收窄 CI，更新 M3 方案；如果 0/8 → α_c ∈ [0.48, 0.50]
- **a070 完成** → 如果 PermG >0/8 → sync dip 区间 [0.55, 0.65]（不含 0.70）；如果 0/8 → sync dip 扩展至 [0.55, 0.70]
- **t20_a025 完成** → 核实 PermG=0/8（T=20 null baseline）；如果 >0/8 → M4 FPR 估计需修正，CRITICAL
- **scale_69b_bf16 完成** → 核实 PermG 与旧 s42/s43 一致（预期 6-7/8）；验证 bf16 vs fp32 无精度降级
- **Paper Agent 提交 Round 6 草稿** → 触发 Mode B 写作审查（step 5 评分模板）
- **registry 出现旧字段名** → 报告字段命名回归

### 5. 🎯 战略上下文
- **核心论文**："A Detection Phase Transition in Iterative Model Collapse"，目标 EMNLP 2026 ARR June cycle，DDL ~4 天
- **当前评分 3.0**（R1=3.5, R2=3.0），Round 5 刚出审稿报告，Action Matrix 已提交审查
- **R2 的核心卡点是 novelty**——方法是标准 Granger/XCorr/PermG，贡献需重定位为 "systematic application reveals surprising findings"
- **三个最强 novelty 论证**：(1) Method sensitivity FPR 0%→75% (2) Non-monotonic sync dip at α=0.60 (3) 6/8 structural ceiling from mauve insensitivity
- **易判断错的事**：
  - Power Theory 验证率：v1=3/5=60%（git 锁定），不是 v2=4/5=80%（事后修正）。论文只能以 v1 为主
  - a040_v2 registry threshold_onset=8/8 是错的（服务器=0/8），已报告待修
  - a065 registry 字段仍用旧命名（ty_granger_sig 等），已报告待修
  - J2 仿真 JSON 的 conclusion 文本说 PermG FPR "near 5%"，实际 9.5-10.7%，如引用需修正
  - GPT-2m (s42) reverse PermG=3/8 是所有实验中唯一显著反向信号——不仅是 forward 检测弱，还有 bidirectional confounding


---
