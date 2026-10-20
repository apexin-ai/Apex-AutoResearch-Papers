# D102 k=1 RSFT Eval Commands

参照成功的 eval 实验（plan_006_qwen3_1_7b_rsft_eval_r2, plan_006_llama_rsft_r3_eval）格式。

**重要约束**：
- C001: 提交前必须 `nvidia-smi` 确认目标 GPU 显存 < 2GB
- C002: 必须设置 CUDA_VISIBLE_DEVICES

---

## 1. Qwen3-1.7B k=1 s42

- **exp_id**: `d102_1_7b_k1_eval`
- **GPU**: cuda:0 (CUDA_VISIBLE_DEVICES=0)
- **预计时间**: ~2.5h（参考 plan_006_qwen3_1_7b_rsft_eval_r2: 9464s）

```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1/checkpoint-567 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d102_1_7b_k1_eval"
```

---

## 2. Qwen3-8B k=1 s42

- **exp_id**: `d102_8b_k1_s42_eval`
- **GPU**: cuda:1 (CUDA_VISIBLE_DEVICES=1)
- **预计时间**: ~2.5h（参考 plan_006_llama_rsft_r3_eval: 8650s）

```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1/checkpoint-1134 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d102_8b_k1_s42_eval"
```

---

## 3. Qwen3-8B k=1 s43

- **exp_id**: `d102_8b_k1_s43_eval`
- **GPU**: cuda:2 (CUDA_VISIBLE_DEVICES=2)
- **预计时间**: ~2.5h

```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s43/checkpoint-1134 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d102_8b_k1_s43_eval"
```

---

## 4. LLaMA-3.1-8B k=1 s42

- **exp_id**: `d102_llama_k1_eval`
- **GPU**: cuda:3 (CUDA_VISIBLE_DEVICES=3)
- **预计时间**: ~2.5h

```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1/checkpoint-1107 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d102_llama_k1_eval"
```

---

## 总结

| # | exp_id | 模型 | Checkpoint | GPU | 预计时间 |
|---|--------|------|-----------|-----|---------|
| 1 | d102_1_7b_k1_eval | Qwen3-1.7B k1 s42 | checkpoint-567 | cuda:0 | ~2.5h |
| 2 | d102_8b_k1_s42_eval | Qwen3-8B k1 s42 | checkpoint-1134 | cuda:1 | ~2.5h |
| 3 | d102_8b_k1_s43_eval | Qwen3-8B k1 s43 | checkpoint-1134 | cuda:2 | ~2.5h |
| 4 | d102_llama_k1_eval | LLaMA-3.1-8B k1 s42 | checkpoint-1107 | cuda:3 | ~2.5h |

4 个 eval 可并行提交，各占一张 GPU。提交前先 `nvidia-smi` 确认 4 张卡均空闲。
