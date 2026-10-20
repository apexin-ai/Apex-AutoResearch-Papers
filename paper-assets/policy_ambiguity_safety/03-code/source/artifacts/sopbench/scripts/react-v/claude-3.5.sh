cd ../..

model="claude-3-5-sonnet-20241022"
domains=("bank")
method="react-v"
tool_lists=("full")

# Experiment 1: full and oracle tool list
for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method
    done
done