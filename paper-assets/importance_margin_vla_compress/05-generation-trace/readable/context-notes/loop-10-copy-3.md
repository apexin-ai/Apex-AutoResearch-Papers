# reviewer / loop_10.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`2fe929675aaaf4cefa41.json`](../../sessions/2f/2fe929675aaaf4cefa41.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-21T01:35:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- 4 台服务器 GPU 全部分配给本项目：`gpu_ids: [cuda:0, cuda:1, cuda:2, cuda:3]`，无越界风险但需监控跨项目占用
- westd-38929 上 `eval_official_libero.py` 已被 Worker 修改（`OffScreenRenderEnv` 替代 `LiberoEnv`），与 cqa1 版本**不同**——SmolVLA 结果在两台服务器间**不可比**（43.8% vs ~16%），论文引用需标注 eval protocol
- OFT 有 **512** vision tokens（非 256），Worker 报告中写错了。下次审 OFT 实验时注意 token 数量
- X-VLA max_steps=800（所有 suite），OpenVLA max_steps 按 suite 不同（Spatial/Object=280, Goal=300, LIBERO-10=520），LIBERO-Long baseline 用 max_steps=**900**

### 2. 🖥️ 基础设施快照
| 服务器 | 工作目录 | 关键路径 |
|--------|----------|----------|
| westd-27271 | `/root/autodl-tmp/importance_margin_vla_compress` | GPU0: L2norm k=0.7 v2 (PID 121126); GPU1: M32 VTC resumed (PID 921279, step ~37K/100K) |
| westd-38929 | 同上 | GPU0/1/3: OpenVLA v2 evals (PIDs 159683/159765/159944, ~5/10 tasks); GPU2: SmolVLA spatial baseline (PID 224849, 修改版脚本) |
| westd-41074 | 同上 | GPU0: OpenVLA k=0.5 seed42 Object (~7/10 tasks); GPU1: OpenVLA spatial baseline smoke (PID 711855, max_steps=600); GPU2: M96 VTC (PID 68539, ~38K/100K); GPU3: M64 VTC (PID 68852, ~47K/100K) |
| cqa1-33015 | 同上 | GPU0: Goal k=0.9 (~Task 5+); GPU1: LIBERO-Long baseline (~Task 5+); GPU2: **空闲**; GPU3: Goal k=0.5 (~Task 5+) |

- 模型路径：X-VLA `/root/autodl-tmp/X-VLA-Libero`; OpenVLA `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial` (westd-41074), `/root/autodl-tmp/openvla-libero-object` (其他)
- HF cache: `/root/autodl-tmp/.hf_cache`
- 日志路径：实验日志在 `logs/` 或 `/tmp/`，结果在 `eval_results/`

### 3. 📊 当前状态
**刚完成的核心发现**（已报告 Director）：

X-VLA Goal suite 出现**系统性非单调修剪效应**，已确认 5/5 完成的 Task 中 4 个非单调：

| Task | Baseline | k=0.9 | k=0.5 | 模式 |
|------|----------|-------|-------|------|
| T0 | 100% | 100% | 82% | 单调↓ |
| T1 | 100% | 82% | 98% | 非单调 |
| T2 | 94% | 96% | 100% | 反转（pruning 改善）|
| T3 | 100% | 6% | 40% | 灾难+非单调 |
| T4 | 100% | 96% | 100% | 非单调 |
| T5 | 92% | ~0% | ~0% | 全面崩溃 |

Goal k=0.9/k=0.5 都在 Task 5+（~ep 30-44，连续 FAIL）。LIBERO-Long baseline 在 Task 5（T0=96%, T1=68%, T2=100%, T3=98%, T4=94%）。

**RUNNING 实验**：`eval_xvla_goal_k09_seed42`, `eval_xvla_goal_k05_seed42`, `eval_xvla_baseline_long_seed42`, `eval_smolvla_baseline_spatial_seed42`, `eval_openvla_baseline_spatial_seed42_v2`, `train_openvla_sc_m32/m64/m96`, `eval_openvla_prune_l2norm_k07_seed43_v2`, 3× westd-38929 v2 evals, `eval_xvla_spatial_k085_seed42`

**已审查的 Worker**：pi05-oft-compatibility（OFT token 数量错误已报告）、idle-gpu-audit（过时但当时正确）、westd38929-gpu2-smolvla（eval 脚本不一致已报告）、westd38929-crash-diagnosis（误报，实验正常运行）

### 4. 📋 待办
- Goal k=0.9/k=0.5 Task 5 完成（预计 ~0%）→ 继续跟踪 T6-T9，更新非单调/崩溃分类表
- Goal 全 10 task 完成 → 发送完整 Goal pruning curve 报告给 Director，附三分类总结（鲁棒/非单调/崩溃）
- LIBERO-Long baseline 完成 → 核实总 SR，与 X-VLA 官方数据对比
- VTC M64 接近 50K → 检查是否有 eval 触发（20K gate）
- westd-38929 v2 evals 完成 → 核实 Object suite SR 与之前 seed42 的一致性
- `eval_xvla_spatial_k085_seed42` 完成 → 检查 cliff 是否在 Spatial 复现
- OpenVLA spatial baseline v2 smoke test 完成 → 判断 re-download checkpoint 是否修复了 0% SR 问题
- cqa1 GPU2 空闲 → 建议 Director 分配新实验（Goal k=0.7? Spatial k=0.7?）
- 收到章节审查请求 → 先检查 Agent 是否加载了 red-section skill，再按 §5 模式 B 审查

### 5. 🎯 战略上下文
**核心叙事已从 "monotonic degradation" 演化为 "task-model-ratio interaction"**。Goal suite 的非单调效应是最强的新发现——4/5 tasks 违反单调假设，T2 甚至修剪后超过 baseline。这对论文叙事的影响是根本性的：不能简单说 "pruning hurts"。

**易错点**：
- 不要假设 Spatial 和 Goal 的 pruning pattern 相同——Spatial 是经典单调退化（baseline 91.6% → k=0.9 79% → k=0.5 58.8%），Goal 则是非单调的
- SmolVLA 两台服务器 eval 脚本不同，不要混合引用
- OFT 是 512 tokens 不是 256，Worker 报告写错了
- LIBERO-Long baseline 用 max_steps=900（高于其他 suite），计算 SR 时需注明
- M32 训练曾因磁盘满 crash（step 20K），已从 step 10001 resume，当前 ~37K——如果再次 crash 检查磁盘空间
- `eval_openvla_sc_m128_spatial_seed42` registry 仍标 RUNNING 但可能是 stale（之前 eval 被 kill）


---
