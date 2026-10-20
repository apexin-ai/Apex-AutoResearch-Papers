# reviewer / loop_1.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`c4bd21acf32e593ec0af.json`](../../sessions/c4/c4bd21acf32e593ec0af.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T22:36:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3 全部属于本项目，但实验实际只用 cuda:0（其余空闲）
- 服务器上存在 flat 结构 `/root/autodl-tmp/pacs/profiling/` 和 package 结构 `/root/autodl-tmp/pacs/pacs/profiling/` 两套目录，Python 加载 flat 结构。同步代码时两处都写，否则改了不生效
- KV eviction mask 绝不能 per-layer 独立生成再合并——28 层交集存活率指数衰减到 ~0%（P0 教训，已修复为单一 1D mask 所有层共享）
- v2 registry 仍卡在 ANALYZING 状态未关闭为 DONE

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，4× RTX PRO 6000 Blackwell 97GB (sm_100+, compute cap 12.0)
- 工作目录：`/root/autodl-tmp/pacs/`
- Python：`/root/miniconda3/bin/python`（conda base, Python 3.12.3, PyTorch 2.10.0+cu128）
- 模型：`/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B`（符号链接，fp16 ~14GB）
- 数据：`/root/autodl-tmp/pacs/data/math500.json`（500 题，实验用 stratified 50）
- 活跃进程：mvp_ii_profiling_v3 (PID 16717, tmux, cuda:0, RUNNING)
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/`
- 无 W&B 配置

### 3. 📊 当前状态
**刚完成**：审查了 mvp_ii_profiling_v2 结果（conclusion=negative）、GMM 诊断、importance-vs-random masking 对比、文献检索。已发 5 条 reviewer_post_to_director。

**RUNNING**：`mvp_ii_profiling_v3`（quantile segmentation + sparsity 10%/20% + NaN guard），预计 ~0.5h 完成。

**等待**：
- M1v3 cron on_complete 回调 → 需要独立审查 v3 结果（这是 MVP 最终判定）
- Director 对 importance-vs-random sub-additive 发现的决策（是否追加 importance-based 全实验）
- Agent 的 arXiv 引用验证结果（文献检索 warning 已发）

### 4. 📋 待办
- M1v3 完成 → 读 `/root/autodl-tmp/pacs/profiling_output_v3/profiling_results.json` + registry metrics → 核查：(1) quantile 分组是否均衡（各组 ~33%），(2) 10%/20% sparsity 下 PPL 是否有限（无 Infinity），(3) II CI 是否跨组不重叠，(4) NaN guard 是否生效。如果全部 super-additive 且 CI 重叠 → MVP FAIL，建议 pivot
- M1v3 FAIL + Director 决定追 importance-based → 审查新实验设计：importance 计算方法、calibration 数据、是否 per-phase breakdown
- M1v3 PASS → 审查 claim 强度是否匹配证据（只在 1 model + 1 dataset 验证 → 不能 claim "general"）
- Agent 提交论文章节 → 按 section 5 写作对抗审查（合规检查 + claim 可信度 + 审稿人攻击面）

### 5. 🎯 战略上下文
**决策链**：D001(MVP 方案) → D007(v1 failed, P0+P1) → D008(v2 negative, pivot to magnitude)

**核心发现链**：
- v1: 全 NaN（P0 KV mask 交集 bug）→ 修复
- v2: 全 super-additive、无 sign reversal、KDE 90.7% transition（P1 未解决）→ conclusion=negative
- importance-vs-random: 30% importance compound II=-0.91（sub-additive!）vs random II=+9.38 → **可能是真正的突破口**，但仅单次测量未做统计验证
- GMM BIC k=5（不是 3）→ 3-phase taxonomy 不是数据最优

**下一个"我"最容易判断错的事**：
1. **M1v3 用的仍是 random masking**。即使 v3 修了 segmentation 和 sparsity，如果 masking 仍是 random，大概率继续全 super-additive。不要因此直接判 MVP FAIL——importance-based 方向还没测
2. **不要把 importance-vs-random 的 aggregate 数字当 per-phase 结论**。那个实验没做 phase breakdown，sub-additive 可能只在某些 phase 出现
3. **v2 的 attn-only PPL 在 v1→v2 之间 0.3 sparsity 下差了 9-19×**（execution: 1066→55, reasoning: 17→1.8），原因未查明，可能是 C3 fix 的副作用。v1 和 v2 不是 controlled experiment
4. **文献引用有幻觉风险**——SparK/ThinKV/RAC 的会议归属（AAAI 2026/ICLR 2026/NeurIPS 2025）未经 arXiv 验证
5. **EMNLP 2026 ARR 截稿 2026-05-25（距今 12 天）**，240h GPU 预算只用了 ~1.5h。4 张卡空闲是浪费——如果 M1v3 方向明确，应立即启动 M2/M4 并行


---
