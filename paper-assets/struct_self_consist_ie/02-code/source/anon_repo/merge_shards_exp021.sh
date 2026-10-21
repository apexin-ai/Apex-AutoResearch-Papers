#!/bin/bash
# Merge 4 shard JSONL files into one, then run evaluation
BASE="output/exp_021_inference"
MERGED="${BASE}/sampled_results.jsonl"

cd /root/autodl-tmp/struct_self_consist_ie

echo "Merging shards..."
cat ${BASE}/shard_0/sampled_results.jsonl \
    ${BASE}/shard_1/sampled_results.jsonl \
    ${BASE}/shard_2/sampled_results.jsonl \
    ${BASE}/shard_3/sampled_results.jsonl \
    > $MERGED

echo "Merged $(wc -l < $MERGED) instances -> $MERGED"
echo ""
echo "Run evaluation with:"
echo "  python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd --dataset fewnerd --subtask ner --skip_sampling --samples_path $MERGED --output_dir ${BASE}"
