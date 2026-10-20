# 诊断报告: generalize_pythia1b_c4_a100_s42

## 失败直接原因

**模型下载中断** (`requests.exceptions.ChunkedEncodingError`)

从 hf-mirror.com 下载 `EleutherAI/pythia-1b` 权重文件时，连接在传输过程中断开：
- 已下载: 138.8 MB (145,523,872 bytes)
- 剩余未下载: 1.85 GB (1,945,177,656 bytes)
- 模型总大小约 2.0 GB，仅完成 ~7%

Traceback 链路:
```
hf_hub_download → http_get → r.iter_content → ChunkedEncodingError
  ← ProtocolError ← IncompleteRead(145523872 bytes read, 1945177656 more expected)
```

## 失败阶段

**Generation 0 启动前**, 模型加载阶段 (`AutoModelForCausalLM.from_pretrained`)。训练尚未开始，没有任何 step 执行。

## 部分结果

输出目录 `results/generalize/pythia1b_c4_a100_s42/` 仅包含:
- `config.json` (实验配置)
- `EXIT_CODE` (退出码记录)

**无任何可利用的训练结果**（无 checkpoint、无 metrics、无 generation 产出）。

HF cache 中存在一个 `.incomplete` 文件 (130 MB)，需清理后重试。

## 磁盘和 GPU 状态

| 指标 | 状态 |
|------|------|
| 磁盘 /root/autodl-tmp | 169G/250G used (82G free, 68%) |
| GPU 0 (RTX PRO 6000) | 空闲, 0 MiB, 29C |
| GPU 1 (RTX PRO 6000) | 被其他进程 (PID 249384) 占用, 27217 MiB, 66C, 96% util |

磁盘空间充足，不是失败原因。GPU 0 可用。

## C4 数据

`data/c4_5k/` 目录结构完整 (train/eval/prompts 三个子目录，含 arrow 文件)，数据不是问题。

## 修复建议

1. **清理不完整的缓存文件**:
   ```bash
   rm /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1b/blobs/*.incomplete
   ```

2. **预下载模型** (独立于训练，带重试):
   ```bash
   cd /root/autodl-tmp/distrib_canary_collapse && \
   export HF_HOME=/root/autodl-tmp/.hf_cache && \
   export HF_HUB_DISABLE_XET=1 && \
   export HF_ENDPOINT=https://hf-mirror.com && \
   python -c "
   from huggingface_hub import snapshot_download
   snapshot_download('EleutherAI/pythia-1b', resume_download=True)
   "
   ```
   如果 hf-mirror.com 不稳定，可尝试去掉 `HF_ENDPOINT` 直接走官方源。

3. **确认下载完整后重新提交训练**:
   ```bash
   python -c "from transformers import AutoModelForCausalLM; m = AutoModelForCausalLM.from_pretrained('EleutherAI/pythia-1b'); print('OK', sum(p.numel() for p in m.parameters()))"
   ```

4. **指定 GPU 0** (GPU 1 当前被占用):
   ```bash
   CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py ...
   ```
