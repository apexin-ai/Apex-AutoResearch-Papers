# reviewer / loop_1.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`3a904d3d4eb8e4ac5035.json`](../../sessions/3a/3a904d3d4eb8e4ac5035.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-19T08:32:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-29046 只有 2 张 GPU (0,1)，westd-28034 只有 4 张 (0,1,2,3)。constraints.yaml 未创建，无显式白名单，但历史分配明确——越界必查。
- `output/directions.pt` 是旧版 320 对数据集产物，已重命名为 `directions_STALE_DO_NOT_USE.pt`。当前唯一合法方向文件是 `results/exp001/directions.pt`（181 对）。任何脚本引用 `output/directions.pt` 必须 CRITICAL 打回。
- exp-002v2-recalib 的 trainer 在 `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`（通过 sys.path.insert 导入），不在 contrastive_entrain_calib 目录下。修改 trainer 会影响所有实验。
- Eval pipeline 必须用 `enable_thinking=False`（Qwen3 thinking token 污染已修复但依赖此参数）。

### 2. 🖥️ 基础设施快照
- **westd-29046** (2× RTX PRO 6000 96GB): 工作目录 `/root/contrastive_entrain_calib`，Python `/root/miniconda3/bin/python`
  - GPU 0: exp-002v2-recalib (PID 172838, tmux `exp002v2-recalib`), ~33s/step, step ~741/8000
  - GPU 1: exp-003 (PID 70649), step ~1894/8000
  - Vanilla baseline eval 也在此服务器运行（自定义脚本 `eval/eval_vanilla_baseline.py`，结果写入 `results/vanilla_baseline_eval/`，约 266/362 完成）
- **westd-28034** (4× RTX 5090 32GB): 同路径
  - GPU 0: exp-004 (PID 18204), step ~6390/8000, ETA 今晚 ~20:40 UTC
  - GPU 1+2: exp-008v3 (PID 104503/104504, tmux `exp-008v3`, DeepSpeed ZeRO-2), step ~291/8000
  - GPU 3: eval 任务（间歇使用）
- 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`（两台服务器均有）
- 数据: `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` (362 pairs)
- NLI: `cross-encoder/nli-deberta-v3-base`（两台已缓存）
- HF_HUB_OFFLINE=1（两台服务器离线模式）
- 无 W&B（report_to=none）

### 3. 📊 当前状态
刚完成一轮全面审查：多实验状态检查 + R1 cosine 矛盾根因确认 + paper gap analysis。

**Registry RUNNING**:
- `exp002v2-recalib`: DC-GRPO cosine R1 + recalibration_interval=500，step ~741。R1≈0 无趋势（信号天然弱，非 drift）
- `exp-003`: R3-only baseline，step ~1894
- `exp-004`: ACT SFT baseline，step ~6390，SFT loss=0 since step 850（过拟合），今晚完成
- `exp-008v3`: Binary Probe GRPO，step ~291，R1=0.375-1.0（远强于 cosine R1），健康

**DONE**: exp-001 (AUROC 0.827), exp-016 (ActAdd α=5 NoF 78.5%), exp-014 (killed, mode collapse)

**PREPARING**: exp-002v3 (scaled cosine R1, scale=5, weight=0.4/0.6, lora_alpha=64, 代码就绪), exp-003-s2 (seed=43, 代码就绪)

**等待中**: 用户 venue 决策 (May 25 vs ARR August); exp-004 完成后 GPU 释放 → exp-002v3 部署

### 4. 📋 待办（条件触发式）
- exp-004 完成 (ETA 今晚 ~20:40) → 审查 eval 结果（multi-checkpoint eval 脚本已就绪 `eval/run_exp004_multi_eval.sh`），核实 GPU 0 释放 → exp-002v3 部署审查
- exp-008v3 step 500 → 审查 probe retrain 是否正常触发（retrain_interval=500），检查 R1 是否持续有效或被 gaming
- exp-002v2-recalib step 1000 → 审查自动 recalibration 是否触发（log 应有 `[RECALIB step 1000]`），R1 是否改善
- exp-003 完成 (ETA May 21) → 审查 eval，与 exp-002v2-recalib 对比确认 "R1 贡献不足" 假设
- exp-002v3 部署通知 → 审查配置（scale=5, R1=0.4, R3=0.6, alpha=64, seed=42）；前 50 步密切监控 grad_norm/entropy（R1 过强可能不稳定）
- vanilla baseline eval 完成 (~362 samples) → 审查 NoF/WRR 作为 paper baseline
- Director 转发 framing 调整提案 → Read negative-framing-review skill，四维度审查
- 任何 worker 提交训练代码 → 检查 GPU 设备号是否在已分配范围内

### 5. 🎯 战略上下文
**核心决策链**: D001(MVP) → D004(v1 confound) → D007(v2.1 PASS, AUROC 0.827) → D020(tanh→cosine) → D021(gate 移除) → D024(drift 误报) → D025(R1 信号弱是真问题, cosine=0.96 稳定)

**最容易判断错的事**:
1. **cosine 矛盾已解决**: `output/directions.pt`(旧) vs `results/exp001/directions.pt`(当前) 是两个不同文件(cosine=0.31)。实际 drift 仅 0.04。不要再被 "方向漂移 74°" 误导。
2. **R1≈0 不是 bug 也不是 drift**: cosine 投影在 3584 维空间天然小(gap~0.098)，R1 weight=0.25 只贡献 8%。这是数学性质不是实现问题。
3. **exp-008v3 的 binary probe R1 (0.375-1.0) 远强于 cosine R1**: 如果 exp-008v3 成功，论文 story 可以 pivot 到 "binarized direction reward" 而非依赖 exp-002v3。准备两条 narrative 路径。
4. **exp-014 是 mode collapse 不是 reward hacking**: 模板化输出(entropy=0.025)，功能正确但多样性为零。可作 negative result。
5. **EMNLP DDL May 25 AoE**: Claim 2 目前 0 实验支撑。exp-002v3 + exp-008v3 是两条平行路径。Venue 决策不在 Reviewer 职责范围。


---
