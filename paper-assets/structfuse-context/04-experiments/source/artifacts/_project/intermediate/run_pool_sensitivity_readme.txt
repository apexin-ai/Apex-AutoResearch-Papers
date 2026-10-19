#!/bin/bash
# Pool Sensitivity Analysis (plan_019)
# Location: /root/structfuse/scripts/run_pool_sensitivity.sh on bjb1-42106
#
# Usage:
#   # Default: pool={50,100,200,500}, strategies=all, seed=43, test set
#   DEVICE=cuda:1 bash scripts/run_pool_sensitivity.sh
#
#   # Quick dry-run (5 queries only)
#   DEVICE=cuda:1 MAX_QUERIES=5 bash scripts/run_pool_sensitivity.sh
#
#   # Single pool size
#   DEVICE=cuda:1 POOL_SIZES="100" bash scripts/run_pool_sensitivity.sh
#
#   # All seeds
#   DEVICE=cuda:1 SEEDS="42 43 44" bash scripts/run_pool_sensitivity.sh
#
# Environment variables:
#   DEVICE        - GPU device (default: cuda:0)
#   POOL_SIZES    - Space-separated pool sizes (default: "50 100 200 500")
#   STRATEGIES    - Space-separated strategies (default: "random embedding_distance dataflow_aware")
#   SEEDS         - Space-separated seeds (default: "43")
#   CKPT_TYPE     - Checkpoint type (default: "best_by_val_loss")
#   MAX_QUERIES   - Limit queries for dry-run (default: 0 = all)
#   EVAL_SUBSET   - "test" | "selection" | "full" (default: "test")
#
# Output: /root/autodl-tmp/structfuse/pool_sensitivity/pool{N}_{strategy}_s{seed}.json