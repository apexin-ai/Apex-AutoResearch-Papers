# agent / loop_9.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`e7a0fdc5eb6ad15e9fbc.json`](../../sessions/e7/e7a0fdc5eb6ad15e9fbc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-16T01:17:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 autodl-5090 的 cuda:0/1/2/3（config gpu_ids 白名单）。其他 GPU 必须 push back Director
- **7-gen vs 6-gen 数字禁止直接对比**（D017）：7-gen binary F1=0.768 不可与 6-gen binary F1=0.723 做 apple-to-apple 比较——训练集组成变化
- **Instruct 方向反转是长度伪影**（D019 已验证）：不可 claim 方向反转。Discussion 只能用 "method boundary" 叙事
- Primary metric 是 **binary LOGO F1=0.723**（gen-1 vs gen-2+，排除 gen-0 shared-seed leakage），3-class F1=0.789 仅作 supplementary
- submit_training_job 中 `--device` 始终 `cuda:0`（框架注入 CUDA_VISIBLE_DEVICES 做映射）
- EMNLP 2026 ARR **DDL: 2026-05-25**，9 天

### 2. 🖥️ 基础设施快照
- 服务器：**autodl-5090**，工作目录 `/root/gen-depth-fingerprint`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型缓存：`/root/autodl-tmp/models/`（Qwen3-0.6B-Base 等已下载）
- 数据：`/root/gen-depth-fingerprint/data/`（wiki_seed_1000.jsonl + 各 generator 输出）
- 活跃进程：
  - plan-006-confound-fix: PID 256127, cuda:1, log `/tmp/plan006_confound_fix.log`（paraphrastic matched-param 生成）
  - plan-012-qwen06b-v2: PID 257903, cuda:2（QLoRA Qwen3-0.6B seed=123 r=32）
- 活跃 Cron：监控上述两个实验
- 活跃 Worker：`worker_diagnose_plan-012-qwen06b`（诊断 v1 失败原因）、`worker_verify_bib-years-m7`（Rd2-M7 bib 年份验证）
- 空闲 GPU：cuda:0, cuda:3（分配了但没跑 = 失职状态）

### 3. 📊 当前状态
**刚做完**：plan-012-pythia410m success（Pythia-410M QLoRA end-to-end classifier 验证通过）；plan-012-qwen06b v1 failed（进程 5 次死亡无 sentinel），已派 Worker 诊断并启动 v2 重试。

**正在跑**：
- `plan-006-confound-fix` (cuda:1)：paraphrastic chains matched generation params（rp=1.0, max_tokens=256），修复 plan-006-paraphrastic 的 confound
- `plan-012-qwen06b-v2` (cuda:2)：Qwen3-0.6B-Base QLoRA seed=123 r=32，hyperparameter sensitivity check

**等待中**：
- 两个 Worker 回调：diagnose plan-012-qwen06b 失败原因 + bib 年份验证
- plan-006-confound-fix 和 plan-012-qwen06b-v2 的 cron 完成回调
- cuda:0 和 cuda:3 空闲——**下一个"你"应立即找任务填满**

**PREPARING（历史遗留可忽略）**：plan-001-restore / mvp-001-gen-s0~s3 都是早期条目，已被后续实验覆盖。plan-004-prep 是 downstream utility 脚本准备（conclusion=success 但 status 卡 PREPARING），Claim 3 已确定 negative，不再需要跑。

### 4. 📋 待办（条件触发式）
- plan-006-confound-fix cron 回调 → 分析 matched-param paraphrastic 结果，与 plan-006-paraphrastic（unmatched）对比，更新 registry + report.md，汇报 Director
- plan-012-qwen06b-v2 cron 回调 → 与 plan-012-pythia410m 对比 QLoRA 跨模型表现，更新 registry，汇报 Director
- Worker diagnose plan-012-qwen06b 回调 → 确认 v1 失败根因，决定是否需要进一步修复
- Worker bib-years-m7 回调 → 处理 bib 年份验证结果，完成 Rd2-M7
- **cuda:0 / cuda:3 空闲** → 立即从 ROADMAP 近期任务找可跑的实验。候选：(a) abstract + intro 数字更新可派 CPU Worker；(b) related_work CI 残留修复可派 CPU Worker；(c) P1-E ordinal 结论写入论文可派 CPU Worker。**论文写作类任务不占 GPU 但必须开 Worker 做**
- 全部 Rd2 修复完成 → post_to_reviewer 一致性检查 → submit Round 3
- Round 3 通过 → EMNLP ARR 提交材料准备

### 5. 🎯 战略上下文
**核心结论链**：递归 LLM 生成链中 central-tendency/diversity 特征随深度漂移，shape 特征近稳态。7-feature ensemble binary LOGO F1=0.723 优于所有单检测器 baseline。Claim 3 (downstream utility) 为 honest negative：depth fingerprinting 是 diagnostic 工具而非 curative 工具。

**关键决策**：
- D017: primary metric 改为 binary F1（排除 gen-0 leakage）
- D019: 撤回 instruct inverted DDR 叙事（长度伪影）
- D024: 5-class ordinal negative（gen-2/gen-3 不可分），3-class 是天花板

**最容易判断错的事**：
1. **不要把 cuda:0/cuda:3 闲着当正常**——这是失职状态，但目前 GPU 密集型实验不多（主要是论文修改冲刺），所以要主动找可并行的实验或验证性任务
2. **plan-004-prep 看起来像待办但实际不需要跑**——Claim 3 已 negative (D023)，downstream fine-tuning 不再需要
3. **Round 2 修复还剩 abstract/intro 数字更新、related_work CI、P1-E ordinal 写入、M7 bib 验证**——这些全是论文文本修改，应派 CPU Worker 并行处理，不要串行等
4. **EMNLP DDL 5月25日，只剩 9 天**——Round 3 reviewer 审查 + 最终提交材料准备至少需要 2-3 天，留给论文修改的实际时间约 6 天


---
