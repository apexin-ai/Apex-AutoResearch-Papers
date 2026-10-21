# reviewer / loop_12.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`08fd4a186c5c6e756f39.json`](../../sessions/08/08fd4a186c5c6e756f39.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-17T17:05:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目使用 gpu-6000pro-2 的 cuda:0 和 cuda:1，两张卡均属本项目
- 新增云服务器 westd-48862（2× RTX PRO 6000 Blackwell 96GB）用于 plan_024/025，cuda:0 和 cuda:1 均可用
- qwen25_14b 模型下载反复失败（SSL/TLS），shards 1-3 完整，shard 4 部分，5-8 缺失。当前用 `hf download` 重试中
- prompted_gen_gpt2xl_001 registry 标记 "failed" 是 server restart desync 导致，实际结果有效（69.5% 4-class acc），需修正
- plan_018 detector baselines worker 报 "failed" 但实际 GPU 进程已正常完成（summary_v2.json 存在），同属 registry desync

### 2. 🖥️ 基础设施快照
- **主服务器**: gpu-6000pro-2, 工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- **云服务器**: westd-48862, 同路径结构, Python 3.10, PyTorch 2.11.0+cu128
- **Python**: `/root/miniconda3/bin/python3.12`（主服务器）
- **模型路径**: `/root/autodl-tmp/models/` (pythia-1.4b, gpt2-xl, olmo-1b, qwen25_14b[不完整], qwen2.5-1.5b-instruct)
- **HF Cache**: `/root/autodl-tmp/.hf_cache`, mirror: `hf-mirror.com`
- **活跃进程 (gpu-6000pro-2)**:
  - wild_data_features_001: PID 788803, tmux `wild_data_features_001`, cuda:0 (c4+fineweb 特征提取)
  - qwen25-1p5b-instruct-001: PID 795692, tmux `qwen25-1p5b-instruct-001`, cuda:1 (d0 生成中)
  - qwen25_14b download: PID 789171 (hf download shards 5-8)
- **活跃进程 (westd-48862)**:
  - downstream_benchmark_001 (plan_024): cuda:0, LoRA fine-tuning Pythia-410M
  - learned_estimator_001 (plan_025): cuda:1, 9 runs (3 methods × 3 holdouts)

### 3. 📊 当前状态
**刚完成的审查：**
- plan_023 theory draft: 发现 critical BibTeX key 错误 + 多项 warning → 已修复（Theorem→Hypothesis, AUC 数值修正, γ→0.75）
- plan_018 detector baselines: 实验完成，RF 78.2% vs 最佳单检测器 Log-Rank 64.0% (-14pp)，narrative 强力支撑
- plan_020 bootstrap CI / plan_022 text length: 数据核实通过
- plan_021 instruct model: cuda:1 运行中 (~4-5h total)
- plan_024/025: 已部署到 westd-48862 云服务器，正在执行

**Registry 需修正**: prompted_gen_gpt2xl_001 (failed→应为 success/negative), bootstrap_ci_table1_001 (PREPARING→DONE), plan_018 detector baselines 需注册

### 4. 📋 待办（条件触发式）
- qwen25-1p5b-instruct-001 完成 → 核实结果 (instruct vs base 对比)，验证 chat template 生成质量
- wild_data_features_001 完成 → 核实 C4/FineWeb depth 分布，检查 FPR 是否与先前 calibration 一致
- qwen25_14b download 成功 → 验证 8 shards 完整性，确认 pipeline 自动启动
- learned_estimator_001 (westd) 完成 → 核实 XGBoost 67.2% claim，验证 cross-model holdout 公平性
- downstream_benchmark_001 (westd) 完成 → 核实 depth-filtered 数据是否真正改善下游任务，这是 plan_024 核心 claim
- 任何新增 citation → 逐条验证 bib key 正确性 + 论文真实性（hallucination 防线）
- plan_023 theory 集成到 main.tex 时 → 重验 BibTeX keys 是否在最终编译中正确解析

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 Main via ARR May 25 cycle (距截稿 ~8 天)
- **核心结论**: 19-feature RF 在 9-cell atlas 上 68.8-85.9% 4-class acc, EDD=4, 跨模型 transfer 66.4%
- **D038 "Strong Accept 冲刺"** 正在执行 plan_014(14B)/016(prompted gen✓)/018(detectors✓)/021(instruct)/023(theory✓)/024(downstream)/025(learned estimator)
- **易错点**:
  - Registry 有多处 desync（server restart 遗留），不要信 registry status=failed 的实验结论，必须 ssh 看 summary.json
  - Theory section 的 AUC 数值是 3-model 均值（0.922/0.802/0.712/0.653），任何改动需重新核对来源
  - Fast-DetectGPT 在 pythia_nucleus cell 有数值溢出（d1 mean=28515），论文引用需 caveat
  - prompted_gen 的 -13.78pp delta 是 relative to BOS-seeded 83.3%，不是 relative to atlas RF；科学结论是"生态场景下 signal 退化但仍可检测"
  - qwen25_14b 下载已失败 2 次（aria2 SSL 问题），第 3 次用 `hf download` 重试中——如果再失败，建议放弃 14B 或换源


---
