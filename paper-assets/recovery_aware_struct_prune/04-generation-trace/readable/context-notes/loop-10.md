# director / loop_10.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`66f0214539aab1c5c67d.json`](../../sessions/66/66f0214539aab1c5c67d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-16T18:43:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C004）：westb-23072 cuda:0/1 + westd-11672 cuda:0/1/2/3（共 6 张），严禁越界
- GRPO save_steps=100（不是 5！7B 模型每 checkpoint 25GB，save_steps=5 撑爆磁盘）
- eval_gsm8k.py 用 CUDA_VISIBLE_DEVICES 环境变量（不支持 --gpu）；sft_recovery.py 用 --gpu 参数
- Qwen Math 模型必须设 eos_token_id=[151643, 151645]
- westb↔westd 无 SSH key 互信，scp 不通
- Calibration 不一致已决定不重跑（D046）：DeepSeek cal=512, Qwen-Math cal=256，论文加 footnote
- wandb 日志通过 symlink 写到 /root/autodl-tmp/（根分区空间极小）

### 2. 🖥️ 基础设施快照
- westb-23072: connect.westb.seetacloud.com:23072, root, /root/recovery_aware_struct_prune
- westd-11672: connect.westd.seetacloud.com:11672, root, 密码 p1IO5kjrDeYv, 4×RTX PRO 6000 96GB
- Python: /root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型/数据/输出: /root/autodl-tmp/recovery_aware_struct_prune/
- HF cache: /root/autodl-tmp/.hf_cache
- 磁盘: westb ~85%, westd ~36%
- 活跃进程（RESET 前最后确认）：
  - westb cuda:0: eval_sft_rasp_25 (N=1319, 极慢因 DeepSeek CoT 长 response，不是 bug)
  - westd cuda:1: grpo_standard_25 (刚启动)
  - 其他 4 张 GPU 空闲！Agent 死了 4h 未执行分配指令

### 3. 📊 当前状态
**本轮完成了 3 个关键决策**：
- D048: C3 reframe — "RASP enables better recovery" 否定，C1 (decoupling) 成为主锚
- D049: 不采纳 "pruning disables GRPO" 叙事，pass@k 仅作 C1 补充证据
- D050: RLVR 降级为 ablation（DeepSeek -3.19pp p=0.014；Qwen Math +0.5pp noise）

**pass@k 最终数据 (Qwen Math, N=200, pass@8, T=0.7)**：
- Unpruned GRPO: 0.965 ±0.013
- RASP 20% SFT: 0.935 ±0.017
- RASP 20% GRPO: 0.915 ±0.020
- SFT vs GRPO: Δ=-2pp, p=0.44 不显著 → collapse 对 diversity 也是 cosmetic

**grpo_rasp_25**: DONE, frac_zero=0.875, reward=0.009, 100 steps（极端 collapse）
**eval_sft_rasp_rlvr_20**: 58.30% (N=1319), 显著差于 RASP 61.49%
**Qwen Math RLVR SFT**: 73.00% (N=200)，vs RASP 72.5% 纯噪声

**Agent 死了 ~4h**（idle 240min），所有 GPU 分配指令未执行。RESET_BOTH 已批准。

### 4. 📋 待办（条件触发式）
- Agent 重启后第一件事 → **填满 4 张空闲 GPU**：
  - westb cuda:1 → grpo_rasp_rlvr_20（SFT checkpoint 在 /root/autodl-tmp/.../sft_rasp_rlvr_20/，ablation）
  - westd cuda:0 → Standard 20% post-GRPO pass@k（grpo_standard_qwen_math checkpoint，C1 diversity 对照）
  - westd cuda:2 → α ablation SFT 继续（alpha_ablation_westd_cal256 Phase A 已完成，Dream Critical plan_015）
  - westd cuda:3 → Qwen Math RLVR GRPO（检查之前 PID 32087 是否完成/失败，按需重启）
- grpo_standard_25 完成 → 对比 grpo_rasp_25 (frac_zero=0.875)，确认 25% C1 decoupling
- Standard pass@k 完成 → 如果 frac_zero=0.85 模型 pass@8 也 ~0.91 → C1 超级坚固
- 所有关键数据到齐 → ROADMAP 大更新 + paper_framing.md 改写（align D048-D050）
- paper_framing 改写后 → 通知 Paper Agent 做 Reframe（C1 主锚 + RLVR ablation）
- eval_sft_rasp_25 完成 → 记录 25% RASP full accuracy
- α ablation 全部完成 → 写入论文（Dream Critical，0 分析 = 审稿必打回）

### 5. 🎯 战略上下文
- **论文定位 (D048-D050 后)**：solid diagnostic paper。C1 (GRPO collapse = cosmetic) 是唯一强 claim，跨模型×跨 sparsity×跨 metric（accuracy + diversity）验证。RASP scoring mechanism 是 secondary。RLVR 是 negative ablation。
- **Reviewer 安全叙事**："GRPO collapse metrics (frac_zero_std) do not predict catastrophic diversity loss; pass@8 decreases modestly (−2pp, n.s.) despite severe metric collapse"
- **Dream 评估**：best=4/6, median=3/6, worst=3/6。当前 framing 对齐 3-4/6 (borderline~weak accept)
- **DDL**: ARR May 25, 2026（~9 天）
- **最容易判断错的事**：
  1. Agent 报 Qwen Math RLVR 73% 是 "成功" — 不是，vs 72.5% 纯噪声 (p=0.87, N=200)
  2. eval_sft_rasp_25 极慢不是 bug — DeepSeek CoT 生成长 response，不要 kill
  3. Cron on_failed 系统性误报 — 正常完成的实验也会触发 "failed" CRON（检测进程退出但 registry 未更新）
  4. pass@k 0.935 vs 0.915: 方向负但 p=0.44 不显著，不要 claim "GRPO hurts diversity"
  5. Agent 之前混淆 bash wrapper PID vs Python PID，kill 时确认实际进程
- **用户态度**：已授权"你和 Reviewer 一致觉得没问题就做，并行去做"——不用逐个请示
- **Paper Agent**: Step 4 完成，等 Reframe 指令（需 paper_framing.md 先改写）


---
