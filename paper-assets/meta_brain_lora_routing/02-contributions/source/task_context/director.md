---
loop: 1
reason: max_messages
updated: '2026-05-16T20:40:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0/1/2/3 @ westd-34142（project gpu_ids 白名单）
- **废弃 checkpoint**：`/root/autodl-tmp/checkpoints/pi0_libero/` 是 lerobot base model（未微调），绝对不能用于训练或 eval
- **正确 checkpoint**：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/`（官方 fine-tuned JAX→PyTorch 转换，777 keys）
- **Eval 脚本**：只用 `eval_base_no_lora.py`（OpenPIMetaBrainPolicy 路径），不用 `evaluate_libero_plus.py`（MetaBrain 路径仍 0%）
- LIBERO 和 LIBERO-Plus 环境用户要求严格区分（实际发现 LIBERO-Plus 包含原版 tasks，但概念上分开讨论）
- HuggingFace 网络不通，所有资源必须用本地缓存

### 2. 🖥️ 基础设施快照
- 服务器：westd-34142 (connect.westd.seetacloud.com), 4× RTX PRO 6000 96GB
- 工作目录：`/root/meta_brain_lora_routing/`
- Python：`/root/miniconda3/bin/python`（aml-train 镜像, conda base）
- 正确 base checkpoint：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/model.safetensors`（7GB, bfloat16）
- JAX 原始：`/root/.cache/openpi/openpi-assets/checkpoints/pi0_libero/`
- v3 LoRA checkpoints：`/root/autodl-tmp/checkpoints/v3_lora_{visual,spatial,physical,universal}_r16/.../final/`
- openpi 代码：`/root/openpi/`
- 数据：66984 frames (libero_object_image), norm_stats 在 checkpoint 目录内
- 活跃：rank-48 training PID 118481 (cuda:1), eval Workers on cuda:2/3

### 3. 📊 当前状态
**刚完成**：Eval pipeline 终于通了（66% nominal baseline, 50 episodes）。v3 LoRA 3/4 完成（physical/spatial/universal done, visual 接近完成）。

**RUNNING**：
- v3_lora_visual_r16: cuda:0, 接近完成
- v3_lora_universal_r48: cuda:1, step 250/10K (~3.5h), plan_013 parameter-matched ablation
- Perturbation degradation eval Worker: cuda:2, 测 _table/_tb/_add/_language 各 20 ep
- v3 LoRA routing eval Worker: cuda:3, 先 universal 对照再 PAR routing

**等待关键结果**（40-60 min 内返回）：
- Perturbation degradation 数据（frozen model 在扰动下的成功率）
- v3 LoRA routing eval 数据（PAR vs universal vs frozen）

### 4. 📋 待办
- Perturbation eval Worker 完成 → 看 degradation 幅度（期望 <40%，vs nominal 66%）。如果无显著 degradation → 研究假设不成立，需 pivot
- v3 LoRA routing eval 完成 → 看 PAR > universal？如果 PAR ≈ universal → PAR Router 可能需重训（当前 router 基于旧 pi0_base activations 训练，换了 fine-tuned checkpoint 后分布可能变了）
- v3_lora_visual_r16 完成 → 更新 registry，GPU 0 加入 eval
- rank-48 完成 → 与 4×r16 PAR routing 做参数量对比（Claim 3）
- 所有 eval 出齐 → 如果核心 claims 成立，启动 Paper Agent 写 CoRL 论文

### 5. 🎯 战略上下文
- Phase 0 (PAR Router F1=1.0) 已完成：证明 PI0 内部 activations 可完美分类扰动类型
- 关键决策链：D001(MVP定义) → D004(Phase0 GO) → D010(换 fine-tuned checkpoint) → D011(v3 loss=2.0 是 OOD 预期)
- **最容易判断错的事**：如果 PAR routing 表现不好，第一反应不要怀疑 LoRA 训练质量——先检查 PAR Router 是否兼容新 checkpoint（router 在旧 pi0_base activations 上训练的，新 checkpoint 的 layer 6 activation 分布可能完全不同）
- **12 小时排障教训**：eval 0% 经历了 checkpoint 搞混、环境版本不对、jaxtyping 严格检查等多个叠加问题。现在唯一可靠的 eval 路径是 `eval_base_no_lora.py` + OpenPIMetaBrainPolicy
- rank-48 参数对比不完全精确（r48=11.1M active vs PAR=3.7M active），论文中需说明"inference-time active params"而非 total stored
