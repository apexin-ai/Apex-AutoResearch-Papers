# SciERC NER N=16 多种子实验准备状态报告

**日期**: 2026-05-15  
**服务器**: autodl-5090 (4× RTX 5090 32GB)

## 总结

| 项目 | 状态 | 说明 |
|------|------|------|
| 代码 | ✅ | `code/run_mvp_pilot.py` 支持 `--n_samples 16 --seed N --collect_logprobs` |
| 模型 | ✅ | Qwen3-8B-SciERC + LLaMA-3.1-8B-SciERC merged checkpoints 均存在 |
| 数据 | ✅ | `data/test.jsonl` = 551 instances |
| 依赖 | ✅ | vLLM 0.18.1 + xgrammar 0.1.33 |
| seed42 N=16 | ✅ 已完成 | `output/exp001_n16_seed42/` (551 instances) |
| seed123 N=16 | ✅ 已完成 | `output/exp001_n16_seed123/` (551 instances) |
| seed456 N=16 | ❌ 缺失 | `output/exp001_n16_seed456/` 为空，仅有 `_200only` (200 instances) |

**结论: 只需运行 seed456 的 full N=16 实验。seed42 和 seed123 均已完成。**

## 代码

- **推理脚本**: `/root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py`
- 关键参数: `--n_samples` (default 8), `--seed` (default 42), `--temperature` (default 1.0), `--collect_logprobs`, `--subtask joint`
- 辅助模块: `code/sampling.py` (VLLMSampler + XGrammar 约束解码), `code/consistency.py`, `code/evaluation.py`, `code/data_utils.py`

## 模型

| 模型 | 路径 | 状态 |
|------|------|------|
| Qwen3-8B-SciERC (v2) | `checkpoints/qwen3-8b-scierc-merged-v2` | ✅ |
| LLaMA-3.1-8B-SciERC | `checkpoints/llama3.1-8b-scierc-merged` | ✅ |
| Qwen3-8B-ConLL2003 | `checkpoints/qwen3-8b-conll2003-merged` | ✅ |
| LLaMA-3.1-8B-ConLL2003 | `checkpoints/llama3.1-8b-conll2003-merged` | ✅ |

## 数据

- **SciERC 测试集**: `data/test.jsonl` — **551 instances** ✅
- 另有 `data/scierc/processed_data/test.json` (100 行，不同格式，非推理用)

## 已有 N=16 结果详情

### seed42 (output/exp001_n16_seed42/)
- 模型: qwen3-8b-scierc-merged-v2
- subtask: joint, n_samples=16, temperature=1.0
- 551 instances, 含 logprobs
- NER greedy F1: 0.659, NER oracle F1: 0.804, NER ρ(SJ,F1) cond: 0.416
- 运行时间: ~8 min (20:15 → 20:24, May 14)

### seed123 (output/exp001_n16_seed123/)
- 同配置, seed=123
- 551 instances, 含 logprobs
- NER greedy F1: 0.663, NER oracle F1: 0.809, NER ρ(SJ,F1) cond: 0.420
- 注: `exp001_n16_seed123_full` 是旧服务器上被 kill 的尝试（空目录），`exp001_n16_seed123` 是成功的运行

### seed456 — 缺失
- `output/exp001_n16_seed456/` — 空目录
- `output/exp001_n16_seed456_200only/` — 仅 200 instances (partial)

## 依赖

| 包 | 版本 | 状态 |
|----|------|------|
| vLLM | 0.18.1 | ✅ |
| xgrammar | 0.1.33 | ✅ |
| PyTorch | (conda base) | ✅ |
| transformers | (已安装) | ✅ |

## 预计运行命令

**seed456 (唯一需要运行的)**:
```bash
cd /root/autodl-tmp/struct_self_consist_ie && \
python code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-scierc-merged-v2 \
  --data_dir data/ \
  --dataset scierc \
  --subtask joint \
  --n_samples 16 \
  --temperature 1.0 \
  --seed 456 \
  --output_dir output/exp001_n16_seed456 \
  --collect_logprobs \
  2>&1 | tee output/exp001_n16_seed456_run.log
```

## 预计运行时间

- 单次 N=16 推理 (551 instances): **~8-9 分钟** (基于 seed42 实测)
- 仅需运行 1 次 (seed456)

## 缺失项

| 缺失项 | 修复方案 |
|--------|---------|
| seed456 full N=16 结果 | 运行上述命令 |
| (无其他缺失) | — |
