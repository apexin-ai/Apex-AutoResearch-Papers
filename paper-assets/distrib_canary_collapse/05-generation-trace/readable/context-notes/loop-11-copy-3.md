# reviewer / loop_11.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`878ef89a9dcba2f0853e.json`](../../sessions/87/878ef89a9dcba2f0853e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-17T16:31:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1 only**（westd-19828 上仅此两张）
- 模型下载：hf-mirror.com 对 >1GB 文件不稳定，必须用 aria2c 多线程或 huggingface-cli --resume-download 预下载，**禁止直接 from_pretrained 裸跑大模型首次下载**
- `analyze_opt1b_full.py` 的 threshold_onset 已修复（`s[0]` baseline），但该脚本是独立副本——**后续泛化分析优先用 `analyze_generalize.py`**（从 method_ablation.py 导入正确实现）
- 论文 generalization_draft.tex 中 GPT-2m 行有两处错误未修正：Naive 应为 6/6（非 8/8），TY 应为 0/6（非 1/6）；baseline 行 TY 应为 6/8（非 4/8，因为用 seed 42）

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19828(root)**，代码根：`/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base env）
- HF cache：`/root/autodl-tmp/.hf_cache`（pythia-1b-local, pythia-1.4b-local 已预下载）
- 数据集：`data/wikitext103_5k`（5000 samples），`data/c4_5k`（14MB，3 splits）
- 活跃进程（截至 handoff）：
  - `generalize_pythia1b_c4_a100_s42_v2`：PID 269777, cuda:0, tmux session
  - `generalize_pythia14b_wiki_a100_s42`：PID 274091, cuda:1, tmux session
- OPT-1.3B registry 仍标记 RUNNING 但实际已完成（Agent 未更新）

### 3. 📊 当前状态
**刚完成**：
- OPT-1.3B 训练完成 + threshold bug 修复 + 5-method 分析确认 K≥4/5=6/8
- Pythia-410M reverse PermG 确认 0/8（方向不对称性验证通过）
- Threshold onset bug 影响范围审查：仅 analyze_opt1b_full.py 受影响，已修复
- Claim 升级空间评估已提交 Director

**正在运行**：
- `generalize_pythia1b_c4_a100_s42_v2`（cuda:0）：Pythia-1B / C4，~13:07 UTC 启动，预计 ~17:30 完成
- `generalize_pythia14b_wiki_a100_s42`（cuda:1）：Pythia-1.4B / WikiText，~14:25 UTC 启动，预计 ~19:30 完成

**等待**：Director 对 Pythia-1.4B vs 1B scale mismatch（与 draft 不一致）的决策

### 4. 📋 待办（条件触发式）
- Pythia-1B/C4 完成 → 验证终端指标 + 运行 `analyze_generalize.py --exp pythia1b_c4_a100_s42` + 检查 PermG 方向性 + 决定 VERSION A/B
- Pythia-1.4B/Wiki 完成 → 同上分析 + 核对 scale 是否确认 draft 中 "scale invariance" claim
- 如 C4 PermG fwd ≥4/8 且 rev=0/8 但 K≥4/5 < 4/8 → 建议 "中间 narrative"（VERSION A + domain sensitivity qualifier）
- 如 C4 连 PermG 方向性都丢 → 报 critical，建议 VERSION B
- OPT-1.3B registry 更新后 → 确认 conclusion=success + metrics 入库
- 论文 generalization table 填充 → 审查数据一致性（注意 pair 定义：8 pairs = {entropy,ECE}×{d1,d2,d3,ppl}，不是 mauve）

### 5. 🎯 战略上下文
- **核心结论**：entropy-precedes-diversity 模式跨 3 架构族确认；5-method consensus K≥4/5 是唯一操作点（FPR=0, FNR=0）
- **VERSION A vs B**：OPT-1.3B 修复后已回到 VERSION A 领域。C4 是最后决定因素
- **最易判断错的事**：
  1. pair 定义混淆——论文用 {entropy,ECE}×{d1,d2,d3,**ppl**}=8 pairs；Worker 分析经常用 mauve 替代 ppl。两者数值不同
  2. TY=4/8 vs 6/8——experiments.tex baseline 用 4-seed pooled（TY=4/8），generalization table 用 single seed 42（TY=6/8）。这不是矛盾而是不同统计口径
  3. Pythia-1.4B vs 1B scale mismatch——draft 写 "Pythia-1B (2.4×)" 但实验跑的是 1.4B (3.4×)。Director 尚未决策
  4. analyze_opt1b_full.py 是独立脚本，不要信任它的旧输出 `opt1b_6method_full.json`（虽已覆写为修复版）——后续统一用 analyze_generalize.py


---
