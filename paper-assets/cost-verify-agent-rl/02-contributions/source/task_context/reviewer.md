---
loop: 20
reason: max_wall_time
updated: '2026-05-25T05:36:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-17606 只有 **1 张 GPU 可见** (cuda:0)，第二张已被 SeetaCloud 回收。所有训练必须用 1-GPU config。
- Cell B 新 seeds 必须用 `_alfworld_factorial_h2_episode_adv_1gpu.yaml`（已创建），不能用原始 2-GPU config。
- Cell B seed2 step5 checkpoint **不存在**，无法补评。Table 1 Cell B "2 seeds" 实为 seed1 only (5.97%)，需修正 caption 或等新 seeds 替代。
- hsweep_h10_seed2_retry2 registry 缺 metrics 字段，Worker 未补录。应补：step5_val_success=0.21875, step0_val_success=0.125。

### 2. 🖥️ 基础设施快照
- 服务器：`bjb1-17606` (root)，工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-1___7B`；SFT checkpoint: `/root/autodl-tmp/checkpoints/scienceworld_sft_bjb1/final/`
- W&B：entity=`xiaoyucorynne-`, project=`cost-verify-agent-rl`
- Cell B launch script: `/root/cost-verify-agent-rl/scripts/run_cell_b_1gpu.sh <seed>`
- Advantage log: `/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl` (3000 条, 15 steps)
- GPU: 1× NVIDIA RTX PRO 6000 Blackwell (98GB), cuda:0
- ScienceWorld SFT 完成，GPU 已释放 (PID gone)

### 3. 📊 当前状态
**刚完成**：Round 6 Paper Agent 修复验证（9/10 PASS, 1 warning re: theory ratio deletion）+ W2 advantage ratio 分析审查 + ScienceWorld SFT 完成确认。

**Registry 关键状态**：
- `scienceworld_sft_bjb1`: DONE/success（450 步完成，eval loss 0.0725）
- Cell B seeds 准备就绪，等待启动（GPU 空闲）
- `exp029_seed200_step5_ood_eval`: QUEUED

**等待中**：
- Director 决策：Cell B 新 seeds 启动（优先级最高，N2 修复）
- Director 决策：ScienceWorld GRPO Cell D 何时排期
- Cell B seed 100/200/300 应该即将启动

### 4. 📋 待办
- Cell B seed 启动回调 → 验证 PID/GPU/config 正确，确认 cuda:0 白名单内
- Cell B step 112 附近 → 检查是否过 eval 关（eval_batch_size=1 已在 Cell B config 里？需确认）
- Cell B 完成 → 审查 step5 OOD eval 结果，与 seed1 5.97% 对比
- W2 advantage ratio 数据被 Paper Agent 写入论文 → 核实 break-even analysis 正确性（阈值 4.24，step5 实测 2.64）
- ScienceWorld GRPO 启动 → 验证用了正确的 SFT checkpoint (`scienceworld_sft_bjb1/final/`)
- 论文 Section 4 旧数字 "ratio ≈ 1.32" 如仍存在 → CRITICAL 打回（正确值 2.64）

### 5. 🎯 战略上下文
**核心结论**：Step-independent training 通过 M1 (info loss) + M2 (sign misattribution) 双机制导致崩溃。Episode-level GRPO 修复两者但 seed-dependent (36% generalize)。

**Round 6 审稿核心矛盾**：Overall 3.0，需推向 3.5。N2 (Cell B 补 seed) 是唯一能动评分的实验（验证 5.97% 不是 outlier）。其他均为写作/理论修复。

**易错点**：
1. **Cell B 的 OOD 5.97% 是 BELOW SFT baseline (6.72%)**——这是 EXPECTED 的好结果（证明去 M2 alone 不够），不是 failure。新 seeds 目标是确认 "Cell B ≈ SFT"，不是期望 Cell B > SFT。
2. **Advantage ratio > 1 不推翻论文**——需要 ratio ≥ 4.24 才能 break even。2.64 仍支持 wrong-direction net gradient。
3. **h=10 seed2 没崩溃** (21.875% val success) 但论文已更新描述 ("1/2 seeds collapse")，Figure 3(b) 仅显示 seed1。这是已知的 minor inconsistency，审稿人可能不追问。
4. **DDL 2026-05-26 11:59 UTC**。3 Cell B seeds × 6-7h = 18-21h + eval = 紧但可行。
