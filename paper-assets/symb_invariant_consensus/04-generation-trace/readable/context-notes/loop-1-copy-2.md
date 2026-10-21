# agent / loop_1.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`a30501520c29dd282fd8.json`](../../sessions/a3/a30501520c29dd282fd8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T15:44:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 `cuda:0` @ westd-32608（gpu_ids 白名单只有这一张）
- vLLM max_model_len=16384（32768 会 crash engine core）
- 模型固定 QwQ-32B，不可替换（D002/D003 明确）
- submit_training_job 命令必须 `bash -c "..."` 包裹（tmux 用 sh 不支持 source/conda activate）
- AIME v2 实验如果还在跑（PID 121139），不要 kill——Director 明确说继续收集数据

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608，账号 root，工作目录 `/root/symb_invariant_consensus/`
- Python：conda base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/`（ModelScope 嵌套路径）
- vLLM：port 8000, bfloat16, max_model_len=16384, gpu_memory_utilization=0.90
- 数据集：`data/math500_subset.json`(50题), `data/aime2024_subset.json`(30题), `data/proofwriter_subset.json`(10题)
- 活跃进程：sica_aime30_v2 (PID 121139, tmux=sica_aime30_v2)——但可能已完成或 crash，有 Worker 正在检查
- Cron：`sica_aime30_v2` @5min 监控已注册
- 准备好的脚本：`run_math50_fixed.sh`, `run_proofwriter.sh`

### 3. 📊 当前状态
刚派出 Worker `infra:aime-progress-check` 检查 AIME v2 进度（Director 指令），**尚未收到回调**。这是最关键的待处理事项。

Registry 状态：
- `sica_aime30_v2` — RUNNING（可能已结束，等 Worker 确认）
- `sica_aime30_t07` — DONE(killed)：v1 卡死 6.4h
- `mvp_math50_t07` — DONE(killed)：25-30h 不可接受
- `sica_temp_diversity` — DONE(negative)：QwQ-32B 零答案分歧
- `sica_smoke_5q` — DONE(success)：pipeline 功能验证

代码已累计修复 7 个 bug（全在服务器上生效，但 AIME v2 跑的是修复前的旧代码）：
1. regex `\\\\s` → `\\s`
2. response_format=json_object
3. extraction max_tokens 4096→512→1024
4. max_workers 4→12→6（加 Semaphore）
5. HTTP timeout=120s + future timeout=180s
6. Z3 is_bool 类型检查
7. pipeline fallback 补全 constraints_stats/maxsat_stats + compute_summary 安全访问

### 4. 📋 待办
- Worker `aime-progress-check` 回调 → 三种分支：
  - **还在跑** → 汇报进度（题数、耗时、矛盾数），继续等
  - **正常完成** → 分析结果，crash 题数 ≤5 用修复代码补跑，>5 整体重跑（注册 sica_aime30_v3）
  - **crash 了** → 报错误，用修复后代码重跑全量 AIME
- AIME 有信号（≥3 题矛盾 + SICA > SC）→ 立即跑 `run_math50_fixed.sh`（MATH 50 再跑）
- AIME 无信号 → 准备 FAIL 路径讨论，向 Director 汇报
- MATH 50 完成后 → 顺序跑 `run_proofwriter.sh`（ProofWriter 10 题 sanity check）
- **May 19 UTC checkpoint**：MVP 未 pass → 放弃 EMNLP May 25，切 AAAI 2027

### 5. 🎯 战略上下文
- 核心假设：SICA 跨路径 MAX-SAT 约束共识能检测统计方法遗漏的矛盾 → 提升准确率
- **关键发现**：QwQ-32B（reasoning model）在 MATH 上近零答案分歧，SICA 退化为 SC。但 AIME smoke test（1题）显示 4 个约束被 MaxSAT 排除 → **AIME 是最后的 sweet spot 机会**
- 决策链：D001(MVP 方案) → D002(拒绝 CRD 回归 SICA) → D003(三档判定标准) → D004(继续 MVP) → D005(双管齐下) → D006(Kill MVP 修 bug AIME 优先)
- **易错点**：
  - 两个 Worker 同时编辑同一文件会冲突——修复后必须派 Worker 验证最终代码状态
  - extraction max_tokens 需要根据数据集调整（MATH 512 够，AIME 需要 1024）
  - `run_full_mvp.py --seed` 参数已添加但 AIME v2 没用上（旧代码），后续实验必须加 `--seed 42`
  - Narrative 预判：如果 AIME 有信号 → "SICA 价值随问题难度递增，在 frontier model 不确定区间最有效"


---
