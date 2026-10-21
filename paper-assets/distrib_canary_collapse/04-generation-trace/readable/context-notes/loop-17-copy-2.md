# agent / loop_17.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`26e9301af4e51d893d77.json`](../../sessions/26/26e9301af4e51d893d77.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-22T19:59:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5, westd-19828 cuda:0-1（共 8 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- d102 分析唯一有效参数组合：`downstream=mauve, threshold=true_3sigma_d105`（M063/M064/M066）。用错参数出的数据全部作废
- PermG 6/8 ceiling 是 MAUVE bottleneck 导致的已知上界，不要把 6/8 当 8/8 解读，也不要把 6/8 报为异常
- T=25 α=0.60★ 是 Phase Diagram 最关键单格（sync-dip dissolution 终态测试），该格结果决定 C3 claim 走向（场景 A vs B，见 D170）
- 17855 ↔ 19828 SSH 不互通，跨服务器操作必须分别 SSH
- HF_HOME 三件套必带：`HF_HOME=/root/autodl-tmp/.hf_cache && TRANSFORMERS_OFFLINE=1 && HF_HUB_OFFLINE=1`（M060）

### 2. 🖥️ 基础设施快照
- **westd-17855**：6× RTX PRO 6000 Blackwell (98GB)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`，Python `/root/miniconda3/bin/python`，conda base，磁盘 816G/879G 可用（3%）
- **westd-19828**：2× RTX PRO 6000 Blackwell (98GB)，同上路径布局，磁盘 817G/879G 可用（2%）
- 模型：`/root/autodl-tmp/.hf_cache` 下已缓存 EleutherAI/pythia-410m
- 数据：`/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k`（5000 条）
- 活跃 cron：`phase_diagram_t25_a075_s43_fp32`（19828:0），`phase_diagram_t25_a045_s43_fp32`（17855:5）

### 3. 📊 当前状态
**刚做的事**：收到 `phase_diagram_t20_a060_s43_fp32_v2` 完成回调（ANALYZING），已派 Worker `worker_analyze_d102-t20-a060-s43-v2_20260522T034250` 做 d102 分析。**该 Worker 回调尚未返回**——下一个"我"需要处理这个回调。

**RUNNING 实验（7 个）**：
| exp_id | server:gpu | 摘要 |
|--------|-----------|------|
| t25_a075_s43_fp32 | 19828:0 | cross-seed，~1/24 |
| t25_a045_s43_fp32 | 17855:5 | cross-seed，~2/25 |
| t25_a060_s42_fp32_v3★ | 17855:3 | 最关键格 v3 resume --start_gen 14，还需 11 gens |
| t25_a050_s42_fp32_v3 | 17855:0 | v3 resume --start_gen 13，还需 12 gens |
| t15_a075_s43_fp32 | 17855:1 | cross-seed，~2-3h |
| t10_a075_s43_fp32 | 17855:2 | cross-seed |
| t10_a050_s43_fp32 | 19828:1 | cross-seed |

**ANALYZING（1 个）**：t20_a060_s43_fp32_v2（等 Worker 回调）

**其他运行中 Worker**：`ops:download-models-17855` 和 `ops:download-models-19828`（Qwen 3.5 模型下载，qwen35 dryrun 准备）

**PREPARING（2 个）**：t15_a050_s42_fp32、qwen35_dryrun_launch

**空闲 GPU**：17855:4（t20_a060_s43_v2 刚跑完释放）。17855:2 也可能即将释放（t10_a075_s43 应该快完成）。

### 4. 📋 待办（条件触发式）
- **Worker d102-t20-a060-s43-v2 回调到达** → 读取 PermG 结果，update_registry 写 metrics+conclusion+checkpoint_path+log_path → 转 DONE。对比 s42（PermG=0/8, near-miss p_fdr=0.064）：若 s43 也 0/8 + near-miss → 更新 ROADMAP Phase Diagram 表 T=20 α=0.60 为 dual-seed confirmed sync-dip → 汇报 Director
- **17855:4 已空闲** → 检查 PREPARING 中的 t15_a050_s42_fp32 是否可以提交（需 Director 分配 GPU），或汇报 Director 请求分配
- **t25_a060_v3★ 完成** → 这是最关键的实验。PermG>0/8 = 场景 A（sync-dip dissolution confirmed），PermG=0/8 = 场景 B（sync-dip permanent）。结果直接决定 D170 叙事走向。必须立即分析 + 汇报 Director
- **t25_a050_v3 完成** → d102 分析，填 Phase Diagram T=25 α=0.50 格
- **cross-seed 4 组（t10_a050_s43, t10_a075_s43, t15_a075_s43, t25_a075_s43）完成** → 各自做 d102 → 对比 s42 结果 → 更新 Phase Diagram → seed robustness 验证报告
- **Phase Diagram 20/20 全填完** → 生成 heatmap → D170 叙事定稿 → submit_paper_to_review → 目标 EMNLP 2026 ARR June（DDL ~2026-06-15）

### 5. 🎯 战略上下文
- **核心方向已转型**：从"方法论文"转为"现象发现论文"——α×T 2D 相图、非单调 dose-response、step-function transition、检测下界理论
- **Phase Diagram 进度**：20 格中已填 ~14 格，剩余格主要在 T=25 行（v3 重启中）和 cross-seed 验证
- **α_c left-shift 已 5 点验证**：α=0.45 列 0/8→0/8→6/8→5/8→6/8，理论 α_c(T) 递减得到确认
- **sync-dip（α=0.60 列全 0/8）是核心现象之一**：T=10/15/20 都是 0/8，T=25★ 待定。这决定 C3 claim 是"dissolution"还是"permanent structural desynchronization"
- **易踩的坑**：
  - M066 教训：旧版 d102 脚本给出 8/8 是 bug，必须用 downstream=mauve + threshold=true_3sigma_d105 参数组合
  - T=20 α=0.45 s43 的结果是 4/8（不是 5/8），这是 Reviewer 标记的最 fragile cell——如果报告里把 s42=5/8 和 s43=4/8 搞混会被 CRITICAL
  - v2/v3 实验的 output_dir 路径可能和 v1 不同，分析前先 SSH 确认实际路径
  - 17855 之前多次磁盘满 crash（M065），长时间实验完成后先 `df -h` 检查磁盘


---
