cd ../..

model="claude-3-7-sonnet-20250219"
domains=("university" "library")
method="fc"
tool_lists=("full")

# Experiment 1: full and oracle tool list
for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --user_model gpt-4.1-mini \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method
    done
done