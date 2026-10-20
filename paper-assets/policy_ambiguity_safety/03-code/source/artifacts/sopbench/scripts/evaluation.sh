cd ..

models=(
        # "gpt-5"
        # "gpt-5-mini"
        # "gpt-4.1" 
        # "gpt-4o"
        # "gpt-4o-mini" 
        # "claude-3-7-sonnet-20250219" 
        # "claude-3-5-sonnet-20241022" 
        # "gemini-2.0-flash-001" 
        # "gemini-2.5-flash"
        # "gemini-2.0-flash-thinking-exp" 
        "o4-mini-high"
        # "deepseek-r1"
        # "llama3.1-70b-instruct" 
        # "qwen2.5-72b-instruct" 
        # "llama3.1-8b-instruct"
        # "qwen2.5-32b-instruct"
        # "qwen2.5-14b-instruct"
        # "qwen2.5-7b-instruct"
        )
domains=(
    # "healthcare" 
    # "dmv" 
    # "library"
    # "online_market" 
    # "bank"
    # "hotel"
    # "university"
    "all"
    )
tool_lists=(
    "full" 
    # "oracle"
    )
tool_call_modes=(
    "fc" 
    # "react" 
    # "act-only"
    )

# Default settings
for model in "${models[@]}"; do
    for domain in "${domains[@]}"; do
        for tool_list in "${tool_lists[@]}"; do
            for tool_call_mode in "${tool_call_modes[@]}"; do
                CUDA_VISIBLE_DEVICES=$devices python run_evaluation.py \
                    --domain $domain \
                    --assistant_model $model \
                    --tool_list $tool_list \
                    --tool_call_mode $tool_call_mode
            done
        done
    done
done
