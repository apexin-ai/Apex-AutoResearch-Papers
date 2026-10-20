cd ../..

model="o4-mini-high"
domains=("university" "healthcare" "dmv" "library" "online_market" "bank" "hotel")
tool_lists=("full")
method="fc"

# Experiment 1: full and oracle tool list
for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
            --domain $domain \
            --assistant_model $model \
            --env_mode prompt \
            --tool_list $tool_list \
            --tool_call_mode $method \
            --assistant_max_tokens 4096
    done
done

# Experiment 2: Adversarial User Attack
method="fc"
domains=("healthcare")
tool_list="full"
for domain in "${domains[@]}"; do
    CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
            --domain $domain \
            --user_model adv \
            --assistant_model $model \
            --env_mode prompt \
            --tool_list $tool_list \
            --tool_call_mode $method \
            --assistant_max_tokens 4096
done