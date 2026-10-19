# reviewer / loop_2.md

**error diag dpo recovery** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`9dd910f23f5f3870f8fe.json`](../../sessions/9d/9dd910f23f5f3870f8fe.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-12T18:50:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0 和 cuda:1**（cqa1-21977）。三次越界（D007 cuda:2, D008 cuda:3, D019 cuda:3），下次 escalate Manager。
- 所有 GPU 命令必须以 `CUDA_VISIBLE_DEVICES=0` 或 `CUDA_VISIBLE_DEVICES=1` 开头，`--gpu` 参数必须与之一致。禁止 `device_map="auto"`。
- v5_cuda1 (PID 263025) 启动时**未设** CUDA_VISIBLE_DEVICES（已在正确 GPU 上，不要 kill，但后续新进程必须严格执行）。
- v1/v2/v3/v4 数据及其衍生产物（classified_errors.jsonl, correction_span_results.jsonl）**全部作废**，禁止用于 P1 分析或 DPO（D017）。

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977(root)**，工作目录 `/root/autodl-tmp/error_diag_dpo_recovery`
- Python：`/root/miniconda3/bin/python`（conda base, Python 3.12.3）
- 关键版本：PyTorch 2.10.0+cu128, transformers 4.57.6, trl 1.4.0, peft 0.19.0
- 模型：`/root/autodl-tmp/.hf_cache/Qwen3-8B`（收集用），`/root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ`（分类用）
- Expert 数据：`/root/autodl-tmp/error_diag_dpo_recovery/eto_repo/data/alfworld_sft.json`（3119条, 6 task types）
- 活跃进程：
  - **PID 266200** — v5_cuda0 收集，GPU 0，`/tmp/v5_cuda0.log`，~27/250 完成时我最后看的
  - **PID 263025** — v5_cuda1 收集，GPU 1，`/tmp/collect_v5_cuda1.log`，~38/250
- GPU 2 上 VLLM::EngineCore (PID 268087) 和 GPU 5 上 python3 (PID 98594) 不是本项目的

### 3. 📊 当前状态
我审查了 6 个 Worker 的结果：
1. GPU 违规修复（PASS，越界进程已 kill，GPU 3 清空）
2. Registry 和数据清理（PASS，PID 更新，数据无污染——脚本 open("w") 覆盖写）
3. CUDA env 审计（v5_cuda1 仍缺 CUDA_VISIBLE_DEVICES，标 warning 但不 kill）
4. Task overlap 研究（D020：两卡跑同 task 0-249，保留不分片。我建议 P1 做去重版）
5. classify_errors v2 代码审查（PASS，ICL 前缀 bug 已修，divergence-based correction_span 正确）
6. classify_errors dual stats + fix v3（PASS，Version A/B/C 三版 Kruskal-Wallis + confound 自动检测）

**Registry RUNNING**：datagen_traj_v5_cuda0, datagen_traj_v5_cuda1（两卡收集 250 tasks，预计各 ~4-5h）
**Registry PREPARING**：datagen_classify_v2（等 v5 完成后用 14B-AWQ 分类）

### 4. 📋 待办
- **v5 收集完成** → 检查两卡数据量和成功率分布；验证 episode boundary fix 是否持续有效（抽查几条轨迹的 conversation 结构）
- **v5 完成 + classify_errors 跑完** → 审查 p1_analysis.json 的三版 Kruskal-Wallis 结果。重点看 Version C confound_warning 是否触发。若 A/B 显著但 C 全 insufficient/not_significant → 立即通知 Director P1 confound 风险
- **step-1 divergence >80% in full v5** → D021 已规划启动 ICL 增强 v6 收集，审查该决策的实施
- **任何新进程启动** → 必须核查 CUDA_VISIBLE_DEVICES + nvidia-smi 确认 GPU 在 {0,1} 内

### 5. 🎯 战略上下文
- 项目核心：ETADN（error-type-adaptive DPO with DMPO γ_e）。MVP 验证 P1（correction span 单调性：planning > verification > action）和 P2（ETADN 多 γ 优于单 γ DPO）。
- **最大风险是 P1 confound**：8B 模型 91% 在 step 1 diverge，correction_span ≈ expert_total_steps，可能只反映 task complexity 而非 error type 纠正难度。classify_errors.py 已内置 Version C 分层检验，但若全量数据仍 >80% step-1 diverge，P1 需要 ICL-enhanced 收集（D021）。
- **决策链要点**：D009 放弃 self-correction → D015 修 action 翻译 bug 用 8B+ICL 收集 → D016/D017 episode boundary bug 作废旧数据 → D018 排除 14B self-gen expert → D020 两卡重叠保留 → D021 等完整数据再决定是否需要 v6。
- **易错点**：γ_e 是 DMPO 时间折扣因子（D012），不是 DPO β。Expert 数据来自 ETO 的 alfworld_sft.json，不是模型自生成的。


---
