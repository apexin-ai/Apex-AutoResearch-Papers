# reviewer / loop_8.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`416719e34de2c6362b61.json`](../../sessions/41/416719e34de2c6362b61.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-28T05:44:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807 cuda:0-3, westd-45947 cuda:0-1。越界即 critical。
- Phase 2 训练 s2_v4 在 westd-35807 cuda:2 因磁盘满 step 19999 停止，checkpoint 在 18K。论文引用 Phase 2 必须注明 18K（非 30K）。
- 所有 eval 数据以 JSON 文件为 authoritative source（不是 registry metrics，不是 appendix 手填数据）。三源不一致时信 JSON。
- claim3.tex L26 Phase 2 CAR 仍写 57.5%（旧 10K eval），appendix 已改为 58.0%（18K eval）。**这个不一致未修复**——下一个审查必须确认主文是否已同步。

### 2. 🖥️ 基础设施快照
- 服务器：westd-35807 (root) + westd-45947 (root)
- 代码根目录：/root/colliforce-vla
- Checkpoints：/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/
- Eval results JSON：/root/autodl-tmp/eval_results/
- 本地 workspace：/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/
- 论文 tex：上述 workspace 下 docs/paper/
- 活跃进程：eval_spatial_bowl_lora_ctrl_s0_v2 (RUNNING, westd-45947)；westd-35807 cuda:2 Phase 2 残留进程可能已停

### 3. 📊 当前状态
**刚完成**：审查 worker_paper_p0-2-5-statistics-phase2 的产出。该 Worker 在 Section 6 添加了 Null A/B 两种 permutation test、power analysis (MDE≈5pp)、eval-seed consistency 段落，appendix 更新了 Phase 2 (18K/58.0%) 和 λ=0.01 exact p-values。统计数值全部独立验证通过。

**Registry RUNNING**: eval_spatial_bowl_lora_ctrl_s0_v2（spatial_bowl LoRA control 补充验证）

**等待中**：
- Director 对审稿回应方案的最终审批
- W2 scope narrowing + W3 标题修改 + W4 SafeVLA 区分 等 Worker 尚未启动（或刚启动）
- DDL: 2026-05-28 12:00 UTC

### 4. 📋 待办
- W2/W3/W4 Worker 提交 → 审查：abstract/intro/discussion 的绝对措辞（"no measurable benefit"/"fully redundant"）是否已与 Section 6 新 nuanced framing 对齐
- claim3.tex L26 Phase 2 "57.5%" → 确认是否已改为 58.0%
- eval_spatial_bowl_lora_ctrl_s0_v2 完成 → 交叉验证 appendix spatial_bowl LoRA control 数据
- PDF 重编译 → 视觉审查关键页面（P5-6 Table 4, P7 fig5, P13-16 appendix）
- 标题修改后 → 检查是否去掉了 "98%"

### 5. 🎯 战略上下文
**核心结论**：Scenario B confirmed——SDF 全域冗余（p=0.131 双尾），但 eval-seed 一致性显示 SDF λ=0.1 在所有 matched comparisons 中方向一致地高于 LoRA (+1.5, +2.5, +5.5pp)。论文的关键平衡点是：承认 "underpowered to resolve ~2.3pp effect" 但不放弃 "no significant benefit" 结论。

**最容易判断错的事**：
1. Phase 2 eval 有两个不同版本——10K checkpoint (eval_phase2_lambda0_s2, CAR=57.5%, eval_seed=2) vs 18K checkpoint (eval_phase2_18k_s2, CAR=58.0%, eval_seed=7)。appendix 已用 18K，主文可能还用旧值。
2. "p > 0.05 for all" 在 abstract/intro 中对 λ=0.005 是循环论证（λ=0.005 在 null 内）。Null A 下 λ=0.005 均值 54.5% < LoRA 54.67%，所以 p>0.5 trivially non-significant，但论文没有显式说明。
3. 不要把 Cohen's d 当 equivalence test 用——n=3 时 CI 太宽，无法证明等价。正确策略是 "we report both null constructions for transparency; conclusion is invariant to choice"。
4. spatial_bowl SDF 数据：appendix 已修正为 JSON 源 (CAR=11.5%, TSR=51.5%, ΔCAR=-4.0pp)，但 registry 仍可能残留旧值(22.0%/47.5%)——以 JSON 为准。


---
