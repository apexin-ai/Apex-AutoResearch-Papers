# verify s43 warmup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_s43-warmup_20260514T123011_result.json`
- **Structured JSON:** [`6b4bc81b898aa4353cee.json`](../../sessions/6b/6b4bc81b898aa4353cee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕，结论如下：

---

### 回答

**1. s43 是否正常运行？**
**是。** PID 587160，tmux session `plan006-prolog-exec-s43` 存在，当前 step 37/500，运行约 8 分钟。

**2. 远程 train_grpo.py 是否接受 --warmup_ratio？**
**是。** 第 348 行 `parser.add_argument("--warmup_ratio", type=float, default=0.0)`，第 430 行传入 GRPOConfig。

**3. s42 实际用的 warmup_ratio 是多少？**
**0.0。** config `grpo_prolog_exec_only.yaml` 未设置 warmup_ratio，argparse 默认值 0.0，GRPOConfig 默认值也是 0.0。

**4. s43 已到第几步？warmup 阶段是否已过？**
step 37/500。s43 用 `--warmup_ratio 0.1`，warmup 阶段 = 500 × 0.1 = **前 50 步**。当前 step 37，**warmup 尚未结束**。从 lr 看，step 37 的 lr=7.2e-07，而目标 lr=1e-06，符合线性 warmup 的预期（37/50 × 1e-06 ≈ 7.4e-07，接近观测值）。

**5. s42 vs s43 warmup_ratio 是否一致？影响多大？**
**不一致。** s42 = 0.0（无 warmup），s43 = 0.1（前 50 步线性 warmup）。

影响评估：
- **前 50 步内**：s43 的 lr 从 0 线性上升到 1e-6，s42 从第 1 步就用 1e-6。这意味着 s43 前期更新更保守。
- **50 步之后**：两者 lr 完全相同（1e-6 constant），后续 450 步的训练动力学一致。
- **总体影响：中等偏低。** warmup 只影响前 10% 的步数，且 lr=1e-6 本身已很小。对最终收敛结果的影响预计不大，但严格来说**两个 run 的超参不完全可比**。如果论文需要严格的 multi-seed 对比，应让 s42 和 s43 使用相同的 warmup_ratio。

---
