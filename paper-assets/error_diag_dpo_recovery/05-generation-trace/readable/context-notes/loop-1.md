# director / loop_1.md

**error diag dpo recovery** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`f7a3d37ba391f7f72c36.json`](../../sessions/f7/f7a3d37ba391f7f72c36.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T14:05:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单：仅 cuda:0 和 cuda:1**。已发生两次越界（cuda:2, cuda:3），Manager 两次警告。第三次不可接受。
- 所有 GPU 命令**必须**以 `CUDA_VISIBLE_DEVICES=0` 或 `CUDA_VISIBLE_DEVICES=1` 开头，不依赖脚本内 `--gpu` 参数
- 禁止 `device_map="auto"`，必须用 `device_map=f"cuda:{args.gpu}"`
- GPU 3-5 属于其他项目（cost-verify-agent-rl 等），绝不触碰

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，`ssh -p 21977 root@connect.cqa1.seetacloud.com`，密码 `request_secret(key_id="ssh_password_cqa1_21977")`
- 工作目录：`/root/autodl-tmp/error_diag_dpo_recovery`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 代码：`/root/autodl-tmp/error_diag_dpo_recovery/src/`（dmpo_loss.py, dmpo_trainer.py, data_utils.py, train_etadn.py, collect_trajectories.py, construct_preference.py, classify_errors.py）
- 模型：Qwen3-8B `/root/autodl-tmp/.hf_cache/Qwen3-8B`（16.4GB），Qwen3-14B-AWQ 已下载（9.4GB，同 cache 目录）
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- 磁盘：根分区 21G free，数据盘 87G free
- trl 版本：1.4.0
- 活跃进程：可能还有 screen session `traj_p0`（cuda:0 轨迹收集），但已下令停止。需要 Agent 确认

### 3. 📊 当前状态
刚做完数据策略转向决策（D009）：放弃 self-correction 收集（0% 成功率确认），改用 ETO expert trajectories as chosen + 8B 失败轨迹 as rejected 构建 DPO pairs。

已完成：代码全部就绪 + dry-run 通过（loss=0.6931, VRAM=8GB）+ 错误分类 taxonomy + DMPO pipeline 设计 v2 + γ_e 概念修正。
已收集：~52 条 ALFWorld 失败轨迹（全部 reward=False）。
等待中：Agent 处理 D009 新策略指令（停止收集 → 获取 ETO expert data → 错误分类 → 构建 DPO pairs → 7-run 训练）。

Registry 无正式实验记录（MVP 阶段，尚未提交正式实验）。

### 4. 📋 待办
- Agent 汇报 ETO expert data 获取完成 → 确认 task mapping（失败轨迹 vs expert 轨迹的任务对齐）
- 错误分类完成 → **检查 P1 gate**：correction horizon 是否 action < verification < planning（p<0.05）
- P1 pass → 批准 7-run DPO 训练（ETADN×3 + DMPO×3 + DPO×1）
- P1 fail → 项目终止或 pivot
- 7-run 训练完成 → **检查 P2 gate**：ETADN > single-γ ≥3%（3 seeds 平均）+ **P3 surprise check**
- P1+P2+P3 全 pass → `complete_mvp()` + 向 Manager 申请加卡（4 张）+ 展开 WebShop/ScienceWorld
- MVP 通过后 full paper 阶段需要补 SFT→explore→self-correction pipeline（当前 expert-as-chosen 只是 MVP 捷径）

### 5. 🎯 战略上下文
- **KILL_triage idea（19% 接受率）**，novelty 弱是 3/3 共识。用户明确选择继续冲 May 25 ARR。
- 决策链：D001（启动）→ D002（Reviewer 修订 MVP）→ D003（用户确认 A）→ D004（4 卡冲 May 25）→ D005（14B 替代 32B）→ D006（QLoRA + 现代栈）→ D007-D008（GPU 越界事故×2）→ D009（expert as chosen 策略转向）
- **最容易判断错的事**：0% 成功率不代表 pipeline 失败——我们的 DPO pairs 来自 expert vs failure step-level 对比，不需要模型自己生成成功轨迹。但 Reviewer 可能再次 flag 这个问题，需要坚持当前策略除非有新证据。
- **最容易踩的坑**：GPU 越界。Agent 的 Worker 会传错 GPU 编号（已发生两次）。每次看到 Agent 启动 GPU 进程时主动确认 CUDA_VISIBLE_DEVICES。
- Manager 只批了 2 卡用于 MVP，加卡需 MVP 通过后重新申请。
- ScienceWorld 被选为 post-MVP 第一扩展 benchmark（优于 WebShop）。
- φ(t,T) 归一化：Σφ>1 是 DMPO 设计意图，γ=1 特殊处理为 1/T。


---
