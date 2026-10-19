# agent / loop_1.md

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`88fab394dac285c31fb1.json`](../../sessions/88/88fab394dac285c31fb1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T15:56:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（westd-34142），不可用其他设备
- submit_on_allocated 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python ...`
- GPU 编号始终从 0 开始（CUDA_VISIBLE_DEVICES 自动映射物理 GPU）
- sensor_noise.pt 原始 episode-level 文件已丢失（被 per_step worker 覆盖），不可假设存在
- env_wrapper.py 的 `np.float_` 已修为 `np.float64`，但重装/更新 LIBERO-Plus 后需重新检查
- light_conditions 数据是合成生成的（非官方 assets），分析结论需标注 bias discount

### 2. 🖥️ 基础设施快照
- 服务器：westd-34142，工作目录 `/root/meta_brain_lora_routing`
- Python：`/root/miniconda3/bin/python`（conda base），PyTorch 2.8.0+cu128，CUDA 12.8
- 4× RTX PRO 6000 Blackwell 94GB
- 模型：`/root/autodl-tmp/checkpoints/pi0_base`（14GB，ModelScope 下载完成）
- 激活数据：`/root/meta_brain_lora_routing/activations/`（episode-level）+ `activations/per_step/`（per-replan-point）
- Phase 0 代码：`/root/meta_brain_lora_routing/artifacts/phase0/`（configs.py, collect_activations.py, train_classifier.py, eval_classifier.py, collect_per_step.py, collect_per_step_single.py, analyze_few_shot_v2.py, train_per_layer.py, eval_binary.py, analyze_light_bias.py, go_nogo.py）
- LIBERO-Plus：`/root/LIBERO-Plus/`，assets 下载中（~9h ETA，后台进程）
- 活跃进程：PID 148761（sensor_noise 收集，状态未知——新 Worker 正在检查）

### 3. 📊 当前状态
**刚完成**：Few-shot K=1 Visual 子类分析 → **F1=0.898, paligemma_layer_6 单层 K=1 F1=1.0**。已汇报 Director。Registry 已更新 few_shot metrics + verdict=VIABLE。

**Registry**: `phase0_activation_collection` RUNNING（唯一实验）

**运行中的 Workers**（2 个）：
1. `worker_analysis_few-shot-full-3class_20260515T155258` — 完整 3-class（Visual/Spatial/Physical）few-shot K=1/3/5/10 分析，用 5 类 per_step 数据，CPU-only
2. `worker_fix_sensor-noise-check-and-collect_20260515T155517` — 检查 PID 148761 状态，必要时重新收集 sensor_noise（cuda:1）

**等待回调**：上述 2 个 Worker 完成后处理结果

### 4. 📋 待办
- `few-shot-full-3class` Worker 完成 → 更新 registry 的 3-class few-shot 指标 → 汇报 Director → 这是 GO/NO-GO 最后一块拼图
- `sensor-noise-check-and-collect` Worker 完成 → 如果 sensor_noise 数据到位 → spawn Worker 重跑包含 sensor_noise 的完整 7-class sweep + 更新 GO/NO-GO
- sensor_noise per_step 数据到位 → 合并到 full 3-class few-shot 分析（sensor_noise 属于 Visual 类）
- Full 3-class few-shot K=1 F1 ≥ 0.70 → 向 Director 发 **GO 建议**；< 0.70 → 发 Framing 调整提案
- Director 发 GO → 推进 Phase 1 路由器设计
- eval_classifier.py 方法学修复待做（evaluate_model 在全数据集评估 → 应只报 CV 数字或 held-out），Director 已知但非阻塞

### 5. 🎯 战略上下文
- **目标**：CoRL 2026（Abstract DDL 2026-05-26，Paper DDL 2026-05-29）
- **Phase 0 核心结论**：π₀ 激活确实编码扰动类型信息。Episode-level 3-class F1=99.26%，K=1 per-step F1=0.898，paligemma_layer_6 单层完美分类。路由可行性高度确认
- **PaLIGemma >> Expert**：视觉编码器层全 >0.92，Action Expert 层全 <0.58 → Phase 1 路由器应只用 PaliGemma 特征，LoRA 主要修改 PaliGemma 层
- **易错点 1**：episode-level 99%+ 指标是 ~44 replan points 均值的上界，Reviewer 会质疑。必须用 per-step few-shot 数字（K=1 F1=0.898）作为主要论据
- **易错点 2**：objects_layout 收集成功率约 36%（58/90 因 asset 缺失跳过），只有 32 episodes。Spatial 类样本量偏小
- **易错点 3**：sensor_noise episode-level .pt 文件已丢失，需要重新收集才能跑包含 sensor_noise 的完整 sweep
- **7→3 映射**：Visual（Camera+Light+Background+Noise）/ Spatial（Layout）/ Physical（Robot）。Language 排除在外


---
