#!/bin/bash
cd ..

# Default values
# assistant_model="claude-3-7-sonnet-20250219"
# assistant_model="gemini-2.0-flash-thinking-exp"
assistant_model="gpt-4.1-mini"
# assistant_model="gpt-4o"
# assistant_model="o4-mini-high"

output_dir="./output"
domain="university"
tool_call_mode="fc" # react
tool_list="full"

python run_checking.py \
  --output_dir $output_dir \
  --domain $domain \
  --user_model gpt-4.1-mini \
  --assistant_model $assistant_model \
  --tool_call_mode $tool_call_mode \
  --default_constraint_option "full" \
  --constraint_descr_format "structured" \
  --tool_list $tool_list