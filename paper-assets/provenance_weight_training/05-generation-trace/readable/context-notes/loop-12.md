# director / loop_12.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`4f71555c2df6d7f2f81e.json`](../../sessions/4f/4f71555c2df6d7f2f81e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-17T16:55:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-30476 cuda:0-3 + westd-41312 cuda:0-3（共 8 张，全部 RTX PRO 6000 Blackwell）
- westd-30476 并行上限未确定：单卡 40min 探针通过后直接跑 4 卡目前稳定，但此前 4 卡并行在 ~20min 处被平台 SIGKILL（非 OOM，根因不明）。如果再次被杀，不要盲目重试，先单卡探针
- Cron 误报模式（M011）：训练正常完成后进程退出会被 cron auto-resolve 为 failed（无 W&B sentinel）。收到 cron failed 通知时**先检查 checkpoint/final 目录是否存在**再更新 registry
- eval_perplexity.py 必须用 `--max_docs 5000 --stride 1024 --fp16` 统一参数，否则 token 数不一致导致 PPL 对比无效（Reviewer CRITICAL 教训）
- Registry 更新反复失败（Agent 声称改了但 Reviewer 验证未生效）——下次要求 Agent 修改后立即用 get_experiment 回显验证

### 2. 🖥️ 基础设施快照
- **westd-30476**：ssh -p 30476 root@connect.westd.seetacloud.com，代码路径 /root/provenance_weight_training，模型输出 /root/autodl-tmp/output/models/
- **westd-41312**：ssh -p 41312 root@connect.westd.seetacloud.com，代码路径 /root/provenance_weight_training，模型输出 /root/autodl-tmp/provenance_weight_training/output/models/
- 数据：scored_data.jsonl (~930MB), eval_holdout.jsonl（两台服务器均有）
- 基座模型：Qwen3-0.6B（路径在 /root/autodl-tmp/ 下），Llama-3.2-3B（同）
- adaptive_fix_seed42 checkpoint 确认在 41312: /root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final/
- lm-eval-harness 已安装在 41312
- 无 W&B 集成，无 conda（直接用系统 Python + pip）

### 3. 📊 当前状态
**运行中（30476）：**
- bs8_auto_nmin_r5 (cuda:1, ~30%) — D062 coupling rule bs=8
- batch_adaptive_tau_rho06_r5 (cuda:2, ~30%) — D063 Plan B
- rho02_adaptive_tau09_r5 (cuda:3, ~30%) — Claim 3 ρ=0.2
- cuda:0 空闲（random_reweight_seed123 完成，PPL=17.801）

**运行中（41312）：**
- qwen06b_uniform_seed42 retrain (cuda:0, ETA ~18:30 UTC) — 核心 baseline 重训（47453 丢失）
- ess_only_seed456 (cuda:1, ~16%) — Claim 1 统计显著性
- ess_only_seed123 (cuda:2, ~16%) — Claim 1 统计显著性
- cuda:3 空闲（grid_b0_3_seed456 完成但 registry 未更新）

**刚发出的紧急指令（队列中）：**
- Registry 修正 ×5（llama3b_uniform PPL, llama3b_adaptive conclusion, batchsize16 conclusion, ess_only ×2 回滚为 RUNNING, grid_b0_3 → DONE）
- grid_b0_3_seed456 eval
- random_reweight_seed123 registry 更新

### 4. 📋 待办（条件触发式）
- uniform_seed42 retrain 完成 (~18:30 UTC) → eval_perplexity.py + lm-eval (HellaSwag/ARC-Easy/PIQA/WinoGrande) → 与 adaptive_fix_seed42 配对对比 → 这是论文下游 eval 的核心数据
- ess_only_seed123/456 完成 (~19:10 UTC) → eval_perplexity.py → 对比 ess_only_seed42 (PPL=17.720)，确认 Claim 1 统计显著性（adaptive < ess_only < uniform < random 排序跨 seed 稳定）
- 30476 三实验完成 (~2-3h) → eval + 汇报：bs8 验证 coupling rule, batch_adaptive 验证 Plan B, rho02 验证 Claim 3
- 所有 eval 完成后 → 通知 Paper Agent 执行累积 Patch（coupling rule + failure mode + unified ablation table + random baseline + Claim 1 升级）
- grid_b0_3_seed456 eval 出 PPL → 对比 seed42 的 b=0.3 (PPL=17.640)，确认 grid-best 跨 seed 稳定

### 5. 🎯 战略上下文
- **核心结论链**：D064 detector signal load-bearing（random PPL=17.801 >> adaptive 17.653）→ D065 Claim 1 升级为 "both quality signal AND minimum-intervention needed" → D067 跨模型 neutral/parity（非 negative）
- **论文投稿目标**：EMNLP 2026，Core Claims 全基于 Qwen3-0.6B ρ=0.4
- **自查 P0 缺口**：(1) 下游 eval——uniform retrain 完成后即可配对对比 (2) ESS-only 跨 seed——正在跑 (3) loss-based reweighting baseline——尚未开始（~3.6h GPU，优先级 P1）
- **Paper Agent** 有累积 5 项 Patch 等数据（n_min coupling + failure mode + unified table + random baseline + Claim 1 升级），全部实验完成后统一执行
- **易错点**：(1) Agent 声称 registry 已改但实际未生效——必须要求回显验证 (2) Agent 会对已完成实验派"诊断 Worker"而非直接更新——cron failed 时先让它查 checkpoint 再决策 (3) eval 参数不统一会导致假结论（D066→D067 教训）(4) 47453 已注销，早期实验 checkpoint 全丢——需要重训的只有 uniform_seed42（adaptive_fix 在 41312 上找到了）


---
