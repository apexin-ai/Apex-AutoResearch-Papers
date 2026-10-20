# reviewer / loop_16.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`3d2cb0ee41ba11d95206.json`](../../sessions/3d/3d2cb0ee41ba11d95206.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-23T19:48:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5，westd-19828 cuda:0-1。越界进程立即 CRITICAL + kill
- 模型路径：westd-17855 用 `/root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped`，westd-19828 用 `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped`。混用会导致加载失败
- HF_HOME 必须设 `/root/autodl-tmp/.hf_cache`，否则 MAUVE 计算因 gpt2-large 下载失败返回 null（6/8 实验已中招，backfill 脚本已就绪）
- C003 约束：禁止引用 α≤0.50 的 TY Granger 显著率（3-seed 确认种子不稳定）
- C008 约束：K 值计算必须用 registry `threshold_onset_3sigma`，禁止用 JSON 的 `3x_sigma_drift`
- 论文真源为 `docs/paper/`，禁止直接编辑 `artifacts/_project/paper/`（C002）
- `experiments_reframe.tex` 是旧文件不在编译链中，不要引用其内容

### 2. 🖥️ 基础设施快照
- **westd-17855**（root）：工作目录 `/root/autodl-tmp/distrib_canary_collapse`，Python `/root/miniconda3/bin/python`，conda base
  - 实验输出：`results/phase_diagram/t{T}_a{α}_s{seed}_fp32_14b/`
  - 活跃进程（6 个）：PID 749427 (t15_a060_s43 cuda:0)、750075 (t15_a050_s43 cuda:1)、781730 (t10_a050_s44 cuda:2)、780912 (t10_a060_s44 cuda:3)、796629 (t10_a045_s44 cuda:4)、762811 (t15_a045_s43 cuda:5)
- **westd-19828**（root）：同工作目录，同 Python 路径
  - 活跃进程（2 个）：PID 857058 (t15_a075_s43 cuda:0)、865472 (t10_a075_s44 cuda:1)
  - 旧进程 PID 776057 (t10_a050_s42 tmux，1+ 天前，可能已完成但 tmux 未退出)
- MAUVE backfill 脚本：`scripts/backfill_mauve.py`（本地 + westd-17855），55 gen 需补算
- 无 W&B 配置，不检查 W&B

### 3. 📊 当前状态
**刚完成**：Report #153 — 验证了 non-confirming count fix（10/15→11/15, 5→four），确认 Report #146-#152 所有 pending issues 全部关闭。

**8 个 RUNNING 实验**（均 1.4B Pythia fp32 iterative training）：

| 实验 | 进度 | 预计完成 |
|---|---|---|
| t15_a060_s43 | gen_15/16 训练 55% | ~30 min |
| t15_a050_s43 | gen_15/16 训练 26% | ~40 min |
| t10_a075_s44 | gen_10/11 训练 81% | ~30 min |
| t10_a060_s44 | gen_10/11 开始 | ~50 min |
| t10_a050_s44 | gen_9 metrics 中 | ~1h |
| t15_a045_s43 | gen_14/16 训练 54% | ~1.5h |
| t10_a045_s44 | gen_6/11 done | ~2.5h |
| t15_a075_s43 | gen_11/16 done | ~3.5h |

注：T=N 的实验产生 gen_0 到 gen_N（共 N+1 个 dir），不是 gen_0 到 gen_{N-1}。

**无等待中的 Worker 回调 / Director 决策。**

### 4. 📋 待办（条件触发式）
- t15_a060_s43 / t15_a050_s43 完成 → 核实 gen_15 metrics 合理性（PPL 趋势、entropy），检查 MAUVE 是否有效（t15_a060_s43 有 HF_HOME 应该有值，t15_a050_s43 没有应为 null）
- T=15 s43 四个实验全部完成 → 等 Agent 跑 D102 5-method analysis → 核实 PermG 值，特别关注 α=0.60 s43（如果 sync-dip 在 1.4B T=15 复现则 claim 需限定；如果消失则支持 "scale attenuates sync-dip"）
- D102 T=15 s43 分析完成 → 核实 Table 17 是否正确添加 T=15 s43 列，检查 Discussion L12 "forward detection seed-robust at T=10" 是否需要扩展到 T=15
- T=10 s44 四个实验全部完成 → 核实 s44 数据是否 replicate s42/s43 的 dose-response pattern（blind/onset/sync-dip/detection）
- MAUVE backfill 执行后 → 抽查几个 gen 的 MAUVE 值是否合理（MAUVE ∈ [0, 1]，gen_0 应接近 1，后期下降）
- 论文章节审查请求 → 先查 Agent 是否读过 red-section skill（L1 合规），再按 5 维度审

### 5. 🎯 战略上下文
- **核心 story**：canary metrics（entropy/diversity）存在 lead-lag 关系，可用 PermG 检测，detection boundary α_c(T) ∝ T^{-γ}（γ=2.08），predictive intervention 比 reactive 早 1 gen，peak PPL 降 64%
- **α_c 双值**：0.483±0.006（sigmoid fit on T=10 13-point grid）vs 0.487（cross-T power law at T=10）— 不同模型，均合法，但读者可能困惑。已在 experiments.tex 中共存
- **sync-dip**：α=0.60 处 PermG 骤降。410M 下 seed-robust（3/3 seeds 0/8），1.4B T=10 下消失（s42/s43 均 4/8）。T=15 s43 α=0.60 是关键测试点
- **1.4B scale framing**：用 "detection power attenuated" 不用 "model resists"（D204 红线 + feedback memory）
- **易错点**：
  1. T=10 s43 数据之前被误放入 Table 17 的 T=15 s43 列（Report #149 已修正），注意不要再混淆
  2. `num_generations=15` 产生 gen_0-gen_15（16 dirs），不是 gen_0-gen_14
  3. 论文中 `experiments_reframe.tex` 是旧版不在编译链中，真源是 `experiments.tex`
  4. 审 "未改" 类结论时必须双边核对（本地 workspace vs 远程服务器），不要只读一边就下结论
- **已交付 Reports**: #134-#153，所有 pending issues 已关闭


---
