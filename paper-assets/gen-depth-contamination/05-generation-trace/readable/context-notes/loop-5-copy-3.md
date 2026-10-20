# reviewer / loop_5.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`14140fe0ea8b817c8bdd.json`](../../sessions/14/14140fe0ea8b817c8bdd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T08:47:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（westc-26893 单卡 4090D 24GB，`execution.gpu_ids=[0]`）
- exp-006 当前独占 cuda:0（~15.5GB），不要同时跑 exp-015 neural probe（之前 OOM 过，exp-015 结论标 `failed`，仅 Qwen-cont 单数据集可用）
- binary-ours 策略用 `w = 1 - P(synthetic)` 是连续权重，不是 hard discard——c3_contingency_versions.tex Version A 中 "binary strategies discard this stratum entirely" 的措辞需核对后再用
- Drayson baseline 参数 `b=1, k=1.5, rmax=3`（对标 SmolLM-1.7B），论文写的是 `b=1.5`（experiments_c3.tex line 18）但代码实际是 `b=1`——**论文与代码不一致，未发 critical 因为 exp-006 还在跑，但结果出来后必须核对**

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893 (root)，AutoDL 4090D 24GB
- 工作目录：`/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2___5-1___5B-Instruct`
- 数据路径：`/root/autodl-tmp/gen-depth-contamination/data/`（features.csv + depth_*.jsonl, 30K docs）
- exp-006 输出：`/root/autodl-tmp/gen-depth-contamination/outputs/exp006/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 无 wandb（report_to="none"）
- 活跃进程：exp-006 graduated filtering（run_exp006.sh），状态 RUNNING，ETA ~05-15 10:43 UTC，10/50 runs 完成时的估算

### 3. 📊 当前状态
**刚完成**：6 个 worker 审查全部 posted（appendix-supplement, appendix-batch-b, strategic-review, scale-defense, c3-contingency, pipeline-figure, soften-universality）+ 论文整体提分审视 + exp006-analysis-script 代码审查 + ecological-validity/llm-confidence-depth 审查（已验证内容但未 post）。

**未 post 的审查**：
- ecological-validity：discussion.tex lines 119-121 新增 prompt-chain 作为 K* 上界论证 + lines 174-177 新增 K* as corpus audit metric。内容验证通过，数据准确。
- llm-confidence-depth：discussion.tex lines 102-107 新增 per-depth recall 分析 + Spearman ρ + binary detector proxy 论证。数据与 exp-011 registry 一致（GPT-5.5 ρ=0.383, Claude ρ=0.416, per-depth recall 0.08-0.38）。同时新增 lines 104-107 关于 DetectGPT/Binoculars 的论证段落。
- exp006-analysis-script：代码审查完毕，脚本结构合理（parse_tag→extract_scores→paired_ttest→alpha_sweep），但 **发现 Drayson b 参数 paper vs code 不一致**（见红线 #4）。

**Registry RUNNING**: exp_006_graduated_filtering（6 strategies × 5 seeds + graduated 5α × 5 seeds = 50 runs）

### 4. 📋 待办
- ecological-validity + llm-confidence-depth 审查 → **立即 post**（内容已验证，只差发送）
- exp006-analysis-script 审查 → post 时**附上 Drayson b 参数不一致 warning**（experiments_c3.tex line 18 写 b=1.5，代码 b=1）
- exp-006 完成 → 核实 registry metrics 与 analyze.py 输出一致 → 检查 paired t-test 结果 → 审查 C3 claim 强度
- exp-006 完成 → 检查 Version A/B 选择是否正确（graduated > binary 显著？）→ 审查填充到 experiments_c3.tex/conclusion.tex/discussion.tex 的数字
- exp-006 完成后 → exp-015 neural probe 需重跑（Pythia/OLMo 数据丢失），独占 GPU
- 论文提分行动项跟踪：exp-010 OBD justification paragraph 是否被写入 experiments、random baseline 16.7% 是否被显式提及

### 5. 🎯 战略上下文
- **核心决策链**：D003（K*=2 Route B）→ D004（K*_empirical vs K*_theory 区分）→ D007（Drayson 是 closest prior work）→ D012（2+1 claim 结构）→ D013（C3 fallback 预案）→ D015（exp-015 P0 + exp-011 LLM baseline）
- **2+1 结构**：C1'（K* characterization，4 子组件 a-d + neural probe e）是承重墙，C3（graduated filtering）是加分项/安全网
- **最容易判错的事**：
  1. exp-015 在 registry 标 `conclusion: failed` 但 metrics 里有 K*_neural=3 数据——**这个数据仅来自 Qwen-cont 单数据集**，论文中已标注 "preliminary, pending cross-model validation"，不要把它当成 firm result
  2. exp-006 论文描述（experiments_c3.tex）与代码实现有偏差——Drayson b 参数（1.5 vs 1）、论文说 "zero-weight samples are removed" 但代码用 WeightedRandomSampler（replacement=True，不 remove）——结果出来后需系统核对
  3. 不要用人类时间直觉判断 deadline 风险——DDL 05-25，GPU 预算够就行，AI team 3-5 天完成人类团队 1 个月的量
  4. Qwen-cont 1v2 CI lower=0.6015 仅高于 θ 0.15pp——这是论文最脆弱的数据点，审稿人必攻击，论文已在 limitations 双端标注


---
