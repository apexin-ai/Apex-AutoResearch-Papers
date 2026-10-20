Experiment: exp-004 MAVEN BCS Study
Server: cqa1-38874
tmux: exp004_maven_bcs
PID: 224685
Started: 2026-05-15 14:03:36

Command (exp1):
python3 src/run_experiment.py --dataset maven --mode exp1 --prompt_version v2 --eval_mode text_match --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 500 --embeddings_path artifacts/maven_type_embeddings_qwen3.pt --sim_matrix_path artifacts/maven_bcs_matrix_qwen3.pt --types_file configs/maven_event_types.json --output_dir artifacts/exp004

Command (exp2):
python3 src/run_experiment.py --dataset maven --mode exp2 --prompt_version v2 --eval_mode text_match --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 500 --embeddings_path artifacts/maven_type_embeddings_qwen3.pt --sim_matrix_path artifacts/maven_bcs_matrix_qwen3.pt --types_file configs/maven_event_types.json --output_dir artifacts/exp004

Code change: run_experiment.py - added dataset-specific count levels for MAVEN (exp1: [1,6,12,24,42,84,168], exp2: [12,24]) vs Few-NERD (exp1: [1,2,6,12,22,44,66], exp2: [6,12])

Active types: 149/168 (19 types not present in 500-sample subset)