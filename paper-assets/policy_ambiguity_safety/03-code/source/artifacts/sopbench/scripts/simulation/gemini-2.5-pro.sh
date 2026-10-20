cd ../..

model="gemini-2.5-pro"
domains=("healthcare" "university" "dmv" "online_market" "bank" "hotel" "library")
tool_lists=("full")
method="fc"

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

# Experiment 2: Adversarial User Attack
method="fc"
domains=("healthcare")
for domain in "${domains[@]}"; do
    CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
            --domain $domain \
            --user_model adv \
            --assistant_model $model \
            --env_mode prompt \
            --tool_list $tool_list \
            --tool_call_mode $method
done