# director / loop_5.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`272309daf8fa2a1abe54.json`](../../sessions/27/272309daf8fa2a1abe54.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-26T12:31:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807:cuda:0/1/2/3 + westd-45947:cuda:0/1 共 6 张，严禁使用其他卡
- plan_015 已预批准（跳过审批流程），Agent 可直接注册+启动，不需要等 approve_experiment
- λ=0.1 实验（plan_009）是决定性实验——不可中断、不可抢占其 GPU（westd-35807 cuda:1+2）
- D030 已确认：D027 "catastrophic TSR collapse" 是 eval rotation bug 伪影，真实降幅 ~20pp（74.7→51.5%），禁止再用 catastrophic collapse 叙事

### 2. 🖥️ 基础设施快照
- **westd-35807**：工作目录 /root/colliforce-vla，4 GPU（3090/4090 级别）
- **westd-45947**：工作目录 /root/colliforce-vla，2 GPU，account=root
- Python/conda：aml-train 镜像，conda base 环境（/root/miniconda3/bin/python）
- 无 W&B 配置，无 Git 配置
- rotation-fixed eval 脚本已部署在 westd-35807 上
- 活跃 tmux sessions：spatial_bowl SDF s0 (cuda:0)、λ=0.1 s0 (cuda:1)、λ=0.1 s1 (cuda:2)、LoRA s2 (westd-45947 cuda:0)、reeval batch2 (westd-45947 cuda:1)

### 3. 📊 当前状态
**刚做完**：合并 Agent 积压队列（4→1），发出 plan_015 预批准+启动指令。Reviewer 16h 到限一起重置。

**RUNNING 实验**：
| 实验 | 服务器:GPU | 进度 | ETA |
|------|-----------|------|-----|
| train_pi05_a1_spatial_bowl_s0_l005 (plan_007) | westd-35807:0 | 74% | ~10h |
| train_pi05_a1_obj_s0_l01_high (plan_009 s0) | westd-35807:1 | 46% | ~21h |
| train_pi05_a1_obj_s1_l01_high (plan_009 s1) | westd-35807:2 | 44% | ~21.5h |
| train_pi05_lora_baseline_s2 (plan_013) | westd-45947:0 | 37% | ~24h |
| reeval batch2 (4 evals 串行) | westd-45947:1 | 1/4 进行中 | ~2.5h |

**等待中**：
- Agent 处理综合指令 → 启动 plan_015 在 westd-35807:cuda:3
- step curve eval worker 已完成，结果待 Agent 读取汇报
- reeval batch2 新数据增量汇报

### 4. 📋 待办
- Agent 处理完当前消息 → 确认 plan_015 已在 cuda:3 启动（如未启动，再催）
- reeval batch2 全部完成（~22:45 CST）→ 更新所有实验修正数据，重算 SDF vs LoRA 差异
- LoRA s2 训练完成（~24h）→ 立即 eval，完成 3v3 seed 统计对比
- spatial_bowl SDF s0 完成（~10h）→ eval + 与 plan_015 LoRA control 配对对比（plan_015 可能晚 23h）
- **λ=0.1 eval（~21h）→ 最高优先级决策点：Scenario A (全面 redundant) vs B (dose-dependent)**
- λ=0.1 eval 后 → 确定 Claim 3 最终叙事 → 更新 paper_framing.md → 启动写作

### 5. 🎯 战略上下文
**核心结论链**：
- D025: λ≤0.01 SDF=0pp（SDF redundant at low λ），标记 provisional 等 λ=0.1
- D029: Phase 2 (SDF→λ=0) ≈ LoRA-only → SDF 无持久权重编码
- D030: TSR "catastrophic collapse" 是 eval bug，实际 ~20pp 降幅
- Re-Dream: "SDF redundant" framing median=reject，叙事需要 λ=0.1 救场

**新数据信号**：SDF λ=0.005 s0 reeval → TSR=55.5%, CAR=57.0%（vs LoRA mean 51.5%/54.5%，+4pp/+2.5pp）。单 seed 有噪声，但如果 s1/s2 确认，低 λ 可能也不完全 redundant——这会改变叙事方向。batch2 数据是关键。

**易踩的坑**：
- 不要把旧 eval 数据（rotation bug 之前的）当真——所有有效数据以 reeval v2/v3 为准
- Agent 消息队列容易积压（worker done 频繁），定期 get_agent_queue_status 检查是否卡住
- plan_015 已预批准但可能 Agent 还没执行——接手后第一件事确认 cuda:3 是否在跑


---
