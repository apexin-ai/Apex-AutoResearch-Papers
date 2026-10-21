cd ../..
devices="0"

model="claude-3-7-sonnet-20250219-thinking"
domains=("hotel" "university" "dmv" "healthcare" "library" "online_market" "bank")
method="fc"

# Experiment 1: full and oracle tool list
tool_lists=("full" "oracle")
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

# Experiment 2: Full and Env Tool List on Five Domains with React
methods=("react" "act-only")
tool_list="full"
for domain in "${domains[@]}"; do
    for method in "${methods[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method
    done
done

# Experiment 3: Adversarial User Attack
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
            --tool_call_mode $method
done