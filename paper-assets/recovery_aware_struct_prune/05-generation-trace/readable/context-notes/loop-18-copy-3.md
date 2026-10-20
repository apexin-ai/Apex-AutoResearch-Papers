# reviewer / loop_18.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`f3c0ef1c624bd7865b6d.json`](../../sessions/f3/f3c0ef1c624bd7865b6d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-22T18:27:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-32935: 只能用 cuda:0-3（4 张 GPU）
- westb-23072: 只能用 cuda:0-1（2 张 GPU）
- GRPO 脚本必须用 `train_grpo_v5.py`，`train_grpo.py` 是旧版/错误版本
- AutoDL 根分区只有 ~30GB，大文件必须放 `/root/autodl-tmp/`
- 模型下载/pip install 前必须 `source /etc/network_turbo`

### 2. 🖥️ 基础设施快照
- **westd-32935**: 代码 `/root/recovery_aware_struct_prune`，数据 `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westb-23072**: 同上路径结构
- Python: conda base (`/root/miniconda3/bin/python`)
- W&B: 已配置（seed456 run=auv9riek）
- HF cache: `/root/autodl-tmp/.hf_cache` 或 `/root/.cache/huggingface`
- **活跃进程 westd**: PID 66827 (GPU 0, α=3.0 MATH-500), PID 57202 (GPU 1, α=2.0 MATH-500), PID 58276 (GPU 2, α=0.5 MATH-500), PID 58435 (GPU 3, α=4.0 MATH-500)
- **活跃进程 westb**: PID 234500 (GPU 0, CKA-only SFT MATH-500), PID 220343 (GPU 1, MF3 Qwen-Math-7B eval ~90s/sample)

### 3. 📊 当前状态
刚完成：
- MF2 三种子验证全部完成：seed42=50.57%, seed123_v2=50.72%, seed456=50.87%（mean=50.72%, σ=0.15pp）→ 已报告 Director
- MATH-500 dose-response 所有 7 个点均已启动（之前标记的 α=3.0 和 CKA-only 缺口已填补）

MATH-500 已完成结果：Standard=26.0%, α=1.0=24.2%, CKA-only GRPO=26.6%
MATH-500 进行中：α=2.0 ~60%, α=0.5 ~40%, α=4.0 ~45%, α=3.0 和 CKA-only SFT 刚启动
MF3 v3 (Qwen-Math-7B): ~12h total ETA, westb:1

### 4. 📋 待办
- α=2.0 MATH-500 完成 → 立即核实是否为 inverted-U 峰值（GSM8K 上 α=2.0 是峰值 64.79%）；如果 MATH-500 也确认，inverted-U 跨 benchmark 成立
- 如果 MATH-500 inverted-U 不成立（α=2.0 不是峰值）→ [severity: critical] 报 Director，dose-response 需要 multi-seed 补实验
- 所有 MATH-500 SFT 完成 → 汇总 dose-response 表，检查 Standard(26.0%) vs α=1.0(24.2%) 关系是否与 GSM8K 一致
- CKA-only SFT MATH-500 完成 → 对比 CKA-only GRPO(26.6%)，验证 C1 decoupling 在 MATH-500 上的表现
- MF3 v3 完成 → 核实 Qwen-Math-7B CKA-only 跨架构泛化

### 5. 🎯 战略上下文
- **核心论点**：C1 = GRPO 对所有方法无增益（Universal Decoupling），C2 = CKA-only 显著优于其他方法（Recovery Capacity Gradient）
- **MF2 已锁定**：三种子 σ=0.15pp，C1 在 Random 上不可撼动
- **最大风险**：MATH-500 dose-response 能否复现 GSM8K 的 inverted-U。如果 α=2.0 在 MATH-500 上不是峰值，论文 dose-response claim 需要降级或加 caveat
- **易错点**：`eval_math500_sft_rasp_20.json`(24.2%) 和 `eval_math500_sft_rasp_alpha1p0_20` 是同一个模型（sft_rasp_20_westd = α=1.0 default RASP）。不要误以为是两个不同数据点
- **Cron 误报模式**：进程被 kill 或 disk-full 导致 non-zero exit → cron 报 failed，需人工确认实际结果文件是否存在
- **paper_framing.md 自标 gap**："Standard/RASP GRPO GSM8K evals (58.91%/60.65%) may be from pre-fair models" — 这个 traceability 问题尚未解决


---
