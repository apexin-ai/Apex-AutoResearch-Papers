# reviewer / loop_2.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`14992a35359ddbebb9f2.json`](../../sessions/14/14992a35359ddbebb9f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T02:04:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977，6× RTX 4090D（cuda:0-5），全部分配给本项目，无越界风险
- AutoDL 实例 HuggingFace 连接不稳定——evaluate.py 依赖 HF dataset cache，必须确认 cache 存在再跑 eval，否则超时失败
- evaluate.py 旧版缺 `output_dir.mkdir()`，当前版本（09:38 修改）已修复，但已运行的 s42 eval 用的是旧版代码崩溃了
- Stan 模型（exp005/006）在 /tmp 下生成 ~1GB CSV，需设 TMPDIR 到非 tmpfs 路径或提前清理
- exp_001_eval_05B_d000_s42 的 per-item correctness matrix 丢失（JSON 未保存），aggregate 分数可从日志恢复但 IRT 模型需要 item-level data，必须重跑

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（conda base 环境，不用 venv）
- HF cache：/root/autodl-tmp/.hf_cache
- 模型 checkpoints：/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{0.5B,1.5B,3B}_d{000,005,100}_s{42,123}/lora_adapter
- Eval 结果：/root/autodl-tmp/exp001/eval_results/
- SFT 数据：/root/autodl-tmp/exp001/sft_data/sft_dosage_{0,5,100}.jsonl
- exp002 代码已同步到远程：/root/contamcal-irt-calibration/exp002/（信号计算脚本）
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/
- 无 wandb 配置（本项目不用 wandb）

### 3. 📊 当前状态
**刚完成的审查：**
- exp_001_eval_05B_d000_s123 独立验证通过（MMLU 41.82%, GSM8K 34.04%, ARC 39.76%, HumanEval 10.37%）
- exp_001_eval_05B_d000_s42 crash 诊断完毕（FileNotFoundError），从日志提取了全部 4 项分数（MMLU 40.49%, GSM8K 36.47%, ARC 37.80%, HumanEval 10.98%）
- 跨 seed 方差分析完成：Δ 1-2.5pp，合理
- exp005 γ bias 审查完成：N=50 时 +23.6% bias，ME model 更差（+59.2%），已报告 Director

**Registry RUNNING：**
- exp_001_sft_d100_15B_v2（GPU 0，step ~360/4159，~3h 剩余）— 1.5B 100% 剂量训练
- exp_001_eval_3B_d000_s42（GPU 1）— 3B baseline s42 eval
- exp_001_eval_05B_d100（GPU 2）— 0.5B d100 污染模型 eval
- exp_001_eval_3B_d000_s123（GPU 3）— 3B baseline s123 eval
- exp_001_eval_15B_d000_s42_v2（GPU 4）— 1.5B baseline s42 eval
- exp_001_eval_15B_d000_s123（GPU 5）— 1.5B baseline s123 eval
- exp_004_sim_sweep（local-cpu，Stan 模拟扫参）

**Registry PREPARING：**
- exp_001_eval_05B_d005 — 0.5B 5% 剂量 eval（等 GPU 空闲）
- exp_001_sft_d005_15B — 1.5B 5% 剂量 SFT（等 GPU 空闲）
- exp_001_eval_3B_d000_s42_v3, exp_001_sft_d005_05B_r3 — 备选

### 4. 📋 待办（条件触发式）
- exp_001_eval_05B_d100 完成 → 对比 d000 baseline，计算 contamination-induced score inflation（0.5B 上的剂量响应第一个数据点）
- exp_001_eval_3B_d000_s42/s123 完成 → 独立验证 3B baseline 分数 + 跨 seed 方差
- exp_001_sft_d100_15B_v2 完成 → 检查 training loss/accuracy，对比 0.5B d100 的 training metrics
- exp_001_eval_05B_d000_s42 registry 更新（metrics 或 re-run） → 确认 per-item matrix 可用于 IRT
- GPU 空闲 → s42 eval 必须重跑（per-item matrix 缺失是硬阻塞）
- exp_001_eval_15B 完成 → 1.5B baseline 三个 scale 的 baseline 齐全，可开始 dose-response 比较

### 5. 🎯 战略上下文
- **核心方法**：4PL+γ IRT 模型，用 contamination exposure 信号校准 benchmark 分数。γ 是污染对正确率的因果效应参数。
- **γ bias 是核心风险**：模拟实验显示 σ_e=0.1 时 γ 有 +23.6%（N=50）到 +57.5%（N=30）的正偏差。ME model 不仅没改善反而更差。论文必须用 interval estimates + sensitivity analysis 来 frame，不能用 point estimate 做强 claim。σ_e=0.3 时 bias 几乎消失（-8.4%）。
- **易错判断**：不要因为 HumanEval pass@1 只有 10% 就认为评估有 bug——0.5B base model + 非代码 SFT 确实这么低。但 164 items × 90% 错误 = IRT 拟合时有效信息极少，可能需要讨论是否纳入 HumanEval。
- **evaluate.py 的 output_dir bug 是系统性的**：虽然代码已修复，但之前跑的 eval 可能有同样问题。检查每个 eval 的结果目录是否有 eval_results.json + correctness_matrix.json。
- **EMNLP 2026 ARR May 25 截稿**：还剩 11 天。Phase 3 SFT（12 runs）+ Phase 4 eval + IRT fitting 是关键路径。当前 0.5B 的 d000/d100 SFT 完成，d005 完成；1.5B/3B 的 d000 SFT 完成，d100 15B 在跑。还需要 {d005,d025,d050}×{0.5B,1.5B,3B} + d100×3B 的 SFT 和全部 eval。


---
