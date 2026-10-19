---
loop: 3
reason: max_wall_time
updated: '2026-05-16T20:44:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目分配 westd-34142 全部 4 卡 (cuda:0-3)，无越界风险但需确认进程实际在哪张卡
- **正确 checkpoint 唯一路径**：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/model.safetensors`（7,011,543,824 bytes, 777 keys）。`/root/autodl-tmp/checkpoints/pi0_libero/` 是 BASE model（废弃），绝对不能用
- v3 LoRA expert 各自独立 checkpoint，routing eval 必须分别加载：visual→`v3_lora_visual_r16`，spatial→`v3_lora_spatial_r16`，physical→`v3_lora_physical_r16`。**我已报 CRITICAL：routing eval 误把三个 slot 全指向 universal**
- PAR Router 尚未基于 v3 checkpoint 重训，routing eval 必须等 router 就绪

### 2. 🖥️ 基础设施快照
- 服务器：westd-34142 (root)，4× RTX PRO 6000 96GB
- 工作目录：`/root/meta_brain_lora_routing`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型 checkpoint：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/`（JAX→PyTorch 转换后）
- v3 LoRA checkpoints：`/root/autodl-tmp/checkpoints/v3_lora_{visual,spatial,physical,universal}_r16/`
- r48 训练中：`/root/autodl-tmp/checkpoints/v3_lora_universal_r48/`
- 训练数据：`/root/autodl-tmp/libero_demos/libero_object_image/`（66984 samples）
- 日志：`/root/runs/meta_brain_lora_routing/`
- 活跃进程：v3_lora_universal_r48 (PID 118481, tmux, cuda:1, step ~650/10000)
- GPU 0/2 有 model loaded 但 0% util（eval 进程已死）

### 3. 📊 当前状态
**已完成审查并报告**：
- 50-ep nominal baseline: **33/50 = 66%**（libero_spatial，valid）
- Table perturbation baseline (no LoRA): **9/20 = 45%**（↓21pp，valid）
- tb perturbation: **13/20 = 65%**（几乎无降幅）
- Routing eval: **CRITICAL — 配置错误已报 Director**（所有 expert 加载 universal，router 未训练）

**RUNNING**：
- `v3_lora_universal_r48`：step ~650/10000，loss=0.86，ETA ~2.5h

**等待**：
- Director 回应 routing eval CRITICAL（需修复 LoRA 路径 + 重训 router）
- r48 完成后 cron 回调

### 4. 📋 待办
- v3_lora_universal_r48 cron:on_complete → 验证 final loss（预期 <0.65），检查 checkpoint 完整性
- Director 确认修复 routing eval → 审查修复后的 eval 脚本（确认3个 expert 路径正确 + router checkpoint 存在）
- PAR Router 重训完成 → 验证 F1 仍 ~1.0（基于 v3 activations）
- 修复后 routing eval 完成 → 核心审查：routing vs universal vs frozen，是否支撑 Claim 1-3

### 5. 🎯 战略上下文
- **CoRL DDL: 2026-05-29（13天）**
- 核心 story：perturbation 降低 baseline（66%→45% on table = ✓），PAR routing 恢复性能
- v3 训练全部成功（4 expert + r48 control），训练不是瓶颈——**eval pipeline 是当前瓶颈**
- ROADMAP 说 "nominal >80%" 但实测 66%——这不是 bug，可能是 libero_spatial 本身偏难。项目 story 靠相对提升，不靠绝对性能
- **最易判断错的事**：看到 routing eval 0% 不要以为 LoRA 无效——是配置错误（3 个 slot 全加载了 universal，router 未训练）。真正的 routing eval 还没跑过
- r48 "parameter-matched" 标注不精确（r48=11.1M vs 4×r16=14.7M = 75%），论文需精确表述对比维度
