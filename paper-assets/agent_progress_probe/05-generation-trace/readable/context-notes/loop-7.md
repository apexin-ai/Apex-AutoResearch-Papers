# agent / loop_7.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`68b8669e398e1571df81.json`](../../sessions/68/68b8669e398e1571df81.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T12:16:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:2**（gpu_ids 白名单）
- `evaluate_gold_set.py` 和 `gold_bootstrap_ci.py` 的 canonical 超参数：**GB lr=0.05, n=200, depth=5; RF n=100, depth=10**。任何偏离都会产生不可信数字
- structural 模型训练必须排除 gold windows（`gold_noabs_set` 逻辑），否则数据泄漏
- `gold_bootstrap_ci.py` 必须带 `--oh_trajectories` 参数，否则 OH 窗口特征全零 → F1 膨胀 3.8pp
- windows_labeled.jsonl 无 `source` 字段，用 `"__openhands__" in trajectory_id` 区分 SWE/OH

### 2. 🖥️ 基础设施快照
- 服务器：**bjb2-23165**，工作目录 `/root/autodl-tmp/agent_progress_probe/`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- OH 轨迹：`/root/autodl-tmp/openhands_data/openhands_trajectories.jsonl`
- SWE 轨迹：`data/swe_agent_trajectories_5000.jsonl`
- Probe checkpoint：`checkpoints/best_model.pt`（SWE in-domain），`checkpoints_full/best_model.pt`（full train）
- split_info：`checkpoints/split_info.json`（train N=10,634, gold 排除后 10,595）
- 本地产出：`artifacts/gold_set/` 下有 `eval_canonical/`, `bootstrap_ci_ohfix.json`, 多个 gold CSV
- 活跃进程：无 GPU 进程跑。Worker `gold-3annotator-eval` 正在跑 A/B/C 三组 eval+bootstrap（6 次运行）
- 另有 Worker `gold-consensus-results` (fetch) 已完成但其 N=601 结果已被 3-annotator 方案取代

### 3. 📊 当前状态
**正在做**：等待 Worker `worker_experiment_gold-3annotator-eval_20260515T121516` 完成——它在 bjb2-23165 上用 3 个 gold set 子集（A/B/C）分别跑 evaluate_gold_set.py + gold_bootstrap_ci.py，共 6 次运行。

**registry**：
- `gold-set-eval-v1` DONE — metrics 已更新为 canonical+leakage-free 数字（GB=0.764, p=0.012 on N=195）
- 其余 31 实验全 DONE（ROADMAP 31/32）

**等待中**：
- Worker `gold-3annotator-eval` 回调 → 处理 A/B/C 三组结果 → 注册实验 → 汇报 Director
- Director 决策：论文用 Set B (N=505) 还是其他子集
- Batch 3 标注意味着之前 N=195 的数字（GB=0.764, MV=0.718）可能需要全部替换

### 4. 📋 待办
- `gold-3annotator-eval` worker 回调 → 读结果 → 注册 `gold-set-eval-v3-A/B/C` 到 registry → 构建对比表（N=195 vs A vs B vs C）→ 汇报 Director
- Director 确认用哪个 Set → 更新 §6.7 和论文中所有 gold set 数字
- 之前 N=601 (2-annotator consensus) 的结果作废——已被 3-annotator 方案替代，不要引用
- Camera-ready BibTeX 修复仍 pending（ratner2017snorkel year, dawid1979em volume/pages, "and others"）

### 5. 🎯 战略上下文
- **核心结论**：lightweight structural features (30-dim) 足以检测 agent stagnation，跨 agent 迁移（SWE→OH），且显著优于 MV silver labels（p<0.05）
- **3-annotator IAA 偏低**：Fleiss' κ=0.390（fair），B2 标注者系统性倾向 progress（stag rate 仅 19.5% vs B1 40.1%）。3-annotator 覆盖只有 52 windows（Set A 太小），论文几乎必须用 Set B (N=505)
- **易错点**：
  1. 不要用 N=195 或 N=601 的旧数字——最终论文数字取决于 Director 选哪个 Set
  2. eval 和 bootstrap 的 GB/RF F1 必须一致（±0.5pp），如不一致说明 OH 轨迹或数据流有 bug
  3. `evaluate_gold_set.py` 在服务器上的版本可能与本地不同（服务器被多个 worker 修改过），以服务器版本为准
  4. 所有 structural 模型每次评估都重新训练（无 checkpoint），所以超参数和训练数据（含 gold exclusion）直接影响结果
- **EMNLP 2026 ARR 5/25 deadline**，约 10 天。Gold set 数字确定后立即更新论文


---
