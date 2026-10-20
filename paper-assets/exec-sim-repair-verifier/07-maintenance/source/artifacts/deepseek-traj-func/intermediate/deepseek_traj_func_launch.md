Experiment: deepseek-traj-func
Server: seetacloud-westd-4x5090, GPU: cuda:2 (RTX 5090 32GB)
PID: 504483
Started: 2026-05-16 20:07:12

Model: deepseek-ai/deepseek-coder-6.7b-instruct (LoRA r=16, alpha=32)
Task: cls (binary pass/fail)
Data: traj_train_cls.jsonl (8052 samples), traj_val_cls.jsonl (1001 samples)
  - 0% truncation
Hyperparams: epochs=3, bs=4, grad_accum=4, lr=2e-4, seed=42
Total steps: 1512, ~2s/step → ETA ~50min
Output: /root/autodl-tmp/checkpoints_deepseek_traj_func/
Log: /tmp/deepseek_traj_func.log