cd ../..

devices="2,3,4,5"

models=("qwen2.5-14b-instruct")
domains=("bank")
method="react-v"

# Experiment 1: full and oracle tool list
for domain in "${domains[@]}"; do
    for model in "${models[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list full \
                --tool_call_mode $method \
                --num_gpus 4 \
                --gpu_memory_utilization 0.8
    done
done