# agent / loop_3.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`7c78093d60b23a28eb3b.json`](../../sessions/7c/7c78093d60b23a28eb3b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T00:59:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 westb-13313 的 cuda:0 和 cuda:1**（RTX 5090 32GB），无其他服务器/GPU
- plan-001b 数据收集是 **blocking gate**——plan-012 全量分析、plan-002 router SFT、plan-005 routing pattern 全部依赖它完成
- C1 claim 已锁定 **Tier B**（D017）："Death avoidance ~99% 主导，non-death deltas small and inconsistent"——不要用 Tier A（"唯一机制"）或 Tier C
- plan-004b 依赖 plan-002 Step 1 (death_aware_labeling.py) 的输出，**不能与 plan-002 完全并行**
- find-non-living-thing 需要追加 20 eps（--start_episode 20），总目标 40 eps

### 2. 🖥️ 基础设施快照
- 服务器：**westb-13313**，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/`
- 数据：`results/plan_c/` + `results/prescreening/` + `results/research/`（预筛 30 tasks 数据）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：
  - plan-001b-gpu0-v2: PID 853847, tmux session, cuda:0（7 tasks × 20 eps，含 cleanup_gpu_processes() fix）
  - plan-001b-gpu1: PID 773109, tmux session, cuda:1（4 tasks × 20 eps + find-non-living-thing 需追加）
- 活跃 cron：2 个（分别监控上述两个进程）
- 后续脚本已部署就绪：post_collection_analysis.sh、launch_plan002.sh (cuda:0)、launch_plan004b.sh (cuda:1)

### 3. 📊 当前状态
plan-001b 双卡数据收集正在跑（~20h 预计），这是当前唯一的 blocking 任务。

**Registry RUNNING 实验：**
- **plan-001b-gpu0-v2**：7 tasks（5 genuine-det + 2 death-dom）× 20 eps，cuda:0。v2 修复了 vLLM 孤儿进程问题
- **plan-001b-gpu1**：4 tasks（1 internal-pref + 3 death-dom）× 20 eps，cuda:1。完成后需追加 find-non-living-thing 20 eps
- **plan-011-rule-based**：已完成分析（三版 keyword list 全部结构性失效），标记 RUNNING 但实际 DONE，conclusion=success
- **plan-012-decomposition**：预分析已完成（r=0.989, death_fraction=99%），等 plan-001b 全量数据后重跑最终版

**等待中：**
- plan-001b 双卡 cron 回调（完成后触发 post-collection pipeline）
- Director 未有新指令待处理
- research-cf-pilot-gpu1（PENDING/killed）和 mvp-p1-signal（PREPARING/killed）已废弃，不需处理

### 4. 📋 待办（条件触发式）
- **plan-001b-gpu1 cron 回调** → spawn worker 追加 find-non-living-thing 20 eps（--start_episode 20）在 cuda:1 → 再检查 gpu0 进度，如 gpu0 有剩余未跑 tasks 则 gpu1 接管
- **plan-001b 双卡全部完成** → 运行 post_collection_analysis.sh → 重跑 plan-012 death decomposition 全量版 → 更新 registry metrics
- **plan-012 全量完成** → 启动 plan-002 router SFT (launch_plan002.sh, cuda:0) + plan-005 routing pattern analysis（可并行）
- **plan-002 Step 1 完成** → 启动 plan-004b ablation (launch_plan004b.sh, cuda:1)
- **所有实验数据就绪** → 开始论文写作（EMNLP 2026 ARR short paper, DDL 2026-05-25, 剩 11 天）

### 5. 🎯 战略上下文
**核心结论链：** D005(MVP PASS) → D011(death avoidance = sole mechanism) → D013(framing pivot: empirical finding, not router architecture) → D015(r=0.989 confirms at 30 tasks) → D017(C1 Tier B locked)

**论文 story（v3）：** Episode-level counterfactual analysis 揭示 LLM agent routing 本质 = death avoidance（~99%）。贡献 = empirical finding + methodology，非 router 架构。Novelty confirmed（12 篇文献扫描无 direct competitor）。

**易错点：**
- plan-011 和 plan-012 在 registry 里标 RUNNING 但实际已完成分析——不要给它们派 worker 或等 cron 回调
- vLLM EngineCore 孤儿进程问题：脚本崩溃后残留进程占 GPU 显存。plan-001b-gpu0-v2 已含 cleanup_gpu_processes() fix，但如果重启任何 vLLM 相关任务仍需注意
- find-non-living-thing 是唯一的 internal-preferred 候选（DAF=0%），但 D016 评估后可能翻转为 no-preference——framing 对此 robust，无需 pivot
- 关键路径极紧：~2 天实验 + ~3 天写作，余量近零。plan-001b 完成后应立即并行铺 plan-002/005/012-full + 论文骨架


---
