# agent / loop_14.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`5a696c8ff999ddf262ab.json`](../../sessions/5a/5a696c8ff999ddf262ab.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T16:26:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb cuda:0/1，westd cuda:0/1（C001）。其他设备号绝对禁止
- eval_gsm8k.py 不支持 --gpu 参数，必须用 CUDA_VISIBLE_DEVICES 环境变量
- sft_recovery.py 参数名：--learning_rate / --num_train_epochs / --gradient_accumulation_steps / --batch_size / --max_seq_len（不是 --lr / --epochs）
- Qwen Math 模型 generate() 必须加 eos_token_id=[151643, 151645]，否则每 sample 跑满 max_tokens
- westb↔westd 间无 SSH 互信，模型不可 SCP 直传
- DDL: EMNLP 2026 ARR May 25（距今 ~9 天），禁止任何 fallback/降级讨论

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× ~98GB GPU (cuda:0/1)，代码 `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westd-11672**: 2× ~95GB GPU (cuda:0/1)，代码同路径
- Python: `/root/miniconda3/bin/python`（conda base，不是 venv）
- HF_HOME: `/root/autodl-tmp/.hf_cache`
- W&B project: recovery_aware_struct_prune
- 活跃进程（cron 监控中）：
  - eval_sft_rasp_25: PID 602990 (westb/westd)
  - eval_sft_rasp_rlvr_20: PID 625453
  - grpo_rasp_25: PID 21408
  - sft_standard_25_westd: PID 21488
- 另有 4 个 RUNNING eval（eval_grpo_standard_20_qwen_math, eval_grpo_rasp_20_qwen_math, eval_grpo_standard_25_qwen_math, eval_grpo_rasp_25_qwen_math）—— 无 cron 记录，可能已完成未回调或由前 session Worker 启动

### 3. 📊 当前状态
**刚完成**：D044/D045 narrative pivot（"Universal Decoupling" framing），core 20% 数据全齐，Paper Agent Step 2 (Plot Generation) 进行中。

**RUNNING (8)**：
| exp_id | 摘要 |
|--------|------|
| grpo_rasp_25 | 25% RASP GRPO 100 steps，验证 collapse 加剧 |
| sft_standard_25_westd | 25% Standard SFT（grpo_standard_25 前置） |
| eval_sft_rasp_25 | RASP 25% post-SFT N=1319 eval |
| eval_sft_rasp_rlvr_20 | RASP-RLVR 20% post-SFT eval |
| eval_grpo_*_qwen_math (×4) | Qwen Math 20%/25% GRPO checkpoint eval |

**Worker 池 = 0** ⚠️ 违反 L1（池<2=失职）。需立即铺 Worker。

**等待中**：4 个 cron 回调（上述 PID）；grpo_standard_25 blocked on sft_standard_25_westd 完成。

### 4. 📋 待办（条件触发式）
- sft_standard_25_westd 完成 → 立即启动 grpo_standard_25（同 GPU）+ eval_sft_standard_25（如未做）
- eval_sft_rasp_25 完成 → 更新 paper_framing.md 25% 数据行，对比 20% (57%)
- grpo_rasp_25 完成 → spawn worker 分析 collapse timeline，与 20% collapse (~step 10) 对比
- 4 个 Qwen Math eval 完成 → 汇总跨模型×跨稀疏度 Table，确认 C2 泛化性
- eval_sft_rasp_rlvr_20 完成 → 与 RASP SFT (61.49%) 和 Standard SFT (59.29%) 对比，判断 RASP-RLVR 分支是否有价值
- 所有 25% 数据到齐 → patch paper_framing.md + plots，推进 Paper Agent Step 3
- GPU 空闲时 → 铺 eval_sft_standard_20_n1319 (Standard full eval) 和 eval_postprune_25

### 5. 🎯 战略上下文
**核心结论链**：
- D044: Major pivot — GRPO 对 pruned model 普遍失败（reward↑ accuracy 不动 = universal decoupling）
- D045: Unpruned GRPO v2 也 decouple（81.27% 不变），但不 collapse → collapse 是 pruning-specific
- D047: RASP-RLVR（反向 CKA）实验验证 "保护冗余结构" 能否缓解 collapse

**三个 Claims**：
- C1: Universal decoupling（reward-accuracy 分离，pruned + unpruned 都有）
- C2: Collapse gradient（pruned 独有，RASP ~step10 permanent vs Standard ~step60 transient）
- C3: Recovery method conditions pruning（SFT 下 RASP≈Standard p=0.25 不显著，但 GRPO collapse pattern 显著不同）

**易错点**：
- 不要把 N=100 结果（Standard 64% > RASP 57%）当 paper claim——N=1319 显示 p=0.25 不显著
- Unpruned v1 (collapse) vs v2 (stable) 是设计缺陷问题，不要混用
- α ablation 有两套（westb cal=512, westd cal=256），论文用 westb 数据，westd 仅做 robustness footnote
- 4 个 Qwen Math GRPO eval 无 cron——可能需要 spawn worker SSH 检查状态


---
