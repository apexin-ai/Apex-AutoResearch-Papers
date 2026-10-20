# reviewer / loop_24.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_24.md`
- **Structured JSON:** [`d450f51c739ef708fc90.json`](../../sessions/d4/d450f51c739ef708fc90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: max_wall_time
updated: '2026-05-25T22:57:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-45299 和 westd-19154 各 2 张 GPU（cuda:0, cuda:1），需核对 `execution.gpu_ids` 白名单，越界即 critical
- `--dt_embed_dim` 是错误参数名，正确 CLI flag 是 `--gate_dt_embed_dim`（exp_089/090 因此崩溃，已修正为 exp_092/093）
- NVE 计算必须用 step-matched baseline（exp_083 用于 Cheetah），不能用 baseline 全程均值（V2 baseline bug 教训：0.105 vs 0.6，6 倍差异）
- exp_088 有重复 registry 条目：`exp_088`（ALLOCATED, NVE=1.82 错误）和 `exp_088_cheetah_008d_s1`（DONE, NVE=0.517 正确），前者已标 killed 但仍存在，引用时只认后者

### 2. 🖥️ 基础设施快照
- **westd-19154** (root): `/root/autodl-tmp/event-gated-adaptive-horizon`, conda base (`/root/miniconda3`)
  - 活跃：exp_091 PID 47303, cuda:0, tmux, ~2h+ 运行中
  - cuda:1 空闲
- **bjb1-45299** (root): 同路径, conda base
  - 活跃：exp_092 PID 313538 cuda:0, exp_093 PID 313815 cuda:1（均 `--gate_dt_embed_dim 0`）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- NVE 分析产物: `artifacts/plan_034_nve_threshold/analysis_v2.md`（V2.1，最新）
- plan_030 脚本: `artifacts/plan_030_rssm_quality/analyze_rssm_quality.py`（已创建未执行）

### 3. 📊 当前状态
刚完成的审查：
- NVE V2.1 baseline bug 修复 → 确认通过（info），warning 已关闭
- exp_089/090 崩溃 → critical 已报，Agent 修正为 exp_092/093 并重提交
- exp_092/093 registry 仍 PREPARING 缺追溯字段 → warning 已报

Registry RUNNING/PREPARING：
- **exp_091_cheetah_008d_s2** (RUNNING, westd cuda:0) — Cheetah trained dt_emb s2，决定 CIVO onset rate 是 1/3 还是 2/3
- **exp_092_cheetah_no_dt_emb_s1** (PREPARING→应为 RUNNING, bjb1 cuda:0) — Cheetah 因果对照 s1
- **exp_093_cheetah_no_dt_emb_s2** (PREPARING→应为 RUNNING, bjb1 cuda:1) — Cheetah 因果对照 s2

### 4. 📋 待办
- exp_091 完成 → 核实 NVE：若 NVE≥1.5× 则 Cheetah onset=2/3，D156 更新为 ~80%；若 NVE<1.5× 则 onset=1/3，C1 强度需降级
- exp_092/093 完成 → 核实 NVE 应 <1.0×（与 exp_082 s0 NVE=0.33× 一致），确认 C2 因果对照跨 seed 稳健
- exp_092/093 registry 更新为 RUNNING + 补全 spec → 若下次检查仍为 PREPARING 则再报 warning
- plan_030 RSSM quality 分析脚本执行完成 → 审查结果（比较 exp_078 CIVO vs exp_088 non-CIVO 的 RSSM 预测质量）
- 重复条目 `exp_088` (ALLOCATED) 被清理 → 确认

### 5. 🎯 战略上下文
- **核心发现**：CIVO = trained dt_embedding 导致的 value overestimation。C1（CIVO 存在 + 诊断）和 C2（frozen/removed dt_emb 消除 CIVO）是论文两大 claim
- **D156 关键决策**：trained dt_emb 是 CIVO 必要非充分条件，onset 具有随机性（Walker 3/3, Cheetah 1/2）。exp_091 结果将更新这个比率
- **NVE 诊断器**：θ=1.5×, N=63, AUROC=0.9895, F1=0.926, recall=100%。4 个 FP 均在 1.5-1.93× 区间，0 FN。composite diagnostic（peak+sustained+temporal）因 74% 实验缺轨迹数据仅作辅助
- **易错点**：
  - 进程挂起判断需多次快照（feedback memory: exp_009h 教训），单次 nvidia-smi 0% 不等于挂死
  - Registry spec 与实际代码可能不一致，要查代码层 assertions（feedback memory）
  - 本地 vs 远程文件可能同名但版本不同（§2.5 双边核对规则），断言"未改"前两边都读
  - Cheetah baseline 必须用 exp_083 step-matched 值，不能用近似值


---
