# director / loop_2.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`309dd2ea5a0e1b906637.json`](../../sessions/30/309dd2ea5a0e1b906637.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T18:23:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 98GB）
- OLMo 模型路径必须用 `olmo-1b-hf`，不是 `olmo-1b`（后者缺 HF 格式文件）
- 项目配置 server 名必须与实际一致（曾因 westb-52439 事件导致 cron 误杀实验）
- 审稿阶段已启动（review_chat_id: oc_db3bd143165620ee6950e6ef0826eec8），论文格式/投稿由 Group C 负责，你不参与
- Dream D002 的 6 项结构性硬约束写在 ROADMAP"Dream-Derived 论文硬约束"一节，论文写作必须满足

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2 (connect.westb.seetacloud.com)，工作目录 /root/autodl-tmp/recursive_gen_depth_est
- GPU：cuda:0, cuda:1（2× RTX PRO 6000 Blackwell 98GB）
- Python 环境：未确认 conda/venv，Agent 连接时自动探测
- 模型：Pythia-1.4B / OLMo-1B (olmo-1b-hf) / GPT-2 XL，均在远程
- W&B / HF cache：未配置
- 活跃进程：Agent 正在处理 OLMo false-failure 修正 + pythia_topk50 代码提交结果，queue depth=3

### 3. 📊 当前状态
**刚做完**：Dream D002 三档分析 → 提取 6 项行动项写入 framing → 启动 3×3 矩阵补全（3 模型 × 3 解码策略）

**实验状态**（3×3 矩阵进度 2/9 done）：
- `pythia_temp09_001` — ✅ DONE (success)，Pythia nucleus+temp09 完成
- `cross_model_olmo_002` — registry 显示 RUNNING，但 Reviewer 报告 pipeline 实际已完成，Agent 正在修正 false-failure（第二次了）
- `cross_model_gpt2xl_001` — ANALYZING，GPT-2 XL nucleus depth-2 生成 ~100%
- `pythia_topk50_001` — RUNNING/PREPARING，Agent 刚提交代码

**Agent 队列**（depth=3，正在处理）：
1. [处理中] Reviewer critical：OLMo false failure 修正
2. [排队] 紧急指令：OLMo 第二次 false failure 立即修正
3. [排队] Worker done × 2（OLMo 诊断 + pythia topk50 代码提交）

### 4. 📋 待办（条件触发式）
- Agent 消化完队列 → 检查 OLMo 是否已正确标记 success + eval 完成 → 立即排 OLMo temp09 到 cuda:0
- GPT-2 XL nucleus ANALYZING 完成 → eval → 排 GPT-2 XL temp09 到 cuda:1
- Pythia topk50 代码就绪 + GPU 空出 → 提交运行
- 3×3 矩阵 9/9 完成 → 启动 plan_006 Atlas + plan_004 DCOL
- Atlas 生成时同步出图（AUC decay, feature trajectory, heatmap, confusion matrix）
- 写作前必须完成 multi-seed evaluation（≥3 seeds, ~6 GPU·h）

### 5. 🎯 战略上下文
- **核心结论**：递归生成深度可从统计特征高精度区分（MVP 4-class acc 78.2%），D001 确认方向成立
- **Framing 重心**（D002 决策）：Atlas/EDD 为 primary contribution，DCOL 为 secondary。三档 Dream 一致建议此方向
- **最容易判断错的事**：OLMo 实验反复出现 false failure（registry 标 failed 但实际成功），已出现两次。看到 OLMo failure 先检查日志再信 registry
- **容易踩的坑**：Agent 队列里有重复/冲突指令时用 `replace_agent_queue` 清理；3×3 矩阵排队策略是"每模型 nucleus 完成后立即接 temp09 → topk50"，不要打乱顺序
- **GPU 预算**：P0 剩余 ~35 GPU·h (~18h on 2 GPUs)，P0+P1 ~83 GPU·h (~2 days)


---
