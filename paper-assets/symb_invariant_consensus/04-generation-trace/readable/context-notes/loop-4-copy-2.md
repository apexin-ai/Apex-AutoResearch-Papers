# agent / loop_4.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`e82f001058decc86a0fc.json`](../../sessions/e8/e82f001058decc86a0fc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-16T01:19:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-32608:cuda:0（gpu_ids 白名单只有这一张）
- QwQ-32B 模型不可替换（D003 明确锁定）
- May 19 UTC 前 MVP 未 pass → 放弃 EMNLP，切 AAAI 2027
- ProofWriter 是 sanity check，不影响 PASS/FAIL 判定；MATH-500 50 题才是主实验
- SICA 在 AIME 数学域已确认 SICA≡SC（结构性 0pp gap），不要再跑数学域实验期待不同结果

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608，工作目录 `/root/symb_invariant_consensus/`
- Python：conda base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：QwQ-32B FP16，通过 vLLM serving（localhost:8000），单卡 98GB RTX PRO 6000 Blackwell
- 数据：`/root/symb_invariant_consensus/data/` 下有 aime2024_subset.json、math500_subset.json、proofwriter_subset.json
- CRD 遗留资产（可复用 vLLM infra、Z3、FOLIO 数据加载器）：`/root/autodl-tmp/crdd/`
- 结果目录：`/root/symb_invariant_consensus/results/`
- 日志目录：`/root/runs/symb_invariant_consensus/`
- 活跃进程：proofwriter30 已完成（PID 153924 已退出），vLLM 可能仍在 serving（需确认）

### 3. 📊 当前状态
sica_proofwriter30 刚正常退出，cron 已转 ANALYZING。我派了两个 Worker：
1. `worker_analysis_sica_proofwriter30_20260515T221704`（running）— SSH 读日志+结果文件，分析指标，更新 registry
2. `worker_code_sica_folio30_prep_20260515T221825`（running）— 准备 FOLIO 实验代码和数据，基于 eval_proofwriter.py 写 eval_folio.py，dry-run 验证

Registry 状态：
- sica_proofwriter30: ANALYZING（等 Worker 1 分析完设 conclusion + metrics）
- sica_folio30: PREPARING（等 Worker 2 准备代码）
- 其余全部 DONE（4 killed、1 negative、2 success、1 failed）

**尚未向 Director 汇报** — 等 Worker 1 返回分析结果后再汇报。

### 4. 📋 待办
- Worker 1 (analysis) 回调 → 读 conclusion：
  - success → 更新 report.md + 向 Director 汇报（附 ProofWriter sanity check 结果 + 与 AIME 0pp 对比 + 文献联动） + 反思实验计划
  - negative → 按 red-section 产 Framing 提案 → 汇报 Director
- Worker 2 (folio prep) 回调 → 如果代码就绪 + proofwriter30 分析完成 → 提交 sica_folio30 走审批流程（PENDING → Director 批准 → ALLOCATED → submit_on_allocated）
- GPU cuda:0 当前空闲 → Worker 2 完成后应立即铺 folio30 实验上去
- 如果 proofwriter30 和 folio30 都显示逻辑域 multi-candidate rate 仍为 0% → SICA 方法在 QwQ-32B 上结构性失效，需向 Director 提 pivot 建议

### 5. 🎯 战略上下文
- 核心发现：QwQ-32B 太确定性，trace 间答案分歧为零（multi-candidate rate = 0%），导致 SICA≡SC。这是结构性问题，不是 bug。
- 决策链：D002（拒绝 CRD pivot）→ D003（MVP 三档标准）→ D005-D009（AIME 系列 debug）→ D010（确认 0pp 结构性）→ D011（预判 MATH-50 也会单候选）
- ProofWriter/FOLIO 是最后的希望——逻辑域 True/False/Unknown 三分类可能天然产生更多 trace 分歧。如果逻辑域也是 0% multi-candidate，SICA 在 QwQ-32B 上就彻底死了。
- 易错点：不要把 ProofWriter sanity check 结果当作 MVP PASS/FAIL 依据——MVP 判定只看 MATH-500 50 题。但 ProofWriter/FOLIO 的 multi-candidate rate 是判断 SICA 方法本身是否可行的关键信号。
- May 19 checkpoint 还剩 ~3 天，MATH-500 50 题主实验还没跑。时间极紧。


---
