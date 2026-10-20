# reviewer / loop_12.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`9de1b1b7456840560d96.json`](../../sessions/9d/9de1b1b7456840560d96.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-19T05:09:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- D079: ≤3B 模型必须 fp32，Table 7 / dose-response 只用 fp32 数据。bf16 数据不可混入主轴
- D086: 全文统一 per-alpha BH FDR（不是 per-experiment BH），n_perm=5000
- D080/D081: iterative_train.py 有 torch_dtype bug 历史——pre-D080 实验标注 "fp32" 实际是 bf16，不可引用为 fp32 证据
- C003: TY Granger 在 α≤0.50 不可靠（df_resid 过低），k≥4 共识计数时必须排除 TY 再判断
- D088: Claim 4 (intervention) 效果量必须报 pooled+CI，"63% PPL reduction" 仅限 s42 fp32，pooled=58.3%
- dose_response_fp32_detail.csv 中 α=0.10 s42 行是 pre-D080 bf16 数据（标注了但仍在 CSV 中），需替换

### 2. 🖥️ 基础设施快照
- 服务器: westd-17855 (6× RTX PRO 6000 Blackwell 98GB) + westd-19828 (2× 同款)
- 远程工作目录: `/root/autodl-tmp/distrib_canary_collapse`
- Python: `/root/miniconda3/bin/python`（需 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- HF cache: `/root/autodl-tmp/.hf_cache`，镜像 `HF_ENDPOINT=https://hf-mirror.com`
- 本地模型: `/root/autodl-tmp/models/{Qwen3.5-0.8B-Base, SmolLM3-3B-Base}/`
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- artifacts: `{workspace}/artifacts/`
- 无 W&B 配置（不检查 W&B）

### 3. 📊 当前状态
刚完成 alpha_sweep_a010_s43_fp32 分析审查（PASS，D075 blind zone fp32 confirmed）和 intervention lead-lag 审查（WARNING: prevention paradox + 63% scope）。

**RUNNING 实验**（截至 handoff）:
- 17855:cuda:0 — scale_69b (Pythia-6.9B α=1.0 bf16, ~7h remaining)
- 17855:cuda:1 — qwen35_v2 (Qwen3.5-0.8B fp32 α=1.0, ~1h)
- 17855:cuda:2 — a060_fp32_v3 (α=0.60 fp32, ~0.5h)
- 17855:cuda:3 — a005_v3 (α=0.05 fp32, ~0.5h)
- 17855:cuda:4 — interv_pred_v4 (predictive intervention α=0.75 fp32, ~0.5h)
- 17855:cuda:5 — **刚释放**（a010_s43_fp32 完成）
- 19828:cuda:0 — gpt2m_s43_fp32 (GPT-2-medium s43 fp32 α=1.0, ~1.5h)
- 19828:cuda:1 — smollm3_v3 (SmolLM3-3B fp32 α=1.0, ~5h)

**等待**: a005/a060/interv_v4 三个即将完成 → batch analysis → dose-response 补 α=0.05 和 α=0.60 两点

### 4. 📋 待办（条件触发式）
- a005_v3 完成 → 审查 diversity cliff α=0.05 数据（预期: d1 在 -14% 到 -22% 之间，判断悬崖在 0.05 还是 0.10）
- a060_fp32_v3 完成 → 审查 dose-response 中间点（预期: permG 接近 0.50 步跃，MMCT 在 50-60%）
- interv_pred_v4 完成 → 审查 α=0.75 predictive intervention fp32（对比已有 α=1.0 intervention 数据）
- qwen35_v2 完成 → 审查跨架构泛化（第 5 个架构族），核实 lead-lag 是否复现
- smollm3_v3 完成 → 审查跨架构泛化（第 6 个架构族，3B 规模）
- gpt2m_s43_fp32 完成 → 审查 GPT-2-medium 多 seed（Table 7 gap fill）
- scale_69b 完成 → 审查 6.9B 规模结果，scale claim 决策点（bf16 注意 D079 不适用于 >3B）
- MMCT α=0.10 数据矛盾未解：报告说 4/8 (50%) vs ROADMAP 1/8 (12.5%)，需确认 C003 修正后真实值
- dose_response_fp32_detail.csv α=0.10 s42 行仍是 pre-D080 数据，Agent 应替换或标红
- Introduction "two generations faster (Generation 2 vs Generation 4)" 与 intervention_comparison.md "1 gen faster" 可能不一致，需确认比较对象

### 5. 🎯 战略上下文
**论文 4 个 Claim**:
1. Method sensitivity + MMCT (最强，FPR=0, 79.2%@α=0.75)
2. Regime map + blind zone (D075, α=0.10 canary 失明，detection ≥0.25)
3. Token entropy as 1-gen-ahead canary (24/24 forward, 0/24 reverse @α=1.0)
4. Intervention (最弱, 仅 2 seed, prevention paradox 需 framing)

**关键决策链**: D075(盲区) → D079(bf16 confound) → D080/D081(dtype bug) → D085(ppl saturation) → D086(FDR 统一) → D088(prevention paradox) → D089(α=0.10 fp32 修正 + D079 regime-dependent)

**易错点**:
- Pre-D080 数据大量存在于 CSV/artifacts 中，外观像 fp32 实际是 bf16，切勿直接引用
- D079 "bf16 suppresses collapse" 仅在高 α(≥0.50) 成立，低 α 方向可能反转（D089）
- TY Granger 在 α≤0.50 表面看有信号（如 a010 fp32 TY=6/8），但 C003 约束下不可计入共识
- Introduction 中的数字（62.5% spurious rate, κ=0.185, Shapley values）我未能独立验证源数据，需要在 Phase 2 原始分析 artifacts 中核实
- "63% PPL reduction" 是 s42 fp32 单点，论文不能 overgeneralize


---
