# OpenVLA Eval Pipeline 修复报告

## 根因
transformers 5.8 的 `prepare_inputs_for_generation` 将空 DynamicCache 误判为非空，截断 input_ids，导致图像 token 丢失。OpenVLA 的 custom generate() 依赖旧版 transformers 行为。

## 修复方案
使用 OpenVLA 官方 repo 的 eval 代码 + 独立 conda env (transformers 4.40.1)，绕过兼容性问题。

## 环境 (bjb1-18228)
- Conda env: `/root/autodl-tmp/conda_envs/openvla` (Python 3.10, PyTorch 2.2.0+cu121, transformers 4.40.1)
- 官方 repo: `/root/autodl-tmp/openvla` (克隆自 openvla/openvla)
- LIBERO assets: `/root/.cache/libero/assets/`
- 额外修复: 删除手动 OpenVLAConfig 注册、config.json auto_map 修正、numpy 2.x 兼容

## Dry-run 验证
- Benchmark: libero_spatial, 1 episode/task, 5 tasks
- 结果: 4/5 = 80% SR
- 模型: openvla-libero-spatial (finetuned)
- GPU 占用: ~15-19 GB VRAM

## 全量 Eval 命令
```bash
cd /root/autodl-tmp/openvla && \
CUDA_VISIBLE_DEVICES=<GPU> HF_ENDPOINT=https://hf-mirror.com TOKENIZERS_PARALLELISM=false \
/root/autodl-tmp/conda_envs/openvla/bin/python experiments/robot/libero/run_libero_eval.py \
    --model_family openvla \
    --pretrained_checkpoint <MODEL_PATH> \
    --task_suite_name <libero_object|libero_spatial> \
    --center_crop True \
    --num_trials_per_task 50 \
    --seed 42
```

## 待确认
1. 需要 openvla-libero-object finetuned 模型（或用 base openvla-7b）
2. 每次 50-trial eval 预计 8-12h（7B 模型）
3. GPU 释放后部署