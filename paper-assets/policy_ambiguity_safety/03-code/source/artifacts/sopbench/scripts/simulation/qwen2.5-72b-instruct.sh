cd ../..

devices="0,1,2,3,4,5,6,7"

model="qwen2.5-72b-instruct"
domains=("dmv" "healthcare" "library" "online_market" "bank" "hotel" "university")
tool_lists=("full" "oracle")
method="react"

# Experiment 1: full and oracle tool list
for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method \
                --num_gpus 8 \
                --gpu_memory_utilization 0.9
    done
done

# Experiment 2: Adversarial User Attack
methods=("react")
tool_list="full"
for domain in "${domains[@]}"; do
    for method in "${methods[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --user_model adv \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method \
                --num_gpus 8 \
                --gpu_memory_utilization 0.9
    done
done