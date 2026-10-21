# ssh 5090b 7b inference prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090b-7b-inference-prep_20260520T013437_result.json`
- **Structured JSON:** [`bbd72682076cc7fb981a.json`](../../sessions/bb/bbd72682076cc7fb981a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度较慢，但仍在进行中。先输出当前状态总结和 inference 命令模板，下载可在后台继续。

---

## 总结

### 1. 模型状态
- **Qwen2.5-7B-Instruct 不在 5090-b 上**，正在通过 HF CLI 下载到 `/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct/`
- 当前进度：~8.1GB/~15GB，PID=160848，后台运行中
- 监控命令：`tail -5 /tmp/download_qwen25_7b.log` 和 `du -sh /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct/`
- 磁盘空间充足：246GB 可用

### 2. 环境就绪情况
| 项目 | 状态 |
|------|------|
| torch | 2.10.0+cu128, CUDA=True, 4 GPU |
| vllm | 0.18.1 |
| transformers | 4.57.1 |
| peft | 0.17.1 |
| accelerate | 1.11.0 |
| bitsandbytes | 0.49.2 |
| datasets | 4.0.0 |
| llamafactory | **未安装**（merge 需在 5090-c 完成） |
| 数据集 | fewnerd, wnut17, conll2003, scierc 均在 |
| 推理脚本 | `code/run_mvp_pilot.py` 存在 |

### 3. Inference 启动命令模板

**Step A: 在 5090-c 上 merge adapter（训练完成后执行）**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/struct_self_consist_ie

# FewNERD merge
llamafactory-cli export export_config_qwen25_7b_fewnerd.yaml
# 产出: checkpoints/qwen25-7b-fewnerd-merged/
```

**Step B: 从 5090-c 拷贝 merged model 到 5090-b**
```bash
# 在 5090-b 上执行（需要 5090-c 的 SSH 连接信息）
rsync -avP root@<5090-c-ip>:/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged/ \
  /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged/

# 或者也可在 5090-c 上 scp 推过来
```

**Step C: 在 5090-b 上 3-seed N=8 inference（4 GPU tensor_parallel=4）**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/struct_self_consist_ie

for SEED in 42 123 456; do
  echo "=== Seed ${SEED} ==="
  CUDA_VISIBLE_DEVICES=0,1,2,3 python code/run_mvp_pilot.py \
    --model_path checkpoints/qwen25-7b-fewnerd-merged \
    --data_dir data/fewnerd \
    --dataset fewnerd \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed ${SEED} \
    --collect_logprobs \
    --num_test 9999 \
    --output_dir output/exp_7b_fewnerd_s${SEED} \
    --tensor_parallel 4
done
```

WNUT17 类似，替换 dataset/data_dir/model_path/output_dir：
```bash
for SEED in 42 123 456; do
  CUDA_VISIBLE_DEVICES=0,1,2,3 python code/run_mvp_pilot.py \
    --model_path checkpoints/qwen25-7b-wnut17-merged \
    --data_dir data/wnut17 \
    --dataset wnut17 \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed ${SEED} \
    --collect_logprobs \
    --num_test 9999 \
    --output_dir output/exp_7b_wnut17_s${SEED} \
    --tensor_parallel 4
done
```

### 4. 注意事项
- WNUT17 的 merged model 已在 5090-c 上存在（`checkpoints/qwen25-7b-wnut17-merged`），可直接 rsync
- FewNERD 还在训练中，训练完后需先 merge 再传
- `tensor_parallel=4` 利用 5090-b 全部 4 张 GPU，比 5090-c 的 2 卡快约 2 倍

---
