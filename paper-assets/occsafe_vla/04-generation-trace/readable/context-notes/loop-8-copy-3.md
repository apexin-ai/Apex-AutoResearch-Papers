# reviewer / loop_8.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`df2e15a3be5b03f30b56.json`](../../sessions/df/df2e15a3be5b03f30b56.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-27T04:20:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 10894 四卡 cuda:0-3 全部在跑 v2 LN 训练，**禁止 kill 或抢占**——这些是解决 CRITICAL #9 的唯一路径
- 34685 四卡同样全占（2 个 LN v2 + 2 个 n=5 扩展），同样不可中断
- Detach+LN 在 Table 1 已标 $^\star$（v1 数据），ΔCAR 已改为 "---"——**正文 L9 仍写 +2.0pp，必须在下一轮 paper fix 中同步改掉**
- Registry 存在 false-negative bug：10894 上 s1c/s2/s0c 原条目标记 DONE/success 但实际仍在训练，真实状态看 _r2 条目

### 2. 🖥️ 基础设施快照
- **westd-10894** (root): `/root/occsafe_vla`，conda env `occsafe`，Python `/root/miniconda3/envs/occsafe/bin/python`
  - 训练日志: `/root/runs/occsafe_vla/{exp_name}.log`
  - Checkpoints: `/root/autodl-tmp/checkpoints/{exp_name}/`
  - 梯度分析脚本: `/root/occsafe_vla/scripts/run_gradient_analysis_v2.py` (17036B, May 27 04:42)
- **westd-34685** (root): 同结构，脚本已同步（May 27 10:13）
- 论文本地路径: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/`
- Eval+梯度执行命令已就绪: `artifacts/_project/intermediate/eval_and_gradient_commands.md`
- 梯度 v2 sample count 已修正为 800（与 v1 一致），两台服务器已部署

### 3. 📊 当前状态
**我刚完成**：审查了 ~12 个 worker（compile-check、v1v2-consistency、table1-marking、gradient-prep、server-status、eval-failure-analysis）。所有审查已通过 `reviewer_post_to_director` 发送。

**RUNNING 实验（8 个）**（截至 ~04:10 UTC May 27）：
| 服务器 | GPU | 实验 | Step | ETA (UTC) |
|--------|-----|------|------|-----------|
| 10894 | 0 | full_occ_ln_v2_s1c | 12731 (25%) | ~13:46 |
| 10894 | 1 | full_occ_ln_v2_s2 | 12790 (26%) | ~13:38 |
| 10894 | 2 | detach_ln_v2_s0c | 12781 (26%) | ~13:46 |
| 10894 | 3 | full_occ_ln_v2_s0d | 10179 (20%) | ~14:28 |
| 34685 | 0 | detach_ln_v2_s1 | 16994 (34%) | ~12:45 |
| 34685 | 1 | detach_ln_s4 | 17131 (34%) | ~12:57 |
| 34685 | 2 | ablation_occ_detach_s4 | 14407 (29%) | ~14:00 |
| 34685 | 3 | mvp_occ_s4 | 14199 (28%) | ~13:22 |

**Open Issues**:
- CRITICAL #9（v1/v2 mixing）：等 v2 LN 训练完成 → 解决
- WARNING: results.tex L9 正文 Detach+LN ΔCAR=+2.0pp 与 Table 1 "---" 矛盾
- WARNING: Table 2 caption / Fig 2 caption 仍说 "LN cells have n=1"
- WARNING #19: Figure 1 PDF 可能显示旧 78.0%
- WARNING #5: Table 1 Random OCC 位置
- WARNING #13: Discussion BN/CKA 未调和

### 4. 📋 待办（条件触发式）
- **训练完成（~12:45-14:30 UTC）→** 独立核实 checkpoint 存在 → 确认 eval 被调度 → 审查 eval 命令是否与 `eval_and_gradient_commands.md` 一致
- **Eval 完成（~15:20 UTC）→** 交叉验证 eval 结果 vs registry metrics → 检查 Cell 2 (Full OCC+LN) 和 Cell 4 (Detach+LN) v2 数据是否合理（与现有 v1 趋势一致） → 确认 CRITICAL #9 可关闭
- **Paper 更新后 →** 审查：(1) Table 1 Detach+LN 行是否用 v2 数据替换 (2) Table 2 factorial 是否全 v2 (3) 正文 L9 ΔCAR 修复 (4) 所有 caption 更新
- **Gradient 分析完成后 →** 核对图表是否与论文叙事一致（orthogonality claim、norm magnitude claim）
- **reverse_cutoff_s2_v2_eval →** 如有空闲 GPU 且时间允许，可重新调度；否则 n=2 足够

### 5. 🎯 战略上下文
- **核心结论**：gradient flow 降低 CAR，detach 恢复 baseline。BN+gradient flow 最不稳定。空间标签内容无关。
- **论文 narrative**：negative finding paper——"不要用 auxiliary spatial heads with gradient flow 来改善碰撞安全"
- **CRITICAL #9 是提交前唯一阻塞项**：factorial table 的 LN row 混用 v1/v2 数据。v2 训练 ETA ~14:30 UTC，eval ~15:20 UTC，deadline May 28 12:00 UTC → ~20h margin，非常充裕
- **易错点**：
  - memory 文件中旧 ETA (20:30-22:30 UTC) 已过时，实际 12:45-14:30 UTC——已更新 memory
  - Table 1 已经改过一次（加 $^\star$、改 ΔCAR），但**正文段落忘了同步**——下一个 paper-fix worker 很可能再犯同样的错
  - 梯度分析命令中 condition_name 用下划线（如 "Vanilla_v2"），plot 脚本用空格——fuzzy matching 能处理，不是 bug
  - detach_ln_s4 周期性速度骤降（1.80s/it）是 I/O contention 已知模式，不是 stall


---
