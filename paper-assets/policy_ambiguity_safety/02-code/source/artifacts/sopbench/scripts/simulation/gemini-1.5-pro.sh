cd ../..

model="gemini-1.5-pro"
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
                --tool_call_mode $method
    done
done