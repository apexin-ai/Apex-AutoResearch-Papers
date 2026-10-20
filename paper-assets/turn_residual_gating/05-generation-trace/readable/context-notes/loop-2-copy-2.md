# agent / loop_2.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`8299c5146e2f151aadc0.json`](../../sessions/82/8299c5146e2f151aadc0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-22T23:46:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-20861:cuda:0（1×RTX PRO 6000 Blackwell 102GB），白名单仅此一张卡
- llama_lora_only_s42 刚完成训练，GPU 已释放，当前 0 张在跑——下一个实验提交前必须确认 GPU 重新分配
- LoRA-only 是 ablation baseline，不是主方法——registry 里的 conclusion 必须基于 eval 结果（GAR 对比），不能仅凭训练 loss 判定
- 论文已 commit e4522a3，Llama LoRA-only 跨模型结果（C5）已写入论文§5；eval 结果出来后需要核实论文数据是否需要更新

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，工作目录 `/root/turn_residual_gating/`
- Python：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：Meta-Llama-3.1-8B-Instruct，数据：`/root/turn_residual_gating/data/ultrachat_8k`（8000 条）
- 日志：`/root/turn_residual_gating/logs/llama_lora_only_s42.log`（也可能在 `~/runs/turn_residual_gating/`）
- Checkpoint：预期在 `/root/turn_residual_gating/checkpoints/llama_lora_only_s42/`
- W&B：project=turn_residual_gating（entity 从 project config 获取）
- 活跃进程：无（训练已结束）
- Cron：reconcile 返回 0 条活跃

### 3. 📊 当前状态
收到 `llama_lora_only_s42` 完成回调（ANALYZING），已派 Worker `worker_analysis_llama_lora_only_s42_20260522T073713` 分析训练日志和 W&B 指标，**Worker 尚未回调**。

Registry 状态：
- `llama_lora_only_s42`: ANALYZING — 等 Worker 回调提取 metrics
- `llama_tg_training`: PREPARING (conclusion=failed) — 状态矛盾，可能是历史残留，需确认
- 其余 33 个实验全部 DONE（24 success, 5 negative, 3 failed, 1 killed）

等待中：
- Worker `worker_analysis_llama_lora_only_s42_20260522T073713` 回调 → 提取训练 metrics → 判断是否需要 eval
- GPU 当前空闲（0 分配 / 0 在跑）

### 4. 📋 待办
- Worker 回调到达 → 读取训练 metrics → update_registry(metrics) → 判断下一步：
  - 训练正常完成 → 必须跑 eval（与 llama_eval_s42 相同配置：TF+AR, N=50, T=4），对比 LoRA-only vs TG 的 GAR gap
  - 训练异常 → 诊断并决定是否重跑
- Eval 完成 → 核心对比：LoRA-only GAR vs TG GAR（parent llama_tg_s42 TF GAR=0.4836, AR GAR=0.0304, gap=15.9×）
  - 如果 LoRA-only TF GAR ≈ TG TF GAR → gating 零增量，与 Qwen v7 结论一致 → C5 confirmed（跨模型 gating 行为一致）
  - 如果 LoRA-only TF GAR << TG TF GAR → gating 有增量 → 需要修正论文 C5 叙述
- Eval 结果出来后 → 汇报 Director（带 [资源] 行）+ update report.md + 检查论文§5 是否需要更新
- `llama_tg_training`（PREPARING/failed）需要确认：是历史残留还是有待处理的任务

### 5. 🎯 战略上下文
- 项目核心：diagnostic framework 证明 residual gating 的 auxiliary attention loss 在 exposure bias 下泛化失败（TF-AR GAR gap）。双路 mitigation 已验证（attention steering + scheduled sampling）。跨模型泛化（C5）已从 Qwen→Llama confirmed（D045）
- Claims 进度：C1-C5 ✅, C6 ✅(N=50), C7 ⏳ (v8b SS s123 已 DONE，eval 已 DONE)
- Llama LoRA-only 是 C5 的补充数据点（plan_011, nice-to-have），不是 must-do
- 评分预估：ARR 3.0-3.5（Findings-Borderline Conference）
- 易错点：
  - LoRA-only 没有 gate，不要在 metrics 里找 gate_mean/gate_std
  - Eval 脚本需要适配 LoRA-only checkpoint 格式（无 gate 权重），注意不要直接复用 TG eval 脚本中加载 gate 的部分
  - 论文已有 Llama 跨模型数据（commit e4522a3），eval 结果需要与已写入的数字交叉验证
  - 串行队列（v8b s123 → v7 TG s123 → Llama LoRA-only）已全部跑完，当前无排队实验


---
