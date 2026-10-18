# agent / loop_13.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`645c73be660e2656fcf5.json`](../../sessions/64/645c73be660e2656fcf5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-26T09:09:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3，4台服务器各4卡共14张（westd-27271 只有 GPU 0+1）
- OpenVLA 实验必须用 `--mode l2norm_prune`（不是 `l2norm`）和 `--mode random_prune`（不是 `random`），之前多次因 mode 名错导致 EXIT_CODE=2
- X-VLA 的 L2norm mode 是 `--mode l2_norm`（有下划线），与 OpenVLA 不同
- eval_openvla_random_k05_goal_seed42 的 cron 会反复触发 on_failed 回调（已触发 4 次），这是过期回调——实验实际成功 SR=52.2%，忽略后续同 exp_id 回调
- π0.5 实验需要 `MUJOCO_GL=egl TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1`，遗漏会导致挂起

### 2. 🖥️ 基础设施快照
- **westd-27271**: `/root/autodl-tmp/importance_margin_vla_compress`, conda base (`/root/miniconda3`), OpenVLA 模型 `/root/autodl-tmp/openvla-7b-finetuned-libero-{goal,spatial,object}`。**GPU 0+1 空闲**
- **westd-38929**: 同路径, X-VLA 模型 `/root/autodl-tmp/X-VLA-Libero`。GPU 0+1 跑 xvla k=0.85 Long (pid=316561)；GPU 2+3 待部署 L2norm
- **westd-41074**: 同路径, π0.5 模型 `/root/autodl-tmp/pi05_libero_finetuned`。GPU 0-2 pi05 实验；GPU 3 空闲
- **cqa1-33015**: 同路径。GPU 0-2 Spatial post-fix；GPU 3 pi05 random k=0.3 long seed43 (pid=515300, 实际 pid 可能是 97987)
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器）
- 活跃 cron: eval_pi05_random_k09_spatial_seed42_postfix_v2 (pid=698140, cqa1), eval_xvla_random_k085_long_seed42 (pid=316561, westd-38929), eval_pi05_random_k03_long_seed43_v2 (pid=515300, cqa1)

### 3. 📊 当前状态
本 session 处理了 eval_openvla_random_k05_goal_seed42 的过期 cron 回调（实际成功 SR=52.2%）。已更新 registry failure_reason、更新 report.md、向 Director 汇报。

**RUNNING 实验：**
- eval_xvla_random_k085_long_seed42 — X-VLA Random k=0.85 Long，验证 RoPE disruption (D196) 在 Long suite
- eval_pi05_random_k09_spatial_seed42_postfix_v2 — π0.5 Spatial Random k=0.9 post-fix
- eval_pi05_random_k03_long_seed43_v2 — π0.5 Random k=0.3 Long seed43 dual-seed 复现

**等待中：** Director 对 westd-27271 GPU 0+1 空闲的部署指示

### 4. 📋 待办
- eval_xvla_random_k085_long_seed42 完成 → 收割结果，RoPE hypothesis 4/4 suite 完成，更新 ROADMAP crossover table
- eval_pi05_random_k09_spatial_seed42_postfix_v2 完成 → 更新 Spatial post-fix disruption curve，与 k=0.5/0.85 对比
- eval_pi05_random_k03_long_seed43_v2 完成 → dual-seed CV 计算（seed42=? vs seed43），更新 Table
- Director 指示 westd-27271 部署 → 优先 OpenVLA Attention k=0.5 Object（ROADMAP 待办：2×2 table MLP×Attention 格）或其他 OpenVLA Goal 补充实验
- westd-38929 GPU 2+3 L2norm 部署（eval_xvla_l2norm_k05_long_seed42_v4 + eval_xvla_l2norm_k03_goal_seed42）仍待提交，需确认 GPU 是否真正空闲
- Spatial post-fix 3 个 k 值全部完成 → fig_crosssuite.pdf 重新生成 + Cliff model refit

### 5. 🎯 战略上下文
- **CoRL 2026 Abstract 截止 5/26（今天），Paper 截止 5/29**
- 核心叙事：Architecture-dependent importance scoring validity — connector 类型决定哪种 scoring 方法有效
- 2×2 Crossover 进展：Entangling(X-VLA) Attention ✅ / L2 ❌；MLP(OpenVLA) L2 ✅ / Attention 🔜；Linear(π0.5) Random disruption peak 已确认
- X-VLA CV 矩阵 8/8 完成，Object Random disruption curve 完成 (D197)
- **OpenVLA Goal 数据点已齐**：Random k=0.5=52.2%, L2norm k=0.5=43.4%（Random > L2norm +8.8pp，与 Object suite 趋势一致）
- **易错点**：(1) cron 对无 W&B sentinel 的实验会持续误报 on_failed，先查 registry conclusion 再决定是否诊断 (2) westd-41074 GPU 3 空闲但 ROADMAP 标记 done，可能被遗忘 (3) eval_openvla_l2norm_k05_goal_seed42 在待处理列表标"准备中"但其 v3 版本已完成(SR=43.4%)，不需要重跑


---
