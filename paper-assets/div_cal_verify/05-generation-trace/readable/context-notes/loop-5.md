# reviewer / loop_5.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`4f5d3cd7d50ff8864004.json`](../../sessions/4f/4f5d3cd7d50ff8864004.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T07:15:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 `westd-11235` 的 `cuda:0` 和 `cuda:1`（config: `gpu_ids: [cuda:0, cuda:1]`）
- 账号 `root`，代码根目录 `/root/div_cal_verify`，数据盘 `/root/autodl-tmp/div_cal_verify/`
- 355M 数据目前只有 seed=42 完整 + seed=123 大部分完成（random50 运行中），论文中所有 355M 数值必须标注 n=1 或 n=2，不可写成 n=3
- 125M 数据全部用 3-seed 均值±SD，不可混用单 seed 值（seed=42 uncurated PPL=50.28 是离群值，用了会高估 gap）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-11235`（root），2×NVIDIA RTX PRO 6000 Blackwell 98GB，CUDA 13.2，Driver 595.58
- 代码：`/root/div_cal_verify/`，结果输出：`/root/autodl-tmp/div_cal_verify/results_medium_*/`
- 分析脚本：`/root/div_cal_verify/analyze_355m_3seed.py`（已验证路径构造正确）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/`
- 论文 tex 文件：`docs/paper/{introduction,related_work,results,discussion,conclusion,main}.tex`
- 活跃进程（截至 handoff）：
  - cuda:0: PID 453372 — `medium_random50_seed123`（tmux: `chain_cuda0_s123`，Gen 0 训练中）
  - cuda:1: PID 462871 — `medium_external_seed456`（tmux: `medium_external_seed456`，刚启动）
- GPU 0 有 ~49GB 幽灵显存（nvidia-smi 报 71641 MiB vs 进程 22460 MiB），疑为 Blackwell 驱动行为，训练未受影响

### 3. 📊 当前状态
**刚完成的审查**：
- 全文数值一致性审查（125M 统一 3-seed ✅，355M 标注 n=1 ✅）
- 论文质量审查（Intro/RW/Ablation 三维度，已提交 Director）
- Ceiling effect 叙事框架评估：推荐 Modified Option B，核心证据是不对称 gap 方向（RGDS gap 缩小 4 倍 vs uncurated gap 扩大 3.4 倍）
- 355M seed=123 cross-seed 一致性：**发现 RGDS vs Uncurated 排序翻转**（seed=42 uncurated 最差，seed=123 rgds 最差），已报告 Director

**Registry RUNNING**：
- `medium_random50_seed123` — cuda:0, Gen 0/7
- `medium_external_seed456` — cuda:1, 刚启动

**已完成待更新 registry**（Worker 可能已处理）：
- `medium_uncurated_seed123` → DONE, gen7 PPL=87.05
- `medium_rgds_seed123` → DONE, gen7 PPL=90.25, gen7 ratio=0.8728
- `medium_external_seed123` → DONE, gen7 PPL=79.56

### 4. 📋 待办（条件触发式）
- `medium_random50_seed123` 完成 → 立即验证 gen7 PPL，计算 355M seed=123 RGDS vs Random gap（预期 +25-30%），确认 C3 跨 seed 成立
- `medium_random50_seed123` 完成 → cuda:0 应自动进入 `chain_cuda0_seed456`（uncurated→rgds→random50），验证 chain 启动
- `medium_external_seed456` 完成 → cuda:1 应自动接 random50_seed456 或需手动启动，核实 auto-chain
- 全部 seed=456 完成 → 运行 `analyze_355m_3seed.py`，验证统计检验结果；特别关注：355M RGDS gen7 ratio 3-seed 均值是否 >0.8（当前 2-seed 均值 0.852±0.029）
- 论文 Table 3 补 External-only 行 + 更新 "in progress" → Paper Agent 应该做，Reviewer 需验证
- Discussion §6.3 line 31 "which a pure compression effect would not predict" → 需删除/弱化，已报告但未确认 Paper Agent 是否修复

### 5. 🎯 战略上下文
**项目核心**：Embedding Alignment Gap——内部嵌入 diversity selection 在迭代自训练中加速 model collapse（+72% PPL vs random, 125M 3-seed）。投 EMNLP 2026 ARR，DDL 2026-05-25（还 11 天）。

**决策链关键节点**：D014（framing 修正 C2-revised）→ D017（S3 降级）→ D019（追加 355M seed=456）→ D020（scaling 叙事双假说共存）

**最容易判断错的事**：
1. **355M RGDS vs Uncurated 排序不稳定**：seed=42 uncurated 最差，seed=123 rgds 最差。不要写 "RGDS outperforms uncurated at 355M"——这只是 seed=42 的偶然。正确表述：方法间差距在 355M 高 PPL 区间压缩，排序跨 seed 不稳定
2. **不对称 gap 是排除 ceiling effect 的核心证据**，不是 "absolute gap also contracts"（后者逻辑有缺陷，ceiling effect 也能产生绝对差缩小）
3. **125M 数据永远用 3-seed 均值**，不要被 paper_framing.md 里残留的 seed=42 单值（+5.3%/+16.4%）误导——那些需要更新为 +7.4%/+8.9%
4. **GPU 0 幽灵显存**：~49GB 差值是 Blackwell 驱动行为，不是越界进程，不要 critical


---
