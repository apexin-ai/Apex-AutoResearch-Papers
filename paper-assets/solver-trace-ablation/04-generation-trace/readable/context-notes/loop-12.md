# agent / loop_12.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`d572b648dee23cdc438e.json`](../../sessions/d5/d572b648dee23cdc438e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-15T14:53:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`，禁止用其他 GPU
- 所有 eval 必须用 `proofwriter_fol_100.jsonl`，不能用 `test_100.jsonl`（D062/D063 教训）
- 提交 eval 前必须检查 GPU 空闲，避免 OOM
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Taxonomy 已升级到 8 种 hacking modes（H1-H8），不是 7 种。H8 = conjunction collapse
- D076 纠正：ISR β=0.3 1000步的 genuine=43.2% 是误标，实为 H8。不要引用旧数据
- D051：2.4x 作废，premise-count-matched 1.06x 定论。论文中不得出现 2.4x
- plan013 vs plan017 公式结构不同，不可简化为 "additive vs convex" 对照（D027）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-39279`，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型输出：`/root/autodl-tmp/outputs/`（各实验子目录）
- HF cache：未确认（可能 `/root/autodl-tmp/.hf_cache`）
- 基础模型：Qwen3-4B
- 数据：`/root/solver-trace-ablation/data/train_500_seed42.jsonl`（500条）
- 活跃进程：
  - `plan001-exec-only-s43-1000-r2`: PID 363692, tmux session, cuda:0, cron 监控中
  - `plan001-exec-only-s44-1000-r2`: PID 363840, tmux session, cuda:1, cron 监控中
- 活跃 Worker：`worker_code_classify-h7-bugfix-clean-run`（H7 分类器 bugfix，14:50 启动）

### 3. 📊 当前状态
**刚完成**：磁盘满事故修复（D080），清理磁盘后重提交 exec-only s43/s44 1000步（r2）。SFT 3-seed 1000步 Reviewer PASS（D079）。Taxonomy 升级 7→8 modes（D081/D082）。Bootstrap CI 统计检验完成。

**RUNNING (2)**：
- `plan001-exec-only-s43-1000-r2`：exec-only 1000步 seed=43，cuda:0——最后缺的 3-seed 数据点之一
- `plan001-exec-only-s44-1000-r2`：exec-only 1000步 seed=44，cuda:1——最后缺的 3-seed 数据点之二

**PREPARING (3，等 GPU 空出)**：
- `plan002-additive-b01-s43-r2`：ISR β=0.1 s43 重训，checkpoint+eval 丢失需补
- `plan018-additive-random-b01-s44-r2`：Random β=0.1 s44 重训，数据丢失需补
- `plan018-additive-random-b01-s43-r3`：Random β=0.1 s43 重训，数据丢失需补

**等待中**：
- 2 个 cron 监控 exec-only s43/s44 完成回调
- Worker `classify-h7-bugfix-clean-run` 完成回调
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- exec-only s43-1000-r2 或 s44-1000-r2 cron 回调(ANALYZING) → spawn Worker 做 eval + taxonomy 分类 + 与 s42 1000步(PR=0.96, ISR=0.003, H1=100%) 对比
- exec-only 3-seed 1000步全部完成 → 计算 3-seed mean±std → 更新论文 §4 主表（SFT 92.2% vs exec-only ?% vs ISR ~3% vs random 0%）
- 两个 RUNNING 实验完成释放 GPU → 立即提交 PREPARING 队列的 3 个 500步重训（plan002-s43-r2 + plan018-random-s44-r2 + plan018-random-s43-r3），注意只有 2 块 GPU，需排优先级（plan002 ISR 数据更关键）
- H7 bugfix Worker 完成 → 检查分类器修复是否影响历史 taxonomy 数据，可能需要回溯验证
- 所有重训数据补齐 → 论文 TeX 数字最终一致性审计 → submit_paper_to_review
- 论文 DDL 2026-05-25，剩 10 天

### 5. 🎯 战略上下文
**核心结论**：ISR/STA 是 GRPO 的诊断工具，不是优化目标。当 ISR 被加入 reward（任何 β），训练最终都 Goodhart collapse（1000步 genuine→0%），但 collapse 路径因 reward 类型不同（exec-only→H1, ISR→H7, ISR β=0.3→H8, random→tautology）。SFT 免疫（genuine=92.2%），证明 Goodhart collapse 是 RL(GRPO) 特有。

**决策链关键节点**：D057（Goodhart/ISR 无结构优势确认）→ D059（Prolog 跨逻辑泛化）→ D076（ISR β=0.3 数据纠正）→ D079（SFT 对照 PASS）→ D080（磁盘满事故）→ D081/D082（Taxonomy 8 modes）

**易错点**：
- 不要把 exec-only s42 的 1000步数据（已完成，PR=0.96, ISR=0.003）与 s43/s44 的 500步数据混用——s43/s44 1000步正在跑
- H8（conjunction collapse）仅在 ISR β=0.3 1000步出现，不要推广到其他条件
- Random 两个 seed 的 ISR 差异（0.333 vs 0.689）来自 tautological 结构差异，不是推理质量差异，论文中不要过度解读
- 3 个 PREPARING 实验是补数据（原始 checkpoint/eval 丢失），不是新实验。重训参数必须与原实验完全一致
- Worker 容易卡死（memory.md 有记录），分析 Worker 核心产出是 artifact JSON，registry 更新可由 Main Agent 接手


---
