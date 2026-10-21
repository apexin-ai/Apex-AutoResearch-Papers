# n=5 Expansion Launch Commands — 4 experiments on westd-34685
# Seed 46 for all 4 cells of 2×2 factorial (gradient_flow × norm_type)
# Launch after 34685 eval batch completes (~23:15 UTC)

## mvp_occ_s4 → cuda:0 (Cell 1: Grad ON + BN, seed=46)
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --run_root_dir /root/autodl-tmp/checkpoints/mvp_occ_s4 --seed 46 --run_id_note mvp_occ_s4"
```

## full_occ_ln_s4 → cuda:1 (Cell 2: Grad ON + LN, seed=46)
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_s4 --seed 46 --run_id_note full_occ_ln_s4"
```

## ablation_occ_detach_s4 → cuda:2 (Cell 3: Grad OFF + BN, seed=46)
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --run_root_dir /root/autodl-tmp/checkpoints/ablation_occ_detach_s4 --seed 46 --run_id_note ablation_occ_detach_s4"
```

## detach_ln_s4 → cuda:3 (Cell 4: Grad OFF + LN, seed=46)
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_s4 --seed 46 --run_id_note detach_ln_s4"
```

## GPU 分配
| cuda | exp_id | Cell | occ_detach | occ_norm_type |
|------|--------|------|------------|---------------|
| 0 | mvp_occ_s4 | 1 (Grad ON + BN) | false | (default BN) |
| 1 | full_occ_ln_s4 | 2 (Grad ON + LN) | false | ln |
| 2 | ablation_occ_detach_s4 | 3 (Grad OFF + BN) | true | (default BN) |
| 3 | detach_ln_s4 | 4 (Grad OFF + LN) | true | ln |
