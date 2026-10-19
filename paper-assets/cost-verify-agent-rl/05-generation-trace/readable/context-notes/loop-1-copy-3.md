# reviewer / loop_1.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`ed091b4e098b2a770d25.json`](../../sessions/ed/ed091b4e098b2a770d25.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T21:43:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1** only（bjb1-17606 上只有这两张卡分配给本项目）
- 模型路径软链接：`/root/cost-verify-agent-rl/models/Qwen3-1.7B` → `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`，不要重新下载
- conda 环境，不是 venv：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- ALFWORLD_DATA 必须设为 `/root/autodl-tmp/alfworld`，否则训练脚本找不到数据
- Reviewer 只读：不执行实验、不修改文件，唯一输出通道 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- 服务器：**bjb1-17606** (root)，2× RTX PRO 6000 Blackwell 94GB，CUDA 12.8
- 工作目录（远程）：`/root/cost-verify-agent-rl/RAGEN/`
- Python：`/root/miniconda3/bin/python` (3.12.3)，PyTorch 2.10.0+cu128，vLLM 0.18.1
- 模型：Qwen3-1.7B **base**（非 Instruct），路径见上
- 数据：ALFWorld 3553 train / 140 eval_in_distribution
- B-IAVR 代码模块：`/root/cost-verify-agent-rl/RAGEN/ragen/biavr/`（verify_mechanism / action_canonicalize / pre_action / reward，已有单元测试）
- prompt 截断实现：`ctx_manager.py:461 _apply_max_length()`，通过 `agent_proxy.max_prompt_length` 配置
- 活跃进程：**exp003** PID 157852 (tmux)，Ray workers 161295/161296，~41.4GB/GPU

### 3. 📊 当前状态
刚完成 worker_code_prompt_truncation_v2 审查。exp003（Phase A 全量 100-step 训练）已启动，正在跑初始 validation（140 games，预计 ~10min）。

Registry 关键条目：
- **exp003** PREPARING（实际 RUNNING）：Phase A v3，base Qwen3-1.7B，128 traj/step，max_prompt_length=4096，100 steps
- exp_001 / exp_001b / exp_002：全部 DONE/failed
- exp_003_dryrun / dryrun2 / dryrun3 等：PREPARING 僵尸条目，未清理

无等待中的 Worker 回调。需要主动监控 exp003 前几步。

### 4. 📋 待办
- exp003 完成初始 validation → 检查 val success=0%（expected）+ invalid_action 率（应 ~73% 类似 exp_002）
- exp003 step 1 完成 → **核心验证点**：(1) 无 prompt length crash = 截断生效 (2) pg_loss 非零 = GRPO 有学习信号 (3) success > 0 = bootstrap 成功。如果 advantages 仍为零 → 立即 CRITICAL
- exp003 step 1 完成 → 校准新的 step/h 速率（128 traj 比之前 16 traj 慢很多）
- exp003 Ray dashboard_agent 崩溃 → 建议加 `RAY_DISABLE_DASHBOARD_AGENT=1`
- exp003 达到 step 20（save_freq=20）→ 检查 checkpoint 保存 + val metrics 趋势
- exp003 达到 ~76% success → Phase A PASS，可启动 Phase B（biavr 模块已就绪但未集成到训练循环）
- exp003 到 step 100 仍 <60% → Phase A FAIL (kill)，需要排查原因

### 5. 🎯 战略上下文
- **D001**：MVP = ALFWorld + Qwen3-1.7B 单环境验证 B-IAVR
- **D002**：全量微调（非 LoRA），匹配 Self-Guide 论文
- **核心教训**：Self-Guide 论文证明 Qwen3-1.7B **base** 可以通过 GRPO 达 72.7%，无需 Instruct。之前 exp_001/001b 失败根因是 batch size 太小（16 vs 128 traj/step），**不是** base vs Instruct 的问题。我之前错误建议换 Instruct，后来已修正。
- **最易判断错的事**：看到 base 模型 95% invalid action 就断定"必须用 Instruct"——错。128 traj/step + response_length=1024 + format_penalty=-0.1 才是关键。Self-Guide 用 base 模型 100 步就到 72.7%。
- **Phase B biavr 模块**：工具库已就绪（reward / Lagrangian / action compare / VERIFY token parse），但**未集成到 RAGEN 训练循环**（无 rollout hook、无 Phase B config、无 a_pre 前向 pass 集成）。Phase B 需要大量工程。
- **GPU 预算**：exp_001/001b/002 合计 ~3 GPU-hours 浪费。exp003 100 步 × 128 traj 预计耗时较长，首步速率待校准。总预算 200h H100-equivalent。


---
