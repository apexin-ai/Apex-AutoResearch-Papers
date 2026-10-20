# agent / loop_1.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`3a45ce66e5d4fd31fff6.json`](../../sessions/3a/3a45ce66e5d4fd31fff6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-16T15:36:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 (exp_001, 410M) + cuda:1 (exp_002, 1B)，不可交叉占用
- checkpoints 必须写 /root/autodl-tmp/（根分区 30GB，84% 占用，再写 checkpoint 会满）
- checkpoints → /root/autodl-tmp/spectral_collapse_ews/checkpoints_410m/ (symlink)
- checkpoints_1b → /root/autodl-tmp/spectral_collapse_ews/checkpoints_1b/ (symlink)
- Go/no-go 未通过前禁止在论文中断言正向结果（Gen 0-2 eff_rank 仍在上升）
- ECE 未接入 pipeline，论文中只能作为 "planned extension / future work"

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，SSH account: root
- 工作目录：/root/spectral_collapse_ews/
- Python：source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
- 模型缓存：/root/autodl-tmp/spectral_collapse_ews/models/
- 数据：/root/spectral_collapse_ews/data/（pile-uncopyrighted, 50K train + 5K eval + 1K spectral）
- 活跃进程：
  - exp_001: PID 7396, cuda:0, Pythia 410M Phase 0 (已跑 ~6h+)
  - exp_002: PID 25232, cuda:1, Pythia 1B Phase 0 (刚重启)
- Cron: exp_001 (PID 7396, 120s) + exp_002 (PID 25232, 120s)
- 无 W&B（本地 JSON 记录）

### 3. 📊 当前状态
刚完成论文跨章节一致性修复（intro/method/conclusion/abstract 贡献结构对齐）。所有论文章节框架就绪，等实验结果填 [TBD]。

Registry:
- exp_001 RUNNING: Pythia 410M Phase 0, 100% synthetic, 10 gen, cuda:0 — 核心 go/no-go 实验
- exp_002 RUNNING: Pythia 1B Phase 0, 同上, cuda:1 — scale transfer pilot

等待中：
- exp_001 cron 完成回调 → 跑 analyze_phase0.py → 报 Go/No-go
- exp_002 cron 完成回调 → 分析 1B 结果
- 无待处理的 Worker/Director 决策

### 4. 📋 待办（条件触发式）
- exp_001 完成 → `python analyze_phase0.py --results-path results/phase0_results.json` → 3 条件判断 → 汇报 Director Go/No-go
- Go/No-go PASS → 校准 τ/k → 立即铺 Phase 1（3 seeds × 4 conditions，需 Director 审批 GPU 分配）
- Go/No-go FAIL（eff_rank 不单调下降）→ 产出 Framing 调整提案（red-section skill），不默默跑下一实验
- exp_002 完成 → 分析 1B collapse 动态，与 410M 对比 scale transfer
- 两实验都完成后 → HellaSwag batch eval（之前被 kill 了）+ 补 Gen 0/1 log-det 到结果 JSON
- Phase 1 开跑后 → 论文填充 [TBD] 占位符

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 ARR May 25（DDL 9 天，从 5/16 算起）
- D004: decline rate baseline 从 Gen 1 开始（Gen 0→1 是 pretraining shift，不算 collapse）
- **关键风险**：Gen 0-2 eff_rank 和 log-det 都在上升（417→492→496），波动容忍已用完。Gen 3 是生死线——如果继续升则 condition 1 失败。但增速急剧衰减（+74 → +4.7），大概率即将拐点。
- ppl/distinct4/train_loss 已支持 degradation，只有 spectral 信号滞后
- 论文已留条件性语言，不预设正向结果
- 易错点：不要在 Phase 0 完成前断言 collapse 已确认；不要把 Gen 0→1 的增加算作 collapse 信号失败（这是 D004 已知的 pretraining shift）


---
