# agent / loop_4.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`dbc619fe629d23c52599.json`](../../sessions/db/dbc619fe629d23c52599.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T04:04:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0 和 cuda:1（服务器 westb-13313），不可用其他 GPU
- 服务器仅 westb-13313，2× RTX 5090 32GB
- episode_level_collection.py 必须加 `--reuse_dirs` 参数防止数据重复（已踩坑多次）
- 禁止 Worker 用 `kill_job` 回收正在运行的实验，禁止 `pkill -f` 宽泛 pattern（两次 SIGHUP 误杀根因）
- 判断进程存活用 `ps -p PID`，不能依赖 nvidia-smi（ScienceWorld 推理是 bursty 的，GPU 利用率长期 0% 正常）
- C1 claim 采用 Tier B（D017）："Death avoidance ~99% of routing signal, non-death deltas small and inconsistent"，不可升级到 Tier A "唯一机制"

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/`
- 数据路径：`results/plan_c/`（episode-level 收集数据），`results/prescreening/`，`results/research/`（MVP 数据）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：
  - plan-001b-gpu0-v5: PID 698985, tmux session, cuda:0（measure-melting-point 20eps + lifespan-longest-lived ep19）— cron 活跃
  - plan-001b-gpu1-freeze-chem: PID 788058, tmux session, cuda:1（freeze 20eps + chemistry-mix 20eps）— **刚提交，确认 cron 是否已注册**（reconcile 只发现 gpu0-v5 的 cron）
- 后续脚本已就绪：`post_collection_analysis.sh`、`launch_plan002.sh`（cuda:0）、`launch_plan004b.sh`（cuda:1）

### 3. 📊 当前状态
**刚做完**：plan-001b-fnlt-v2（find-non-living-thing 40eps 完成，0% 死亡率确认），提交了 plan-001b-gpu1-freeze-chem（freeze+chemistry-mix on cuda:1）。

**Registry 活跃实验**：
- `plan-001b-gpu0-v5` RUNNING — measure-melting-point-unknown-substance 20eps + lifespan-longest-lived ep19（cuda:0）
- `plan-001b-gpu1-freeze-chem` PREPARING — freeze 20eps + chemistry-mix 20eps（cuda:1，PID 788058 已提交但 registry 仍 PREPARING）

**plan-001b 数据收集完成度**：
- ✅ 已完成（8/11 tasks）：find-non-living-thing(40ep), grow-fruit(20), inclined-plane(20), identify-life-stages-2(20), find-animal(partial from gpu0-v2), identify-life-stages-1(partial), lifespan-longest-lived-then-shortest(partial), lifespan-longest-lived(16-19ep)
- ⏳ 运行中（3 tasks）：measure-melting-point(gpu0), freeze(gpu1), chemistry-mix(gpu1)
- ⚠️ gpu0-v2 跑了 7 个 task 但在 Episode 15 vLLM 崩溃，find-animal 等 5 个 genuine-det task 数据需确认完整度

**等待中**：
- plan-001b-gpu0-v5 cron 回调（估计 ~1-2h）
- plan-001b-gpu1-freeze-chem 完成回调（估计 ~2-3h）
- research-cf-pilot-gpu1: PENDING 但已标记 killed（可忽略）
- mvp-p1-signal: PREPARING 但已标记 killed（可忽略）

### 4. 📋 待办（条件触发式）
- plan-001b-gpu1-freeze-chem 回调到达 → 检查 freeze/chemistry-mix 数据完整性 → 更新 registry
- plan-001b-gpu0-v5 回调到达 → 检查 measure-melting-point 20eps + lifespan-longest-lived ep19 → 更新 registry
- **两卡都完成后** → spawn Worker 跑 `post_collection_analysis.sh`（汇总全部 plan-001b 数据）→ 重跑 plan-012 death decomposition 最终版（全量数据）→ 更新 ROADMAP
- plan-012 最终版完成 → plan-002 router SFT（cuda:0）+ plan-004b（cuda:1，依赖 plan-002 Step 1 输出）
- gpu0-v2 部分完成的 5 个 genuine-det task（find-animal 等）数据完整度需确认——如果不足 20eps，需补跑
- **⚠️ 紧急检查**：plan-001b-gpu1-freeze-chem 的 cron 是否已注册（reconcile 只发现 gpu0-v5）——如果没有 cron，需手动 register_cron

### 5. 🎯 战略上下文
- **核心结论**：Death avoidance = ~99% routing signal（D013/D015/D017 确认），novelty confirmed（文献扫描无 direct competitor）
- **DDL**：EMNLP 2026 ARR May 25（剩 11 天），关键路径 ~2 天实验 + ~3 天写作，余量极小
- **Framing v3**：贡献 = empirical finding + counterfactual methodology，不是 router 架构。C1 = death avoidance dominates，C2 = episode-level labeling 方法论
- **决策链**：D008(1-step失败) → D010(fork废弃) → D011(safety-aware) → D013(pivot to finding) → D015(30tasks r=0.989确认) → D017(C1 Tier B)
- **易错点**：
  - gpu0-v2 的 7 个 task 部分数据可能不完整（vLLM 在 ep15 崩溃），不要假设都有 20eps
  - find-non-living-thing 是唯一 internal-preferred task（0% 死亡率），是 C1 的关键 counter-example，数据已在 fnlt-v2 收齐 40eps
  - grow-plant 是 no-signal（delta=0），不是 internal-preferred
  - plan-004b 依赖 plan-002 Step 1 输出，不能完全并行
  - keywords v1/v2/v3 全部结构性失效（plan-011 已关闭），论文定位为 structural failure analysis


---
