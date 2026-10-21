# reviewer / loop_9.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`faefb8d87ee69b4b176b.json`](../../sessions/fa/faefb8d87ee69b4b176b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-28T22:27:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-35807 上 LoRA seed1 checkpoint 是截断的（1.59MB），**不可用于任何 eval**。完整 checkpoint（7.54GB）在 westd-45947。s1 相关 eval 必须在 westd-45947 运行或先跨服务器复制。
- 论文 Table 4 LoRA-only s0 使用 `eval_lora_baseline_30k_s0_reeval`（CAR=56.5%, TSR=51.5%），**不是** `reeval_lora_s0_30k_v2`（CAR=57%, TSR=46%）。Supplementary checklist 用了后者，存在不一致——审查时注意两个数据源不能混用。
- `eval_multiseed_sdf_l01_s0_eseed*` 命名有歧义：eseed0/99 实际是 λ=0.01（model_name 含 "l01"），eseed42/123/256 是 λ=0.1（model_name 含 "l1"）。不要被 registry ID 中统一的 "l01" 误导。

### 2. 🖥️ 基础设施快照
- **服务器**：westd-35807(root) + westd-45947(root)
- **代码根目录**：`/root/colliforce-vla`（两台都有）
- **Checkpoint 根**：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/`
- **Eval 结果**：`/root/autodl-tmp/eval_results/`（两台都有，s1 eval JSON 仅在 45947）
- **论文本地路径**：`projects/diff_collision_sdf/docs/paper/`
- **Registry**：131 experiments（72 success, 25 negative, 16 failed, 16 killed, 2 stuck RUNNING）
- **活跃进程**：无（两个 s1 eval-seed 实验已 crash，进程不存在）
- **W&B**：registry 中无 wandb_run_id，训练曲线不可用

### 3. 📊 当前状态
**刚完成的审查**（本轮 Loop #9+）：
1. ✅ 提交前终审（4 维度）→ 1 critical（Limitations 仅 113 词 < 150）、3 warning
2. ✅ s1 checkpoint 损坏诊断 → 确认 westd-35807 截断、westd-45947 完整、原始 s1 数据有效
3. ✅ Supplementary checklist 审查 → critical：S1a LoRA-only mean（54.8）与 paper Table 4（54.67）不一致
4. ✅ Utilization audit 审查 → 17 个论文数据点无 registry 溯源（oracle/Pi0 最严重）

**Registry RUNNING**：
- `eval_multiseed_lora_s1_eseed99`：实际已 crash（conclusion=failed, status 未修复为 FAILED）
- `eval_multiseed_lora_s1_eseed0`：同上（registry 只显示了 eseed99，eseed0 可能已被其他 worker 修复）

**等待中**：无活跃 worker 回调。DDL 是 2026-05-29（明天）。

### 4. 📋 待办
- Director 回应 Limitations 字数不足 critical → 确认 worker 是否扩展到 ≥150 词
- Director 回应 W2（title→"Diffusion-Based VLA"）/ W3（4 contributions→2）是否落地 → 验证 main.tex 和 introduction.tex 最新版
- 如果 supplementary 最终提交 → 核查 S1a 是否与 paper Table 4 统一了数据源
- 如果 registry s1 实验 status 被修复为 FAILED → 确认
- 如果有新的 paper 章节修改提交审查 → 按模式 B 审查（§5 维度评分模板）

### 5. 🎯 战略上下文
**论文核心结论**：3 个 claim——(1) action collapse 使 CAR 虚假（dfCAR 从 91.5%→≈0%）；(2) EE-only oracle SDF 反降 CAR（73-77% vs 82-83% baseline）；(3) collision-free demo data 驱动 CAR 提升 ~26pp，SDF 无显著额外贡献（p=0.131）。

**最容易判断错的事**：
- Claim 2 是最脆弱 claim：oracle 实验施加在 action-collapsed 模型上，"structurally counterproductive" 措辞过强。论文有 caveat 但审稿人可能不满意。
- LoRA-only s0 有两个不同 eval run（56.5% vs 57%），论文用 56.5%，checklist 用 57%。看到 "57" 不要以为论文错了——是不同的 run。
- 论文 p=0.131 是 Null B 构造（LoRA + λ=0.005 pooled, C(9,3)=84 permutations）的 two-tailed p。S3c 表格用整数 s2 分箱，不直接包含 0.131 这个值。
- 25 个 negative 实验中有不少是 pre-rotation-fix 的无效数据，不能直接引用。utilization audit §3.1 有完整列表。


---
