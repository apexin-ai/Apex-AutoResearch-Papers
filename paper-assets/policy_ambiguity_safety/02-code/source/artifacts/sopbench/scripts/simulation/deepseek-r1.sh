cd ../..

model="deepseek-r1"
domains=("hotel" "university" "dmv" "healthcare" "library" "online_market" "bank")
method="react"
for domain in "${domains[@]}"; do
    CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
            --domain $domain \
            --assistant_model $model \
            --env_mode prompt \
            --tool_list full \
            --assistant_max_tokens 4096 \
            --tool_call_mode $method
done
