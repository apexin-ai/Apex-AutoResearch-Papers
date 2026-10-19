# reviewer / loop_1.md

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`d07171c0cfa76319b21a.json`](../../sessions/d0/d07171c0cfa76319b21a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-16T01:09:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `cuda:0/1/2/3` 全部合法（项目配置确认），但每个训练进程必须设 `CUDA_VISIBLE_DEVICES` 隔离——JAX 会默认预分配所有 GPU 显存导致并行加载冲突
- `par_router.py:95` 的 `.float()` 强制转换不可删——π₀ 输出 BFloat16，PAR Router 权重 Float32，删了就 RuntimeError
- sensor_noise per-step 收集进程（PID 182971, GPU 0）可能仍在跑，不要 kill——它启动慢（torch.compile 32 workers），但确认已过 task matching 阶段
- plan_002 描述写的 "scripted oracle policy" 不存在——LIBERO 没有 oracle policy，实际用 π₀ rollout + success filtering

### 2. 🖥️ 基础设施快照
- 服务器：`westd-34142`，账号 `root`，工作目录 `/root/meta_brain_lora_routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：PI0 safetensors 在服务器上（`load_pi0_for_collection()` 自动加载），~3.5B params
- LIBERO-Plus：`/root/LIBERO-plus/`，`new_objects/` 已下载完成（6.3GB, 208 个 `_add_N` 任务可用）
- PAR Router checkpoint：`/root/meta_brain_lora_routing/checkpoints/phase1/par_router/best_router.pt`
- 激活数据：`/root/meta_brain_lora_routing/activations/`（episode-level 全部完成含 sensor_noise 17MB；per_step/ sensor_noise 可能仍在收集）
- Phase 1 代码：全部在 `/root/meta_brain_lora_routing/phase1/`（meta_brain_assembly.py, train_lora_expert.py, collect_expert_demos.py, par_router.py, ablation_ladder.py, evaluate_libero_plus.py, data_loader.py, visual_augmentation.py）
- 活跃进程：PID 182971（sensor_noise per-step 收集，GPU 0，已运行 1h+）；其余 GPU 空闲

### 3. 📊 当前状态
Phase 1 代码全部 dry-run 通过，D007 批准 4 路 LoRA 训练启动。我刚审完以下 worker：
- `worker_fix_assembly-dryrun-and-cleanup`：PASS — assembly 端到端验证通过，actions=(1,50,32), routing 正常
- `worker_research_spatial-physical-data-collection`：WARNING — 确认无 oracle policy，用 π₀ success filtering 替代
- `worker_data_download-libero-plus-new-objects`：assets 下载完成，208 `_add_N` 任务可加载
- `worker_fix_spatial-add-n-collection`：spatial 模式切换为官方 `_add_N` 扰动（解决了我之前的 train/eval 分布 mismatch WARNING）
- ROADMAP 更新审查：PASS，Dream #1 修复方案合理，GPU 预算充足

Registry：`phase0_activation_collection` = DONE（唯一条目）。无 RUNNING 实验。
等待中：可能有 re-dream 回调（`dream_20260515T165902`），以及 4 路 LoRA 训练启动的 worker 通知。

### 4. 📋 待办
- LoRA 训练 worker 完成通知 → 检查 GPU 分配合规（CUDA_VISIBLE_DEVICES 隔离）、W&B loss 曲线、trainable params 数量、early stopping 是否正常触发
- sensor_noise per-step 完成 → 验证文件大小（应为 ~276MB，不是 1.3KB）；完成后需要重跑 classifier sweep 更新 GO/NO-GO verdict
- re-dream 回调 → 审查修复后的 Dream 评分是否有实质改善；如果仍低于 5/10 需要立即提建议
- plan_013（rank-48 universal）启动 → 核实使用 `--lora_rank 48 --lora_alpha 96`，验证 trainable params ≈ 12M（与 Meta-Brain 总量匹配）
- plan_002 cross-eval 结果出来 → 这是 Claim 2 的存亡时刻：如果 universal rank-16 ≈ specialized experts，routing 价值存疑

### 5. 🎯 战略上下文
- 决策链：D001(MVP定义) → D002(Reviewer增强) → D003(架构修正) → D004(Phase 0 GO) → D005(Research阶段) → D006(first-token pooling) → D007(Dream修复+训练批准)
- 核心风险：**plan_013 rank-48 universal 是存亡实验**——如果 rank-48 universal ≈ Meta-Brain，Claim 2 崩溃，整个 routing story 不成立。不要在这个结果出来前帮 Agent 把 routing 的好处写死在论文里
- 参数量：每 expert ~3.69M × 3 + router ≈ 12M（不是 paper_framing 曾声称的 6M，已修正）
- Phase 0 结果近乎完美（F1=0.993, K=1=1.000 with first-token），这恰恰是 Reviewer 可能攻击的点——"routing 太 trivial，universal LoRA 就够了"。plan_013 是唯一能回答这个攻击的实验
- 易错判断：不要因为 Phase 0 F1 太高就认为 Phase 1 一定成功——诊断容易 ≠ 纠正有效，这是两个独立假设


---
