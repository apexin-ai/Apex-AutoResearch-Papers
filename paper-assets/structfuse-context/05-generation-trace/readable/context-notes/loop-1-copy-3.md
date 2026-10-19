# reviewer / loop_1.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`d1931fa07f7be9aa8cbd.json`](../../sessions/d1/d1931fa07f7be9aa8cbd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T14:42:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:4**（服务器 cqa1-21977，6x RTX 4090 D 24GB）。之前 GPU 5 违规被 CRITICAL 打回 3 次才修复。
- `/root/structfuse` 是指向 `/root/autodl-tmp/structfuse` 的 **symlink**——对此目录执行 rm/mv 前必须 `ls -la` 确认，上次 model migration worker 没查就 rm -rf 导致误删模型。
- 根分区只有 30GB，checkpoint/模型/大文件**必须**存 `/root/autodl-tmp/`。上次 P2b 因 checkpoint 写根分区爆盘崩溃。
- 训练时 eval 的 recall@5/10 是**退化指标**（候选池=4，等于 recall@1），P2b pass/fail 判定必须用 `scripts/eval_p2b.py`（完整候选池）。

### 2. 🖥️ 基础设施快照
- **服务器**：cqa1-21977(root)，工作目录 `/root/structfuse`（→ symlink `/root/autodl-tmp/structfuse`）
- **Python**：`/root/miniconda3/bin/python`，conda base 环境（不是 venv）
- **模型**：`/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B/`（已重新下载验证，5.75GB）
- **Checkpoints**：`/root/autodl-tmp/structfuse/checkpoints/`（已迁离根分区）
- **训练数据**：`/root/structfuse/mvp_data/training_data/`（train_{random,embedding,dataflow}.jsonl 各 505 条，val.jsonl 127 条）
- **Eval 输出**：`/root/autodl-tmp/structfuse/eval_results/`
- **训练日志**：`/tmp/p2b_p2b_{strategy}_s{seed}.log`
- **Pipeline 日志**：`~/runs/structfuse-context/mvp_p2b_contrastive_training.log`
- **W&B**：disabled（`WANDB_MODE=disabled`），审查只能靠日志
- **活跃进程**：P2b 9-run pipeline（PID 132149 bash wrapper / 132163 python train），tmux session `mvp_p2b_contrastive_training`，当前在 Run 2/9 (p2b_random_s123)

### 3. 📊 当前状态
**MVP 进度**：P1 PASS, P2a PASS（方向性，n=3 caveat），P2b 正在训练 Run 2/9。

- Run 1 (random/s42) **已完成**：eval_p2b.py recall@1=0.945, recall@5=0.984（127 samples, 完整候选池）
- Run 2 (random/s123) **训练中**：step 50, loss=0.3109，GPU 4 100% util
- Run 3-9 **排队中**：顺序执行，预计 ~8-10h

Registry 只有 2 条实验（mvp_p1 + mvp_p2a），P2b 尚未注册（训练完成后需要注册）。

**已发但未处理的 reviewer 建议**：
- eval_p2b.py `strict=False` 已修复（assert missing_keys 为空）✓
- 空 tokens train/eval 不一致（train 用 "[empty]" fallback，eval 过滤）— 未修复，影响小
- `set -e` 改为 per-run 错误处理 — 未采纳
- 文献 CoCoHaNeRe 缺失 + curriculum mining 条目可能幻觉 — 未处理

### 4. 📋 待办（条件触发式）
- **P2b 9 runs 全部完成** → 验证 `scripts/run_eval_all.sh` 是否自动执行 eval_p2b.py → 对比 3 strategy × 3 seed recall@5 → 按 pass criteria 判定（dataflow ≥ random+2pp in ≥2/3 seeds）
- **任一 run 再次崩溃** → 检查 `/tmp/p2b_*.log` 尾部错误 + GPU 状态 + 磁盘空间
- **P2b PASS** → 审查 post-MVP 规划（M1 全量提取 batch_extract.py 已就绪、run_m1_extraction.sh 已创建）
- **P2b FAIL** → 审查 fail_action（调训练策略 1 次：降 lr / 加 weight decay / 增大 num_negatives / early stopping），过拟合是首要排查方向（train loss 在 step 200 即为 0）
- **论文章节审查请求** → 先检查 Agent 是否读过 red-section skill（L1 红线 #1），再按 5.1/5.2 维度审查

### 5. 🎯 战略上下文
- **核心假设链**：CodeQL data-flow 可提取(H1 ✓) → data-flow 特征有区分度(H2 ✓) → data-flow hard negatives 训练优于 random/embedding(H3 待验证)
- **P2a 的 log_bm25 负系数**是有趣发现：BM25 在 bug fixing 定位中可能有误导性，值得论文讨论
- **最易判断错的事**：训练日志里的 recall@5/10 看起来很高（>96%），但这是 pool=4 的退化指标，没有区分度。必须用 eval_p2b.py 的结果（pool=25+）做判断。
- **过拟合风险已暴露**：Run 1 train loss step 200 起恒为 0，505 条数据对 3B 模型太少。如果 3 个 strategy 的 eval_p2b.py recall@5 差异 <2pp，过拟合导致所有策略趋同是最可能的解释——此时需要增大训练集或降低模型容量。
- **时间线**：EMNLP 2026 ARR deadline May 25（13 天窗口从 May 12 开始）。P2b 训练 ~10h，后面还有全量提取(M1 ~2d) + 全量训练(M2 ~2d) + 评估(M3 ~3d) + 写作(M4 ~3d)。时间紧但 AI agent 节奏下可行。


---
