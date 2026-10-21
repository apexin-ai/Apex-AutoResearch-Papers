# K=16 Eval 连续失败诊断报告

**日期**: 2026-05-23
**服务器**: westd-34887
**Checkpoint**: `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s42_v3/predictor_perlayer_kl_k4.pt` (确认存在，151MB)

---

## 失败 1: perlayer_kl_k16_s42_v3_eval (EXIT_CODE=1)

**根因**: 网络不可达

服务器无法直连 HuggingFace Hub，lm_eval 尝试下载 `allenai/ai2_arc` 时报错：
```
[Errno 101] Network is unreachable
RuntimeError: Cannot send a request, as the client has been closed.
```

PPL=8.6737 采集成功（WikiText-2 数据已本地缓存），但 downstream tasks 需要从 Hub 下载数据集。
未设置 offline 模式环境变量，也未执行 `source /etc/network_turbo`。

## 失败 2: perlayer_kl_k16_eval_v2 (EXIT_CODE=1)

**根因**: `HF_DATASETS_OFFLINE=1` 已设置，但 `HF_HOME` 未设置

数据集缓存在 `/root/autodl-tmp/.hf_cache/datasets/`，但 lm_eval 在默认路径 `~/.cache/huggingface/` 查找，找不到后报错：
```
ConnectionError: Couldn't reach 'allenai/ai2_arc' on the Hub (OfflineModeIsEnabled)
```

所有 6 个 downstream 数据集其实都已缓存在 `/root/autodl-tmp/.hf_cache/datasets/`（ai2_arc, winogrande, hellaswag, gsm8k, mmlu, piqa），但因 HF_HOME 缺失而不可见。

## 失败 3: perlayer_kl_k16_s42_eval_final (EXIT_CODE=127)

**根因**: `python: command not found`

nohup 启动的 shell 不继承 conda 环境，PATH 为：
```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```
不包含 `/root/miniconda3/bin/`。脚本使用裸 `python` 调用，导致 command not found。

日志全部内容仅两行：
```
bash: line 1: python: command not found
EXIT_CODE=127
```

## 当前状态: eval_final2 正在运行 ✅

**PID**: 114997（启动于 13:17）
**GPU**: cuda:0，48GB/97GB 已用

第 4 次尝试修复了全部三个问题：
1. ✅ `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` — python 可用
2. ✅ `HF_HOME=/root/autodl-tmp/.hf_cache` — 数据集缓存路径正确
3. ✅ `HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1` — 完全离线模式

日志显示已成功加载缓存数据集，正在处理 arc_challenge loglikelihood 请求（~32% 进度）。
预计 30-60 分钟完成全部 6 个 downstream tasks。

完整命令：
```bash
cd /root/distill_sparse_swiglu && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled \
HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
HF_HOME=/root/autodl-tmp/.hf_cache \
nohup python -u src/benchmark_eval.py \
  --exp_id perlayer_kl_k16_eval_final2 \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --checkpoint /root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s42_v3/predictor_perlayer_kl_k4.pt \
  --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform \
  --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa \
  --seq_len 2048 --gpu 0 \
  > /root/runs/distill_sparse_swiglu/perlayer_kl_k16_eval_final2.log 2>&1 &
```

---

## 根因总结

三次失败的共同主题：**nohup 环境隔离**。nohup 不继承交互式 shell 的 conda 环境和自定义环境变量。每次启动 eval 时必须显式：
1. Source conda 并 activate
2. 设置 `HF_HOME` 指向数据盘缓存
3. 设置 offline 模式（服务器无外网）

## K=8 Eval 对比

K=8 eval 日志不在 `~/runs/distill_sparse_swiglu/` 中（`find` 未找到任何 k8 相关日志文件），无法直接对比命令结构。K=8 eval 可能通过不同方式执行（直接在交互式 shell 中运行，或日志存于其他位置）。
