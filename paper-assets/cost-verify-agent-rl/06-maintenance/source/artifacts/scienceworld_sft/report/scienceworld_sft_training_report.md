# ScienceWorld SFT Training Report

## 概览
- **服务器**: westd-47453 (4× RTX PRO 6000 Blackwell 96GB)
- **模型**: Qwen3-1.7B (从 ModelScope 下载)
- **数据**: 3592 train / 1796 val (多轮对话, messages 格式)
- **W&B Run**: `dqoxg94e` (scienceworld-sft-qwen3-1.7b)

## 数据格式
- JSONL → Parquet 转换 (添加 `enable_thinking=False` 列)
- 每条数据包含 system/user/assistant 多轮对话，含 `<think>...</think><answer>...</answer>` 格式
- Token 长度统计 (前100条): min=2625, median=8752, P95=18031, max=32464
- 58% 样本 > 8192 tokens, 7% > 16384 tokens
- 设置 max_length=16384 + left truncation 覆盖 93% 样本

## 关键配置
| 参数 | 值 |
|------|------|
| model | Qwen3-1.7B (Qwen/Qwen3-1.7B) |
| strategy | FSDP2 (4 GPUs) |
| attn_implementation | sdpa (修改了硬编码的 flash_attention_2) |
| LR | 5e-6 (cosine, 5% warmup) |
| Epochs | 2 |
| Batch size | 16 (global), 4 per GPU, micro=1, grad_accum=4 |
| max_length | 16384 |
| truncation | left |
| Steps/epoch | 224 |
| Total steps | 448 |
| Save freq | 112 (每半 epoch) |
| Checkpoint contents | model + optimizer + extra + hf_model |

## 代码修改
- `verl/verl/trainer/fsdp_sft_trainer.py` line 237: 将硬编码的 `attn_implementation="flash_attention_2"` 改为可配置 `self.config.model.get("attn_implementation", "sdpa")`，解决 Blackwell GPU 不兼容 flash attention 的问题

## Dry-run 结果
- 模型加载成功 (sdpa attention)
- 数据集处理正常 (token mismatch warnings 是预期行为)
- GPU 显存: ~47GB/96GB per GPU
- 无 OOM，训练正常启动

## 训练进度
- 19-21 秒/step
- 初始 loss: 0.595-0.838 (warmup 阶段)
- 预计完成时间: ~2.4 小时

## 产出路径
- Checkpoint: `/root/autodl-tmp/checkpoints/scienceworld_sft/`
- Log: `/root/autodl-tmp/scienceworld_sft.log`
- 启动脚本: `/root/cost-verify-agent-rl/RAGEN/scripts/run_scienceworld_sft.sh`
