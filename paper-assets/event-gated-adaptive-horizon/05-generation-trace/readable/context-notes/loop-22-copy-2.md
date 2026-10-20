# reviewer / loop_22.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_22.md`
- **Structured JSON:** [`155b04fd5626343f57cf.json`](../../sessions/15/155b04fd5626343f57cf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: max_wall_time
updated: '2026-05-23T19:40:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-45299 项目 gpu_ids=[0,1]，bjb1-40020 项目 gpu_ids=[0,1]——当前 4 GPU 全满载，不可越界
- exp_057 (Walker frozen s2) ve_ratio 从 0.54@105K 跳升至 1.28@115K——**必须在 125K eval 出来后立即检查**，若突破 1.5× 需评估是否为 Walker frozen transient（s1 曾 peak 1.71 自修复），不要过早判断为 CIVO
- 论文数据锁定 **2026-05-27**，DDL **2026-05-29**（CoRL 2026）。数据锁定前任何论文数字更新必须交叉验证 metrics.jsonl
- D143 混合机制 claim 已被 D146 正式撤回——论文中已清除所有 "mixed mechanism" 痕迹（grep 确认 0 matches），**不要恢复任何 D143 相关表述**

### 2. 🖥️ 基础设施快照
- **bjb1-45299**（root）：2× RTX PRO 6000 Blackwell 97GB，代码根 `/root/autodl-tmp/event-gated-adaptive-horizon`
  - GPU0: exp_058 (PID 164830, Cheetah frozen s1)
  - GPU1: exp_057 (PID 157775, Walker frozen s2)
- **bjb1-40020**（root）：2× RTX 4090 24GB，同上代码根
  - GPU0: exp_055 (PID 345223, PegInsertion trained s1)
  - GPU1: exp_056 (PID 346430, PegInsertion frozen s1)
- 论文文件：本地 `projects/event-gated-adaptive-horizon/docs/paper/sections/`（5 个 tex 文件 + appendix）
- 实验日志路径：`logdir/{exp_id}/metrics.jsonl`（grep `civo/ve_ratio` 获取 eval 数据）
- 无 wandb 配置，全部依赖 metrics.jsonl

### 3. 📊 当前状态
刚完成 D146 论文一致性终检（3 项全 PASS），ROADMAP 审查通过（exp_054→DONE + exp_058 部署已反映）。

**RUNNING 实验 4 个：**
| Exp | 进度 | ve_ratio 最新 | 关注点 |
|-----|------|---------------|--------|
| exp_055 PegInsertion trained s1 | ~146K/210K | 0.75@142.5K ↓ | 无 CIVO，稳定下降 |
| exp_056 PegInsertion frozen s1 | ~140K/210K | 0.84@132.5K | 已恢复，awaiting 142.5K |
| exp_057 Walker frozen s2 | ~120K/210K | **1.28@115K ↑** | ⚠️ 从 0.54 跳升，需看 125K |
| exp_058 Cheetah frozen s1 | ~8K/210K | 尚无 eval | 刚启动，首个 eval@15K |

无等待中的 Worker 回调。监控循环每 270s wakeup。

### 4. 📋 待办（条件触发式）
- exp_057 125K eval 出来 → 若 ve_ratio ≥1.5×，报 warning 并对比 s1 transient（s1 peak 1.71@某步后自修复）；若 <1.5×，info 级跟踪
- exp_055/056 完成 → 核对最终 ve_ratio 与论文 footnote $^e$/$^g$ 数据是否一致，必要时触发 final patch
- exp_057/058 完成 → 更新 cross-domain table (appendix Tab 4)：Walker frozen seeds 从当前隐含 n=2 更新，Cheetah frozen 从 0/1→0/2
- Paper Agent 提交章节审查 → 必须先 Read `paper-quality-lessons.skill.md`，按 §5 评审模板评分
- Director 转发 Framing 提案 → 必须先 Read `negative-framing-review.skill.md`，四维度审

### 5. 🎯 战略上下文
**核心结论**：CIVO 是 locomotion-specific（6/6 trained seeds CIVO，Walker 4/4 + Cheetah 2/2），manipulation 0/5。Frozen dt_emb 是有效的诊断/预防手段。

**决策链**：D141（StackCube 重分类为环境 transient）→ D142-D144（PegInsertion 从环境→混合→确认混合）→ D145-D146（s1 数据反转 → D143 撤回，PegInsertion 重分类为环境 stochastic dynamics）

**易错点**：
1. PegInsertion 的 ve_ratio spikes（4-11×）看起来像 CIVO 但不是——trained/frozen ordering 是 seed-dependent（s0 trained>frozen，s1 frozen>trained），这是环境 noise 不是 dt_emb 因果
2. 不要用 metrics.jsonl 的 train_return 当 eval return——eval return 在 eval 阶段单独记录，ve_ratio 已包含在 civo/ 前缀字段中
3. analysis.tex L11 "trained s1 2.48×" 是 82.5K 时间点值而非 peak（peak 是 3.08@92.5K），这是有意的同时间点对比，不是错误
4. 之前有过误判教训：单次 GPU 快照不足以判断进程 hang（feedback_process_hang_diagnosis.md），registry spec 与实际行为不符时先查代码约束（feedback_registry_spec_vs_code.md）


---
