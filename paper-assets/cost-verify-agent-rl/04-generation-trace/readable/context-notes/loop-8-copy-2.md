# agent / loop_8.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`fbb0ea72104e29ac8c17.json`](../../sessions/fb/fbb0ea72104e29ac8c17.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T10:33:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-17606 cuda:0, cuda:1（仅此两张，不可用其他）
- verl-agent 代码在 `/root/autodl-tmp/verl-agent/`，不是 RAGEN 目录
- SFT baseline 用 16-episode eval 的 6.25%（不是早期 4ep 的 25%，那是小样本噪声）
- RAGEN GRPO 路线已终止（D026），不要再用 RAGEN 框架跑 GRPO
- 模型是 Qwen3-1.7B（不是论文原版 Qwen2.5-1.5B），这是框架验证不是严格复现

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，aml-train 镜像
- Python：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- verl-agent 代码：`/root/autodl-tmp/verl-agent/`
- 训练脚本：`examples/grpo_trainer/run_alfworld_exp025.sh`
- SFT checkpoint：`/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/`
- 日志目录：`~/runs/cost-verify-agent-rl/`
- 活跃进程：无（exp025 已崩溃，PID 555182 已退出）
- Worker：`worker_code_exp025_verl_agent_setup_20260515T062446` 可能仍在运行（06:24 启动的 setup worker），`worker_diagnose_exp025_failure_20260515T071627` 正在诊断中

### 3. 📊 当前状态
exp025（verl-agent ALFWorld GRPO 复现）提交后仅 143 秒即崩溃，`ModuleNotFoundError` in `ray::TaskRunner.run()`。已派诊断 Worker 读日志定位具体缺失模块，**尚未收到回调**。Registry 已更新 failure_reason，Director 已收到初步失败报告。

两张 GPU 均空闲。16 个实验处于 PREPARING 状态（多为 RAGEN 时代遗留，pivot 后大部分已不适用）。

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读取具体缺失模块名 → 派修复 Worker 安装依赖 → 重提交 exp025
- exp025 重跑成功（verl-agent GRPO 能启动） → 注册 cron 监控 → 向 Director 汇报框架可行性验证进展
- exp025 重跑再次失败 → 评估是否需要更深度的 verl-agent 环境重建（pip install -e . 等）
- setup Worker（06:24 那个）回调到达 → 检查它是否已完成 verl-agent 环境搭建，与诊断结果交叉验证

### 5. 🎯 战略上下文
项目处于 **Framework Pivot** 阶段（D026）：RAGEN GRPO 3/3 失败后转向 verl-agent。exp025 是 pivot 后第一个实验，验证 verl-agent 框架能否在 ALFWorld 上训练出 >20% success。MVP 目标是 ALFWorld success ≥20%（从 SFT baseline 6.25% 出发需 ~3x 提升）。

决策链：D018(SFT 不够) → D020(两阶段 SFT 通过) → D021(格式不匹配) → D025(sparse GRPO 终止) → D026(RAGEN GRPO 终止, pivot verl-agent) → D027(kill exp024)。

**易错点**：
- exp025 崩溃是环境问题不是算法问题，不要因此质疑 verl-agent 路线
- verl-agent 用 Ray 做分布式，依赖链比 RAGEN 复杂（ray, vllm, verl 等），环境搭建可能需要多轮调试
- 不要混淆 RAGEN checkpoint 和 verl-agent 期望的模型格式，SFT checkpoint 兼容性待验证


---
