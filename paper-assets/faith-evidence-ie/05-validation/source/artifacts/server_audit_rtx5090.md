# rtx5090-4x 服务器审计报告

**时间**: 2026-05-24 04:11 UTC (北京时间 12:11)

## GPU 状态

| GPU | 型号 | 显存 | 已用 | 利用率 |
|-----|------|------|------|--------|
| 0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 96 GB | 32 GB | 85% |
| 1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 96 GB | 0 | 0% |
| 2 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 96 GB | 0 | 0% |
| 3 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 96 GB | 0 | 0% |

**GPU 进程**: PID 260785 占用 GPU 0 (32 GB)，运行 `plan017_14b_rsft_s43_eval`

## 14B Dev Eval 状态

- **任务**: plan017_14b_rsft_s43_eval
- **模型**: Qwen3-14B + sft_output_14b_s43 + rsft_output_14b_s43
- **进度**: 909/985 (92%)，已运行 ~5h15m
- **预计剩余**: ~1h
- **参数**: `--split dev --batch_size 1 --no-quantize --seed 43 --CUDA_VISIBLE_DEVICES=0`

## 磁盘使用

总容量 350G，已用 286G (82%)，剩余 65G。

| 目录 | 大小 | 说明 |
|------|------|------|
| models/ | 97G | 基座模型（Qwen3-14B 等） |
| sft_output_14b/ | 7.3G | 14B SFT checkpoint |
| dpo_output_rebuilt_3ep/ | 7.0G | DPO 3-epoch checkpoint |
| rsft_output_14b/ | 6.8G | 14B RSFT checkpoint |
| .hf_cache/ | 2.4G | HF 缓存 |
| freige/ | 1.2G | 项目代码 |
| data/ | 993M | 数据集 (DocRED) |
| eval_results/ | 884M | 评估结果 |
| 其他 sft/rsft output | ~150G+ | 大量历史 checkpoint（1.7B/4B/8B/14B 多 seed 多变体） |

磁盘最大消耗来自 models/ (97G) 和大量历史 checkpoint。

## 总结

- GPU 0 正在跑 14B RSFT s43 dev eval，预计 ~1h 完成；GPU 1-3 空闲
- 磁盘 82% 已用，如需更多空间可清理历史 checkpoint（1.7B/8B 的多 seed 变体）
- eval 完成后 4 张卡全部空闲，可用于后续任务
