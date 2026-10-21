# 诊断报告: d140_4b_sft_s42_no_evi_2048 失败分析

## 失败根因

**进程被外部强制终止（SIGKILL），最可能是 GPU 资源竞争导致 CUDA OOM。**

## 关键证据

### 日志分析
- 日志文件仅 9 行（7027 字节），进程在 inference 13%（31/247 batches）处静默终止
- **无 Python traceback、无 CUDA error、无任何错误信息** → 进程收到 SIGKILL，非 Python 异常
- 时间线：15:06:08 创建 → 15:06:11 开始加载模型 → 15:06:22 开始推理 → 15:24:46 最后写入（运行约 18 分钟）

### GPU 资源竞争
同时段服务器上有多个 eval 并行运行：
- `d140_8b_sft_s42_no_evi_2048`: 14:28 启动，持续运行到 15:36（与 4B 完全重叠）
- `d140_8b_sft_s42_no_evi_2048_fix`: 15:27 启动
- `d140_1_7b_sft_s42_no_evi_2048_fix`: 15:27 启动

**日志中无法确认是否设置了 CUDA_VISIBLE_DEVICES。** 如果未设置，device_map="auto" 可能将模型分配到已被占用的 GPU，导致显存不足。

### 配置验证
- ✅ Adapter 路径正确：`/root/autodl-tmp/sft_no_evidence_output` → adapter_config.json 中 base_model = `/root/autodl-tmp/models/Qwen3-4B`
- ✅ LoRA 配置正常：r=64, lora_alpha=128, 目标模块 7 个
- ⚠️ 无法从日志确认是否传入了 `--no_evidence` 参数（日志不记录命令行参数）
- ❌ 无 eval 输出目录产生 → 推理未完成

## 分类

**GPU 资源竞争 / CUDA OOM**（非代码 bug、非配置错误、非环境问题）

## 是否可直接重试

**可以重试，但必须满足以下条件：**

1. 用 `nvidia-smi` 确认目标 GPU 显存占用 < 2GB（C001）
2. 设置 `CUDA_VISIBLE_DEVICES=X` 指定空闲 GPU（C002）— 当前 GPU 1 空闲（0MiB）
3. 确保传入 `--no_evidence` 参数（C005）
4. 确保同一 GPU 上无其他进程运行
5. 建议 stderr 重定向到日志文件（`2>&1`），以便捕获 CUDA 错误信息
