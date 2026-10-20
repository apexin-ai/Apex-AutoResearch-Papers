# agent / loop_16.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`2d885b67555838158feb.json`](../../sessions/2d/2d885b67555838158feb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-21T18:02:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5 + westd-19828 cuda:0-1，共 8 卡。白名单外的 GPU 一律 push back Director
- HF_HOME 三件套必带（M060）：`export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1`。之前 t25_a045_v1 和 t15_a075_v1 因缺 HF_HOME 失败
- 精度：≤3B fp32，>3B bf16（D079）
- 17855↔19828 SSH 不通，两台服务器独立操作
- T=20 α=0.60 PermG 是 **0/8**（D176 修正），不是 6/8。曾被误标，千万别引用错
- T=20 α=0.50 PermG 是 **6/8**（M062），heatmap 需用此值

### 2. 🖥️ 基础设施快照
- **westd-17855**（6× RTX PRO 6000 Blackwell 98GB）
  - 工作目录：`/root/autodl-tmp/distrib_canary_collapse/`
  - Python：`/root/miniconda3/bin/python`，conda base 环境
  - HF cache：`/root/autodl-tmp/.hf_cache`
  - 活跃进程：
    - t15_a060 PID 509841 tmux cuda:1
    - t15_a075_v2 PID 513367 tmux cuda:2
    - t25_a060 PID 515617 tmux cuda:3（★最关键格）
    - t25_a045_v2 PID 519272 tmux cuda:5
    - t25_a050 PID 519969 tmux cuda:0
  - **cuda:4 已空闲**（t15_a050 已完成 success）
- **westd-19828**（2× RTX PRO 6000 Blackwell 98GB）
  - 同样路径/环境
  - 活跃进程：
    - t25_a075 PID 671833 tmux cuda:0
    - t20_a045_s43 PID 688680 tmux cuda:1（刚启动）
- Cron 监控：7 个实验均由 submit_training_job 自动注册 cron，reconcile 确认全部 still running

### 3. 📊 当前状态
Phase Diagram 20/20 填充进行中。**14/20 格已完成**，6 格 RUNNING（t15_a060, t15_a075_v2, t25_a045_v2, t25_a050, t25_a060, t25_a075），另有 1 个 cross-seed 验证 t20_a045_s43 RUNNING。

刚完成的关键结果：
- **t15_a045 = 8/8**（D178）：α_c(15)≈0.304 理论验证，从 T=10 的 0/8 跳到 8/8 是 step-function，打破 6/8 ceiling
- **t15_a050 = success**：已完成，GPU 17855:cuda:4 已释放但尚未接力
- **t05 全行 = 0/8**（D173）：anchor row 四点验证 α_c(5)≥1.0

PREPARING：phase_diagram_t20_a060_s43_fp32（desync cross-seed），qwen35_dryrun_launch

Worker 池 = 0（无活跃 Worker）。所有实验通过 cron 自动监控。

### 4. 📋 待办（条件触发式）
- **立即**：17855:cuda:4 空闲 → 启动 t20_a060_s43（PREPARING，desync cross-seed 验证，P1 优先）
- t15_a060 完成 → spawn worker 跑 5method 分析 → 填 Phase Diagram T=15 α=0.60 格 → 释放 17855:cuda:1 给下一个任务
- t15_a075_v2 完成 → 同上，填 T=15 α=0.75 格 → T=15 行 4/4 完成 → 汇报 Director
- t25_a060 完成 → **最关键判断点**：>0/8 = dissolution confirmed（场景 A，最佳叙事）；=0/8 = sync-dip permanent（场景 B，C3 升级）→ 汇报 Director 决定叙事走向
- t25 四格全完成 → T=25 行 5method → Phase Diagram 20/20 → heatmap 定稿 + D170 叙事升级 → Paper Agent R8 → submit_paper_to_review
- t20_a045_s43 完成 → s43 ≥4/8 确认 robust；≤2/8 则 s42=5/8 可能是 noise，需更新 Phase Diagram 注释
- 所有 Phase Diagram 完成后 → 按 ROADMAP 近期任务推 heatmap 定稿 + D170 叙事

### 5. 🎯 战略上下文
**核心叙事**：从"方法论文"转为"现象发现论文"——α×T 2D 相图、非单调 dose-response、step-function transition、检测下界理论。目标 EMNLP 2026 ARR June（DDL ~2026-06-15）。

**决策链关键节点**：
- α_c(T) = 0.193 + 75.68·T^(-2.41)，R²=0.883（D168）
- FPR = 2/56 = 3.57%（D171）
- PermG 6/8 ceiling 跨 T 一致（MAUVE bottleneck），但 T=15 α=0.45=8/8 打破它
- α=0.45 列是信息密度最高列：0/8→0/8→8/8→5/8（step-function + 非单调）
- Sync-dip 在 α≈[0.55,0.65] 且 T=20 仍 0/8（structural, not power issue）
- Reviewer Report 27 已完成，S×R predictive scoreboard 2 PASS + 1 POSITIVE_SURPRISE + 1 FAIL

**易错点**：
- 不要把 T=20 α=0.60 的值引用为 6/8（D176 已修正为 0/8）
- t20_a045 的 s42=5/8 是 Phase Diagram 中最脆弱的格，s43 cross-seed 结果决定是否需要加注释
- T=25 四格出结果后需要区分场景 A/B/D（见 ROADMAP 叙事预案），不要默认场景 A
- 17855:cuda:4 已空但 ROADMAP GPU 表未更新（仍写着 t15_a050 ~75%），registry 是 truth source
- Worker 池 = 0 是因为所有实验通过 cron 自监控，但新任务（如 5method 分析、t20_a060_s43 提交）需要 spawn worker


---
