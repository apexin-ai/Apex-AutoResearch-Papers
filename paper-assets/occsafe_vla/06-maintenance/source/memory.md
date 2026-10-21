# OccSafe VLA Memory

## [2026-05-29] GPU 队列计划（两台服务器各 1 GPU）

两台服务器各只有 1 张物理 GPU (cuda:0)。6 个实验需排队逐个执行。

**westd-10894 队列**（random_occ_v2_s0_r4 完成后启动）：
1. P0: full_occ_bn_eval_v2_s0_r2 — BN eval mode（机制验证，最高优先）
2. P4: full_occ_bn_lambda001_v2_s0_r2 — λ₀=0.001
3. P5: full_occ_bn_lambda01_v2_s0_r2 — λ₀=0.1

**westd-34685 队列**（full_occ_bn_v2_s2_r5 完成后启动）：
1. P1: vanilla_v2_s3_r2 — Vanilla seed 45
2. P2: full_occ_bn_v2_s4_r2 — Cell 1 seed 46
3. P3: detach_bn_v2_s3_r2 — Cell 3 seed 45

**关键变更**：全部改用 cuda:0（不再用 cuda:1/2/3）。每个实验 ~13h，6 个串行最快 ~39h（3 轮 × 13h，两台并行）。

## [2026-05-28] libero_object 实验批量失败 — checkpoint 不完整

### 失败模式
三个 libero_object 实验（full_occ_bn_object_s0, detach_bn_object_s0, vanilla_object_s0）全部因 checkpoint 目录缺少模型权重文件而失败。

**模式 A（resume 启动崩溃）**: `--resume True --resume_step 5000` 时，5000_chkpt 目录无 pytorch_model.bin / model.safetensors → `from_pretrained` 在 finetune.py:912 抛 OSError。影响: full_occ_bn_object_s0, detach_bn_object_s0（westd-10894）。

**模式 B（save checkpoint 崩溃）**: 训练正常到 35%，save_training_checkpoint（finetune.py:1265）尝试从 10000_chkpt 加载 base_vla 时失败 → HFValidationError（路径格式含 `+` 等特殊字符被 HF Hub 当 repo_id 验证）。影响: vanilla_object_s0（westd-34685）。

### 教训
- libero_object 实验的 checkpoint 保存可能不完整（首次训练 0→5000 可能因某种原因未保存完整权重）
- save_training_checkpoint 函数对本地路径的处理可能有 bug（HF Hub 路径验证干扰本地路径解析）
- **resume 前必须验证 checkpoint 完整性**：至少检查目录下存在 model*.safetensors 或 pytorch_model.bin

## [2026-05-28] full_occ_ln_v2_s3 失败诊断

### 根因
**FileNotFoundError，非 SIGHUP/OOM。** 实际 exitcode=1（EXIT_CODE=129 由 wrapper 脚本打印，非真实信号）。

训练在 step 40000 保存 checkpoint 时崩溃。`save_training_checkpoint`（finetune.py:1265→727）调用 `AutoModelForVision2Seq.from_pretrained()` 加载基础模型用于合并 LoRA 权重，但基础模型目录 `/root/autodl-tmp/models/openvla-7b/` 的 `model.safetensors.index.json` 被篡改。

### 修复前提
**恢复基础模型的 `model.safetensors.index.json`**：将 `/root/autodl-tmp/models/openvla-7b/model.safetensors.index.json` 还原为引用 3-shard 命名。

## [2026-05-28] detach_ln_v2_s4 + vanilla_object_s2 + full_occ_bn_v2_s3 批量死亡诊断

westd-10894 上 3 个实验在 ~19:04 北京时间几乎同时被杀。最可能原因：系统 RAM OOM killer（SIGKILL -9 + 多进程连续死亡 + 无服务器重启）。建议减少同时运行实验数量（3→2）以避免系统 RAM 再次不足。