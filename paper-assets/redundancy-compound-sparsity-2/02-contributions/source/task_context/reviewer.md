---
loop: 2
reason: max_wall_time
updated: '2026-05-12T19:32:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（项目配置 `config/projects/solver-verified-formalizer-rl.yaml`）。之前因双进程共享 GPU 0 导致 OOM + 进程被 kill，**严禁在同一 GPU 上并行跑两个 14B 模型推理任务**。
- analysis_gamma_sweep 是 **D008 final gate**，不得被其他进程干扰或 kill。Gate 标准：任一 gamma beat random ≥5% → continue；全部 fail → archive 项目。
- inverted_ema_reasoning_v2 已被 Director 取消（D007），不得重跑。
- KeyDiff 描述已修正：kvpress 实现是 centroid-based O(B)（exact per-step mean），**不是** pairwise O(B²)。论文原始算法才是 block-wise iterative pairwise。memory.md / literature_map.yaml 中仍有不一致处需统一。

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，2×NVIDIA RTX PRO 6000 Blackwell 96GB
- 代码根目录：`/root/carc`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：`/root/carc/models/DeepSeek-R1-Distill-Qwen-14B`
- 数据：WikiText-2 arrow cache `/root/.cache/huggingface/datasets/wikitext/`；MATH 问题内嵌于脚本
- 结果目录：`/root/carc/results/`
- 活跃进程：analysis_gamma_sweep（PID 40063，GPU 0，31764 MiB）
- GPU 1：空闲（heatmap 已完成释放）
- 无 W&B 配置，不检查 W&B

### 3. 📊 当前状态
**我刚完成的审查**：
- inverted_ema_wikitext 结果核实（FAIL，PPL 8.79 vs random 7.71）
- GPU 0 双进程 OOM 事故审查（inverted_ema_reasoning 被 kill）
- gamma_sweep full eval 完整性确认（与 d003 交叉验证通过）
- KeyDiff 机制核实（kvpress 源码确认是 centroid-based）+ 自我修正
- analysis_heatmap 两批（WikiText + reasoning）完成确认，9 PDF 产出

**Registry 状态**：
- RUNNING：`analysis_gamma_sweep`（2/8 gamma 完成，gamma=0.1 PPL=8.17, gamma=0.3 PPL=8.21，当前跑 0.5，预计 ~2h 全部完成）
- PREPARING（需清理）：`inverted_ema_reasoning_v2`（应→CANCELLED）、`carc_generate_rope_test`（应→CANCELLED）、`analysis_heatmap`（应→DONE）
- DONE + negative：10/10

**等待中**：gamma_sweep 完成回调是唯一待处理事件。

### 4. 📋 待办
- gamma_sweep 完成 → 逐 gamma 核实 PPL 数据，交叉验证与 d003 baseline 一致性（gamma=0.9 应接近 7.78），判定 gate PASS/FAIL
- gamma_sweep gate FAIL（预期大概率）→ 确认 D008 archive 条件满足，无 rationalization
- gamma_sweep 中有任一 gamma beat random ≥5% → 仔细审查该数据点是否可复现（seed、OOM 影响等），不轻信单点结果
- Registry 清理提醒（已提 3 次）：inverted_ema_reasoning_v2 → CANCELLED，carc_generate_rope_test → CANCELLED，analysis_heatmap → DONE + 补 spec
- literature_map.yaml Synthesis 第 1 点 KeyDiff 描述仍不一致（写"每步精确重算 mean"但主条目写"O(B²) pairwise"），需统一

### 5. 🎯 战略上下文
**项目核心结论**：EMA centroid similarity 作为 KV cache eviction signal 被彻底证伪。10 连 negative，双向（evict low / evict high）都不如 random。根因：EMA running average 随序列增长收敛到全局均值，丧失区分度。文献（DefensiveKV）确认 mean aggregation 在 importance 突变时灾难性失败。

**决策链**：D001(MVP 定义) → D002(cross-axis FAIL, pivot to KV eviction) → D003-D004(sanity retry) → D005(sanity gate FAIL) → D006(inverted EMA pivot) → D007(inverted also FAIL) → D008(**gamma_sweep 是 final gate，FAIL 则 archive**)

**易错点**：
- 不要因为 recency baseline 极强（仅差 full 0.09%）就认为"所有 eviction 方法在 WikiText-2 上都不行"——H2O/SnapKV 等 attention-based 方法在此 benchmark 上是有效的，失败的是 EMA centroid 这条技术路线
- KeyDiff kvpress 实现 ≠ 论文原始算法。前者是 exact mean O(B)，后者是 block-wise iterative pairwise O(B²)。Agent memory.md 混淆了二者
- gamma_sweep 期间曾发生 OOM（GPU 0 双进程），full/random/recency baseline 已交叉验证有效，但若 OOM 后某个 gamma 的结果异常偏低（好得反常），要怀疑是 OOM 导致的截断/不完整 eval
