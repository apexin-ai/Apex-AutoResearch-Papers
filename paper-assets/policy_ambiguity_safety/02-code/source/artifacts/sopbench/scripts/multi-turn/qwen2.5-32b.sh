cd ../..

devices="4,5,6,7"

models=("qwen2.5-32b-instruct")
domains=("university" "library")
method="react"

# Experiment 1: full and oracle tool list
for domain in "${domains[@]}"; do
    for model in "${models[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --user_model gpt-4.1-mini \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list full \
                --tool_call_mode $method \
                --num_gpus 4 \
                --gpu_memory_utilization 0.75
    done
done