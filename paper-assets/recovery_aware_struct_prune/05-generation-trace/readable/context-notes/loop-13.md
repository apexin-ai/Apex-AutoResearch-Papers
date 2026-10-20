# director / loop_13.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`8aa8585cab688c118040.json`](../../sessions/8a/8aa8585cab688c118040.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-17T11:04:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 cuda:0/1 + westd-11672 cuda:0/1/2/3（共 6 张）
- GRASPrune baseline 数据已存在 (D033/D034)，**不要重新启动 plan_005**
- scoring ablation 必须加 `--skip_attention`（否则 magnitude/random 会剪 attention groups 导致 load_pruned_model 崩溃）
- eval 脚本必须带 `--output_path`（之前遗漏导致结果未保存）
- SFT 脚本必须用 `--save_strategy no`（sft_recovery.py 已加 CLI 参数），否则 epoch checkpoints 35G×2 会撑爆 westb 磁盘
- Agent 反复出现"写代码不执行"模式（M003）——收到 Worker done 后必须确认 GPU 进程实际启动（要 PID + nvidia-smi）
- HumanEval eval 当前 max_new_tokens=512 太短（thinking model 截断严重），需 ≥2048 重跑全部。已有 HumanEval 数据（1.83%/3.05%/7.32%/10.37%）相对排序可能仍有效但绝对值不可信

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com, root) + westd-11672 (connect.westd.seetacloud.com, root)
- 代码路径：`/root/recovery_aware_struct_prune`（两台均有）
- 数据/模型：`/root/autodl-tmp/recovery_aware_struct_prune/`
- SFT 模型：`sft_{rasp,standard}_20_westd` (westd), `sft_{rasp,standard}_20_westb` (westb，已删，westd 有副本)
- GRPO 模型：`grpo_stage2_rasp_20_v9` (westd), `grpo_stage2_standard_20_v8/checkpoint-50` (westd)
- 磁盘：westb 89G 可用 (65%)，westd 33G 可用 (96%，紧张)
- 活跃进程 westd：MATH-500 unpruned (cuda:0, ~完成), MATH-500 grpo_standard (cuda:1, 极慢 20h+), HumanEval grpo_standard (cuda:2, ~完成), MATH-500 grpo_rasp (cuda:3, 极慢 10h+)
- 活跃进程 westb：cka_only prune+eval 刚指示启动 (cuda:0), random eval 171/200 即将完成 (cuda:1, PID 696141)
- scoring ablation pipeline: magnitude done, gradient done, random eval 接近完成, cka_only 刚启动

### 3. 📊 当前状态
刚完成 Loop #13，处理了 scoring ablation 磁盘危机（三次 disk full）、HumanEval 截断问题发现、MATH-500 初步结果分析。

**已确认的 scoring ablation 数据：**
| Method | Post-prune | Post-SFT |
|--------|-----------|----------|
| Magnitude | 0% (N=60) | FAILED (unrecoverable) |
| Gradient | 25.5% (N=200) | **61.5%** (N=200) |
| Random | ~34-37% (N=100-150, 进行中) | 待 SFT |
| CKA-only | 待启动 | 待 SFT |
| RASP | ~31% | 61.49% (N=1319) |
| Standard | ~27% | 59.29-64% (N=1319) |

**关键发现：gradient post-SFT (61.5%) ≈ RASP post-SFT (61.49%)**——SFT 恢复后不同 scoring 方法差异消失，CKA 价值在 post-prune survival 而非 final accuracy。

**MATH-500 进行中数据：**
- Unpruned: 73.75% (400/500, 即将完成)
- SFT RASP: 24.20% (done)
- SFT Standard: 26.00% (done)
- GRPO RASP: 34% at N=64 (**C1 可能被挑战——GRPO > SFT +10pp**)
- GRPO Standard: 刚启动 (4%)

等待中：Agent 处理我的三决策指令（cka_only 启动 + GRPO MATH-500 继续跑 + HumanEval 重跑暂缓）

### 4. 📋 待办
- Random eval N=200 完成 → 汇报 final accuracy，立即启动 random SFT (cuda:1, --save_strategy no)
- cka_only eval 完成 → 启动 cka_only SFT → 完成后 scoring ablation table 全部到齐
- MATH-500 unpruned 完成 (westd cuda:0) → 空出 cuda:0，启动 HumanEval unpruned 重跑 (max_new_tokens=2048)
- HumanEval grpo_standard 完成 (westd cuda:2) → 空出 cuda:2，安排 HumanEval 重跑 queue
- GRPO RASP MATH-500 到 N=100-150 → post_to_reviewer 评估 C1 是否确认被挑战。若 acc 仍 >30%，开始准备 C1 framing 备案："GRPO fails on in-distribution (GSM8K) but transfers to harder OOD tasks (MATH-500)"
- Scoring ablation table 全部完成 + MATH-500 全部完成 → dream_simulate(review_mode="full") 评估最终论文强度
- 所有 scoring ablation SFT 完成后若有 GPU 余量 → 考虑补跑 magnitude SFT（Reviewer 建议的 supplementary data point）

### 5. 🎯 战略上下文
- **C1 可能需要根本性重新定义**：GSM8K 上 C1 (GRPO≈SFT) 成立，但 MATH-500 GRPO RASP 34% >> SFT 24.2% 且 HumanEval GRPO>SFT +3pp。若确认，C1 从"GRPO doesn't work"变为"GRPO's benefits are orthogonal to its training signal"——这是更 nuanced 更有趣的发现
- **C3 已非常弱**：RASP vs Standard 在 GSM8K 仅 2.3pp (p=0.09 marginal)，MATH-500 上 Standard 略高。Multi-seed 方差大（Standard 3.5pp range）。Reviewer 建议不追 stability claim，仅报 CI
- **Scoring ablation narrative 转向**：gradient post-SFT ≈ RASP post-SFT，random post-prune > RASP post-prune。CKA 的论文价值不在 final accuracy，而在 (1) post-prune survival 差异, (2) GRPO collapse dynamics 差异, (3) 层分布均匀性
- **DDL: ARR May 25 (~8 天)**，算力充足 (768h budget, <100h used)
- **易错点**：Agent"写脚本不执行"(M003 logged 3 次)；westb 磁盘容易满（250G 盘，checkpoint 35G×2）；westd 磁盘也紧（33G）；HumanEval 数据因截断不可直接引用需重跑


---
