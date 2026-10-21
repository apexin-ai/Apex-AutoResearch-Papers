cd ..
devices="0"

model="gpt-4o-mini"
domains=("dmv" "healthcare" "library" "online_market" "bank" "hotel" "university")
tool_lists=("full" "oracle")
method="react"

# The interact mode with human input
for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method \
                --user_model human \
                --print_conv
    done
done
