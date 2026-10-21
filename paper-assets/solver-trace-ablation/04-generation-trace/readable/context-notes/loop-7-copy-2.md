# agent / loop_7.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`18e41bb8ba917000e69f.json`](../../sessions/18/18e41bb8ba917000e69f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-14T17:31:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 只能用 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`，gpu_ids=[cuda:0, cuda:1]。历史上有违规用其他 GPU 被 CRITICAL 的先例
- **submit_training_job 命令格式**: 必须 `bash -c "export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ..."`。不能假设 .venv 存在，这是 conda 环境（aml-train 镜像）
- **kill_job 后必须 SSH 验证子进程已清理**——kill_job 只杀 tmux wrapper，Python 子进程可能残留
- **磁盘约束 C003**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`。系统盘只有 30GB
- **数据约束 C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`
- **ISR raw 对比不可信**: 必须 premise-count-matched（D051 定论），论文中不可标"no hacking"只能标"lowest hacking rate"（D044）
- **plan013 vs plan017 公式结构不同**，不可简化为"additive vs convex"对照（D027）

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，2× RTX PRO 6000 Blackwell 96GB
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CUDA**: 12.8, PyTorch 2.10.0+cu128
- **模型**: Qwen3-4B（7.6GB, ModelScope 下载）
- **Solvers**: Prover9 (LADR 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
- **数据盘**: `/root/autodl-tmp/` 250GB (~131G free)
- **活跃进程**:
  - `plan006-prolog-sta-s44`: PID 908945, cuda:0, cron 监控中
  - `plan006-prolog-sta-s43`: PID 901135, cuda:1, cron 监控中
- **活跃 Worker**: `worker_knowledge_table-data-json_20260514T172336` (running, 可能已完成待回调)

### 3. 📊 当前状态
**Registry**: 50 实验总计——48 DONE + 2 RUNNING。成功 11 / 负向 17 / 失败 18 / killed 2。

**RUNNING**:
- `plan006-prolog-sta-s44` (cuda:0): Prolog exec+STA GRPO seed=44，Claim 3 第三 seed
- `plan006-prolog-sta-s43` (cuda:1): Prolog exec+STA GRPO seed=43，与 exec-only s43 对照

这两个是 **Claim 3（跨逻辑泛化）的最后两个数据点**。Prolog STA s42 已完成（negative: 100% H7, PR=50%）。两卡满载，cron reconcile 确认进程存活。

**等待中**:
- 两个 cron 回调（plan006-prolog-sta-s43/s44 完成时触发）
- Worker `worker_knowledge_table-data-json_20260514T172336` 状态待确认

**DDL**: 2026-05-25（剩 11 天），时间充裕（剩余 GPU 需求 ~6h）

### 4. 📋 待办（条件触发式）
- **plan006-prolog-sta-s43 cron 回调到达** → spawn worker 跑 eval_sta.py（Prolog STA s43 eval）→ 更新 registry metrics → 等 s44
- **plan006-prolog-sta-s44 cron 回调到达** → spawn worker 跑 eval_sta.py（Prolog STA s44 eval）→ 更新 registry metrics
- **s43 + s44 eval 全部完成** → 汇总 3-seed Prolog STA 统计（mean±std）→ 与 Prolog exec-only 3-seed 对照 → 判断 Claim 3 结论:
  - 若 H7 rate 一致高（如 s42 的 100%）→ Claim 3 confirmed: Prolog Goodhart 比 FOL 更极端，跨 logic type 泛化
  - 若 s43/s44 与 s42 差异大 → 需要讨论 seed 不稳定性
- **3-seed 全部出齐** → Table 1 + Table 2 定稿 → paper_framing.md 更新 → 向 Director 汇报完整证据链 → 提交 Paper Agent 启动写作
- **Worker table-data-json 回调** → 检查产出，整合到项目知识

### 5. 🎯 战略上下文
**项目核心结论（决策链）**:
- **Claim 1 (STA 诊断能力) ✅**: ISR 崩塌轨迹 0.64→0.13→0.003; 3-seed exec-only 展现多模式退化（冗余 embedding / length explosion / tautological collapse）; SFT 零 hacking 对照
- **Claim 2 (Goodhart / ISR 无结构优势) ✅** (D057 closed): H7=0% 全 3 seed random 一致; Random PR 0.85±0.06 > ISR 0.77±0.14; premise-count-matched ISR 1.06x 无差异; β 剂量效应（β=0.1 sweet spot vs β=0.3 collapse）
- **Claim 3 (跨逻辑泛化) ⏳**: exec-only 3-seed done; STA s42 done (100% H7 极端 Goodhart); s43/s44 RUNNING

**最容易判断错的事**:
1. **不要把 Prolog STA s42 的 100% H7 当 failure**——这恰恰是最强的跨 logic type Goodhart 证据（Prolog 比 FOL 更极端）
2. **Claim 2 已从"纯 negative"转为"Goodhart 双面性"叙事** (D049→D051→D057)——ISR-as-reward 完全失败，但作为 diagnostic tool 有价值。论文 framing 是"诊断工具 + Goodhart 案例研究"
3. **exec-only s42 不是 healthy seed**——87.1% conclusion embedding，所有 exec-only seeds 都有 87-100% embedding。不要在论文中称任何 exec-only seed 为"healthy"
4. **ISR raw 数值对比陷阱**: D051 证明 2.4x ISR 优势完全是 premise-count artifact。任何 ISR 对比必须 premise-count-matched
5. **Prolog 训练 ~100 步即饱和**（s42 经验），s43/s44 可能也很快完成——cron 回调可能比预期来得早


---
