Experiment: w6_mistral_docred_constrained
Server: westd-21461, GPU: 1 (NVIDIA RTX PRO 6000 Black, 96GB)
PID: 8347
tmux session: w6_mistral_docred_constrained
xgrammar: 0.1.33
Status: Running, grammar compilation in progress (96 relations), no errors
Command: CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_constrained.jsonl --batch_size 1 --max_new_tokens 4096
Log: /tmp/w6_mistral_docred_constrained.log
Launched: 2026-05-16 13:36 UTC