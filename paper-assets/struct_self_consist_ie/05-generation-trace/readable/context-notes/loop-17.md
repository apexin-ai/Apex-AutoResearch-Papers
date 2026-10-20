# agent / loop_17.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`e4322a3c4871d6d26fc6.json`](../../sessions/e4/e4322a3c4871d6d26fc6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-21T20:50:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: autodl-5090 / 5090-b / 5090-c 各 cuda:0-3（共 12 卡）。不得使用白名单外设备。
- **14B 推理诊断**: 已 5 次误判。判定失败**必须同时**确认 `ps -p PID` 死亡 + `nvidia-smi` GPU 空闲。"无输出文件"不能单独判 failed（vLLM 加载 15-20min 无输出正常）。14B 单卡必须 `--enforce_eager`。
- **SCD 数字已证伪**: +3.84pp 完全虚假（micro vs instance-avg F1 口径不一致 + eval 集大小不同）。不得在论文引用。
- **B2 verifier +3.62pp 是 91% 泄露**: OOF 后仅 +0.30pp。不得在 main text 引用 B2。
- **API 余额耗尽**: TUM 代理 `http://47.94.22.126/v1` 返回 402。Frontier SC / Spider SQL / HumanEval 全部阻塞，不要尝试启动依赖 API 的实验。
- **DDL 2026-05-25**: ARR May cycle，仅剩 ~4 天。
- **Probe 数字只用 GroupKFold 版本**（CoNLL 0.882 / FewNERD 0.636 / SciERC 0.630），不要引用 StratifiedKFold 旧值（0.98+）。
- **叙事 B 已确认**，不要回退到 "probe >> MV" 旧叙事。

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090 / autodl-5090-b / autodl-5090-c，均为 RTX 5090 × 4
- **工作目录**: `/root/autodl-tmp/struct_self_consist_ie`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **模型路径**:
  - 8B FT (FewNERD): `checkpoints/qwen3-8b-fewnerd-exp021-merged`
  - 8B FT (SciERC): `checkpoints/qwen3-8b-scierc-merged-v2`
  - 7B base: `checkpoints/qwen25-7b-fewnerd-merged`
  - 14B: `/root/autodl-tmp/.hf_cache/modelscope_hub/Qwen/Qwen2___5-14B-Instruct`
  - 32B merged: `qwen25-32b-fewnerd-merged`（5090 上，14 shards ~61GB）
- **数据**: `data/fewnerd/`, `data/conll2003/`, `data/scierc/processed_data/`
- **活跃进程（reconcile 确认）**:
  - exp_14b_inference_fewnerd: PID 252310, autodl-5090-c cuda:0（唯一 cron 活跃）
- **磁盘**: 5090 盘 250G 已用 92%（仅 ~22GB 可用），操作前先 `list_large_dirs`

### 3. 📊 当前状态
**我刚完成**: Session #17 启动初始化 — registry 同步、reconcile crons、资源诊断、向 Director 汇报。

**关键发现**: Registry 有 10 个 RUNNING 实验，但 `get_project_resource_usage` 仅确认 5 个有实际 GPU 活动。8/12 GPU 空闲 = 资源严重浪费。已向 Director 汇报并请求 CoNLL N=16 GPU 分配。

**Registry 实际状态**:
- RUNNING (10): exp_14b_inference_fewnerd, exp_14b_inference_conll, exp_fewnerd_7b_n16_s42, exp_fewnerd_t05_s456, exp_fewnerd_t12_s456, exp_scierc_n16_s123, exp_scierc_n16_s456, exp_fewnerd_n16_s456, exp_fewnerd_n16_s42, exp_fewnerd_n16_s123
- QUEUED (2): exp_conll_n16_s123, exp_conll_n16_s456（已审批，待 GPU 分配）
- 仅 5 个有确认的 GPU 活动，其余 5 个可能是 phantom RUNNING

**Workers (3)**:
- worker_diagnose_gpu_snapshot_d217 — turn 16，正在 SSH 查各服务器进程状态（已发现 5090 全空闲）
- worker_8gpu_fill_priority — ⚠️ turn 1（30+ 分钟仅 1 轮），疑似卡住
- worker_t_ablation_3seed_summary — turn 11，正常推进中

**已向 Director 发出汇报**，等待回复 + GPU 分配。

### 4. 📋 待办（条件触发式）
- worker_diagnose_gpu_snapshot 完成 → 根据诊断结果确认哪些 RUNNING 是 phantom，更新 registry（标 failed 或重新提交）
- worker_8gpu_fill 确认卡死 → cancel 并 spawn 新 worker 重新填充空闲 GPU
- worker_t_ablation_3seed_summary 完成 → 检查 3-seed 均值和 CI，更新论文 T-ablation 表格
- Director 分配 GPU 给 CoNLL N=16 → submit_on_allocated 提交到指定卡
- FewNERD T=0.5/T=1.2 s456 完成 → 汇入 T-ablation 3-seed 汇总
- SciERC N=16 s123/s456 完成（如确认实际在跑）→ 合并 3-seed N-scaling curve
- 14B FewNERD 推理完成（PID 252310）→ **双信号诊断**（ps + nvidia-smi），提取 metrics 填 scale curve
- API 余额恢复 → 重启 Frontier SC
- 5090 空闲卡分配后 → 优先跑 CoNLL N=16（QUEUED），其次填 phantom RUNNING 的重提交

### 5. 🎯 战略上下文
**论文核心**: "Strong Predictors, Weak Selectors" — LP 能预测质量（QE）但不能选出更好的输出（selection）。三大贡献: (1) QE framework + selection diagnostic, (2) N-scaling / T-ablation / cross-model 实验矩阵, (3) complexity-dependent introspection boundary (probe)。

**叙事 B**: ESJ(0.51) << Probe(0.63-0.88) ≤ MV(0.87)。Probe > MV 仅在 CoNLL（低复杂度），FewNERD/SciERC 上 probe < MV。结论是 complexity-dependent introspection boundary，不是 "probe 全面优于 MV"。

**当前最大风险**: 12 卡分配仅 5 卡在跑。诊断 worker 正在查清 phantom RUNNING 的根因。如果 5 个 phantom 确认没进程，需要全部重新提交——这会消耗时间，DDL 压力更大。

**易踩的坑**:
1. 14B 绝不轻易标 failed（5 次误判历史）
2. `read_registry` 工具可能返回不完整结果（本轮只返回 3/223），需要 grep registry.yaml 原文件验证
3. 5090 磁盘 92%，跑新实验前检查空间
4. exp_b1_scd 虽然 PENDING 但 conclusion=killed，不要重启
5. F1 scaling law 写作约束：不报 c 均值（分数据集）、CoNLL 不报 c、N=1 低于 greedy 需解释


---
