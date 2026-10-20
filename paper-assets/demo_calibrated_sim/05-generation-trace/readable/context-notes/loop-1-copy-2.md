# reviewer / loop_1.md

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`91535e7e31793db2cf3a.json`](../../sessions/91/91535e7e31793db2cf3a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T14:48:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- gpu_ids=[2,3] 严格执行。本 session 已出过一次 GPU 1 越界（mvp-003 被 CRITICAL kill）
- 服务器代码路径已统一到 `/root/democalib/`（根目录）。旧 `/root/democalib/code/` 已删除，**不要重建**
- Worker 代码部署后必须独立 `ssh_read_only` + `grep` 验证关键函数存在。**不信任 Worker 自报**——本 session 出现过两次 Worker 声称部署成功但实际未部署的情况
- vLLM port 8000 = mvp 实验用，port 8001 = 语料生成用。两个实例分别在 GPU 2 和 GPU 3

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977(root)，工作目录 `/root/democalib/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：Qwen/Qwen2.5-7B-Instruct（vLLM 在线服务，max_model_len=32768）
- τ-Bench：`/root/tau-bench/`
- 实验结果：`/root/democalib/results/`
- 语料输出：`/root/democalib/synthetic_corpus/`
- 活跃进程（截至 handoff）：
  - GPU 2: vLLM port 8000（mvp-004 实验，PID 110596）
  - GPU 3: vLLM port 8001（语料生成，PID 141319/worker 141024）
  - mvp-004 实验：PID 111195，日志 `full_experiment_v4.log`
  - AAVE 语料生成：PID 142096，日志 `aave_corpus_gen.log`

### 3. 📊 当前状态
**两个进程并行运行中：**
1. **mvp-004**（registry RUNNING）：Phase 1+2 全量 20-task 实验，首次同时具备所有修复（检测器精度修复 + H-gate 重构 + context overflow 过滤 + max_model_len=32768）。v4 日志在增长。
2. **AAVE 语料生成**（GPU 3）：20 tasks × 5 trials，dialect=aave，target question=0.10 / politeness=0.20。含 postprocess_traces 后处理。产出供后续 DPO 训练。

**DPO 训练 dry-run 已通过**（GPU 3，QLoRA 4-bit，已释放）。正式训练等语料完成后启动。

Registry: mvp-001 failed, mvp-002 killed, mvp-003 killed (L1), mvp-004 RUNNING。

### 4. 📋 待办
- mvp-004 完成 → 检查 full_experiment_v4.log 中 task 结果 + H-gate 评估。**重点验证**：(a) H1 politeness ≥30% 在 n=20 下是否成立（之前仅 n=2 确认），(b) context overflow 过滤是否生效（task 2 之前 crash），(c) H2 politeness gap reduction ≥30%
- AAVE 语料生成完成 → 检查 trace 质量 + 后处理前后行为率对比 + slot 一致性。然后 build_dpo_pairs.py 构建训练数据 → train_dpo.py 在 GPU 3 正式训练（QLoRA 4-bit）
- DPO 训练完成 → 用 DPO 模型替换 vLLM base model 重跑 H-gate 评估
- 任何新 Worker 部署代码 → 独立 grep 验证（系统性缺陷，必须每次检查）

### 5. 🎯 战略上下文
- **D001**: MVP 三阶段验证。**D002**: H-gate 重构——politeness 为主维度，question rate 降为 secondary。原因：QuestionDetector 修复后 baseline question_rate=11.4%（接近 AAVE 目标 10%），question gap 是测量假象。Politeness gap 真实存在（45% vs 20%）。
- **关键方法论风险**：修正后的检测器显示 LLM question_rate (11.4%) < Seshadri 人类基线 (18.8%)。论文需要精确表述为"DemoCalib 旧检测器的定义差异导致 gap 放大"，而非"Seshadri 的测量有误"。
- **易错点**：(1) bf16→QLoRA 是硬件约束下的妥协，如果 DPO 效果不显著需 ablation 排除量化噪声。(2) H1 "已确认 PASS" 仅基于 n=2，需 mvp-004 全量确认。(3) 语料生成的 postprocess pipeline 用 LLM rewrite 强制对齐行为率——如果改写损坏 slot 一致性，DPO 训练数据质量会有问题。
- **EMNLP 2026 ARR deadline 2026-05-25**，剩余 13 天。GPU 预算：全量 research ~360h，2 卡 wall-clock ~8-9 天。时间紧但算力上可行。


---
