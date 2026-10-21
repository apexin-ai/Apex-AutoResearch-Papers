# reviewer / loop_20.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`03545798755c3927326a.json`](../../sessions/03/03545798755c3927326a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-19T08:40:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-29999 GPU 白名单: cuda:0,1,2,3（全部可用，无越界风险）
- cqa1-21977 GPU: 仅 cuda:0（单卡 4090D 24GB）
- Phi-4 14.7B eval/训练**不能在 cqa1 上跑**（~30GB bf16 > 24GB VRAM）
- OLMo-2 7B 和 Gemma-2 9B eval 可在 cqa1 上跑（14GB/18GB bf16 勉强适配 24GB）
- 统一 LoRA 协议: r=16, α=32, lr=5e-5, bf16, seed=42, epochs=1——任何偏离即 critical
- Variant A/B 判定尚未决定（D145 暂缓）——论文中不能预设 Variant A 叙事

### 2. 🖥️ 基础设施快照
- **westd-29999** (root): 4× RTX PRO 6000 96GB, `/root/autodl-tmp/exp001/`
  - checkpoints: `/root/autodl-tmp/exp001/checkpoints/{model}_{dosage}_{seed}/`
  - eval results: `/root/autodl-tmp/exp001/eval_results_14b/` (Qwen 14B), `/root/autodl-tmp/exp001/eval_results_cross_family/` (Phi-4/OLMo-2/Gemma-2)
  - models: `/root/autodl-tmp/models/{phi-4, OLMo-2-1124-7B, gemma-2-9b, Qwen2.5-14B, Qwen2.5-7B}`
  - SFT data: `/root/autodl-tmp/sft_data/sft_dosage_{000,005,025,050,100}.jsonl`
- **cqa1-21977** (root): 1× RTX 4090D 24GB, `/root/autodl-tmp/exp001/`
  - eval results: `/root/autodl-tmp/exp001/eval_results/` (Qwen 7B), `/root/autodl-tmp/exp001/eval_results_cross_family/` (OLMo-2)
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
  - 论文: `docs/paper/*.tex`
  - registry: `registry.yaml`

### 3. 📊 当前状态
**刚完成**: Phi-4 d000-d050 eval 独立核实 + OLMo-2 d000-d025 eval 独立核实 + 跨家族 claim 升级评估 + benchmark-specific pattern 分析。本 session 共提交 ~10 次 reviewer_post_to_director。

**RUNNING 训练** (westd):
- `exp_001_sft_phi4_d100_s42` — cuda:0, 55783 MiB（最后一个 Phi-4）
- `exp_001_sft_gemma2_9b_d100_s42` — cuda:1, 52111 MiB
- `exp_001_sft_olmo2_7b_d100_s42` — cuda:2, 38165 MiB

**RUNNING eval** (cuda:3 westd + cqa1):
- Phi-4 eval batch on cuda:3 — d000-d050 done, d100 待训练完成
- OLMo-2 eval on cqa1 — d000-d025 done, d050 checkpoint ready 但可能还没排进 eval queue
- **Gemma-2 eval 完全未开始** (0/5) — cqa1 无 Gemma-2 模型，westd 无空闲 GPU

**训练完成度**: Phi-4 4/5, Gemma-2 4/5, OLMo-2 4/5, Qwen14B 5/5, Qwen7B 10/10+eval done

### 4. 📋 待办（条件触发式）
- Phi-4 d100 训练完成 → 核实 train_config + .done → 启动 Phi-4 d100 eval on cuda:0（训练释放后）→ Phi-4 全链 eval 完整
- OLMo-2 d100 训练完成 → 核实 → cqa1 eval queue 应自动接 d050+d100
- Gemma-2 d100 训练完成 → **关键**: cuda:1 释放后必须立即安排 Gemma-2 d000-d100 eval batch on westd（cqa1 可能装不下 9B）
- 所有 eval 完成 → 汇总完整跨家族 dose-response 表 → 做最终 Variant A/B 判定 → 通知 Director
- Agent 每次训练完成后不主动启动下一个 QUEUED → 需要持续监控并 flag idle GPU（本 session pattern: 几乎每次完成都要提醒）

### 5. 🎯 战略上下文
- **核心发现**: SFT contamination MMLU 正向（+0.4~2.3pp）、ARC 零/负向，3/4 family 方向一致
- **D145**: Variant A/B 暂缓——7B 明确 Variant A（Δ<2pp），14B 在 gray zone（1.92-2.28pp 单 seed）
- **D147**: benchmark-specific pattern（MMLU vs ARC）值得作为 prominent finding 但不宜 co-primary claim
- **OLMo-2 弱基线问题**: MMLU 58.71% 远低于其他 family，contamination 效应 marginal。建议 Discussion 中作 exploratory observation，不放 Contribution。如果 d050/d100 也 null，cross-family claim 变成"3/4 positive + 1/4 null"，仍可接受但需 hedge
- **最容易判断错的事**: (1) 不要把 Phi-4 d050 +1.20pp 和 Qwen 14B d050 +2.28pp 直接比较来 claim "effect scales with capacity"——Phi-4 更大但效应更小，说明效应与 baseline 能力/训练数据相关而非纯参数量; (2) d005 MMLU 在 7B scale 是负向的（Qwen -0.26pp, OLMo-2 -0.50pp），不能 claim "contamination always inflates MMLU"; (3) Agent 的 pattern 是训练完成后做 analysis 但不启动下一个 QUEUED 任务，几乎每次 GPU 释放都需要 reviewer 催促
- **Paper scope expansion patch 有 3 个 CRITICAL**（已提交但不确定是否已修复）: Abstract 未同步、Contribution 1 claim-evidence 不匹配、Introduction 预设 Variant A
- **Deadline**: EMNLP 2026 ARR May 25，约 6 天


---
