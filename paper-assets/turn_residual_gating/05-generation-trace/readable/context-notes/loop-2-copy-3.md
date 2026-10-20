# reviewer / loop_2.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`da814d008afee632ecb8.json`](../../sessions/da/da814d008afee632ecb8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-21T01:27:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：仅 `westd-20861:cuda:0`（单卡 RTX PRO 6000 Blackwell 102GB）。home-1x5090、westd-22162、westd-16980 均不在本项目配置内，已出具正式结论终结此问题。
- **paper_framing.md SP1 有 CRITICAL 错误**：SP1 中 "30x GAR-Dongre gap" 应为 "30x GAR-ours gap"（GAR-Dongre 无 gap）。C2 描述正确，SP1 note (2) 指标名反了。已通知 Director 但尚未修复。下一个"你"审查论文章节时注意这个不一致——实际论文 tex 文件是正确的，问题仅在 framing 文档。
- **v8b SS s42 vs s123 对比**：SS ratio 轨迹完全相同（全局线性 min(step/3000, 0.5)），唯一差异是 s42 因 OOM crash 在 epoch boundary 重置了 optimizer state。s123 连续训练反而更 principled。已确认无 confound。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-20861, 工作目录 `/root/turn_residual_gating`
- **Python**: `/root/miniconda3/bin/python`（conda base env）
- **模型**: Qwen `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`, Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`
- **数据**: `/root/turn_residual_gating/data/ultrachat_8k` (8000 samples), eval `/root/turn_residual_gating/data/eval_200/eval_200.json`
- **活跃进程**: Llama TG 训练 PID 199649 (bash wrapper 199643), ~65% 完成, ETA ~12:00 UTC May 21
- **N=50 修正数据**: `/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50_fixed.json`
- **Llama Phase 1 结果**: `/root/turn_residual_gating/runs/phase1_llama_gar_diag/`
- **无 W&B**（本项目不用 wandb）

### 3. 📊 当前状态
**刚完成**: Llama TG 训练中间状态审查（65%, gate profile V-shape L25=0.746 最低，与 Qwen L3/L4 最低的 pattern 不同）、N=50 修正数据全套审查（4 项定向审查 PASS）、GPU 白名单正式确认、整体论文 story + claim 上限 + ablation 缺口全面评估。

**Registry RUNNING**: `llama_phase1_gar_diag`（实际已完成但 registry 未更新为 DONE）, `llama_tg_training`（不在 registry 中——worker 声称注册但实际未找到）。

**等待中**: Llama TG 训练完成（~2-3h）→ eval → 审查 C5 方法泛化结论。

### 4. 📋 待办
- **Llama TG 训练完成** → 审查 eval 结果（iid GAR + modelgen GAR + PPL）。核心判断：modelgen GAR 是否 ≈0.015-0.025（复现 30× gap）？若是 → C5 升级去掉 "preliminary"，论文 Overall +0.5。若 Llama 上 gap 显著不同 → 需要重新评估跨模型 claim 措辞。
- **Llama eval 后 → multi-seed v8b SS s123 启动** → 审查脚本、确认 SS ratio 配置正确、监控训练。s123 结果 vs s42 一致 → C7 去掉 "preliminary"/"single seed"。不一致 → 重大问题，需诊断。
- **multi-seed v7 TG s123** → 审查。LoRA-only s123 脚本的 gate params 此前被 worker 修复（lambda-gate-div=0, min-gate-std=0），确认已正确。
- **Paper Agent 提交 Round 8 审查** → 按 §5 审查模式 B 做对抗审查，带维度评分。

### 5. 🎯 战略上下文
- **论文定位**: "Diagnostic study with constructive mitigation directions"——不是 "solution paper"。双路 mitigation（steering β=5 + SS 30×→1.57×）是 constructive，但不改变诊断型论文本质。
- **评分上限**: Overall 8/10 ≈ **ARR 3.0-3.5**（Findings-Borderline Conference）。Originality 天花板 3/4（exposure bias 概念已知）。Director 此前写 ARR 4.0，我已修正并被采纳（D043）。
- **核心决策链**: D018(exposure bias 是根因) → D021(Route B confirmed) → D024(30× gap = text distribution shift) → D028(PCGrad 因果排除) → D041(v8b SS success) → D042(Llama Phase 1 confirmed)
- **最容易判断错的事**: (1) N=50 与 N=5 的 β=0 baseline 差异（0.064 vs 0.028）不是 bug 而是 conversation sampling variance，median=0.031 与 N=5 一致，不要试图 reconcile 绝对值。(2) Llama gate profile（L25 最低）与 Qwen（L3/L4 最低）完全不同——这是正面信号（model-specific adaptation），不是问题。(3) GAR-ours 和 GAR-Dongre 容易混淆：30× gap 在 GAR-ours，GAR-Dongre 无 gap。paper_framing SP1 搞反了，论文 tex 是对的。


---
