# agent / loop_6.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`70a9844b20efc8045d03.json`](../../sessions/70/70a9844b20efc8045d03.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-16T04:42:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1** on westd-19183。不得使用其他 GPU，即使 Director 指令也必须 push back
- 服务器**无外网**：所有 HF/AutoProcessor 操作必须 `local_files_only=True`，不能 pip install / git clone
- westd 是 **SeetaCloud**（非 AutoDL），不适用 network_turbo / ModelScope
- RSA 数值**仅用 Method B**（within-task + euclidean + full trajectory, 50 demos/task）。D039 前的 Method A 数值全部废弃，禁止引用
- `fulllayer_action_probe` 已占用 cuda:0+cuda:1（PID 700649），状态 PREPARING——下一个"你"接手后先 poll 确认进程状态再做任何 GPU 操作
- CoRL abstract deadline **2026-05-26**（10天），paper deadline **2026-05-29**（13天）

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19183**，工作目录 `/root/vla-ssd`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/vla-ssd/` 下（checkpoint、features cache）
- 数据：LIBERO-Goal features 已全量提取（33层 × trained/untrained × with_inst/no_inst/random/shuffled/empty）
- 统一 RSA 结果：`/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json`（D041 权威数据）
- W&B：项目内实验未用 W&B（probe/RSA 均本地运行）
- 活跃进程：`fulllayer_action_probe` PID 700649，log `~/runs/vla-ssd/fulllayer_action_probe.log`——**状态卡在 PREPARING，需要立即 poll 确认是否在跑**
- Cron：reconcile 返回 0 条活跃 cron
- Worker 池：0 running（全部 done）

### 3. 📊 当前状态
**刚完成**：D041 全层统一 RSA 数据定稿 + paper_framing.md 全面重写（D042）。所有 3 条 Core Claims 数据完整，进入论文全面重写阶段。

**Registry 概况**：48 实验，46 DONE（31 success / 7 negative / 8 killed），2 PREPARING：
- `fulllayer_action_probe`（PREPARING, westd-19183 cuda:0+1, PID 700649）——统一超参全层 action probe，但状态未推进到 RUNNING，可能卡住
- `plan_011_fulllayer_r2`（PREPARING, 无服务器分配）——Full-layer R² scan (L0-L32)，验证 R² peak L19 vs RSA peak L12 的差异。Worker 已写好代码但未提交

**等待中**：
- 无活跃 Worker / Cron / Director 决策待处理
- Paper Agent UNHOLD 任务在 ROADMAP 中标注"进行中"，但实际未看到 running worker

### 4. 📋 待办（条件触发式）
- 接手后第一件事 → poll `fulllayer_action_probe` 确认进程状态（alive → 注册 cron 监控；dead → 诊断 + 重新提交）
- `fulllayer_action_probe` 完成（success）→ 结果写入 registry + 与 RSA L12 peak 对比 + 汇报 Director
- `fulllayer_action_probe` GPU 释放后 → 立即提交 `plan_011_fulllayer_r2`（代码已就绪，需分配 cuda:0 或 cuda:1）
- plan_011 出结果 → R² peak 在 L12 附近 = 强化 C2 claim；R² peak 在 L19 = RSA/R² dissociation，需更新 paper_framing C2 措辞
- 论文重写 → spawn paper_writing Worker 逐章重写（7章），需发送 D041 完整数据 + 新 narrative。优先 Method + Experiments 章节
- references.bib 补全（black2024_pi0, swann2026, rizzardo2026 等）——Worker 已完成初步搜索但 2026 citation 需验证真实性
- plan_010 LIBERO-Spatial（P2, 4 GPU·h）——仅在时间和 GPU 预算允许时做

### 5. 🎯 战略上下文
**项目核心结论**：VLA action-relevant 表征由 frozen self-supervised vision encoder（DINOv2）主导，LLM 对 action geometry 做非单调变换（前12层增强，后20层退化），fine-tuning 重新分配层间信号分布而非注入新知识。

**决策链关键节点**：
- D037: DINO RSA 方法论错误修正（0.388→0.692），彻底改变 encoder 排序
- D038: Geometric-Functional Dissociation 失效——RSA 和 R² 排序一致，跨编码器 dissociation 是伪影
- D039: 全部 RSA 统一为 Method B
- D041: 权威全层数据确认 inverted-U（L12 peak）+ peak shift（training effect）
- D042: paper_framing.md 基于 D041 全面重写

**易错点**：
- 不要混淆 Method A（旧, cross-task + cosine + phase-split）和 Method B（新, within-task + euclidean + full trajectory）——任何旧数值都不能用
- R² peak 在 L19，RSA peak 在 L12——这是**预期的 metric dissociation**，不是 bug。paper_framing 已标注"R² 可能在 RSA 下降后继续积累"
- `no_inst` 条件有混合 demo 数（trained_no_inst 4个task仅10 demos），引用时需注明
- `fulllayer_action_probe` 虽然有 PID 但状态是 PREPARING 不是 RUNNING——很可能是上一轮 session 提交后未来得及 poll 就被 reset 了，优先确认
- GPU 预算剩余 ~9 GPU·h，plan_011 预估 1h，plan_010 预估 4h——够用但不能浪费


---
