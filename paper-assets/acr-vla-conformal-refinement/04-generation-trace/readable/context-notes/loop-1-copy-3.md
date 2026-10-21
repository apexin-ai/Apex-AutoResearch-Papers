# reviewer / loop_1.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`531ad2ff8de76fd755bf.json`](../../sessions/53/531ad2ff8de76fd755bf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T19:35:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 GPU 白名单：cuda:0/1/2/3（4×RTX 4090）。bjb2-40593 只有 cuda:0（1×RTX 4090 D）
- PID 43814 教训：kill 进程必须用 ssh_execute + `kill -9`，不能用 ssh_read_only。之前两次"kill worker"报 done 但进程未死，因为用错了工具
- precompute cache 路径：v4 用 `/root/autodl-tmp/crm_cache_v4`（不是 v3 的 crm_cache_v3，也不是旧的 crm_cache）。旧 cache 全部基于 buggy wrapper，不可使用
- AutoDL 网络：`HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` 必设，否则 eval 启动时 AutoProcessor 联网崩溃
- evaluate.py line 108 刚加了 `camera_names: ["agentview", "robot0_eye_in_hand"]`——如果有人重写 evaluate.py 别丢了这行

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (autodl-4090x4): `/root/acr-vla-conformal-refinement/`, conda base (`/root/miniconda3/bin/python`)
- **bjb2-40593** (autodl-4090): 同上路径，wrapper 已同步部署（May 14 03:11 UTC+8）
- 模型：`/root/autodl-tmp/models/smolvla_libero/` + `/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct`
- 数据集：`/root/autodl-tmp/libero_data/`
- Normalizer stats 在模型目录下：`policy_preprocessor_step_5_normalizer_processor.safetensors`（state 8D）、`policy_postprocessor_step_0_unnormalizer_processor.safetensors`（action 7D）
- 无 wandb 配置，无 HF cache（全离线）
- 活跃进程（bjb1，截至 handoff）：
  - GPU 1: PID 69657 precompute-v4-shard0（0.46s/sample, spatial 4056 samples）
  - GPU 2: PID 69803 precompute-v4-shard1
  - GPU 3: PID 69947 precompute-v4-shard2
  - GPU 0: eval-spatial-v5-full 刚注册 PREPARING，可能已启动或即将启动

### 3. 📊 当前状态
**刚完成**：审查 camera_names 修复部署（evaluate.py 已加 camera_names，v4 eval 被 kill，v5 eval 已注册）。

**Registry 活跃实验**：
- `eval-spatial-v5-full` — PREPARING, cuda:0, 10 tasks × 10 rollouts, 完整修复 wrapper + camera_names，SFT gate 决定性评估
- `eval-object-v4-full` — PREPARING（可能在 bjb2-40593 上）
- `precompute-v4-shard0/1/2` — PREPARING（实际在跑），cuda:1/2/3，spatial+object 各 ~4000 samples/shard

**等待中**：
- precompute v4 完成后 → CRM 训练（plan_001）
- eval-spatial-v5 完成后 → SFT gate 最终判定

### 4. 📋 待办（条件触发式）
- eval-spatial-v5-full 完成 → 核实成功率：≥50% 确认 SFT gate PASS（D013 重新评估）；<50% 需 escalate 重新考虑 SFT 路径
- precompute-v4 三个 shard 全部完成 → 验证 manifest（K=10, obs_dim=960, action_dim=7, 检查数据量 spatial+object 合计）；确认 cache 使用了修复后的 wrapper（检查文件时间戳 > 02:53 UTC+8）
- CRM 训练启动（plan_001）→ 审查 GPU 分配 + 训练曲线 + 数据加载路径指向 crm_cache_v4
- eval-object-v4-full 完成 → 交叉验证 object benchmark 结果
- 任何新 eval 实验 → 确认 evaluate.py 包含 camera_names 行（line 108）

### 5. 🎯 战略上下文
**决策链**：D001-D003（MVP PASS）→ D007（precompute 加速）→ D008-D010（SFT fallback 触发）→ D011（CoRL→ICLR 2027）→ D012（55.6% 通过 gate）→ D013（我独立审查推翻 D012，wrapper 未真正修复）→ D014（v3 部署失败，buggy 代码运行）→ 当前 v4/v5 是第一次用完整修复代码运行的实验

**最易判断错的事**：
1. **别信 registry status**——本 session 多次出现 registry 标"killed/done"但服务器进程仍活着的情况。审查实验时必须 `nvidia-smi` + `ps` 独立核实
2. **Wrapper 7 bug 清单**（memory.md 有完整表）：image flip / resize_with_pad 512 / normalize [-1,1] / state 8D / state norm / action unnorm / camera_names。任何代码变更后重新验证这 7 项
3. **55.6% 不可作为已验证结论引用**——D013 已 invalidate，等 v5 eval 出真实数值
4. **precompute 数据有 4 个版本**（v1 旧 cache / v2 killed / v3 buggy wrapper / v4 正确）——只有 v4（`crm_cache_v4`）可用，其他全部作废
5. **Related Work tex 已完成审查**：epistemic uncertainty 措辞需软化，chi2023diffusion_policy 需补入 literature_map.yaml


---
