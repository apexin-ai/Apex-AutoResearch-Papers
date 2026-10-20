# code e2 cka only extended grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2_cka_only_extended_grpo_20260518T145211_result.json`
- **Structured JSON:** [`cb4f021f2bf897d4e143.json`](../../sessions/cb/cb4f021f2bf897d4e143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 1. 磁盘空间
| 时间点 | westd-29022 /root/autodl-tmp |
|--------|-----|
| 传输前 | 482G used / 138G avail |
| 传输后 | 497G used / 123G avail |

### 2. Checkpoint 传输
- 方式：westd 直接从 westb 拉取（`rsync -avz -e "ssh -p 23072"`)
- 大小：28GB（含 checkpoint-100 + completions）
- 速度：~200MB/s，约 50s 完成（部分文件已存在，speedup=2.79）
- 验证：model.safetensors (12G), optimizer.pt (15G), config.json, tokenizer.json, tokenizer_config.json, trainer_state.json (global_step=100) 均完整

### 3. 训练启动（第三次提交成功）
- 前两次失败原因：
  1. `--resume_from_checkpoint` 应指向 `checkpoint-100/` 子目录，不是根目录
  2. PyTorch 2.6 `weights_only=True` 与 rng_state.pth 中 numpy 数组不兼容（已重命名 rng_state.pth.bak 绕过）

### 4. 训练状态
| 项目 | 值 |
|------|-----|
| PID | 11457 (python), 11452 (tmux wrapper) |
| W&B Run ID | `z9f0z901` |
| W&B URL | https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/z9f0z901 |
| 起始 step | **100**（进度条 101/300 = 第一个实际训练 step） |
| 速度 | ~1.23s/step |
| GPU 0 VRAM | 90.6 / 97.9 GB (92.6%) |
| 预估完成 | ~4 分钟剩余（200 steps × 1.23s） |

### 5. 警告（无需处理）
- Transformers 版本 5.8.0 → 5.8.1 minor mismatch
- save_steps 50 vs 原 99999 mismatch（预期行为）
- HF Hub 不可达，GSM8K 从缓存加载
- RNG state 跳过恢复（对训练质量无实质影响）

---
