# director / loop_1.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`ebd0970e432a763ecafd.json`](../../sessions/eb/ebd0970e432a763ecafd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T13:32:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（autodl-rtx6000 仅 2 卡，项目配置 gpu_ids=["cuda:0","cuda:1"]）
- 启动命令必须带 `PYTHONUNBUFFERED=1` 和 `CUDA_VISIBLE_DEVICES=X`（v3 因缺这两项静默崩溃，浪费 8h+）
- kill_job 只杀 tmux session 不杀子进程——必须 `kill -9 $(pgrep -P $PID)` 级联 kill
- 数据/模型/缓存全部放 `/root/autodl-tmp/`（系统盘仅 30G）
- HF_HOME=/root/autodl-tmp/.hf_cache, HF_HUB_DISABLE_XET=1
- MAUVE 已被 D005 demote 为 supplementary（基线 0.034 触发 floor effect）——不要把 MAUVE 当 primary downstream 指标

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000，SSH `ssh -p 19828 root@connect.westd.seetacloud.com`，密码在 secret `autodl_ssh_password`
- GPU：2× RTX 6000 Pro Blackwell 96GB
- 工作目录：`/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base，aml-train 镜像）
- 数据：`data/wikitext103_5k/`（train 716K / eval 1564 / prompts 5000）
- 模型：EleutherAI/pythia-410m（HF cache）
- 代码：5 个脚本在 `artifacts/` 和服务器均有副本（iterative_train.py, metrics.py, prepare_data.py, run_mvp.sh, analyze_mvp.py）
- 活跃进程：**状态不明**——最后确认 rep42 PID 13683 (cuda:0) 和 rep43 PID 13763 (cuda:1) 在 Gen 2/10 (~08:41 UTC)，之后 GPU 归零约 4 小时，可能完成或崩溃

### 3. 📊 当前状态
**最紧急**：mvp_v4_rep42 和 mvp_v4_rep43 状态不明，GPU 已空闲约 4 小时。可能已完成 10 gen（预估 ~12:30 UTC 完成），也可能再次崩溃。第一件事 SSH 检查。

Registry 实验：
- mvp_v4_rep42 (seed=42, cuda:0) — RUNNING（可能已完成）
- mvp_v4_rep43 (seed=43, cuda:1) — RUNNING（可能已完成）
- mvp_v4_rep44 (seed=44) — PREPARING，等空出 GPU 后启动

已就绪但未运行：analyze_mvp.py 已更新（含 permutation test、graded verdict、MAUVE floor detection），实验完成后可直接跑。

### 4. 📋 待办
- **立即** SSH 检查 rep42/rep43 → 如果完成：检查 `results/mvp/rep_42/all_metrics.json` 和 `rep_43/all_metrics.json` 存在，启动 rep44 (seed=44) 在空出的 GPU 上，同时对 rep42+rep43 先跑 analyze_mvp.py 看初步趋势
- rep42/rep43 崩溃 → 读日志诊断根因，修复后立即重启两卡
- 3 reps 全部完成 → 运行 `python analyze_mvp.py --n_permutations 10000`，按 mvp_evaluation_criteria.md 做 MVP gate 判定（STRONG PASS / PASS / CONDITIONAL PASS / FAIL）
- PASS 或 STRONG PASS → `complete_mvp()` 进入 research 阶段，启动 post-mvp-kickoff skill
- CONDITIONAL PASS → 扩展到 20 gen + 5 seeds 重新验证
- FAIL → 分析 perplexity 轨迹判断是否 collapse 过快导致无时序结构（如果是，进一步降低 steps_per_gen），或项目前提不成立需 pivot

### 5. 🎯 战略上下文
- 决策链：D001(MVP 设计) → D002(ECE/SC/eff_rank 操作化) → D003(目标 AAAI 2027) → D004(n_prompts 5000, steps 5000) → D005(不重启，MAUVE demote)
- Gen 0→1 初步信号积极：token_entropy(-41%) 和 ECE(+19x) 剧变而 self_bleu/distinct-n 几乎不动——如果 perplexity 也有延迟，有 lead-lag 证据
- 但 perplexity Gen 1 也翻倍了（+108%），可能与 canary 同步而非滞后——需要完整 10-gen 轨迹判断
- effective_rank Gen 0→1 反直觉上升 +71%——evaluation criteria §3 用 Gen 4-9 OLS slope 处理非单调，等完整数据
- 100% SC full replacement 是最激进条件，如果 FAIL 可解释为 Truong & Truong 一阶相变理论的验证，pivot 到 50% accumulation 测 lead-lag
- 3 次连续失败（v1/v2/v3）已浪费大量 GPU 时间，Manager 强调资源利用——新 session 必须确保实验稳定运行
- 评估标准文档不是严格 pre-registered（受 gen_0 数据启发），论文中不要声称 pre-registered


---
