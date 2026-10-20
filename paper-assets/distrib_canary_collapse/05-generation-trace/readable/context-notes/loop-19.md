# director / loop_19.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`09e9a8e14e8799a01d26.json`](../../sessions/09/09e9a8e14e8799a01d26.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-22T23:02:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 (cuda:0-5) + westd-19828 (cuda:0-1) = 8 GPU，不得使用其他设备
- D102 标准：downstream=mauve, threshold=true_3sigma_d105, n_perm=5000，不可更改
- D102 启动前必须验证：(1) gen_10/metrics.json 存在且非空 (2) 训练 PID 已退出（M075 教训）
- `--num_generations` 语义是"从 start_gen 再跑 N 代"不是"总共 N 代"（M076 教训）
- M077：部署实验必须用本地模型路径（17855=.ms_cache/, 19828=.hf_cache/），不用 HF model ID（TRANSFORMERS_OFFLINE=1）；cross-seed 必须先从 s42 /proc/PID/cmdline 提取完整参数，逐参数 diff 确保仅 seed+output_dir 不同
- 410M = non-deduped `pythia-410m`（D200 确认）；1.4B = deduped `pythia-1.4b-deduped`（D196）
- D079: ≤3B 用 fp32, >3B 用 bf16
- D189: 论文语言——"consistent across" ≠ "scale-invariant"；1.4B 是 additive evidence，不改 abstract 的 "primarily Pythia-410M"

### 2. 🖥️ 基础设施快照
- 服务器 1：westd-17855 (connect.westd.seetacloud.com)，root，6× RTX PRO 6000 98GB
- 服务器 2：westd-19828 (connect.westd.seetacloud.com)，root，2× RTX PRO 6000 98GB
- 工作目录：`/root/autodl-tmp/distrib_canary_collapse`
- Python/conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 1.4B 模型：17855=`/root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped`，19828=`/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped`
- 410M 模型：默认 `EleutherAI/pythia-410m`（non-deduped），本地路径需确认
- D102 分析脚本：`run_5method_analysis_d102.py`（两台已统一）
- 磁盘：17855=91% (32GB可用，偏紧)，19828=7% (817GB充裕)
- 活跃进程（截至 ~22:54 UTC）：
  - 17855:cuda:0 t15_a060_v2 | cuda:1 t15_a050_v3 | cuda:2 t10_a075_s43 PID 719178 | cuda:3 t10_a060_s43 PID 719252 | cuda:4 t10_a045_s42 | cuda:5 t15_a045
  - 19828:cuda:0 t15_a075 | cuda:1 t10_a050_s43 PID 822048

### 3. 📊 当前状态
**刚做完**：
- D197-D200 决策链：Scenario B strongly supported，sync-dip 非 scale-invariant，4/8 ceiling 被打破（α-dependent），claim 升级 "qualitatively preserved"（D199）
- s43 cross-seed 三组修复重启（M077: 模型路径 + gen_batch_size 两个 bug）
- Paper Agent 完成：He2025→Shi2025 引用修正 + Truong 反向定位 + detection→action gap + Discussion 骨架（D199 措辞）+ 全文一致性扫描（无 "partially preserved" 残留）
- Reviewer #108 定义了 Scenario B "confirmed" 的 C1-C4 量化标准；#109 确认 claim 升级；#110 完成 gap analysis
- literature_map.yaml 修正：he2025closer → shi2025closer（两份副本 + 交叉引用）
- 410M s44 已有完整数据（`results/alpha_sweep/a050_s44_fp32`），D102 待跑（D200）

**RUNNING 实验**：
- T=10 s42: t10_a045 gen 9/10（~00:40 UTC 完成，C2 判定点）
- T=10 s43: a050/a060/a075 各 gen 2/10（~05:20-05:50 UTC）
- T=15 s42: a050 gen 12/15, a060 gen 12/15, a045 gen 10/15, a075 gen 9/15（01:20-03:50 UTC）

**等待中**：
- Agent 正在处理我的决策指令（D200 + s44 D102 + cuda:4 部署计划）
- scale_14b_t10_a050_s43_fp32 registry 仍为 DONE/failed（cron 误杀），需创建 v2 条目
- R10 审稿结果尚未返回

### 4. 📋 待办
- t10_a045 完成（~00:40 UTC）→ D102 → PermG ≤1/8 = C2 PASS → "strongly supports" 正式成立；≥2/8 = 需修订 framing 为 "boundary left-shift"
- t10_a045 D102 后 → cuda:4 立即部署 1.4B t10_a045_s43（seed=43, α=0.45, ~11h）
- 410M s44 D102（CPU 任务，与上述并行）→ PermG 结果 = onset boundary tie-breaker（s42=6/8, s43=0/8, s44=?）→ 2/3 detect 则 boundary 稳固
- t15_a050/a060 完成（~01:20）→ batch D102 → C4 跨 T 验证开始
- t15_a045/a075 完成（~02:50-03:50）→ D102 → C4 ≥2/4 pattern consistent = "cross-T validated"
- s43 三组完成（~05:20-05:50）→ D102 → C3 ≥2/3 方向一致 = "seed-robust" → 升级为 "confirms qualitative consistency"
- 全部 1.4B 完成 → Paper Agent 填充 Discussion Template B 去除 [PENDING] 标记
- R10 审稿结果到达 → 按 review-report-action skill 处理
- 17855 磁盘 <15GB → 触发中间 checkpoint 清理（保留 gen_0 + gen_10 + 所有 metrics.json）

### 5. 🎯 战略上下文
- **论文**："Mapping the Detectability Landscape of Iterative Model Collapse"，目标 EMNLP 2026 ARR June (DDL ~6/15, 距今 ~24 天)
- **当前分数** R8=3.0 → 目标 3.5。R10 提交审稿中
- **410M phase diagram 20/20 COMPLETE**，6/8 ceiling confirmed，k_obs=15.7
- **1.4B T=10 行 3/4 完成**：a050=4/8, a060=4/8（sync-dip 消除✨）, a075=5/8（near 410M）
- **Scenario B confirmation 标准**（Reviewer #108）：C1✅ + C2 pending(~1h) + C3 pending(~7h) + C4 pending(~5h)
- **D199 claim 升级**："qualitatively preserved, with PermG attenuation driven by metric-level scale effects" 替代 "partially preserved"
- **决策链**：D189(additive) → D192(shape) → D196(deduped标准) → D197(sync-dip) → D198(Scenario B) → D199(claim升级) → D200(410M non-deduped确认)
- **易错点**：(1) 不要混淆 scale/ 和 phase_diagram_14b/ 路径 (2) 410M=non-deduped, 1.4B=deduped, 跨 scale 比较要注意 (3) kill+restart 后必须同步 cron PID (4) gen_batch_size=8 必须显式指定（默认 16）(5) a050_s43 registry 是 DONE/failed 但实际在跑——需要 v2 条目 (6) 论文中 1.4B 数据标 [PENDING C2] 直到 t10_a045 确认


---
