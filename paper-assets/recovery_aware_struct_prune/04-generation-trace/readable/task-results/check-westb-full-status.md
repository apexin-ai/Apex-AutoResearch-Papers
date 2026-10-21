# check westb full status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_full_status_20260520T091017_result.json`
- **Structured JSON:** [`a2bcc7bb703f1e2f33d2.json`](../../sessions/a2/a2bcc7bb703f1e2f33d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 两个 SFT 都失败了 — 数据盘 100% 满

| 项目 | 状态 | 详情 |
|------|------|------|
| **CKA-only SFT (cuda:0)** | **训练完成但保存失败** | 1870/1870 steps 跑完 (epoch 2.0)，final loss ~0.35，token_acc 0.905。但保存 checkpoint-1870 时磁盘满，`model.safetensors` 仅 40KB（损坏）。checkpoint-935（中间点）完好：model 12.3GB + optimizer 24.7GB |
| **Standard SFT (cuda:1)** | **训练中途崩溃** | 仅跑到 935/1870 (50%, epoch ~1.0)，loss 0.53。保存 checkpoint-935 时 optimizer.pt 写入失败（iostream error）。model.safetensors 12.3GB 可能完好 |
| **GSM8K eval** | **未跑** | 两个 SFT 都没成功保存最终模型 |
| **空闲 GPU** | cuda:0, cuda:1 | 均 0% 利用率，0 MiB 显存 |
| **数据盘** | **250G/250G = 100% 满** | 无剩余空间 |

### 磁盘占用大户（数据盘）

主要是历史实验 + 本次 checkpoint 中的 optimizer 状态文件：
- `sft_qwen_math_cka_only_20/checkpoint-935/optimizer.pt` = **24.7GB**
- `sft_standard_20_qwen_math/checkpoint-935/optimizer.pt` = **10.5GB**
- 旧 7B 模型目录 (`pruned_*`, `sft_*`, `grpo_*`)：各 ~12GB，共十几个

### 恢复方案建议

需要先清磁盘才能重跑。最快路径：
1. 删除两个 SFT 的 `checkpoint-935/optimizer.pt`（回收 ~35GB）——model weights 保留
2. 如果还不够，清理不再需要的旧实验目录
3. 训练时加 `save_only_model=True` 避免保存 optimizer（每个 checkpoint 省 10-25GB）

需要我执行清理并重启 SFT 吗？

---
