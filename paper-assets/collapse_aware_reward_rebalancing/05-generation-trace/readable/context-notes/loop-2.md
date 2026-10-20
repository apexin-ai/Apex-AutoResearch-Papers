# agent / loop_2.md

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`c7ee2c426e62a0099ff6.json`](../../sessions/c7/c7ee2c426e62a0099ff6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-16T20:56:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb2-23165 的 cuda:0 和 cuda:1（2× RTX 5090 32GB）
- 所有实验启动命令必须包含 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`（网络不通）
- Full-FT 模式必须用 `bf16=True`，不能用 `fp16=True`（GradScaler 不兼容 FP16 梯度）
- conda 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- GPU 编号始终从 0 开始（CUDA_VISIBLE_DEVICES 映射物理 GPU）

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 `/root/autodl-tmp/carr/`
- Python：`/root/miniconda3/bin/python3`（conda base 环境）
- 模型：Qwen3-0.6B 在 `/root/autodl-tmp/carr/` 下（目录名可能有转义 `Qwen3-0___6B`）
- ArmoRM：本地已 patch（LLAMA_INPUTS_DOCSTRING + gating token 容错）
- 数据集：openbmb/UltraFeedback（2200 条，已离线缓存）
- 输出目录：`outputs/`（baseline/LoRA）、`outputs_k8/`（K=8）、`outputs_fullft_k4/`（Full-FT）
- 活跃进程：carr_quick_probe_k8_02 (PID 507603, cuda:0, tmux 管理, cron 监控中)
- Worker：`worker_fix_carr_fullft_k4_fp16_20260516T165400` 正在修复 train_sft.py 并重提交

### 3. 📊 当前状态
刚诊断完 `carr_fullft_k4_probe_01` 失败（fp16+Full-FT 不兼容），已派 Worker 修复并重提交为 `carr_fullft_k4_probe_02`。

Registry:
- `carr_quick_probe_k8_02` — RUNNING (cuda:0)：K=8 LoRA T=3，验证更强选择压力能否触发 collapse
- `carr_fullft_k4_probe_01` — DONE/failed：fp16 梯度错误，Worker 正在修复重跑
- `carr_baseline_no_curation_01` — DONE/success：no-curation baseline 完成，Vendi 稳定 ~105-108
- `carr_quick_probe_03` — DONE/negative：K=4 LoRA Vendi 仅降 0.28%，P1 FAIL

等待中：
- Worker 回调：fix worker 修完 → carr_fullft_k4_probe_02 自动提交到 cuda:1
- Cron 回调：carr_quick_probe_k8_02 完成时触发

### 4. 📋 待办
- fix Worker 完成回调 → 确认 carr_fullft_k4_probe_02 已在 cuda:1 运行，更新 registry
- carr_quick_probe_k8_02 完成 → 看 Vendi 下降幅度：≥5% → P1 pass，用该配置跑 Full MVP；<5% → 继续诊断阶梯（K=16 或 Full-FT）
- carr_fullft_k4_probe_02 完成 → 同上判断逻辑，与 K=8 结果交叉对比
- 两者都 FAIL → 向 Director 提 pivot 讨论（DDL 2026-05-25 仅剩 9 天）

### 5. 🎯 战略上下文
- 核心问题：P1 前提验证——能否在 iterative training 中观测到 diversity collapse。K=4+LoRA 已 FAIL，正在平行测试 K=8（加选择压力）和 Full-FT（去正则化约束）
- D006 决策：P1 从绝对 Vendi 下降改为 baseline-relative gap（baseline 已完成：Vendi 105→108 缓慢上升）
- **关键 baseline 发现**：no-curation 的 Vendi 从 105→108 上升，single_reward 维持 ~107 平稳 → curation 实际上*抑制*了 diversity 增长，但幅度不够显著
- 易错点：不要把 "Vendi 不下降" 直接等同于 "没有 collapse"——对比 baseline 增长趋势才是正确度量（relative gap = baseline 涨了但 curation 没涨 → 存在抑制效应）
- DDL 压力极大（5/25），如果 K=8 和 Full-FT 都不能产生 ≥5% 的信号，需要立即 pivot 而非继续加压


---
