#!/bin/bash
set -e
cd /root/autodl-tmp/struct_self_consist_ie

CONLL_DIR=checkpoints/qwen3-8b-conll2003-merged
FEWNERD_DIR=checkpoints/qwen3-8b-fewnerd-exp021-merged
EXPECTED_SHARD_MIN_SIZE=3000000000

check_model_ready() {
    local dir=$1
    if ls "$dir"/.*safetensors* 2>/dev/null | grep -q .; then
        return 1
    fi
    for i in 1 2 3 4; do
        local f="$dir/model-0000${i}-of-00004.safetensors"
        if [ ! -f "$f" ]; then return 1; fi
        local size=$(stat -c%s "$f")
        if [ "$size" -lt "$EXPECTED_SHARD_MIN_SIZE" ]; then return 1; fi
    done
    return 0
}

echo "$(date): Waiting for CoNLL model..."
while ! check_model_ready "$CONLL_DIR"; do
    sleep 60
    echo "$(date): CoNLL not ready..."
done
echo "$(date): CoNLL model READY"

echo "$(date): Launching CoNLL s123 (cuda:2)"
tmux new-session -d -s exp_conll_mf4_s123 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_mf4_seed123/ 2>&1 | tee logs/exp_conll_mf4_s123.log"

echo "$(date): Launching CoNLL s456 (cuda:3)"
tmux new-session -d -s exp_conll_mf4_s456 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_mf4_seed456/ 2>&1 | tee logs/exp_conll_mf4_s456.log"

echo "$(date): Waiting for FewNERD model..."
while ! check_model_ready "$FEWNERD_DIR"; do
    sleep 60
    echo "$(date): FewNERD not ready..."
done
echo "$(date): FewNERD model READY"

echo "$(date): Launching FewNERD s42 (cuda:0)"
tmux new-session -d -s exp_fewnerd_mf4_s42 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4_seed42/ 2>&1 | tee logs/exp_fewnerd_mf4_s42.log"

echo "$(date): Launching FewNERD s123 (cuda:1)"
tmux new-session -d -s exp_fewnerd_mf4_s123 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4_seed123/ 2>&1 | tee logs/exp_fewnerd_mf4_s123.log"

# FewNERD s456 waits for CoNLL s123 to finish (cuda:2)
echo "$(date): Waiting for CoNLL s123 to finish (cuda:2 needed)..."
while tmux has-session -t exp_conll_mf4_s123 2>/dev/null; do
    sleep 30
done
echo "$(date): cuda:2 free. Launching FewNERD s456 (cuda:2)"
tmux new-session -d -s exp_fewnerd_mf4_s456 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_mf4_seed456/ 2>&1 | tee logs/exp_fewnerd_mf4_s456.log"

echo "$(date): ALL 5 EXPERIMENTS LAUNCHED"
