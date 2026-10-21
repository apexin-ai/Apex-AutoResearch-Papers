# agent / loop_16.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`f4ae59544a5b71f1cbb4.json`](../../sessions/f4/f4ae59544a5b71f1cbb4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-21T04:43:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: autodl-5090 / 5090-b / 5090-c 各 cuda:0-3（共 12 卡）。不得使用白名单外设备。
- **14B 推理诊断**: 已 5 次误判。判定失败**必须同时**确认 `ps -p PID` 死亡 + `nvidia-smi` GPU 空闲。"无输出文件"不能单独判 failed（vLLM 加载 15-20min 无输出正常）。14B 单卡必须 `--enforce_eager`。
- **SCD 数字已证伪**: +3.84pp 完全虚假（micro vs instance-avg F1 口径不一致 + eval 集大小不同）。SCD 不构成论文贡献，不得引用。
- **B2 verifier +3.62pp 是 91% 泄露**: OOF 后仅 +0.30pp（不显著）。不得在 main text 引用 B2。
- **API 余额耗尽**: TUM 代理 `http://47.94.22.126/v1` 返回 402。Frontier SC / Spider SQL / HumanEval 全部阻塞，不要尝试启动依赖 API 的实验。
- **DDL 2026-05-25**: ARR May cycle，仅剩 ~4 天。

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
  - exp_14b_inference_fewnerd: PID 252310, autodl-5090-c cuda:0（cron 活跃）
  - exp_fewnerd_t05_s456: PID 305832, autodl-5090-b cuda:0
  - exp_fewnerd_t12_s456: PID 305834, autodl-5090-b cuda:1
  - exp_scierc_n16_s123: autodl-5090-b cuda:2
  - exp_scierc_n16_s456: autodl-5090-b cuda:3
  - exp_fewnerd_7b_n16_s42: PID 264869, autodl-5090-c cuda:2
  - exp_fewnerd_n16_s456: autodl-5090-c cuda:3
- **autodl-5090 四卡全空闲**，5090-c cuda:1 空闲
- **磁盘**: 5090 盘 250G 已用 92%（32B merge 后剩 22GB），操作前先检查

### 3. 📊 当前状态
**刚完成**: D216 全量 GroupKFold probe 定稿（CoNLL 0.882 > MV ✅, FewNERD 0.636 / SciERC 0.630 < MV ❌），叙事 B 确认。CoNLL N=16 s42 成功完成。SciERC T-ablation 3 seed 全部完成。

**正在进行**:
- 8 个实验 RUNNING（见上）—— 5090-b 四卡满载，5090-c 三卡在跑
- 2 个 Worker 运行中:
  - `worker_run_8gpu_fill_priority` — 填充 GPU 空位（提交 N=16 / T-ablation 剩余 seed）
  - `worker_analysis_t_ablation_3seed_summary` — 汇总 T-ablation 3-seed 统计结果
- 4 个 PENDING 待审批: CoNLL N=16 s456/s123, FewNERD N=16 s123/s42
- Paper Agent 叙事 B patch 派发中（11 处 probe 数字 + 措辞重写）

**等待中**:
- 上述 8 个 RUNNING 实验的 cron 回调
- 2 个 Worker 的完成回调
- Director 审批 4 个 PENDING 实验
- API 余额恢复（Frontier SC 阻塞）

### 4. 📋 待办（条件触发式）
- FewNERD T=0.5/T=1.2 s456 完成 → 汇入 T-ablation 3-seed 汇总，更新论文 T-ablation 表格
- SciERC N=16 s123/s456 完成 → 合并 3-seed N-scaling curve（s42 已有），拟合 F1(N)=a-b*N^(-c)
- FewNERD N=16 s456 / 7B N=16 完成 → 同上，补充 7B vs 8B-FT scaling 对比
- 14B FewNERD 推理完成（PID 252310）→ **谨慎诊断**（参照 memory.md 14B 诊断规则），提取 N∈{1,2,4,8} metrics，填 7B-14B-32B scale curve
- PENDING 审批通过 → submit_on_allocated，CoNLL N=16 可用 5090 空闲卡
- API 余额恢复 → 重启 Frontier SC (FewNERD/Spider/HumanEval)
- Worker t_ablation_3seed_summary 完成 → 检查 3-seed 均值和 CI，更新论文
- Worker 8gpu_fill_priority 完成 → 确认所有提交成功，检查 GPU 利用率
- 5090 四卡空闲 → 可跑 CoNLL N=16 pending 或其他 CPU 分析任务

### 5. 🎯 战略上下文
**论文核心**: "Strong Predictors, Weak Selectors" — LP 能预测质量（QE）但不能选出更好的输出（selection）。三大贡献: (1) QE framework + selection diagnostic, (2) N-scaling / T-ablation / cross-model 实验矩阵, (3) complexity-dependent introspection boundary (probe)。

**决策链关键节点**:
- D208: 4.5 Mandate Sprint 启动（DDL 5/25）
- D216: Contribution #3 定稿为 "complexity-dependent introspection boundary"（probe > MV 仅 CoNLL）
- D215: GroupKFold 修正后 probe < MV for 2/3 datasets → 叙事从 "probe >> MV" 降为 "ESJ << probe ≤ MV"
- D214: probe 发现 instance 泄露（StratifiedKFold vs GroupKFold 差 0.34）
- D210: Reviewer CRITICAL 修复 — Contribution #3 从 "impossibility" 降级为 "introspection boundary"

**易踩的坑**:
1. **14B 实验绝对不要轻易标 failed** — 已 5 次误判，每次 Director 手动恢复。严格按双信号诊断。
2. **Probe 数字只用 GroupKFold 版本**（0.882/0.636/0.630），不要引用 StratifiedKFold 旧值（0.98+）
3. **5090 磁盘紧张**（92%），跑新实验前先 `list_large_dirs` 检查
4. **叙事 B 已确认**，不要回退到 "probe >> MV" 旧叙事
5. **B1 SCD 已 killed**，exp_b1_scd PENDING 状态但 conclusion=killed，不要尝试重启


---
