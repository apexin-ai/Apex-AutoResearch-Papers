# agent / loop_15.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`118544c24dbd016663f2.json`](../../sessions/11/118544c24dbd016663f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-28T05:59:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，当前 4 台服务器各自分配见 ROADMAP GPU 表
- westd-27271 只有 GPU0/GPU1；westd-38929 有 GPU0/1/2/3（GPU2 空闲）；westd-41074 有 GPU0/1/2/3；cqa1 有 GPU0/1/2/3
- π0.5 eval 必须用 strict metric（非 lenient），论文数据全部基于 strict 版本（D265 教训：旧版 lenient 结果因 zero-masking bug 不可用）
- 脚本内 GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- **实验硬截止 May 28 20:00 BJT，CoRL 2026 Paper May 29 提交**——距截止约 11h（从上次 ROADMAP 更新算起，现在更近）

### 2. 🖥️ 基础设施快照
- **westd-27271**: π0.5 eval 服务器，工作目录 ~/runs/importance_margin_vla_compress/
- **westd-38929**: OV + π0.5 eval，GPU2 空闲待部署
- **westd-41074**: π0.5 Attn + Random eval，4 GPU 全满
- **cqa1-33015**: π0.5 L2norm + Random eval，4 GPU 全满
- 所有服务器用 aml-train 镜像，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 日志路径统一：`~/runs/importance_margin_vla_compress/{exp_id}.log`

### 3. 📊 当前状态
**刚发生的事**：收到 CRON 失败回调——`eval_pi05_l2norm_k075_long_seed42_strict_w27` 进程异常退出。但 registry 中该实验已标记 `DONE/success`（D266 记录了其结果，lenient=73.4%）。这是一个**重复/滞后的 CRON 通知**，实验结果早已被上一个 session 处理完毕，无需诊断。

**10 个活跃 CRON 监控的 RUNNING 实验**（reconcile 确认全部仍在跑）：
| exp_id | 服务器 | 内容 |
|--------|--------|------|
| eval_pi05_attn_k05_long_seed42_strict_w41 | w41 GPU1 | π0.5 Attn k=0.5 strict ~2h |
| eval_pi05_attn_k075_long_seed42_strict_w41 | w41 GPU3 | π0.5 Attn k=0.75 strict ~3h |
| eval_pi05_attn_k07_long_seed42_strict_w41 | w41 GPU0 | π0.5 Attn k=0.7 strict ~3h |
| eval_pi05_attn_k075_long_seed42_strict_cqa1 | cqa1 GPU? | π0.5 Attn k=0.75 strict |
| eval_pi05_l2norm_k09_long_seed42_strict_cqa1 | cqa1 GPU3 | π0.5 L2norm k=0.9 strict ~30min |
| eval_pi05_l2norm_k07_long_seed42_strict | cqa1 GPU2 | π0.5 L2norm k=0.7 strict ~2h |
| eval_pi05_l2norm_k05_long_seed42_strict | w38 GPU3 | π0.5 L2norm k=0.5 strict |
| eval_pi05_random_k09_long_seed43_strict_w41 | w41 GPU2 | Random k=0.9 seed43 ~3h |
| eval_openvla_attn_k075_long_seed42_v3 | w38 GPU1 | OV Attn k=0.75 ~7h |
| eval_openvla_random_k095_long_seed42_v3 | w38 GPU0 | OV Random k=0.95 ~7h |

**待处理**：
- westd-38929 GPU2 空闲，应部署实验（ROADMAP 标记待处理）
- 95 项 QUEUED 实验等待 GPU（含 seed 复制 + 补充数据点）

### 4. 📋 待办（条件触发式）
- eval_pi05_l2norm_k09_long_seed42_strict_cqa1 完成（~30min 级）→ 收割 strict 值，更新 π0.5 L2norm cliff curve k=0.9 格
- eval_pi05_l2norm_k07_long_seed42_strict 完成 → 更新 k=0.7 格
- w41 上 3 个 Attn strict 完成 → 填 π0.5 Attn k=0.5/0.7/0.75 strict 格，cliff curve 闭合
- OV Attn k=0.75 v3 + OV Random k=0.95 v3 完成（~7h）→ OV Long cliff curve 最后两格闭合
- **全部 cliff curve 闭合 → 通知 Director，Paper Agent 更新 cliff curve figures → May 29 提交**
- westd-38929 GPU2 空闲 → 部署 π0.5 L2norm k=0.95 seed43 strict（error bar 实验）或其他 QUEUED 高优实验
- eval_pi05_l2norm_k075_long_seed42_strict_w27 的 CRON 失败通知是滞后重复，不需要重跑

### 5. 🎯 战略上下文
- **核心发现**：VLA vision token 压缩的 importance margin——scoring method × connector × task 三维交互。π0.5 和 OV 方法排序翻转（π0.5: L2norm > Attn > Random; OV: Attn > L2norm），支持 2-Axis Framework
- **Random U-shape 已确认**：π0.5 Random strict = 49.8→66.0→63.0→🏃→34.2→60.6，k=0.9 valley 是关键发现
- **D265 教训**：π0.5 Attn 旧版 lenient 结果全部不可用（zero-masking 而非物理移除），论文只能用 strict 版本
- **易错点**：
  - 不要混淆 lenient 和 strict 指标——本项目论文全用 strict
  - eval_pi05_l2norm_k075_long_seed42_strict_w27 已经 DONE/success，CRON 失败是滞后通知，不要重跑
  - OV 实验需要约 7 小时（500 episodes × 10 tasks），不要低估时间
  - 距 CoRL 截止极近，所有决策以"闭合 cliff curve → 更新论文 figures"为最高优先级


---
