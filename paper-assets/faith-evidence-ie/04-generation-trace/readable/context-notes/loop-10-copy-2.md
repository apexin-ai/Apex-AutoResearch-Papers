# agent / loop_10.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`555a48b5d8da369b456e.json`](../../sessions/55/555a48b5d8da369b456e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T21:03:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **cuda:0/1/2/3** on **rtx5090-4x**，绝不碰白名单外 GPU（即使 Director 指令也要 push back）
- 项目路径 `/root/autodl-tmp/freige`，根分区空间有限，大文件只往 `/root/autodl-tmp/`
- SFT baseline 推理必须用 `--no-quantize`（D058 发现量化 confound，之前 eval 数字有污染）
- plan_009 reward eval 两次都 failed（extract + flatnli_r2），不要再重试同样方式——需要换思路或确认底层问题
- CED vs flat-NLI **统计不可区分**（D056），CED 不再作为独立贡献，Claim 3 已降级——写论文别再把 CED 当 selling point

### 2. 🖥️ 基础设施快照
- **主服务器**: rtx5090-4x（4× RTX 5090 32GB），account=root
- **备用服务器**: bjb2-12179（account=root）
- **工作目录**: `/root/autodl-tmp/freige`
- **Python/环境**: 服务器用 `aml-train` 镜像 → conda 环境，`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **W&B**: 项目已配置，metrics 自动同步
- **活跃 cron（3 个）**:
  - `plan_008_rsft_topk3` — pid=234494, cuda:3
  - `eval_plan_012_dpo_ced_1ep` — eval 进程
  - `plan_011_bf16_g8_step_eval` — cuda:1
- **无运行中 Worker**（全部 done）

### 3. 📊 当前状态
**刚完成的关键结果**:
- `plan_001_flat_nli_seed43` (DONE/success) — flat-NLI RSFT seed=43 补跑完成，证实 CED≈flat-NLI
- `eval_plan_014_sft_no_evidence` (DONE/success) — SFT-without-evidence rel_f1=0.4893, evi_f1=0（符合预期，ablation 证据到位）
- `plan_011` bf16 GRPO eval — Reviewer PASS，C2+C3 证据链完整（QLoRA rel_f1=0.2167 vs bf16 rel_f1=0.4549）

**RUNNING（3 个实验，cron 监控中）**:
- `plan_008_rsft_topk3` — top_k ablation, cuda:3
- `plan_011_bf16_g8_step_eval` — bf16 GRPO step-level eval, cuda:1
- `eval_plan_012_dpo_ced_1ep` — DPO+CED 1ep eval（验证 3ep 过拟合是否消除）

**PREPARING/QUEUED**:
- `eval_plan_001_flat_nli_s43` — QUEUED，等 cuda:0 空出
- `plan_011_eval_g8_bf16_ckpt100` — PREPARING, 分配 cuda:3（等 plan_008 完成）
- `mvp2_eval_rsft_s44` — PREPARING，Full dev eval RSFT seed=44

**ANALYZING**: plan_012_dpo_ced_1ep（训练完，eval 在跑）、plan_012_dpo_ced（原 3ep 版本）

**cuda:0 当前空闲** — eval_plan_001_flat_nli_s43 在 QUEUED 等它，应优先提交

### 4. 📋 待办（条件触发式）
- **eval_plan_012_dpo_ced_1ep cron 回调到达** → spawn worker 分析 metrics，与 3ep 版本对比，判断过拟合是否消除。若 rewards_acc < 0.95 且 rel_f1 > RSFT → DPO 作为 alternative method 写入论文
- **plan_011_bf16_g8_step_eval cron 回调到达** → 提取 step-level metrics，生成 forgetting dynamics figure（plan_009 的替代方案）
- **plan_008_rsft_topk3 cron 回调到达** → top_k ablation 结果分析，对比 top_k=1/3/5 效果。cuda:3 释放后提交 plan_011_eval_g8_bf16_ckpt100
- **cuda:0 确认空闲** → 立即提交 eval_plan_001_flat_nli_s43（QUEUED 状态，seed=43 eval）
- **所有 P0 eval 收齐后（plan_001 + plan_011 + plan_012 + plan_014）** → 触发 Paper Agent retitle + reframe + related work 扩展
- **plan_002 test set eval** → D057 决定推迟到论文终稿阶段，不要现在跑

### 5. 🎯 战略上下文
**项目核心结论链**:
- **C1**: FREIGE task definition + EDCR metric（稳定贡献）
- **C2**: GRPO evidence-extraction decoupling 是 **QLoRA-specific**（非 RL 通病）。证据：bf16 GRPO rel_f1=0.4549 vs QLoRA GRPO rel_f1=0.2167（D054）
- **C3**: bf16 GRPO ≈ RSFT（差 0.47pp），两者均 >>SFT baseline（+4.9pp）。CED 已降级，不作独立贡献（D056）
- **C4**: CED 优势重新定位为 output quality control / compliance（D055）

**投稿**: EMNLP 2026 Main，ARR July cycle（~7月15-25），剩余约 2 个月

**最易判断错的事**:
1. **不要把 CED 当 selling point** — D056 已确认 CED≈flat-NLI 统计不可区分，Claim 3 降级了
2. **plan_009 forgetting dynamics** — reward eval 路径两次 failed，plan_011 step eval 是替代方案，别再走 plan_009 老路
3. **SFT baseline 数字有量化污染** — D058 发现推理时量化 confound，所有涉及 SFT baseline 对比的数字要核实是否用了 `--no-quantize`
4. **Dream v2 评分 3.0/2.5/2.5 未达标**（需 ≥3.5），结构性问题正在修复中，不要假设论文框架已定型
5. **plan_012 DPO 有过拟合信号** — 3ep 版本 rewards_acc=1.0（Reviewer WARNING），1ep 版本是补救，结果待出


---
