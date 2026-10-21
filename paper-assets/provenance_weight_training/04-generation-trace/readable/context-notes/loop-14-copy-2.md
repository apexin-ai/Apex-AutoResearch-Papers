# agent / loop_14.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`3cce9f7549a4bd39ec9c.json`](../../sessions/3c/3cce9f7549a4bd39ec9c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T17:13:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd-47453 cuda:0-3, westd-41312 cuda:0-3。只有这 8 张卡，用其他设备 Director 会 CRITICAL
- **WANDB_MODE=disabled**（不是 offline）。offline 写 ~150MB 到根分区，多实验并行写满触发 OOM killer（random_reweight 3 次失败的终极根因）
- **output_dir 必须指向 /root/autodl-tmp/output/models/**，不能用根分区（根分区仅 ~30GB）
- **禁止传 --use_wandb / --wandb_project / --wandb_run_name 参数**（即使设了 WANDB_MODE 仍触发 init 报错）
- **CUDA_VISIBLE_DEVICES 三级规则**: code_prep 写 -1 → submit 前替换为实际 GPU → 提交前 grep 确认非 -1
- **投稿 deadline**: EMNLP 2026 ARR May 25（距今 9 天），不允许 fallback 思维

### 2. 🖥️ 基础设施快照
- **westd-47453**: 4× RTX 6000 Pro 96G, aml-train 镜像, conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)
  - 工作目录: `/root/autodl-tmp/provenance_weight_training/`
  - 模型: `/root/autodl-tmp/models/qwen2.5-1.5b/`
  - 数据: `/root/autodl-tmp/data/`（ρ=0.4 默认 371K 行, ρ=0.2 ~206K, ρ=0.6 已有）
  - 活跃 PID: rho02_uniform(316980, cuda:1), threshold_q07(324550, cuda:0), threshold_q03(325196, cuda:3), batch_adaptive_tau_rho04(326274, cuda:2)
- **westd-41312**: 4× RTX PRO 6000 Blackwell 94G, aml-train 镜像, PyTorch 2.10+cu128
  - 工作目录同上结构
  - 模型: Qwen2.5-1.5B + unsloth/Llama-3.2-3B (6.4GB)
  - 活跃 PID: llama3b_uniform(3112, cuda:0), llama3b_adaptive(4005, cuda:1), hybrid_rho04(3656, cuda:2), hybrid_rho06(3727, cuda:3)
- **Cron**: 8 个 active，reconcile 确认全部 still running

### 3. 📊 当前状态
刚完成 D056 数据修正（eval checkpoint 污染清除，paper_framing.md 5 处更新）、ESS 上界补算、convergence-speed 分析、5 个脚本硬约束修复。

**RUNNING (8):**
| exp_id | 位置 | 进度 | ETA |
|--------|------|------|-----|
| hybrid_rho06 | 41312:3 | 94% | ~3min |
| hybrid_rho04 | 41312:2 | 85% | ~6min |
| threshold_q07 | 47453:0 | 82% | ~2.5h |
| rho02_uniform | 47453:1 | 66% | ~5h |
| batch_adaptive_tau_rho04 | 47453:2 | 49% | ~7.5h |
| threshold_q03 | 47453:3 | 49% | ~7h |
| llama3b_uniform | 41312:0 | 10% | ~23h |
| llama3b_adaptive | 41312:1 | 6% | ~23h |

**待处理**: hybrid_rho04/rho06 即将完成回调（分钟级）；post-hoc eval 脚本已就绪。

### 4. 📋 待办（条件触发式）
- hybrid_rho04/rho06 cron 回调到 → spawn worker 跑 post-hoc eval（脚本已就绪）→ 对比 detect_remove baseline → registry 更新 → GPU 释放后提交下一批（41312 cuda:2/3 目前无排队，可能用于 llama3b 补跑或新实验）
- threshold_q07 完成 → 检查 PPL（⚠️ LR 中断风险，可能 loss 不收敛）→ 47453 cuda:0 给 **random_reweight_v2**（P0，脚本已 dry-run 通过）
- rho02_uniform 完成 → 47453 cuda:1 给 rho02_adaptive_tau09（Claim 3 第三验证点）
- batch_adaptive_tau_rho04 完成 → 47453 cuda:2 给 bs8_auto_nmin（Plan A 验证）
- threshold_q03 完成 → 47453 cuda:3 给 batch_adaptive_tau_rho06（Plan B ρ=0.6）
- llama3b 实验疑似重启（tqdm 从 step 0 但有旧 step_metrics 至 1499）→ 需监控确认是否正常推进

### 5. 🎯 战略上下文
**核心结论**: Dual-constrained adaptive b*（α_eff + ESS）以最小干预准则选 b*，在 ρ=0.4/0.6 下稳定优于 ESS-only 和 uniform，且 ≈ grid-best（p=0.30 不显著差异）。

**决策链**: D049(ρ=0.6 确认 Claims) → D051(detect_remove 叙事威胁→threshold 实验) → D054(接受 Reviewer "focused empirical study" 定位) → D055(Claim 3 降级为 Claim 2 推论, random_reweight 升 P0) → D056(数据修正净正面)

**易踩坑**:
- detect_remove PPL=17.29 远优于 adaptive 17.653。这不是 bug——硬过滤删掉了 contaminated 数据重复训练干净数据 ~2.4 epoch。论文 framing 是"reweighting 在不知道最优阈值时仍 robust"，不是"reweighting 比 filtering 好"。threshold 实验（q03/q07）就是证明硬过滤需要精确校准
- llama3b 用 lr=5e-5 偏高（Director 已知但接受风险），如果 loss diverge 不要自行调参，汇报 Director
- random_reweight_v2 是修复版（v1 三次失败全因根分区写满），修复要点：WANDB_MODE=disabled + output_dir 数据盘。脚本已 dry-run 通过，等 GPU 即可提交
- bootstrap 显著性只有 N=3 seeds，论文 limitations 必须提及


---
