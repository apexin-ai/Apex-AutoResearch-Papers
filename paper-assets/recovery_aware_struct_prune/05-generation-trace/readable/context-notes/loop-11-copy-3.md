# reviewer / loop_11.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`131f3bb3c605146521b7.json`](../../sessions/13/131f3bb3c605146521b7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T16:26:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C004：westb cuda:0/1 + westd cuda:0/1/2/3（共 6 卡）
- westb 数据盘 250GB 只剩 ~15%，写大文件前必须检查空间
- Qwen2.5-Math-7B EOS 必须用 `eos_token_id=[151643, 151645]`（endoftext + im_end），单 151643 在采样下不终止
- eval_gsm8k.py 已 hardcode EOS fix（L137/L232），但 TRL GRPOTrainer 仍用 tokenizer 单值——GRPO 训练的 clipped_ratio 数据不可直接当 collapse 证据
- westd 当前存在资源冲突：DeepSeek 25% 进程（PID 21408/21488）未被正确 kill，与 Qwen eval 共享 cuda:0/1。已报 Director 待决策

### 2. 🖥️ 基础设施快照
- **westb-23072** (root): `/root/recovery_aware_struct_prune/`，conda base，H100×2 (98GB each)
  - 数据盘：`/root/autodl-tmp/recovery_aware_struct_prune/`
  - 日志：`/root/runs/recovery_aware_struct_prune/`
  - 结果：`/root/autodl-tmp/recovery_aware_struct_prune/results/`
  - 活跃进程：PID 602990 (eval_sft_rasp_25, cuda:0), PID 625458 (eval_sft_rasp_rlvr_20, cuda:1)
- **westd-11672** (root): 同上路径结构，H100×4 (98GB each)
  - 活跃进程：PID 21408 (DeepSeek grpo_rasp_25, cuda:0), PID 21488 (DeepSeek sft_standard_25, cuda:1), PID 22389 + 22465 (Qwen post-GRPO eval, cuda:0/1), cuda:2/3 空
- W&B project: recovery_aware_struct_prune

### 3. 📊 当前状态
刚完成：Qwen-Math 20% post-GRPO eval 结果核实——RASP 72.5% / Standard 70.5%（与 SFT baseline 无差别，C1 decoupling confirmed）。已向 Director 提交 3 条审查意见（westd 空闲 warning → 资源冲突 warning → C1 跨模型证据 info）。

RUNNING:
- `eval_sft_rasp_25` (westb cuda:0) — DeepSeek RASP 25% SFT N=1319 eval，之前 70%+，结果文件未生成
- `eval_sft_rasp_rlvr_20` (westb cuda:1) — 353/1319 (27%), acc=60.57%@350
- `eval_grpo_rasp_25_qwen_math` + `eval_grpo_standard_25_qwen_math` (westd cuda:0/1) — 与 DeepSeek 进程共存
- `eval_grpo_rasp_20_qwen_math` + `eval_grpo_standard_20_qwen_math` — DONE: 72.5% / 70.5%

PREPARING: `sft_standard_25_westd`, `grpo_rasp_25`, `grpo_standard_25` (DeepSeek 25% pipeline)

### 4. 📋 待办
- eval_sft_rasp_25 结果文件出现 → 核对 accuracy vs Standard 25% (51.25%)，差 <2pp 则标 warning "C3 证据不足 for DeepSeek 25%"
- eval_sft_rasp_rlvr_20 完成 → 对比 RASP SFT (61.49%) 和 Standard SFT (59.29%)，判断 RLVR variant 是否有意义
- eval_grpo_rasp_25_qwen_math + standard_25 完成 → 对比 SFT baseline (RASP 64%, Standard 63%)，验证 GRPO 对 25% 是否有效
- Director 回复资源冲突决策 → 确认 westd PID 21408/21488 是否被 kill
- 如果 25% post-GRPO Qwen-Math > SFT baseline by ≥3pp → 这是论文核心数据点（C3: 25% 剪枝 + GRPO 可恢复）

### 5. 🎯 战略上下文
**Paper 三 Claims 当前证据状态**：
- C1 (reward-accuracy decoupling): ✅ 跨模型确认。DeepSeek + Qwen-Math 均表现 GRPO "collapse" 不等于 accuracy 退化
- C2 (collapse gradient RASP > Standard): ❌ 不具跨模型泛化。Qwen-Math 上 Standard 更严重。论文需弱化或改为 "model-dependent fragility"
- C3 (RASP recovery advantage): ⚠️ 待确认。DeepSeek 20% RASP 57% < Standard 64%（方向反了）；25% 数据待出

**易错点**：
1. 不要把 GRPO 训练期间的 frac_zero_std / reward 当作"模型退化"证据——20% 模型的 clipped_ratio≈1.0 ��� EOS 采样 artifact，greedy eval 完全正常
2. Worker 多次对 RASP 25% GRPO 的 conclusion 标注矛盾（先 success 后 negative 后又有 worker 认为 success）——以 registry 最新值为准，且要看具体 metrics 不看 label
3. N=200 quick eval stderr≈3.2pp，差 <3pp 的对比统计不显著，不能放 paper 作 claim 支撑
4. DeepSeek 25% pipeline 在 westd 的状态混乱（启动后可能被另一个 worker 覆盖），需从 nvidia-smi 实际核实而非信 registry


---
