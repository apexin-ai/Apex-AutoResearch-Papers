cd ../..

model="gpt-5"
domains=("bank" "healthcare" "university" "dmv" "online_market" "hotel" "library")
method="fc"

# Experiment 1: full and oracle tool list - Running domains in parallel
tool_lists=("full")
pids=()  # Array to store process IDs

echo "Starting parallel execution for ${#domains[@]} domains..."

for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        echo "Starting domain: $domain"
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method \
                --num_run_per_interaction 1 &
        pids+=($!)  # Store the process ID
    done
done

echo "All domains started. Waiting for completion..."
# Wait for all background processes to complete
for pid in "${pids[@]}"; do
    wait $pid
    echo "Process $pid completed"
done

echo "All domains completed!"
