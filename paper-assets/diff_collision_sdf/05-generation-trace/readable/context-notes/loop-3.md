# director / loop_3.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`a2bf96b2bfce3a6595bb.json`](../../sessions/a2/a2bf96b2bfce3a6595bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-25T04:22:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807 cuda:0-3（4张）、westd-45947 cuda:0-1（2张），严禁用其他服务器/设备
- 两台服务器当前 SSH Authentication failed（密钥不匹配），/gpu API 可达但 SSH 不通，等用户提供新密码
- 6 个实验被 cron 标记 failed 实际是 SSH 监控失败非训练失败——SSH 恢复后必须逐一核实 checkpoint，不要直接重跑
- 论文真源在本地 `projects/diff_collision_sdf/docs/paper/`，不在远程服务器
- 项目仍在 MVP 阶段，不要调 `complete_mvp()`，Claim 4 的 30K eval 还没做

### 2. 🖥️ 基础设施快照
- **westd-35807** (connect.westd.seetacloud.com, root): 4× NVIDIA RTX PRO 6000 Blackwell (98GB)，工作目录 `/root/colliforce-vla`，SSH 端口待确认
- **westd-45947** (connect.westd.seetacloud.com, root): 2× NVIDIA RTX PRO 6000 Blackwell (98GB)，工作目录 `/root/colliforce-vla`，SSH 端口待确认
- Python/conda 路径：上次连接时为 aml-train 镜像（conda base），具体路径 SSH 恢复后确认
- 模型/数据/checkpoint 均在 `/root/colliforce-vla/` 下，HF cache 在 `/root/autodl-tmp/.hf_cache`
- 活跃进程：SSH 不可达无法确认，LoRA baseline 2-seed 训练可能已跑完（wall_clock ~17h）
- 本地论文：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex`，已编译 16 页 PDF

### 3. 📊 当前状态
**刚完成**：6 项接受率改进全部落地并编译通过（VLA Safety Survey 引用、Abstract 强化、caption 改进、Beyond Binary Success 引用、Appendix 计算成本框架）。Reviewer 逐项验证 PASS。

**RUNNING/待核实实验**（registry 状态 vs 实际）：
- `train_pi05_lora_baseline_s0` — 标记 failed（SSH 监控失败），实际可能完成 30K
- `train_pi05_lora_baseline_s1` — 同上
- `train_pi05_a1_obj_s1_l005` — 标记 failed，SSH 中断前可能完成
- `train_pi05_a1_obj_s1_l01` — 同上
- `train_pi05_a1_obj_s2_l005` — 同上
- `train_pi05_a1_obj_s2_l01` — 同上

**等待中**：Agent 已派 Worker 诊断 SSH 连接（大概率也失败）。核心阻塞项是用户提供新 SSH 密码。

### 4. 📋 待办
- 用户发来 SSH 密码 → `remove_server` + `register_server` 更新凭据 → 派 Agent 验证连接
- SSH 恢复 → 检查 6 个 "failed" 实验的 checkpoint 存在性 → 存在则更新 registry conclusion=success → 启动 6 模型 30K eval
- LoRA baseline checkpoint 确认 → eval 跑完 → 填充 §5.4 Table 的 LoRA-only 行（归因分析：SDF vs LoRA 贡献）
- 30K eval 数据到位 → 填充 §5.4 所有 placeholder + Appendix 计算成本 + 替换 displacement histogram mock
- westd-35807 4 GPU 空闲恢复后 → 并行派：30K eval + λ_sdf=0 Phase 2 ablation + spatial_bowl 第 2 task（spatial_bowl deadline 5/28）
- 所有数据到位 + 论文更新 → 派 Reviewer 重新评估接受率（目标 45%+）→ 满足则 `complete_mvp()`

### 5. 🎯 战略上下文
- **核心 story**：VLA safety 指标被 action collapse 污染（fake safety），提出 CARf 修正 + SDF aux loss 在强 VLA 上的正面效果。Analysis paper with positive method contribution。
- **决策链**：D009/D010 终止 runtime refinement → D011 启动 training-time SDF → D015/D016 10K positive → D017 碰撞重分布发现 → D018 确认 gradient correction 结构性失败（collapsed policy 不接受修正，需 base capability 前提）
- **易错点 1**：6 个标记 failed 的实验大概率训练已完成，SSH 恢复后先查 checkpoint 再决定是否重跑，不要浪费 GPU 时间
- **易错点 2**：spatial_bowl deadline 5/28，SSH 恢复后要优先分配 GPU 给它（同时跑 30K eval）
- **易错点 3**：论文当前所有不依赖数据的改进已穷尽（~9.6/10），下一步提分完全依赖 30K eval 数据 + LoRA 归因 + spatial_bowl 泛化性
- **接受率**：当前估 38-40%，6 项改进 +~2%，30K 数据 + LoRA 归因 + spatial_bowl 预计再 +5%，目标 45%+


---
