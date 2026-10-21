# code prep code qwen14b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-code-qwen14b_20260519T080334_result.json`
- **Structured JSON:** [`f48838286891374f0195.json`](../../sessions/f4/f48838286891374f0195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建。以下是调查结果：

## 报告

### 1. 14B 模型：**不可用（阻塞）**
- cqa1 上**没有 base Qwen2.5-14B** 缓存
- 仅有 `Qwen2.5-14B-Instruct-AWQ`（4-bit 量化 Instruct 版本，9.4GB），不适合 K* 测量
- exp_14b_c4 是在 `westd-42896` 上跑的，模型从未下载到 cqa1
- **需要先下载 base 模型**（~28GB），下载命令：
  ```bash
  HF_ENDPOINT=https://hf-mirror.com huggingface-cli download Qwen/Qwen2.5-14B \
    --local-dir /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B
  ```

### 2. 磁盘空间：充足
- `/root/autodl-tmp/` 总 250GB，已用 101GB，剩余 **150GB**（下载 28GB 模型没问题）

### 3. 显存：**单卡不够，双卡可行**
- 4x 4090D（24GB/卡）
- GPU 0、2 空闲；GPU 1、3 被占用
- 14B fp16 需 ~28GB，单卡 24GB 不够
- **方案**：`CUDA_VISIBLE_DEVICES=0,2` + `device_map="auto"` 跨双卡分片（48GB 总可用）
- bitsandbytes 未安装，无法走 int8 量化路径

### 4. Code seed data：可复用
- `data/exp_code_qwen1b5/depth_0.jsonl`（5500 行，CodeSearchNet Python）
- 脚本已设为 symlink 复用

### 5. 启动脚本已就绪
- `/root/autodl-tmp/gen-depth-contamination/scripts/run_code_qwen14b.sh`
- `generation_mode=continuation`（base model）
- `scorer_path=Qwen2.5-1.5B`
- `batch_size=4`（14B 双卡，保守设置避免 OOM）
- 脚本包含模型存在性检查，模型下载完成后即可启动

### 下一步
需要你确认是否**现在下载 base Qwen2.5-14B 模型**。下载约 28GB，取决于 hf-mirror 带宽。

---
