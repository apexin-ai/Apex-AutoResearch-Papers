# director / loop_8.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`43a55a3012723c0e51c5.json`](../../sessions/43/43a55a3012723c0e51c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-25T17:24:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894:0-3 + westd-34685:0-3（C001），严禁使用其他卡
- C002：cutoff 实验禁止 resume（batch_idx bug 未完全修复）
- D050：旧 v1 BN 数据不得与新 v2 数据混合做 ANOVA——代码版本与归一化类型完美共线（所有 BN=v1 May21, 所有 LN=v2 May24），交互效应 p=0.025 不可信
- D052：v1≠v2 已确认（Full OCC BN v2 CAR=0.746 vs v1 CAR=0.832，同 seed 差 8.6pp），v1 数据全部不可用于 factorial
- 用户要求摘要不罗列数字（叙述性语言）
- 审稿阶段已启动（review_chat_id: oc_faa96524df7d6444f5c8cbc48d5a616b），论文格式/投稿由 Group C 负责

### 2. 🖥️ 基础设施快照
- **westd-10894**: connect.westd.seetacloud.com, root, 代码路径 /root/occsafe_vla, v2 代码 ✅
- **westd-34685**: connect.westd.seetacloud.com, root, 代码路径 /root/occsafe_vla, v2 代码 ✅（finetune.py 已修复 occ_norm_type 参数）
- 模型：/root/autodl-tmp/models/openvla-7b/（pretrained baseline）
- Eval 脚本：evaluate_safelibero.py，--num_rollouts 50，输出 TSR+CAR
- CKA 脚本：/root/occsafe_vla/run_command.sh（已验证，CUDA_VISIBLE_DEVICES=3）
- W&B：未配置
- 磁盘：34685 仅剩 2% (819G/879G)，10894 50% (425G/879G)

### 3. 📊 当前状态
**刚做的**：发了 replace_agent_queue 综合指令，清除 21 条重复 cron 通知。两台服务器疑似同时崩溃——34685 dose-response 4 个实验在 82% (step ~41000) 同时死亡，10894 的 s3 实验也可能崩溃（cron 报告进程退出）。

**等待 Agent 回复**：两台服务器全面状态检查结果。指令是：
- 34685 确认空闲后立即启动 D051 v2 rebuild（4 runs: detach_bn_v2_s0/s1/s2 + full_occ_bn_v2_s1）
- 10894 检查 s3 (ablation_occ_detach_s3 / mvp_occ_s3 / full_occ_ln_s3) 存活状态

**Registry**: 96 个实验，8 RUNNING（可能已崩溃），6 PENDING，82 DONE (65 success)

### 4. 📋 待办
- Agent 汇报服务器状态 → 34685 四卡空闲则确认 D051 启动成功；10894 s3 崩溃则决定 resume/restart
- s3 (ablation_occ_detach_s3) eval 完成 → **叙事门控决策**：CAR<0.750→Branch A "aux heads hurt safety"；CAR 0.770-0.780→Branch B "gradient flow hurts"；CAR>0.780→Branch C "detach helps via regularization"（Reviewer 三分支方案已就绪）
- s3 CKA 完成 → 漂移→部分保留 drift 叙事；无漂移→转 representation-behavior dissociation
- D051 v2 rebuild 完成（~启动后 13h）→ eval → v2 ANOVA 重算 → 论文重写
- 论文重写完成 → submit_paper_to_review 提交审稿

### 5. 🎯 战略上下文
- **CoRL 2026 Paper DDL May 29**，Abstract 已提交。核心危机是 factorial 代码版本共线（D047→D052 决策链），正在用 v2 代码重建 BN 格
- **原始交互效应 (p=0.025) 几乎肯定不成立**：Reviewer 估计存活概率 10-15%。v2 Full OCC BN CAR=0.746 ≈ Full OCC LN CAR=0.743，BN 优势消失
- **CKA drift 数据 (0.539/0.312) 确认为旧代码 bug artifact**（D049），论文中的 "catastrophic representational drift" claim 必须移除
- **最容易判断错的事**：Agent 之前错误报告 v1≈v2 等价性（把 v1 mvp_occ_s0 CAR=0.832 误标为 v2 retrain_s0 的数据）——任何跨版本比较必须从 registry 拉完整指标并列验证（M060）
- **34685 磁盘仅 2%**：启动新训练前确认空间足够
- Dose-response 3rd seed 实验在 82% 崩溃，有 40k checkpoint 但 C002 禁止 resume——低优先级，先完成 D051


---
