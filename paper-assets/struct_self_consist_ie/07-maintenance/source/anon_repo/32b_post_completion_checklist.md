# Qwen2.5-32B FewNERD: Post-Training Checklist

## 状态
- 训练配置: train_config_qwen25_32b_fewnerd_s42.yaml
- 输出目录: checkpoints/qwen25-32b-fewnerd-qlora-s42/
- 基座模型: /root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-32B-Instruct/snapshots/5ede1c97bbab6ce5cda5812749b4c0bdf79b18dd/

## ⚠️ 磁盘空间警告
当前 /root/autodl-tmp/ 仅剩 ~79GB，merged 32B 模型需要 ~62GB。
执行 export 前必须先清理空间（建议至少释放 20GB）：
```bash
# 可清理项（按优先级）:
du -sh checkpoints/qwen3-8b-wnut17-lora/        # 5.3G - 如果不再需要
du -sh checkpoints/qwen3-4b-conll2003-lora/      # 4.1G
du -sh checkpoints/qwen3-8b-scierc-lora-v2/      # 3.4G
du -sh checkpoints/llama3.1-8b-scierc-lora/      # 3.2G
du -sh checkpoints/llama3.1-8b-fewnerd-lora/     # 3.2G
du -sh checkpoints/ft_fewnerd_smoke/             # 1.7G
# 总计可回收 ~21GB
```

## Step 1: Export (LoRA Merge)

```bash
cd /root/autodl-tmp/struct_self_consist_ie

# 验证训练完成 & best model adapter 已保存
ls checkpoints/qwen25-32b-fewnerd-qlora-s42/adapter_model.safetensors

# 执行 merge
llamafactory-cli export export_config_qwen25_32b_fewnerd.yaml
```
预计耗时: ~15-20 min（加载 32B 全精度 base + merge + 写 62GB）

## Step 2: 验证 Merged Model

```bash
python -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
t = AutoTokenizer.from_pretrained('checkpoints/qwen25-32b-fewnerd-merged')
m = AutoModelForCausalLM.from_pretrained('checkpoints/qwen25-32b-fewnerd-merged', torch_dtype=torch.bfloat16, device_map='auto')
print(f'OK: {sum(p.numel() for p in m.parameters())/1e9:.1f}B params')
"
```

## Step 3: 3-Seed Inference (TP=2, 两轮)

32B bf16 需要 ~64GB VRAM → tensor_parallel=2 (2x RTX 5090)。
4 张卡可同时跑 2 个 seed。

### 第一轮 (2 seeds 并行)
```bash
cd /root/autodl-tmp/struct_self_consist_ie

# Terminal 1: seed=42, GPU 0,1
nohup bash run_32b_fewnerd_inference.sh 42 0,1 2 > logs/32b_fewnerd_seed42.log 2>&1 &
echo "seed42 pid=$!"

# Terminal 2: seed=123, GPU 2,3
nohup bash run_32b_fewnerd_inference.sh 123 2,3 2 > logs/32b_fewnerd_seed123.log 2>&1 &
echo "seed123 pid=$!"
```

### 第二轮 (等第一轮任一完成)
```bash
# seed=456, 用空出的 GPU pair
nohup bash run_32b_fewnerd_inference.sh 456 0,1 2 > logs/32b_fewnerd_seed456.log 2>&1 &
echo "seed456 pid=$!"
```

## Step 4: 监控

```bash
# 实时查看
tail -f logs/32b_fewnerd_seed{42,123,456}.log

# 检查进程
ps aux | grep run_mvp_pilot | grep -v grep
```

## Step 5: 结果验证

```bash
for seed in 42 123 456; do
    echo "=== seed=$seed ==="
    ls output/qwen25_32b_fewnerd_n8_seed${seed}/
    python -c "
import json
with open('output/qwen25_32b_fewnerd_n8_seed${seed}/metrics.json') as f:
    m = json.load(f)
    print(f'  F1={m.get(\"f1\", \"N/A\")}, P={m.get(\"precision\", \"N/A\")}, R={m.get(\"recall\", \"N/A\")}')
" 2>/dev/null || echo "  metrics not found yet"
done
```

## 时间估算
| 步骤 | 预计耗时 |
|------|---------|
| Export (merge) | ~15-20 min |
| 验证 merged model | ~5 min |
| Inference per seed (N=8, TP=2) | ~2-4 hours (外推自 8B 约 1h, 32B 约 3-4x) |
| 第一轮 (2 seeds 并行) | ~2-4 hours |
| 第二轮 (1 seed) | ~2-4 hours |
| **总计 (export 后)** | **~4.5-8.5 hours** |
