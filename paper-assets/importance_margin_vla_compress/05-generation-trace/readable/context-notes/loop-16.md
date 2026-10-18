# director / loop_16.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`100739276e1c0aae841b.json`](../../sessions/10/100739276e1c0aae841b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-26T13:32:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（每台服务器 4 张），严禁使用其他 GPU
- 4 台服务器：westd-27271, cqa1-33015, westd-41074, westd-38929，不可跨项目占用
- C001 约束：Spatial suite 对比禁止用 LoRA baseline (6.2%) 作基准，必须用 official baseline 或 full-FT
- **CoRL 2026 Paper DDL: May 29**（距今 3 天），Abstract 已提交
- 审稿阶段已启动（review_chat_id: oc_83179cdc26b856fbbaf531d145edb3bd），Group C 独立处理论文格式/投稿

### 2. 🖥️ 基础设施快照
- 服务器均为 AutoDL，工作目录 `/root/autodl-tmp/importance_margin_vla_compress`
- 账户：root（所有服务器）
- westd-27271: 2 GPU 在用（cuda:0, cuda:1）
- westd-38929: 4 GPU 满载
- westd-41074: 4 GPU 满载（cuda:1 刚部署 Attn k=0.5 Object seed42）
- cqa1-33015: 4 GPU 满载（π0.5 系列实验）
- Provenance 覆盖率 70/73，3 个 tier-3 gap 待补

### 3. 📊 当前状态
刚完成本轮 session 6 个新结果收割 + 14/14 GPU 满载部署 + Abstract 提交确认 + D237 position encoding sensitivity 叙事升级。

**13 个 RUNNING 实验**（cliff curve 填充）：
- westd-38929: Rnd k=0.85 Goal / Rnd k=0.5 Long / Attn k=0.7 Goal / Attn k=0.85 Long
- westd-41074: Rnd k=0.85 Long / L2n k=0.85 Obj / Attn k=0.7 Obj / L2n k=0.75 Obj（cuda:1 部署中 Attn k=0.5 Obj）
- westd-27271: L2n k=0.7 Goal / Rnd k=0.7 Goal
- cqa1: π0.5 Rnd k=0.85 Long v2 / π0.5 Attn k=0.75 Long / π0.5 Attn k=0.5 Long / π0.5 Attn k=0.85 Long

**等待中**：91 个 PENDING 实验（大部分是 cliff curve 候选点）；Agent 已 stall 16h 被 RESET。

### 4. 📋 待办（条件触发式）
- Agent RESET 完成 → 立即检查 13 个 RUNNING 实验状态，收割已完成的结果
- 任一 cliff curve 实验完成 → 更新 ROADMAP 表格，部署下一个 PENDING 到空出的 GPU
- OpenVLA Object/Goal/Long 三方法 cliff curve 数据齐全 → 整合 cliff curve 图表数据，通知 Paper Agent patch
- Provenance 3 个 tier-3 gap 补全 → 通知 Paper Agent 更新
- 所有 cliff curve 完成 + Paper Agent 收敛 → May 29 提交

### 5. 🎯 战略上下文
- **核心结论**：VLA vision token 压缩的 scoring method × connector × task 三维交互。L2norm 在 OpenVLA（linear proj）上单调优于 Random/Attn，但在 Long suite 该优势消失——因为 position encoding 敏感性（D237 确认）
- **关键证据链**：crossover table 16/16 完成 ✅；π0.5 L2norm 完美单调 ✅；Random V-shape 非单调性确认为真实现象 ✅；zeromask 实验证明 Random 置零后性能恢复（D234）
- **最容易判断错的事**：westd-41074 cuda:1 在 session 末尾刚从 Random k=0.85 Object 改派为 Attn k=0.5 Object seed42，Agent stall 前 Worker 正在部署，需确认是否成功启动
- **易踩坑**：M129/M130 教训——所有实验必须 tmux 部署，部署后必须验证 GPU PID；report.md 资源状态段经常漂移，以 SSH 实际查询为准


---
