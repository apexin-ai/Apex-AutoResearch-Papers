# setup pi05 libero checkpoint

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_pi05_libero_checkpoint_20260516T093550_result.json`
- **Structured JSON:** [`68cf19387633b7092adb.json`](../../sessions/68/68cf19387633b7092adb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 执行结果汇报

### 1. Kill 结果 ✓
所有 `evaluate_libero` 进程已终止。GPU 0-3 全部空闲。

### 2. 下载状态：进行中，受网络限制

**文件**：`lerobot/pi0_libero` (HuggingFace) → 6.5GB (bfloat16 safetensors)
**当前进度**：49MB / 6.5GB (0.7%)
**速度**：~250KB/s（XET CDN 从中国访问极慢）
**预估 ETA**：7+ 小时

已配置弹性下载脚本（PID 637757，100次重试 + wget -c 断点续传）和 watchdog（PID 637861，下载完成后自动启动 eval）。

**尝试过的下载路径**：
| 方案 | 结果 |
|------|------|
| hf-mirror.com → xethub CDN | ~100-250KB/s（当前使用） |
| ModelScope 国内CDN | ~350KB/s（但 no_proxy 导致直连极慢） |
| GCS gsutil | 大文件超时 |
| GCS HTTP API | 元数据可访问，数据流超时 |

### 3. 关键架构发现

**`pi05_libero` 与 MetaBrain 不兼容**：
- pi05 是 pi0.5 架构（`pi05=True`，含 adarms 模块，`max_token_len=200`）
- MetaBrain 用 `Pi0Config(pi05=False)`（pi0 架构，`max_token_len=48`）
- 权重 key 不匹配，无法强行加载

**`pi0_libero`（`lerobot/pi0_libero`）兼容**：
- 同为 pi0 架构（gemma_2b + gemma_300m, tokenizer_max_length=48）
- config.json 与 pi0_base 一致（仅 n_action_steps 不同：10 vs 50，不影响架构）
- bf16 safetensors 可直接加载到 MetaBrain（`Pi0Config(dtype="bfloat16")`）

### 4. 代码修改
- **evaluate_libero_plus.py line 554**: 修复 `from_dummy()` 调用，传入 `pi0_checkpoint=args.pi0_checkpoint`（原来硬编码 pi0_base）
- **run_nominal_eval.sh**: 创建 eval 脚本，用 `--perturbation_types nominal --routing none`

### 5. Nominal eval 准备就绪
一旦下载完成，watchdog 会自动执行：
```bash
CUDA_VISIBLE_DEVICES=0 python phase1/evaluate_libero_plus.py \
    --pi0_checkpoint /root/autodl-tmp/checkpoints/pi0_libero \
    --routing none --perturbation_types nominal \
    --num_episodes 5 --seeds 42 --no_wandb --gpu 0
```

### 6. 后续检查方式
```bash
# 查下载进度
ls -la /root/autodl-tmp/checkpoints/pi0_libero/model.safetensors | awk '{printf "%.0f MB / 6691 MB\n", $5/1024/1024}'

# 查 eval 结果
cat /tmp/watchdog_eval.log
```

**总结**：下载是唯一瓶颈。网络条件限制了从 XET CDN 的速度。如果有其他方式获取 `lerobot/pi0_libero` 的 model.safetensors（例如从其他机器 scp），可以大幅加速。

---
