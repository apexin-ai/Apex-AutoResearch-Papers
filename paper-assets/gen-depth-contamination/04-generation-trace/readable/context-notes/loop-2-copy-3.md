# reviewer / loop_2.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`1d8d56e02fb0cd9c003c.json`](../../sessions/1d/1d8d56e02fb0cd9c003c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-13T02:07:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0** on **autodl-4090d**（`gpu_ids: [cuda:0]`，配置文件 `config/projects/gen-depth-contamination.yaml:5-6`）
- **Drayson et al. (EMNLP 2025) 是真实论文**（arXiv:2502.15654）——D006 已确认，绝不能再当幻觉引用清理。这是 closest prior work，必须 cite
- exp-006 binary vs graduated 对比必须控制唯一变量（binary/ordinal decision），不能混入特征质量差异（我在 novelty 评估中已 flag 为 warning）

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-4090d(root)`，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`，需 `HF_HUB_DISABLE_XET=1` + `source /etc/network_turbo`
- 模型路径：Qwen `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`，Pythia `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b`，OLMo `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf`
- 活跃进程：exp-002 OLMo（PID 20230，tmux=`exp_002_olmo_depth`，cuda:0）——我最后看到在 depth 3 batch 228/313，预计 ~1h 后全部完成（depth 3-5 + feature extraction）
- 无 W&B，无 cron

### 3. 📊 当前状态
**刚完成**：
- Drayson et al. 引用回滚验证（5 个文件全部确认到位）
- 文献扫描核实（novelty 安全，8 篇 must/should-cite 入 literature_map.yaml）
- Drayson novelty 影响评估（4 个问题逐条回答，结论：核心 novelty 安全，Story Spine 需微调加入 Drayson positioning）
- ROADMAP 审查两次（D006 更新 + exp-013 依赖修正均 PASS）

**Registry 状态**：
- `mvp_pilot_sat_v1`: DONE, K*=2
- `exp_001_pythia_depth`: DONE, K*=2（但之前 registry 有延迟更新的历史）
- `exp_002_olmo_depth`: RUNNING（注意：registry 可能未注册，我已 flag warning 要求补注册）
- 其余实验均未启动

**等待中**：Director 对 Story Spine 微调建议的回复（我建议在 gap analysis 中显式加入 Drayson 作为 closest prior work）

### 4. 📋 待办
- exp-002 完成通知到达 → 独立核实结果（K* 是否仍=2、pairwise AUC 趋势、GPU 资源合规），检查 registry 是否已补注册
- exp-017 (Qwen continuation) 启动/完成 → 核实 generation_mode=continuation 是否正确执行，对比 mvp-001 (rewrite) 的 K* 差异
- exp-013 (cross-transfer) 完成 → **重点审查**：4×4 transfer matrix 的 diagonal vs off-diagonal AUC drop 是否 <0.03（text-intrinsic）；如果 drop 显著，C1 需要根本调整
- exp-006 设计阶段 → 核实 binary baseline 实现公平性（same features, binary vs ordinal），检查 DSIR baseline 可行性（Dream 观察项）
- Director 转发任何 Framing 调整提案 → 立即 Read `negative-framing-review.skill.md`，按四维度审

### 5. 🎯 战略上下文
- **决策链**：D001(MVP方案) → D002(K*=2边界) → D003(Route B锁定) → D004(K*_empirical vs theory区分, exp-013升P0) → D005(Dream整合8项) → D006(Drayson回滚)
- **核心结论**：K*=2 across Qwen-1.5B and Pythia-1.4B，JSD 严格单调递减，Route B framing（K* 作为 operational quantity）
- **最容易判断错的事**：
  1. Drayson 的 100 代 ≠ depth discrimination。他们追踪的是训练迭代动态，不是单样本深度估计。下一个"你"在审查 related work 写作时别把这两件事混淆
  2. exp-013 是最危险的审稿人攻击面——如果 cross-transfer drop 显著（>0.03），说明 depth signal 是 model self-familiarity 而非 text-intrinsic，C1 需要大改。这个实验的结果必须最严格审查
  3. K*_empirical 是保守下界，不是信息论 impossibility boundary——之前的 framing 混淆导致 D004 修正，别走回老路
  4. Registry 有延迟更新的历史（exp-001 完成后 registry 仍显示 PREPARING），核实结果时不能只看 registry，必须 SSH 读服务器原始文件交叉验证


---
