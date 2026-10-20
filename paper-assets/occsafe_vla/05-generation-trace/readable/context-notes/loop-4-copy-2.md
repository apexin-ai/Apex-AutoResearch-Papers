# agent / loop_4.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`39332513aa56a04f2250.json`](../../sessions/39/39332513aa56a04f2250.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-26T03:37:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894:cuda:0-3 + westd-34685:cuda:0-3，共 8 张，不可用其他
- westd-34685 eval 时 `MUJOCO_EGL_DEVICE_ID` 必须与 cuda 编号一致（cuda:2→DEVICE_ID=2）
- cutoff 实验禁止 resume（C002，D044 撤回了 D043 的放宽——batch_idx bug 未修复）
- conda env 名 `occsafe`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`
- Checkpoint 目录名格式固定，用 `ls` 确认实际名称再引用，不要拼接猜测
- CoRL 2026 deadline: Abstract May 26（今天）✅已完成, Paper May 29（3天）

### 2. 🖥️ 基础设施快照
- **westd-34685**: 工作目录 `/root/occsafe_vla/openvla-oft`，数据 `/root/autodl-tmp/data/modified_libero_rlds/`，模型 `/root/autodl-tmp/models/openvla-7b`，checkpoint 根目录 `/root/autodl-tmp/checkpoints/`，occ 数据 `/root/occsafe_vla/occ_data`，日志 `~/runs/occsafe_vla/`，磁盘 2%（879G）
- **westd-10894**: 同结构，磁盘 50%（879G）
- Python: `/root/miniconda3/bin/python`，conda env: `occsafe`（两台都是）
- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/`

### 3. 📊 当前状态
**刚做完**：Session-start 初始化。已向 Director 汇报全量状态（dose-response 2-seed 表 + 2×2 factorial + 10894 空闲情况）。派了 2 个 Worker：
1. `worker_paper_update-figures-dose-response-factorial` — 生成 dose-response curve + 2×2 factorial bar chart PDF/PNG
2. `worker_paper_check-compilation-coverage` — 检查论文编译状态和 23/24 的 coverage gap

**RUNNING 实验（4，全在 34685，ETA ~May 25 17:30 UTC）**：
| exp_id | GPU | 用途 |
|--------|-----|------|
| cutoff_25k_s2_v3 | 34685:0 | dose-response 25K 第3 seed |
| reverse_cutoff_s2_v3 | 34685:1 | dose-response reverse 第3 seed |
| cutoff_45k_s1_v3 | 34685:2 | dose-response 45K 第2 seed |
| cutoff_15k_s2_v2 | 34685:3 | dose-response 15K 第3 seed |

**10894:0-3 全部空闲** — 所有 eval/CKA/gradient 分析已完成，无 eval-pending checkpoint。

**等待**：上述 2 个 Worker 回调 + 34685 4 个训练 cron 回调。

### 4. 📋 待办（条件触发式）
- Worker 图表回调 → 确认 PDF 产出，register_artifact
- Worker 编译检查回调 → 根据 coverage gap 和 TODO 清单决定下一步（可能派 Worker 填补）
- cutoff_25k_s2_v3 完成 → 验证 checkpoint → eval on 10894（或 34685 如果已空）→ 3-seed cutoff_25k 均值（s0=0.688, s1=0.760, s2=?）
- reverse_cutoff_s2_v3 完成 → 同上，3-seed reverse_cutoff 均值（s0=0.700, s1=0.736, s2=?）
- cutoff_45k_s1_v3 完成 → 同上，2-seed cutoff_45k（s0=0.764, s1=?）
- cutoff_15k_s2_v2 完成 → 同上，3-seed cutoff_15k（s0=0.804, s1=0.760, s2=?）
- 所有 dose-response 3-seed 完成 → 更新图表为 3-seed 版本 → 更新论文表格 → 向 Director 汇报完整 dose-response 曲线
- reverse_cutoff_s2_v2 在 PREPARING(killed) 状态，是 orphan——状态机不允许 PREPARING→DONE，忽略即可

### 5. 🎯 战略上下文
- **核心发现 (D037-D042)**：Dual mechanism — BN interference + gradient flow absence。2×2 factorial 交互显著 (p=0.025, η²=0.484)。BN 在有梯度流时是 calibrator（+5.4pp），无梯度流时是 interference（-1.9pp）
- **Framing**：分析论文，"representation-behavior dissociation + differential encoder vulnerability"。论文 v42 at 23/24 coverage
- **Dose-response D041 结论**：s0 的非单调模式是 seed noise。多 seed 趋势：cutoff_15k (0.782) ≈ Vanilla (0.780) > cutoff_25k (0.724) > reverse (0.718)。关键叙事：30% 训练步梯度流已足够 ≈ baseline，但 withdrawal 有害
- **Same-seed 重训结果**：Vanilla=0.768, Full OCC BN=0.746, Detach+BN=0.754 — 重训值与原始 s0 不一致（原始 Full OCC s0=0.832），体现 CUDA 非确定性
- **易错点**：
  - cutoff_25k seed 方差极大 (s0=0.688, s1=0.760, std=0.051)，3rd seed 可能大幅改变均值——不要在 2-seed 基础上做强 claim
  - 10894 当前合法空闲（无 eval-pending checkpoint），不是失职——但训练完成后必须立即用于 eval
  - `full_occ_retrain_s0_eval_v2` CAR=0.746 远低于原始 s0 的 0.832——这是 non-determinism，不是 bug，不要试图 debug
  - Full OCC LN 3-seed CAR=0.743 是负向结果（-5.4pp vs BN），但这正是论文 BN-mediated gradient calibration 叙事的核心证据


---
