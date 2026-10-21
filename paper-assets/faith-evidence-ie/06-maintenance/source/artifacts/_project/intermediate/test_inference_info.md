# Plan_002: Test Set Inference Script

## 部署位置
`/root/autodl-tmp/freige/eval/test_inference.py`

## 运行命令 (from /root/autodl-tmp/)
```bash
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_s43 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/test_rsft_s43 \
  --no-quantize --batch_size 16 --max_new_tokens 1024
```

## 输出
- predictions.json: 1000 docs 预测结果
- codalab_submission.json: CodaLab 提交格式
- test_summary.json: 统计摘要
