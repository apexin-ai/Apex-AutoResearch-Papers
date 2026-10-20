# reviewer / loop_3.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`7e1495da7d4abbb1cb02.json`](../../sessions/7e/7e1495da7d4abbb1cb02.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T21:18:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（autodl-rtx6000pro 单卡，vLLM + pipeline 共享）
- vLLM serving PID 19902 **不能 kill**——pipeline 依赖 localhost:8000 推理服务
- Pipeline 输出分裂为两个文件：`mvp_v4_full.json`（前 126 samples，JSON array）+ `mvp_v4_full.jsonl`（125 旧 + 新 samples，JSONL）。**JSONL 缺第 126 号 sample**（folio_validation_125 或类似 ID），最终评估必须合并两个文件
- `repair.py` prompt 已修复（`{repr_type}` 替代硬编码 "Python script"），但 **当前运行的 pipeline PID 47964 使用旧代码**（Python 模块缓存）。新 prompt 仅在 restart 或 `repair_only.py` 中生效

### 2. 🖥️ 基础设施快照
- 服务器：**autodl-rtx6000pro**（root），工作目录 `/root/autodl-tmp/crdd`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型：`/root/autodl-tmp/models/Qwen3-32B-AWQ`（vLLM awq_marlin，PID 19902/19633，GPU 0，localhost:8000）
- 数据：FOLIO validation set 204 samples，内置 data_loader
- 活跃进程：**pipeline PID 47964**（tmux=mvp_pipeline_004，CUDA_VISIBLE_DEVICES=0），第 4 次 restart，1h+ 稳定运行
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/`

### 3. 📊 当前状态
Pipeline 第 4 次 restart 稳定运行中。JSONL **143/204**（02:59 北京时间处理 #145），速率 ~2.6min/sample，**ETA ~05:35 北京时间**。内存稳定 107MB。

Registry: **mvp_pipeline_004** status=ANALYZING（实为 RUNNING），metrics 在 126 samples 快照：
- All-mode: **5/5 PASS**（C1=36.4%, C2=88.4%, C3=3 types, C4=+7.3pp, C5=80.0%）
- Excl-Unknown: **4/5**（C4=+0.0pp FAIL）

等待：pipeline 完成 204 samples → 合并数据 → 运行 `repair_only.py`（用修复后 prompt 重跑 repair）→ 最终 C1-C5 评估

### 4. 📋 待办
- Pipeline 完成（JSONL=204 行 or pipeline.log 出现 "pipeline complete"）→ 合并 JSON+JSONL → `evaluate_mvp.py` 全量评估 → 更新 registry
- 全量评估后 → 运行 `python src/repair_only.py --input results/mvp_v4_full.json --input-jsonl results/mvp_v4_full.jsonl --output results/mvp_v4_repair_fixed.json` → 用修复后 prompt 重跑 repair → 重新评估 C4
- C4 repair-fixed 结果出来 → 若 all-mode ≥5pp → MVP 正式 PASS，进入 post-MVP（ProofWriter 第二数据集 + ablation）；若 <5pp → 需重新审视 targeted repair 方法论
- Pipeline 再次崩溃 → 检查 JSONL 行数，直接重启（内存修复已部署），不需要额外 fix

### 5. 🎯 战略上下文
- **核心发现**：9:1 不对称性稳定（FOL 几乎总是对的，Code 几乎总是错的）。论文不能 claim "bidirectional diagnostic"，需 honest framing
- **C4 是最大风险**：从 +21.9pp（83 samples）持续下降到 +7.3pp（126 samples）。根因：FOL targeted repair 只有 50% 成功率（prompt bug，已修），但修复不影响已处理的 samples。`repair_only.py` 是唯一救场方案
- **C4 两个口径**：evaluate_mvp.py=+7.3pp（含 single_error，官方 gate 用），c4_analysis=+12.5pp（仅 disagree，论文叙事用）。7 个 single_error samples 的 blind=100% 拉低了 evaluate_mvp 的 targeted advantage
- **C5 已修复**：之前 100% 是循环论证 bug（`disagreement.error_side` 与 actual 同源），修复后用 `stability.predicted_error_side`（ground-truth-free），80% at 126 samples
- **ROADMAP 和 report.md 严重过时**（仍显示 80/204、C5=45.8%），需 Director 指派更新
- **易错点**：不要把 JSONL 的行数当总进度——它缺第 126 号 sample（JSON 有但 JSONL 转换时时序差异丢了）。最终评估必须 merge 两个文件


---
