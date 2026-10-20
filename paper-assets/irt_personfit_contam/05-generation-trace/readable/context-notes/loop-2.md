# director / loop_2.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`fb27c7c251e865e1d03b.json`](../../sessions/fb/fb27c7c251e865e1d03b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-21T13:07:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35694 cuda:0-3 + westd-19912 cuda:0-3，共 8 卡，不可使用其他服务器/卡
- GRPO v3 必须独占一张卡，不可与其他训练共享（M019 教训：v2 与 Llama s2 共享 GPU 0 导致 2x 减速）
- 每个训练/eval 必须 `CUDA_VISIBLE_DEVICES=X` + `assert torch.cuda.device_count() == 1`（M013/M015 教训：不设导致 DDP 4x batch）
- GRPO 修改代码后必须先出 diff 给 Director 审批才能启动（M019 教训：v2 没改代码就重启）
- exp-post-rl(v1/v2) 已标 DONE(negative)，不要重跑。当前有效实验是 exp-post-rl-v3

### 2. 🖥️ 基础设施快照
- **westd-35694** (connect.westd.seetacloud.com): RTX 6000 ×4
  - Qwen MMLU: `/root/autodl-tmp/ctrl_contam_pilot/` (train.py, eval_lz.py, eval_with_ht.py)
  - Llama MMLU: `/root/autodl-tmp/ctrl_contam_llama/` (train.py, eval_lz.py)
  - Mistral MMLU: `/root/autodl-tmp/ctrl_contam_mistral/`
  - GRPO: `/root/autodl-tmp/post_rl_contam/` (train_grpo.py 已修改: num_gen=16, temp=1.2, max_steps=3000, save_steps=500)
  - MIA: `/root/autodl-tmp/post_rl_contam/eval_mia.py`
  - ConStat: `/root/autodl-tmp/post_rl_contam/run_constat.py` (已 bugfix)
- **westd-19912** (connect.westd.seetacloud.com): RTX 6000 ×4
  - ARC-C: `/root/autodl-tmp/arcc_contam/` (train.py, eval_lz.py, arc_c_params.csv)
  - Llama/Mistral 代码可能尚未同步到此服务器
- Python: aml-train 镜像用 `/root/miniconda3/bin/python`，conda base 环境
- 活跃进程状态未知（Agent 连续两次 16h idle，需要 SSH 重新探查）

### 3. 📊 当前状态
**Agent 连续两次 16h idle 被 reset**，所有训练任务应早已完成但结果未收集。需要全面 SSH 探查。

**应已完成（需确认）：**
- GRPO v3: step 3000/3000，PID 141861 @ westd-35694:cuda:2。**最关键** — 需要 eval lz* 确认 post-RL 信号
- Llama s8/s9/s10 训练 @ westd-35694:cuda:0/1/3
- ARC-C s7-s10 训练 @ westd-19912:cuda:0-3

**已确认完成的数据：**
- Qwen n=10 clean: mean lz*=8.684, std=0.736. Cohen's d: contam_15=6.575 [CI 4.51-15.20], contam_50=1.897 [CI 1.04-4.92]
- Llama clean s2-s7 eval done: mean≈0.49, std≈1.49 (高方差)
- Mistral clean s1-s3 eval done: s1 lz*未知, s2=-1.046, s3=3.279 (方差极大)
- ARC-C clean s1-s6: lz*≈-5.2~-5.6 (一致), contam_15 Δ=+0.5, contam_50 Δ=+0.9 (model-level 弱)
- MIA: base AUC=0.49, SFT best=0.611 (Min-K% 10%)
- ConStat: bugfix 完成，simulation 确认 lz* absorbed by θ-shift

**Registry RUNNING**: exp-post-rl-v3, exp-ctrl-contam-llama-contam15, exp-ctrl-contam-llama-contam50

### 4. 📋 待办
- SSH 探查两台服务器 GPU 状态 → 确认 GRPO v3 / Llama s8-s10 / ARC-C s7-s10 是否完成
- GRPO v3 完成 → eval_with_ht.py + eval_lz.py 跑 post-RL lz* → **如果 lz* 信号保持 = R7 claim 成立**（最大 blocking 项）
- Llama s8-s10 完成 → eval → 合并 s2-s10 算 n=9 Cohen's d（重算 cross-family 检测力）
- ARC-C s7-s10 完成 → eval → 扩展 clean baseline 到 n=10
- Llama/Mistral contam eval 是否已有 → 若有则用新 n 重算 d；若无则需跑
- 全部 eval 收齐 → 通知 Director 启动论文更新（n=10 d, MIA table, ARC-C power analysis, θ-shift discussion, cross-model calibration discussion）
- 8 GPU 空闲时 → 填 Llama seeds 扩展 / Post-RL Llama SFT / 其他 ablation

### 5. 🎯 战略上下文
**目标**: EMNLP 2026 Main (score 4.0)，当前 Dream Round 2: Best/Median 3.0, Worst 2.5

**决策链**:
- D025: 冲 4.0 — 三大补充实验 (ConStat/MIA/ARC-C)
- D027: ARC-C 重新定位为 power function 验证（model-level 检测力弱是 295 items + 天花板效应）
- D028: Kill GRPO v1/v2 (reward saturation)，修复后重跑 v3
- D029: θ-shift boundary condition — contam_50 d=1.9 vs contam_15 d=6.6，高污染率下信号被吸收，论文需正面讨论
- D030: 跨模型 IRT 校准差异 — Qwen lz*=+8.68 vs Llama=-0.18，每个模型需独立 calibration

**易错点**:
- Llama/Mistral clean lz* 方差极大（Llama std≈1.49, Mistral std≈3.06 vs Qwen std≈0.73）→ Cohen's d 天然偏小，Reviewer 可能攻击"只对 Qwen 有效"。应对：强调 item-level 信号一致性 + per-model calibration 作为方法论贡献
- GRPO v3 即使修复后仍有 60-80% batch 零梯度（binary reward 固有限制）→ 如果 eval 显示模型几乎没变，需要考虑换 DPO 或 reframe 为 "reward saturation = contamination evidence"
- 8 GPU 利用率是用户硬要求（反复强调"GPU利用率拉满"），空卡 >10 min 不可接受
- M019 教训：Agent 容易不改代码就重启失败实验，GRPO 相关操作必须验证 diff


---
