# director / loop_19.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`c9e9e30ac039ea65c9bd.json`](../../sessions/c9/c9e9e30ac039ea65c9bd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-27T08:34:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-27271 (2 GPU), westd-38929 (4 GPU), westd-41074 (4 GPU), cqa1-33015 (4 GPU)，共 14 张
- cqa1/AutoDL 上所有 π0.5 实验启动必须加：`HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl`（M147 教训，缺了会 ConnectError 崩溃）
- π0.5 Attn k=0.95/0.9/0.85 strict 已全部 DONE (D250/D251)，**绝对不要重跑**
- Worker 部署实验前必须查 registry 确认不重复（M146：上轮 Worker 未查 registry 重复部署了已完成实验）
- 实验硬截止 May 28 20:00 BJT (C002)，CoRL 2026 论文 May 29

### 2. 🖥️ 基础设施快照
- 4 台服务器，代码路径均为 `/root/autodl-tmp/importance_margin_vla_compress`
- westd-41074 代码已同步到 464 行（之前 426 行差异已确认不影响 strict 逻辑正确性）
- HF cache: `/root/autodl-tmp/.hf_cache`（cqa1 必须离线模式）
- 无 wandb 配置，实验结果通过 JSON 文件收割
- cron 监控覆盖所有 RUNNING 实验（本 session 修复了 7 个缺失 cron）

### 3. 📊 当前状态
**已下达但 Agent stall 未执行的关键决策**：cqa1 GPU1 上的 OV Attn k=0.95 Goal backup 是多余的（结果 76.8% 已确认），应 kill 后部署 π0.5 Random k=0.5 Long strict。

**确认完成的关键结果**：
- D251: π0.5 Attn 全线 strict 确认 max bias <2pp，论文可安全用 lenient 值
- D252: OV Random k=0.95 Goal = 78.4%，Goal k=0.95 三方法均≈baseline
- D253: π0.5 Random k=0.75 strict = 63.0% (Δ+0.6pp)，Random 污染偏差也极小

**运行中（约 14 GPU）**：
- OV Long k=0.95: L2norm/Attn/Random (westd-38929) + L2norm k=0.75
- OV Goal: Attn k=0.5 (cqa1 GPU3)
- OV Object: L2norm k=0.85 重跑 (westd-27271)
- π0.5 strict: Random k=0.95 + L2norm k=0.95 (westd-41074 GPU2/3), Random k=0.7 (cqa1 GPU0), L2norm k=0.85 (cqa1 GPU2)
- westd-41074 GPU0: OV Random k=0.95 Long

### 4. 📋 待办
- Agent 新 session 就绪 → 发综合指令：kill cqa1 GPU1 backup → 部署 π0.5 Random k=0.5 strict（加离线 flags）
- OV Long k=0.95 三方法完成 → 收割结果，Long cliff curve 补全
- OV Goal Attn k=0.5 完成 → Goal cliff curve 完全闭合
- π0.5 Random k=0.7 strict (cqa1 GPU0) 完成 → 收割，与 lenient 62.4% 对比（注意：上次因缺离线 flags 失败过，确认这次成功）
- π0.5 Random k=0.5 strict 完成 → π0.5 cliff curve 最后 ⚠️ 值验证
- 全部 cliff curve 闭合 → 通知 Paper Agent 更新论文数据

### 5. 🎯 战略上下文
- 核心结论链：D250→D251→D253 确立"cqa1 污染偏差 <2pp，所有方法 lenient 值可用于论文"。这大幅减少了必须 strict 重跑的实验量
- OV cliff curve 主要缺口是 Long k=0.95（三方法均在跑）和 Goal Attn k=0.5
- π0.5 cliff curve 中 Attn 全线不需要 strict（D251），只有 Random 和 L2norm 仍有少量 ⚠️ 值待验证
- **最易判断错的事**：Agent 反复 stall+rotation（本 session 经历 5+ 次），导致队列消息过时。新 session 第一件事用 replace_agent_queue 发最新综合指令，不要让旧消息通过
- **M145 教训**：Reviewer 更正了 CRITICAL 后，必须立即 replace_agent_queue 清除基于旧报告的指令，否则 Agent rotation 后会执行过时的 kill 命令


---
