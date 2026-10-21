# code plan 801 openvla patch and eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_801-openvla-patch-and-eval_20260517T144456_result.json`
- **Structured JSON:** [`3a26e217570bc186f63b.json`](../../sessions/3a/3a26e217570bc186f63b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成汇报

### Part 1: 4 个补丁执行结果
1. **config.json** — `AutoModelForVision2Seq` → `AutoModelForImageTextToText`，移除 `openvla/openvla-7b--` 前缀，`_name_or_path` 改为本地路径。（注：下载进程覆盖了首次补丁，已二次修复）
2. **preprocessor_config.json & tokenizer_config.json** — 移除所有 `openvla/openvla-7b--` 前缀
3. **modeling_prismatic.py / processing_prismatic.py / configuration_prismatic.py** — 从 Spatial 模型直接复制（已含 `_supports_sdpa=False`、`tie_weights(**kwargs)` 等修复）

### Part 2: 模型加载验证
- 加载成功，参数量 7,541,237,184 (7.5B)
- Processor 加载成功 (PrismaticProcessor)
- VRAM 占用 ~15.1 GB (bf16)

### Part 3: plan_801 部署
- **exp_id**: `eval-openvla-object-vla-only-seed42`
- **GPU**: cuda:2 (19.2G used / 24.5G total)
- **PID**: 667642
- **tmux session**: `eval-openvla-object-vla-only-seed42`
- 首个 rollout 已开始运行，avg step 177ms

### 异常记录
- Object checkpoint 下载未完成，safetensors 缺失。通过 `hf download` + `HF_HUB_DISABLE_XET=1` 重新下载，总耗时约 50 分钟（xet bridge CDN 从中国极慢，禁用后回退到标准 LFS CDN 约 5MB/s）
- 下载进程覆盖了已打补丁的 config 文件，需二次修复
- 首次提交 eval 时 `--gpu 2` 与 `CUDA_VISIBLE_DEVICES=2` 冲突（CUDA 重映射为 cuda:0），已修正为 `--gpu 0`

---
