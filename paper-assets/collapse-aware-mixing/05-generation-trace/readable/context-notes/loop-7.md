# agent / loop_7.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`de28c224f1322f959d69.json`](../../sessions/de/de28c224f1322f959d69.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-14T15:14:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0`（cqa1-38874），无其他可用 GPU
- **MVP 已判定 FAIL (D018)**，三条路径全封——不要尝试重新验证 eff_rank 作为 leading indicator，这个方向已被 18 checkpoint 公平对比 definitively 否定
- Pivot B generated eff_rank 噪声是 n-gram entropy 的 573 倍——不要试图用更密的 checkpoint 采样"救"它
- 当前项目处于**待 Director 决策**状态（Q2 negative result paper 或 archive），未获决策前不动 paper、不开新方向实验
- submit 命令必须包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，tmux 默认用 sh 不继承 conda
- AutoDL 网络访问需 `source /etc/network_turbo` + SSL 证书环境变量，否则 HF 不可达

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-38874, 1× RTX PRO 6000 96GB
- **工作目录**: `/root/collapse-aware-mixing/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，Python 3.12, PyTorch 2.10.0, transformers 4.57.6）
- **输出目录**: `/root/autodl-tmp/output_v7/`（v7 主实验）, `/root/autodl-tmp/output_seed0/`（seed0 复现）
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **数据**: wikitext-103-raw-v1（HuggingFace），20M tokens/gen × 3 generations
- **模型**: EleutherAI/pythia-1b
- **活跃进程**: mvp_seed0_replication_r2（PID 122208, tmux session, cuda:0）
- **活跃 cron**: mvp_seed0_replication_r2（reconcile 确认 still running）
- **磁盘注意**: 根分区 ~30GB，大文件必须放 `/root/autodl-tmp/`

### 3. 📊 当前状态
**刚做完**: 文献扫描确认 negative result 有 novelty（无人报告过 holdout eff_rank 在 collapse 中上升），artifact `literature_scan_20260514.md` 已注册。D018 确认 MVP FAIL，三条路径总结写入 ROADMAP。

**RUNNING**: `mvp_seed0_replication_r2` — seed=0 复现 v7（seed=42）实验，验证 holdout eff_rank 上升是否 seed-robust。截至 09:15 UTC，G0 完成，G1 generation 95%（291/306 batches），G0 metrics 与 v7 高度一致（eff_rank 676.89 vs 676.96, ppl 13.27 vs 13.27）。`analyze_seed0_vs_v7.py` 已部署在服务器上。预计还需 ~8-10h 完成全部 3 代。

**其余实验**: 全部 DONE（5 failed, 2 negative, 3 killed）。

**等待中**: 
- mvp_seed0_replication_r2 cron 回调（完成后需分析 seed0 vs v7 一致性）
- Director 决策：Q2（negative result paper → EMNLP 2026 Findings）或 archive

### 4. 📋 待办（条件触发式）
- **seed0 cron 回调到达** → spawn worker 运行 `analyze_seed0_vs_v7.py` 做 seed0 vs v7 跨代对比 → 更新 registry metrics → 汇报 Director（若两 seed 一致则 Q2 multi-seed 条件部分满足）
- **Director 决策 = Q2** → 需补实验：(1) multi-scale（Pythia-410M / Pythia-2.8B，每个 ~1 天），(2) seed0 已在跑，再补 seed=123 → 3 seeds 完整。总计 ~3-4 天 GPU。同时启动 paper outline（negative result framing）
- **Director 决策 = archive** → kill seed0 进程，释放 GPU，关闭项目
- **seed0 失败（磁盘满/OOM 等）** → 检查 `/root/autodl-tmp/` 空间，上次 seed0 第一次尝试就因磁盘仅剩 7GB 失败过。必要时清理旧 output（v5 的 `/root/autodl-tmp/output/` 可安全删除）

### 5. 🎯 战略上下文
**核心结论链**:
- D014: C1 原假设 falsified — holdout eff_rank 在 collapse 中反向上升 +0.96%
- D016→D018: Pivot B generated eff_rank 信号存在但不优于 n-gram entropy（同时检测、噪声高 573 倍）
- 唯一剩余价值：**negative result 本身** — "holdout spectral eff_rank rises during mode collapse" 挑战了 SIGMA 等工作的隐含假设

**易判断错的事**:
- 不要被 seed0 G0 metrics 与 v7 的高度一致性误导为"方法可能有效"——一致性恰恰证明 eff_rank 对 collapse 不敏感（两个 seed 都不下降）
- Q2 negative result 的卖点**不是** "eff_rank 检测不到 collapse"（太平凡），而是 "eff_rank 反向上升"——这才是反直觉的、有发表价值的发现
- memory.md 记录了 `compare_eff_rank_vs_ngram.py` 阈值不对称问题（eff_rank 0.5% vs n-gram 10%），写论文时必须用统一阈值重新判定，否则审稿人会攻击
- SVD vs Gram matrix 命名不一致（代码用 SVD σ_i，framing 写 Gram λ_i = σ_i²）——论文描述需与代码对齐
- padding_side='right' confound 可能人为加速了 collapse 的 quantitative magnitude，但不影响 holdout failure 的定性结论


---
