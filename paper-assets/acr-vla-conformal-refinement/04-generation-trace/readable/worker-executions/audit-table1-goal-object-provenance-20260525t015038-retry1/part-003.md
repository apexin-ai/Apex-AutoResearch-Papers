# audit table1 goal object provenance 20260525T015038 retry1 — Part 3 of 4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../audit-table1-goal-object-provenance-20260525t015038-retry1.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/68/68b953382a27770f9703.json)

## Before a recorded user message

### Large event (continued)

```text
eated_at\": \"2026-05-19T15:30:26.607Z\", \"updated_at\": \"2026-05-19T16:31:06.453Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-random-selection-object-k5-seed42\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 5 --output_file logs/eval_object_random_selection_k5_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 10, \"model_name\": \"SmolVLA\", \"seed\": 42, \"gpu\": \"cuda:5\", \"pid\": 939548, \"checkpoint_source\": \"N/A (random selection baseline)\", \"eval_data\": \"LIBERO-Object\", \"tmux_session\": \"eval-random-selection-object-k5-seed42\", \"output_file\": \"logs/eval_object_random_selection_k5_seed42.json\", \"log_file\": \"logs/eval_object_random_selection_k5_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:18:49.960Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:18:51.282Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T16:19:03.242474+00:00\"}]}, \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:30:32.306Z\", \"updated_at\": \"2026-05-19T16:30:37.908Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed44\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed44.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 10, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"gpu\": \"cuda:2\", \"pid\": 843594, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-spatial\", \"output_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed44.json\", \"log_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed44.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:24:46.925Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:24:38.292Z\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:30:33.621Z\", \"updated_at\": \"2026-05-19T16:30:18.549Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed45\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed45.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 10, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"gpu\": \"cuda:5\", \"pid\": 845019, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-spatial\", \"output_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed45.json\", \"log_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:25:51.927Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:25:54.177Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T16:26:43.837743+00:00\"}]}, \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:13:57.251Z\", \"updated_at\": \"2026-05-19T16:17:38.007Z\", \"hypothesis\": \"Latency profiling: 正式测量 VLA+CRM pipeline 各组件 wall-clock time，覆盖 K=1/5/10/20 batched vs sequential，生成论文 Table 级结果。预期 CRM overhead < 1ms，pipeline 主要 bottleneck 在 VLA flow-matching sampling。\", \"spec\": {\"command\": \"python profile_latency.py\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"107232\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"submitted_at\": \"2026-05-19T16:14:41.817Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 1, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 171.9, \"gpu_hours\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:17:33.738Z\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"spec\": {\"checkpoint_path\": \"N/A (vla_only baseline)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": \"932535\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 45 --output_file logs/eval_spatial_vla_only_seed45.json\", \"finished_at\": \"2026-05-19T15:17:27.081Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:17:34.738444+00:00\"}]}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-19T15:47:20.192Z\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:50:49.193Z\", \"updated_at\": \"2026-05-19T16:06:07.907Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve perdof ε=0.05 (当前 n=2)。timeout=16h。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"eval-perdof-norm005-seed45-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"conclusion\": \"success\", \"log_path\": \"logs/eval_object_perdof_norm005_seed45.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-19T15:29:57.924Z\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:24:44.727Z\", \"updated_at\": \"2026-05-19T15:30:01.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed44. Spatial benchmark 第三个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 44, \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 44 --output_file logs/eval_spatial_vla_only_seed44.json\"}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:4\", \"pid\": \"835806\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed44.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 44 --output_file logs/eval_spatial_vla_only_seed44.json\", \"finished_at\": \"2026-05-19T15:27:05.121Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:27:13.496164+00:00\"}]}, \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint produced)\", \"completed_at\": \"2026-05-19T15:30:01.540Z\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:50:51.880Z\", \"updated_at\": \"2026-05-19T14:58:17.531Z\", \"hypothesis\": \"obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (当前 n=3)。timeout=16h。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"eval-obs-only-default-seed48-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:55:24.359Z\"}, \"failure_reason\": \"Process gone (cron miss 4/5), no sentinel, no W&B output detected\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:55:30.658Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:55:41.674404+00:00\"}]}, \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"notes\": \"误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 output JSON 完整（59 行，10 tasks × 10 rollouts）。success_rate=0.17，与原 seed48 (bjb2-28827) 一致。\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:01:28.636Z\", \"updated_at\": \"2026-05-19T14:43:19.646Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed43. P1 缺口：与 Spatial K=5 CRM seed43=32% 配对，计算 per-seed improvement。没有此 baseline 无法报告 Spatial 改进幅度。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 43 --output_file logs/eval_spatial_vla_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"80076\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-19T13:01:37.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 43, \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6102.3, \"gpu_hours\": 1.7}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:40:35.939Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:40:44.096497+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\", \"completed_at\": \"2026-05-19T14:43:19.646Z\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:55:51.909Z\", \"updated_at\": \"2026-05-19T14:38:29.599Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed42. P1 缺口：Spatial benchmark 需要 VLA-only baseline 才能报告 CRM 的改进幅度。对标 obs_only spatial K=10 seed42=35%。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"917724\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed42.log\", \"submitted_at\": \"2026-05-19T12:57:06.478Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6083.1, \"gpu_hours\": 1.69}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:36:03.209Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:36:10.920946+00:00\"}]}, \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed42.log\", \"completed_at\": \"2026-05-19T14:38:29.600Z\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:40.507Z\", \"updated_at\": \"2026-05-19T14:32:21.490Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed45.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 5, \"max_correction_norm\": 0.2}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:21.490Z\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:39.233Z\", \"updated_at\": \"2026-05-19T14:32:16.468Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed44.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 5, \"max_correction_norm\": 0.2}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:16.468Z\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:37.093Z\", \"updated_at\": \"2026-05-19T14:32:11.343Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed45\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 45 --K 5 --output_file logs/eval_object_random_selection_k5_seed45.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 45, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"HuggingFaceM4/SmolVLA-base\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:11.343Z\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:34.934Z\", \"updated_at\": \"2026-05-19T14:32:06.313Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-argmin-object-k5-seed44\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 44 --K 5 --output_file logs/eval_object_random_selection_k5_seed44.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 44, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"HuggingFaceM4/SmolVLA-base\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:06.313Z\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:57:11.028Z\", \"updated_at\": \"2026-05-19T14:32:01.561Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed43\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 43 --K 5 --output_file logs/eval_object_random_selection_k5_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 43, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"SmolVLA pretrained (random K=5 selection baseline, no fine-tuning)\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:01.561Z\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:43:11.414Z\", \"updated_at\": \"2026-05-19T14:31:56.882Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-argmin-object-k5-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 5 --output_file logs/eval_object_random_selection_k5_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 42, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"smolvla_libero (pretrained, no finetuning)\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:31:56.882Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:49:54.536Z\", \"updated_at\": \"2026-05-19T14:26:11.536Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"eval-spatial-obs-only-norm02-seed44\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:12:36.942Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:12:33.705Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:12:43.426190+00:00\"}]}, \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:29:55.249Z\", \"updated_at\": \"2026-05-19T13:39:15.552Z\", \"spec\": {\"command\": \"crm_perdof --seed 43 --K 10 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"571010\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed43.log\", \"submitted_at\": \"2026-05-18T01:29:54.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 130160.9, \"gpu_hours\": 36.16}, \"reproduce\": {\"finished_at\": \"2026-05-18T16:26:03.341Z\"}, \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed43.log\", \"hypothesis\": \"per-DoF CRM with max_correction_norm=0.1 on LIBERO-Object (seed43, K=10, n_rollouts=10) should achieve comparable SR to obs_only default, as tighter norm constraint limits correction magnitude per joint.\", \"completed_at\": \"2026-05-19T13:39:15.552Z\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:05:53.834Z\", \"updated_at\": \"2026-05-19T13:35:23.895Z\", \"hypothesis\": \"obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=12%)，需标准化。obs_only default 当前 n=3 (seed42/43/44)。\", \"parent\": \"eval-obs-only-object-default-seed45\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"579212\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed45-r2.log\", \"submitted_at\": \"2026-05-18T13:24:59.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 87024.8, \"gpu_hours\": 24.17}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": \"579212\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed45-r2.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45_r2.json\", \"finished_at\": \"2026-05-19T04:22:06.623Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:22:13.278219+00:00\"}]}, \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:35:23.895Z\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:30.602Z\", \"updated_at\": \"2026-05-19T13:30:16.050Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 42 --K 5 --output_file logs/eval_object_argmin_k5_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"883706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed42.log\", \"submitted_at\": \"2026-05-19T11:36:06.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_reconvla_argmin\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6679.2, \"gpu_hours\": 1.86}, \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed42 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"reproduce\": {\"finished_at\": \"2026-05-19T13:26:43.546Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:26:53.401549+00:00\"}]}, \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:27:25.720Z\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:36:13.145Z\", \"updated_at\": \"2026-05-19T13:26:50.930Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 5 --output_file logs/eval_object_argmin_k5_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"884249\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed45.log\", \"submitted_at\": \"2026-05-19T11:36:12.365Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_reconvla_argmin\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6638.6, \"gpu_hours\": 1.84}, \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed45 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:26:50.930Z\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:15.812Z\", \"updated_at\": \"2026-05-19T13:26:46.918Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 5 --output_file logs/eval_object_argmin_k5_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"883975\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed43.log\", \"submitted_at\": \"2026-05-19T11:36:09.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_reconvla_argmin\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6637.5, \"gpu_hours\": 1.84}, \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed43 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:26:46.918Z\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:18:03.763Z\", \"updated_at\": \"2026-05-19T13:24:40.192Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed43 on LIBERO-Object. 补 magnitude curve：perdof ε=0.3 当前 n=3 (seed42:4%, seed44:4%, seed45:6%)，mean=4.67%。增加第 4 个 seed 强化 error bars。\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-18T15:18:23.972Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed43.json\", \"finished_at\": \"2026-05-18T21:19:30.796Z\", \"training_hours\": 6.02}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"594147\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed43.log\", \"submitted_at\": \"2026-05-18T15:18:27.012Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21673.4, \"gpu_hours\": 6.02}, \"pid\": \"594147\", \"log_path\": \"/root/logs/eval_object_perdof_norm03_seed43.json\", \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:19:40.460Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:20:00.703434+00:00\"}]}, \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:49:55.654Z\", \"updated_at\": \"2026-05-19T13:12:13.645Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"eval-spatial-obs-only-norm02-seed45\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T12:50:07.643Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:50:11.303Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:50:17.204819+00:00\"}]}, \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:40:51.279Z\", \"updated_at\": \"2026-05-19T12:48:29.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=0 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-multistage-object --auto 2>&1 | tee /root/acr-vla-conformal-refinement/logs/train_crm_k1_full.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"434871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42-full.log\", \"submitted_at\": \"2026-05-17T15:40:50.814Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 162458.5, \"gpu_hours\": 45.13}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1_accg_full/crm_best.pt\", \"hypothesis\": \"K=1 CRM full training with multi-stage VLA feature fusion + composite loss (L2 + contrastive + uncertainty-weighted) on full object benchmark dataset. Scaled-up version of train-crm-k1-accg-object-seed42-v2 with complete training data.\", \"completed_at\": \"2026-05-19T12:48:29.290Z\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:11:43.484Z\", \"updated_at\": \"2026-05-19T12:48:27.021Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/precompute_k1.py --benchmark spatial --batch_size 4 --cache_dir /root/autodl-tmp/crm_cache_k1/ 2>&1 | tee logs/precompute_k1.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"649967\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_701-precompute-k1-spatial.log\", \"submitted_at\": \"2026-05-17T14:11:42.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 167804.3, \"gpu_hours\": 46.61}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/precomputed/k1_spatial/\", \"hypothesis\": \"K=1 spatial benchmark precomputation: generate single-sample VLA action predictions and features for CRM K=1 training. Required preprocessing step before K=1 CRM can be trained on spatial tasks.\", \"completed_at\": \"2026-05-19T12:48:27.021Z\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:04:14.203Z\", \"updated_at\": \"2026-05-19T12:48:10.176Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p /root/autodl-tmp/checkpoints/crm_k1 && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm_k1.py --auto --benchmark spatial --epochs 50 --batch_size 512 --lr 1e-3 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-train-spatial --precompute_batch_size 4 --output_dir /root/autodl-tmp/checkpoints/crm_k1/ 2>&1 | tee logs/train_crm_k1.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"422526\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_701-crm-k1-train.log\", \"submitted_at\": \"2026-05-17T14:04:13.752Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 168236.4, \"gpu_hours\": 46.73}, \"hypothesis\": \"K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_best.pt\", \"completed_at\": \"2026-05-19T12:48:10.176Z\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:53.216Z\", \"updated_at\": \"2026-05-19T12:48:06.312Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"774538\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\", \"submitted_at\": \"2026-05-17T22:59:52.629Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 136093.7, \"gpu_hours\": 37.8}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.3 至 n=7。\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:44:29.475Z\"}, \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}, \"completed_at\": \"2026-05-19T12:48:06.312Z\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:51.090Z\", \"updated_at\": \"2026-05-19T12:48:03.869Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"774337\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\", \"submitted_at\": \"2026-05-17T22:59:50.463Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 136093.4, \"gpu_hours\": 37.8}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.1 至 n=7。\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:44:25.580Z\"}, \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}, \"completed_at\": \"2026-05-19T12:48:03.869Z\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:56:16.472Z\", \"updated_at\": \"2026-05-19T12:48:01.446Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file /root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"989694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-vla-only-r3.log\", \"submitted_at\": \"2026-05-19T05:56:15.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24705.6, \"gpu_hours\": 6.86}, \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks r3 rerun. Second reproduction of LTO baseline SR=14%. Confirms v2 result consistency.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"completed_at\": \"2026-05-19T12:48:01.446Z\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:55:29.003Z\", \"updated_at\": \"2026-05-19T12:47:58.882Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file logs/eval_lto_splitA_vla_only_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"976974\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-vla-only-r2.log\", \"submitted_at\": \"2026-05-19T04:55:28.251Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28350.6, \"gpu_hours\": 7.88}, \"hypothesis\": \"VLA-only baseline on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"completed_at\": \"2026-05-19T12:47:58.882Z\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:55:26.507Z\", \"updated_at\": \"2026-05-19T12:47:56.312Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode crm_obs_only --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --K 5 --max_correction_norm 0.2 --output_file logs/eval_lto_splitA_heldout_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"976768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-heldout-r2.log\", \"submitted_at\": \"2026-05-19T04:55:25.815Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28350.5, \"gpu_hours\": 7.88}, \"hypothesis\": \"LTO split-A CRM (K=5, ε=0.2, obs_only) on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"completed_at\": \"2026-05-19T12:47:56.312Z\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:13:30.382Z\", \"updated_at\": \"2026-05-19T12:47:52.436Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 python train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_v3 --input_mode obs_only --task_indices 0,1,2,3,4 --epochs 50 --batch_size 256 --lr 0.008 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_lto_splitA/obs_only/ --hidden_dim 256 --val_split 0.1 --log_every 20 2>&1 | tee /root/runs/acr-vla-conformal-refinement/crm-lto-splitA-train.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"953358\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-lto-splitA-train.log\", \"submitted_at\": \"2026-05-19T03:13:29.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 34462.7, \"gpu_hours\": 9.57}, \"conclusion\": \"success\", \"hypothesis\": \"LTO Split A CRM training (obs_only, 5 tasks, task_indices 0-4). Predecessor to eval-lto-splitA-heldout experiments. Superseded by crm-lto-splitA-train-fixed (task_names matching).\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA/crm_best.pt\", \"completed_at\": \"2026-05-19T12:47:52.436Z\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:31:15.780Z\", \"updated_at\": \"2026-05-19T12:23:18.801Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed48 on LIBERO-Object. 补 magnitude curve 最薄点 perdof ε=0.03 (当前 n=1)。timeout=16h。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.03 --n_rollouts 10 --timeout 57600\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\", \"submitted_at\": \"2026-05-18T21:31:00Z\"}, \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:59:18.061Z\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:22:25.439Z\", \"updated_at\": \"2026-05-19T11:45:28.182Z\", \"hypothesis\": \"Scalar CRM seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current scalar: [9,10,6,9] mean=8.5%\", \"parent\": \"eval-scalar-object-seed45\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed45_r2.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"464950\", \"log_path\": \"logs/eval_object_scalar_seed45_r2.json\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T11:45:28.182Z\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:33.036Z\", \"updated_at\": \"2026-05-19T11:34:16.077Z\", \"spec\": {\"command\": \"K=5 obs_only spatial ε=0.2 seed43\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"786306\", \"log_path\": \"logs/eval_spatial_obs_only_norm02_k5_seed43.json\", \"submitted_at\": \"2026-05-19T04:08:32.396Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"wall_clock_seconds\": 26743.7, \"gpu_hours\": 7.43}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:34:16.077Z\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:04:44.384Z\", \"updated_at\": \"2026-05-19T11:34:12.397Z\", \"spec\": {\"command\": \"K=5 obs_only ε=0.2 seed48\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"784377\", \"log_path\": \"logs/eval_object_obs_only_norm02_k5_seed48.json\", \"submitted_at\": \"2026-05-19T04:04:42.324Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"wall_clock_seconds\": 26970.1, \"gpu_hours\": 7.49}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration 补种到 n=7 统计力度增强。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:34:12.398Z\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:18.656Z\", \"updated_at\": \"2026-05-19T11:31:39.191Z\", \"spec\": {\"command\": \"K=5 obs_only spatial seed42\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"717974\", \"log_path\": \"logs/eval_spatial_obs_only_norm02_k5_seed42.json\", \"submitted_at\": \"2026-05-19T04:08:17.987Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"wall_clock_seconds\": 26601.2, \"gpu_hours\": 7.39}, \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"completed_at\": \"2026-05-19T11:31:39.191Z\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:29:24.718Z\", \"updated_at\": \"2026-05-19T11:30:55.300Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"956475\", \"log_path\": \"logs/eval_object_obs_only_norm02_k5_seed46.json\", \"submitted_at\": \"2026-05-19T03:31:41.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-obs-only-object-norm02-k5-seed46\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 28569.4, \"gpu_hours\": 7.94}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 n≥5。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:27:50.610Z\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:19:21.005Z\", \"updated_at\": \"2026-05-19T11:30:43.198Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval. Retry after .replace task matching bug fix.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file logs/eval_lto_splitA_vla_only_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"log_path\": \"/root/acr-vla-conformal-refinement/src/logs/eval_lto_splitA_vla_only_r2.json\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-lto-splitA-vla-only-r2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:27:47.248Z\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:19:18.968Z\", \"updated_at\": \"2026-05-19T11:30:33.951Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. Retry after .replace task matching bug fix.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode crm_obs_only --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --K 5 --max_correction_norm 0.2 --output_file logs/eval_lto_splitA_heldout_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/acr-vla-conformal-refinement/src/logs/eval_lto_splitA_heldout_r2.json\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-lto-splitA-heldout-r2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA+CRM_lto_splitA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T11:27:43.439Z\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:44.467Z\", \"updated_at\": \"2026-05-19T11:30:18.282Z\", \"hypothesis\": \"Per-DoF CRM (ε=default/unlimited) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed47.json\", \"server\": \"bjb2-28827\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_default_seed47.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T11:24:52.163Z\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束, success_rate=0%\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:47.310Z\", \"updated_at\": \"2026-05-19T11:30:17.012Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed47.json\", \"server\": \"bjb2-28827\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm03_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:49.647Z\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:41.596Z\", \"updated_at\": \"2026-05-19T11:30:15.785Z\", \"hypothesis\": \"Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed48.json\", \"server\": \"bjb2-28827\", \"seed\": 48, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_obs_only\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_default_seed48.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:56.050Z\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:35.770Z\", \"updated_at\": \"2026-05-19T11:30:14.493Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed46.json\", \"server\": \"bjb2-28827\", \"seed\": 46, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm003_seed46.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:58.897Z\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:29:18.036Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"notes\": \"bjb1-32546 GPU process dead, no JSON output\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:23.296Z\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-18T15:16:48.731Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\"}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"652406\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-18T15:16:51.497Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"notes\": \"bjb1-32546 GPU process dead, no JSON output\", \"wall_clock_seconds\": 72677.9, \"gpu_hours\": 20.19}, \"pid\": \"652406\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed45.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:28:09.358Z\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:29:27.251Z\", \"updated_at\": \"2026-05-19T11:27:53.132Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed47.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"956741\", \"log_path\": \"logs/eval_object_obs_only_norm02_k5_seed47.json\", \"submitted_at\": \"2026-05-19T03:31:43.769Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-obs-only-object-norm02-k5-seed47\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 28569.4, \"gpu_hours\": 7.94}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 n≥6。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:27:53.132Z\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:25:28.189Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.1 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/logs/eval_object_perdof_norm01_seed48.json\"}, \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:28.189Z\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:25:18.480Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_default_seed47.log\"}, \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:18.480Z\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:25:13.541Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm03_seed46.log\"}, \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:25:11.008Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_norm03_seed46.log\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:25:07.860Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed46.log\"}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:07.860Z\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:44:44.161Z\", \"updated_at\": \"2026-05-19T05:16:02.877Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. Retry with timeout=16h after r1 timed out. 补 magnitude curve 最薄点 ε=0.03。\", \"spec\": {\"command\": \"timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed45.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"eval-obs-only-norm003-seed45-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T04:44:28.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:44:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:44:37.585122+00:00\"}]}, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/logs/eval_object_obs_only_norm003_seed45.log\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:35:02.089Z\", \"updated_at\": \"2026-05-19T05:13:20.212Z\", \"spec\": {\"command\": \"killed (buggy .replace task matching)\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"970894\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-19T04:35:01.423Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval-only, killed due to task matching bug)\", \"wall_clock_seconds\": 1469.7, \"gpu_hours\": 0.41}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:59:31.167Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval.\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:34:59.607Z\", \"updated_at\": \"2026-05-19T05:13:18.481Z\", \"spec\": {\"command\": \"killed (buggy .replace task matching)\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"970686\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-19T04:34:58.943Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA+CRM_lto_splitA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval-only, killed due to task matching bug)\", \"wall_clock_seconds\": 1469.4, \"gpu_hours\": 0.41}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:59:28.321Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. If SR > VLA-only on held-out tasks, CRM generalizes beyond training distribution.\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:53:33.612Z\", \"updated_at\": \"2026-05-19T04:58:44.483Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 obs_only ε=0.05 seed (n=4→5)。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm005_seed46.log\", \"server\": \"bjb1-18228\", \"seed\": 46, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:58:44.483Z\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:14.835Z\", \"updated_at\": \"2026-05-19T04:58:40.993Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed48 on LIBERO-Object. 补 perdof ε=0.3 至 n=7。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"seed\": 48, \"model_name\": \"crm_v3_norm_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:58:40.993Z\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:09:03.172Z\", \"updated_at\": \"2026-05-19T04:58:36.864Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed49 on LIBERO-Object. 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)，第 6 个 seed 确保极低 norm 端统计可靠。\", \"spec\": {\"command\": \"crm_obs_only --benchmark object --seed 49 --K 10 --max_correction_norm 0.03 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 49, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:58:36.864Z\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:27:23.594Z\", \"updated_at\": \"2026-05-19T04:32:49.103Z\", \"spec\": {\"command\": \"python train_crm.py --benchmark object --task_names alphabet_soup,bbq_sauce,butter,chocolate_pudding,cream_cheese --input_mode obs_only --epochs 50 --output_dir /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"955547\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-lto-splitA-train-fixed.log\", \"submitted_at\": \"2026-05-19T03:27:22.886Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Uses --task_names string matching (bug-fixed, no numeric index).\", \"data_path\": \"/root/autodl-tmp/crm_cache_v3/object/\", \"data_count\": 7499, \"model_name\": \"crm_obs_only_lto_splitA\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\", \"metrics\": {\"best_val_loss\": 0.091861}, \"wall_clock_seconds\": 3926.2, \"gpu_hours\": 1.09}, \"conclusion\": \"success\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks. Uses task_names string matching.\", \"completed_at\": \"2026-05-19T04:32:49.103Z\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:10.585Z\", \"updated_at\": \"2026-05-19T04:32:33.294Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. 补 magnitude curve ε=0.03 至 n=6。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed47.json\", \"server\": \"bjb1-18228\", \"seed\": 47, \"model_name\": \"crm_v3_norm_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A (killed before completion)\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:32:33.295Z\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"submitted_at\": \"2026-05-18T13:25:05.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A-eval\", \"wall_clock_seconds\": 50627.1, \"gpu_hours\": 14.06}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"finished_at\": \"2026-05-19T03:25:56.586Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:26:06.809444+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:28:52.476Z\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"submitted_at\": \"2026-05-18T13:28:51.027Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"max_correction_norm\": 0.05, \"seed\": 43, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"wall_clock_seconds\": 48429.6, \"gpu_hours\": 13.45}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"finished_at\": \"2026-05-19T02:35:05.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:35:13.418956+00:00\"}]}, \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:56:00.676Z\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:17:50.362Z\", \"updated_at\": \"2026-05-19T01:44:05.704Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed43 confirms cross-seed consistency of collapse.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"832702\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-default-seed43.log\", \"submitted_at\": \"2026-05-18T10:31:01.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 54783.7, \"gpu_hours\": 15.22}, \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"log_path\": \"bjb1-18228:/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\", \"completed_at\": \"2026-05-19T01:44:05.704Z\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-19T01:38:34.712Z\", \"completed_at\": \"2026-05-17T02:54:38.157Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed45 confirms cross-seed consistency of collapse.\", \"parent\": \"crm-train-v2-perdof\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"metrics\": {\"kill_reason\": \"Sacrificed for P0 direct-correction experiment (no free GPU). Was at task 5/10 after 6h. Expected result: 0% (confirmed by seed42=0%, seed44 running on autodl-4090).\", \"partial_progress\": \"5/10 tasks, bbq_sauce 0% success\"}}}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"626277\", \"tmux_session\": \"eval_perdof_default_seed45\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof_uncapped\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.log\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:38.704Z\", \"updated_at\": \"2026-05-19T01:33:59.345Z\", \"hypothesis\": \"Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_obs_only\"}, \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.log\", \"completed_at\": \"2026-05-19T01:33:59.345Z\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:51:08.830Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"finished_at\": \"2026-05-18T21:53:11.259Z\", \"training_hours\": 6.03}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"submitted_at\": \"2026-05-18T15:51:11.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21723.3, \"gpu_hours\": 6.03}, \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T21:53:14.790Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:53:20.362616+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:27:12.596Z\", \"updated_at\": \"2026-05-18T21:05:50.448Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=19%, mean=16.5%). Variance 大 (5pp gap), 第三个 seed 对 K-value scaling narrative 至关重要。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"575334\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed44.log\", \"submitted_at\": \"2026-05-18T13:02:07.891Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 29022.6, \"gpu_hours\": 8.06}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": \"575334\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed44.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed44.json\", \"finished_at\": \"2026-05-18T20:50:04.112Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:50:11.696653+00:00\"}]}, \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"completed_at\": \"2026-05-18T21:05:50.448Z\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:31:41.748Z\", \"updated_at\": \"2026-05-18T19:14:55.968Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。重试 r2 修正 python 路径。\", \"parent\": \"eval-perdof-object-norm003-seed44\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"855046\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44-r2.log\", \"submitted_at\": \"2026-05-18T13:32:24.693Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20543.8, \"gpu_hours\": 5.71}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": \"855046\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44-r2.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\", \"finished_at\": \"2026-05-18T19:14:49.922Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T19:14:48.505Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:14:58.108020+00:00\"}]}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:33:39.698Z\", \"updated_at\": \"2026-05-18T16:48:10.654Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.\", \"spec\": {\"command\": \"crm_obs_only --seed 46 --K 10 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"562396\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:26:17.222Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T15:18:13.193Z\", \"spec\": {\"command\": \"crm_perdof --seed 44 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"553052\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-17T23:31:56.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 56776.9, \"gpu_hours\": 15.77}, \"hypothesis\": \"perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。\", \"reproduce\": {\"finished_at\": \"2026-05-18T12:34:49.939Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T12:34:56.300941+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-18T15:18:13.193Z\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:44:42.438Z\", \"updated_at\": \"2026-05-18T14:17:30.462Z\", \"hypothesis\": \"VLA-only baseline seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current VLA-only: [12,12,10,9,13] mean=11.2%\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 45 --K 1 --output_file logs/eval_object_vla_only_seed45_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA (VLA-only)\", \"seed\": 45, \"pid\": 839546, \"tmux_session\": \"eval_vla_only_seed45_r2\"}, \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:17:30.462Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:02:40.444Z\", \"updated_at\": \"2026-05-18T13:27:03.418Z\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 774538, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T13:20:28.460Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:20:31.564Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:20:37.041564+00:00\"}]}, \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A (eval only)\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T04:37:18.401Z\", \"updated_at\": \"2026-05-18T12:39:30.555Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"527465\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed43.log\", \"submitted_at\": \"2026-05-18T04:37:17.870Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 28932.7, \"gpu_hours\": 8.04}, \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.\", \"reproduce\": {\"finished_at\": \"2026-05-18T12:33:47.520Z\"}, \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T12:39:30.555Z\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:32:26.297Z\", \"updated_at\": \"2026-05-18T12:33:45.335Z\", \"hypothesis\": \"perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52 UTC.\", \"parent\": \"eval-perdof-object-norm01-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T12:33:45.336Z\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:32:25.342Z\", \"updated_at\": \"2026-05-18T12:33:41.666Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 07:52 UTC.\", \"parent\": \"eval-obs-only-object-norm01-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T12:33:41.666Z\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:36:46.839Z\", \"updated_at\": \"2026-05-18T10:56:45.558Z\", \"hypothesis\": \"Perdof CRM with norm clipping ε=0.2 provides controlled corrections that preserve baseline policy behavior on LIBERO-Object. Expected SR ~10% (similar to other seeds 42/44/45/46/47 at 9-12%).\", \"spec\": {\"command\": \"crm_perdof --seed 43 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"535595\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:56:45.558Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-18T07:05:38.605Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"393633\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\", \"submitted_at\": \"2026-05-17T06:51:36.171Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof_v3_norm\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 87240.0, \"gpu_hours\": 24.23}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T07:05:36.145Z\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-18T07:05:03.603Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode crm_obs_only --max_correction_norm 0.1 --k 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_norm01_seed45.json > logs/eval_object_obs_only_norm01_seed45.log 2>&1\", \"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"model_name\": \"crm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": -1, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"obs_only CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve data point. seed42=19%.\"}, \"pid\": 474319, \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\", \"conclusion\": \"success\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"completed_at\": \"2026-05-17T13:31:33.316Z\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-18T07:05:02.646Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:32:21.424Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-17T18:32:28.770Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:40.928533+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:54.338Z\", \"updated_at\": \"2026-05-18T07:05:01.672Z\", \"hypothesis\": \"perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": 423767, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T01:27:04.768Z\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-18T06:19:59.229Z\", \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:20:12.857Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-17T07:20:15.008Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:20:19.307187+00:00\"}], \"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Task 10 not started due to 24h timeout. 0/90 rollouts succeeded. Catastrophic collapse at unclipped norm.\", \"seed\": 44, \"mode\": \"crm_perdof\", \"benchmark\": \"object\", \"max_correction_norm\": \"default (~1.42)\"}, \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\"}}, \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"partial results from previous run, 0/90 rollouts across 9/10 tasks\", \"server\": \"autodl-4090 (previous run)\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"model_name\": \"crm_perdof\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 90}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-18T05:54:22.364Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:2\", \"pid\": 13728, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:14.331Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:30:15.807Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:23.476790+00:00\"}]}, \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-18T05:54:21.341Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 288939, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\", \"gpu_ids\": [\"cuda:2\"]}, \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:54.647Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T04:57:55.887Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:57.857060+00:00\"}]}}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-18T05:54:20.300Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:04:16.712Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 7/10 tasks 后在 task 8 启动前被 kill。\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-18T05:54:19.300Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 24161.7, \"gpu_hours\": 6.71}, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:04:17.448Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 6/10 tasks，第 7 个 task (next_to_cookie_box) rollout 5/10 时被 kill。\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-18T05:54:18.227Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 40187.5, \"gpu_hours\": 11.16}, \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:45.148Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T04:57:46.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:50.175181+00:00\"}]}, \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-18T05:54:17.209Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"197057\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:17:05.974Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28899.4, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:44.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:45.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:46.631294+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-18T05:54:16.171Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"197803\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log\", \"submitted_at\": \"2026-05-14T12:17:13.006Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction generalizes from spatial to object benchmark — cross-benchmark validation of ACR-VLA.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28901.2, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:53.408Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:54.185Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:55.466058+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:56:51.046Z\", \"updated_at\": \"2026-05-18T05:54:15.084Z\", \"spec\": {\"command\": \"python -u src/openvla_eval.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --K 1 --gpu 0 --model_path /root/autodl-tmp/models/openvla-libero-object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"667642\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log\", \"submitted_at\": \"2026-05-17T15:57:37.232Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7512.0, \"gpu_hours\": 2.09}, \"hypothesis\": \"OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40.1 in isolated conda env. Dry-run verified 80% SR on libero_spatial. Awaiting GPU for full LIBERO-Object eval.\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:01:16.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:01:26.464150+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}, \"completed_at\": \"2026-05-17T18:02:49.250Z\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log\", \"notes\": \"NEEDS INVESTIGATION: 0% success rate vs OpenVLA paper 88.4% (LIBERO-Object). 100% confirmed code bug. Suspected action tokenization/detokenization or unnormalize issue. Do NOT treat as valid baseline.\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:28.585Z\", \"updated_at\": \"2026-05-18T04:37:10.886Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"404983\", \"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed47.json\", \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T04:37:04.589Z\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:21.870Z\", \"updated_at\": \"2026-05-18T03:04:35.124Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"796895\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed48.log\", \"submitted_at\": \"2026-05-18T03:04:34.555Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:12:19.723Z\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:52.326Z\", \"updated_at\": \"2026-05-18T03:03:50.286Z\", \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 422357, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:20:44.089Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T00:20:46.904Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:20:52.370655+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-18T02:24:22.787Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 389051, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:24:14.354Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-18T01:01:03.202Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --output_file logs/eval_object_obs_only_norm01_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"590833\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.log\", \"submitted_at\": \"2026-05-17T06:54:14.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"seed\": 46, \"wall_clock_seconds\": 65208.4, \"gpu_hours\": 18.11}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-18T01:00:59.710Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T01:01:03.202Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:01:13.372128+00:00\"}]}}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:31.864Z\", \"updated_at\": \"2026-05-17T23:47:05.521Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"448773\", \"log_path\": \"N/A (killed as orphan)\", \"submitted_at\": \"2026-05-17T18:04:30.652Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 47, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 20554.9, \"gpu_hours\": 5.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:47:05.521Z\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:34.999Z\", \"updated_at\": \"2026-05-17T23:47:03.765Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"449059\", \"log_path\": \"N/A (killed as orphan)\", \"submitted_at\": \"2026-05-17T18:04:34.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 46, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 20549.5, \"gpu_hours\": 5.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:47:03.765Z\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T23:17:06.378Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"N/A (killed as duplicate)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:02:21.019Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T23:10:07.386Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"449330\", \"log_path\": \"N/A (killed)\", \"submitted_at\": \"2026-05-17T18:04:36.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_perdof + SmolVLA\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 18330.9, \"gpu_hours\": 5.09}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:10:07.386Z\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T23:00:33.671Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"spec\": {\"command\": \"cd /root/autodl-tmp/acr-vla && python evaluate.py --model smolvla --mode crm_perdof --benchmark object --seed 47 --n_rollouts 10 --norm_limit 0.1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 414817, \"data_path\": \"/root/autodl-tmp/acr-vla/libero/data\", \"data_count\": 100, \"model_name\": \"SmolVLA-450M + CRM-perdof\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks × 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:00:33.671Z\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:06:55.243Z\", \"updated_at\": \"2026-05-17T22:39:25.302Z\", \"hypothesis\": \"OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.\", \"spec\": {\"command\": \"bash -c \\\"source /root/autodl-tmp/conda_envs/openvla/bin/activate && cd /root/autodl-tmp/openvla && MUJOCO_GL=egl python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --num_trials_per_task 10 --seed 42 --local_log_dir /root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 747644, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 10 trials = 100 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}, \"completed_at\": \"2026-05-17T22:39:25.302Z\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T21:14:35.625Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu_id\": \"cuda:3\", \"tmux_session\": \"eval-k1-seed44\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:14:35.625Z\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T21:02:09.738Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 504682, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 44, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:09.738Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:11.800Z\", \"updated_at\": \"2026-05-17T21:02:08.069Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": 503178, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 43, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed43.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:08.069Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:09.846Z\", \"updated_at\": \"2026-05-17T21:02:06.052Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 455518, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 42, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:06.052Z\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T21:01:12.153Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 393646, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"log_path\": \"logs/eval_object_perdof_norm01_seed46.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-17T21:01:12.153Z\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T20:55:55.430Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_multiscale\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu_id\": \"cuda:1\", \"tmux_session\": \"eval-k1-seed43\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"completed_at\": \"2026-05-17T20:55:55.430Z\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:18.289Z\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"634427\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r2.log\", \"submitted_at\": \"2026-05-17T13:35:38.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 17779.9, \"gpu_hours\": 4.94}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:31:54.940Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:31:57.991Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:03.172248+00:00\"}]}}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:34:38.488Z\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"633631\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed43-r3.log\", \"submitted_at\": \"2026-05-17T13:35:14.715Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 17815.3, \"gpu_hours\": 4.95}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:32:06.590Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:32:10.053Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:15.088162+00:00\"}]}}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:20.097Z\", \"updated_at\": \"2026-05-17T18:35:42.842Z\", \"hypothesis\": \"Measure wall-clock latency of ACR-VLA pipeline components: VLA encode, VLA K-sampling (K=1/5/10/20), CGS scoring, CRM forward pass, and full pipeline. Quantify overhead of conformal refinement relative to VLA sampling cost.\", \"spec\": {\"command\": \"python -u src/latency_profile.py\", \"server\": \"bjb2-28827\", \"seed\": 42, \"data_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"completed_at\": \"2026-05-17T18:35:42.842Z\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T15:51:14.367Z\", \"updated_at\": \"2026-05-17T18:31:23.291Z\", \"hypothesis\": \"K=1 CRM with ACCG using full multi-scale features (4×960D from SmolVLA layers [3,7,11,15]). Multi-scale should capture richer correction signals than single-stage 960D fallback (val_loss=0.006505). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:01:06.354Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:01:12.607135+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"HDF5 corruption report was false alarm - all 10 files verified intact (md5 match, h5py OK). Training continued past crash point. Precompute running: 7500/72507, ~75 min remaining. conclusion=failed was set prematurely; training is actually running.\"}}, \"completed_at\": \"2026-05-17T18:01:40.220Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42-v2.log\"}, \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:01.165Z\", \"updated_at\": \"2026-05-17T18:22:02.272Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed44. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460733, \"gpu\": [\"cuda:5\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed44.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"completed_at\": \"2026-05-17T18:02:47.296Z\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:27:59.825Z\", \"updated_at\": \"2026-05-17T18:22:01.354Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460729, \"gpu\": [\"cuda:4\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed43.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"completed_at\": \"2026-05-17T18:02:45.640Z\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:27:58.213Z\", \"updated_at\": \"2026-05-17T18:22:00.464Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460724, \"gpu\": [\"cuda:1\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed42.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T18:02:43.637Z\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T17:32:15.936Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 242264, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 45}, \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-17T17:32:15.936Z\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T17:29:34.723Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_scalar --max_correction_norm 0.1 --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --output_file logs/eval_object_scalar_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 224623, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed45.log\"}, \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}, \"completed_at\": \"2026-05-17T17:29:34.723Z\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T17:03:14.729Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --K 10 --seed 45 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:1\", \"pid\": 222824, \"seed\": 45, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"Perdof CRM norm=0.2 seed=45 on LIBERO object. Additional perdof data point for cross-seed comparison. Expected ~11% based on seed42 data.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\", \"completed_at\": \"2026-05-17T17:03:14.729Z\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T16:52:17.419Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"326081\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"submitted_at\": \"2026-05-17T08:36:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 29777.4, \"gpu_hours\": 8.27}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"checkpoint_path\": \"logs/eval_object_perdof_norm02_seed44.json\", \"completed_at\": \"2026-05-17T16:52:17.419Z\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:02:35.790Z\", \"updated_at\": \"2026-05-17T15:19:16.626Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --reuse_k10_cache --k10_cache_dir /root/autodl-tmp/crm_cache_v5/ --auto --no_wandb\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 456622, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/train_crm_k1_fallback.log\", \"submitted_at\": \"2026-05-17T15:02:35.104Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:4\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 4857, \"model_name\": \"crm_k1_accg_fallback\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/\", \"wall_clock_seconds\": 914.9, \"gpu_hours\": 0.25}, \"hypothesis\": \"CRM K=1 with ACCG architecture trained on K=10 single-stage cache (960D fallback) can learn effective corrections for object benchmark, achieving low val_loss comparable to multi-scale approach\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T15:17:49.965Z\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:48:22.459Z\", \"updated_at\": \"2026-05-17T14:53:10.162Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=0 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-object --auto\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"427856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42.log\", \"submitted_at\": \"2026-05-17T14:48:21.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"CRM_K1_ACCG_v2\", \"data_path\": \"LIBERO-Object precomputed K=1 features\", \"data_count\": -1, \"wall_clock_seconds\": 174.4, \"gpu_hours\": 0.05}, \"hypothesis\": \"K=1 CRM 训练（ACCG 架构）：使用 Action-Conditioned Correction Gating 替代 FiLM，多阶段 VLA 特征融合 + 组合损失函数（L2 + directional + triplet + magnitude），训练专用于 K=1 单采样纠正的 CRM。目标超越 K=1 VLA-only baseline (10.8%)。ACCG 用 action 本身计算动态 gate 选择 correction 维度。\", \"reproduce\": {\"finished_at\": \"2026-05-17T14:49:15.593Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:49:21.444858+00:00\"}]}, \"conclusion\": \"failed\", \"failure_reason\": \"LIBERO HDF5 demo data missing on bjb2-28827. Precompute requires raw demo trajectories but only K=10 cache exists.\", \"completed_at\": \"2026-05-17T14:51:16.090Z\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:34:09.564Z\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45.json 2>&1 | tee logs/eval_object_perdof_norm02_seed45.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"632156\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-deploy.log\", \"submitted_at\": \"2026-05-17T13:34:09.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1025.8, \"gpu_hours\": 0.28}, \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:47:18.573Z\"}, \"failure_reason\": \"**根因**: MuJoCo EGL 渲染初始化 segfault（native crash）。\\n\\n**证据**:\\n- tmux 日志和应用日志均在 `[eval] 10 tasks loaded.` 后中断，无 Python traceback、无 segfault handler 输出\\n- 代码中有 SIGSEGV handler 但未被触发，说明崩溃发生在 native code（MuJoCo/EGL）且 handler 未能执行\\n- 同服务器多个实验表现相同模式（eval_object_obs_only_norm03_seed47、eval_object_perdof_norm01_seed47 等均在 \\\"10 tasks loaded\\\" 后死亡）\\n- 非 OOM：系统 RAM 454GB 空闲，GPU VRAM 仅用 5.6GB/24GB\\n- 崩溃点：第一个 rollout_single() → env.reset() 触发 MuJoCo EGL context 创建\\n\\n**关键日志（最后一行有效输出）**:\\n`[eval] 10 tasks loaded.`\\n（之后无任何输出，进程静默死亡）\\n\\n**可能触发因素**: 4 张 GPU 同时运行 4 个 eval 进程，并发 EGL context 初始化存在 driver 层竞争。较早的单卡实验（seed44/45/46）正常完成。\\n\\n**建议**: PID 634438 已在 GPU 0 上重启并处于 Running 状态，等待其完成。若再次失败，考虑串行执行（不并发跑 4 个 EGL 进程）或降低并发数。\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:47:28.347997+00:00\"}]}, \"completed_at\": \"2026-05-17T13:51:14.936Z\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T13:31:57.433Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 588037, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T13:31:55.004Z\", \"notes\": \"Worker batch7 误杀, 4/10 tasks 完成\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T12:04:17.540Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed45_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"319463\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T21:33:52.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 45, \"wall_clock_seconds\": 48204.7, \"gpu_hours\": 13.39}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:54:49.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:54:55.730176+00:00\"}]}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:57:16.754Z\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:22:10.412Z\", \"updated_at\": \"2026-05-17T12:00:58.173Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 421086, \"seed\": 44, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-17T11:50:26.264Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T11:50:20.975Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:50:33.595081+00:00\"}]}, \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:56.645Z\", \"updated_at\": \"2026-05-17T11:50:09.879Z\", \"hypothesis\": \"obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 error bar。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed47.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 612853, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-17T11:50:06.763Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T11:50:09.879Z\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:28:13.840Z\", \"updated_at\": \"2026-05-17T11:36:55.536Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 392856, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T11:36:55.536Z\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed44.json\", \"server\": \"bjb1-18228\", \"gpu_id\": 1, \"model_name\": \"crm_perdof_norm01\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=44 on LIBERO object. Multi-seed magnitude curve: seed42=11%, expecting similar. Fills the biggest gap in perdof magnitude data (norm=0.1 only has 1 seed).\", \"pid\": 531963}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:48:36.650Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:48:39.951Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:48:45.826946+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 363223, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (killed duplicate)\", \"log_path\": \"N/A (killed duplicate)\"}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:42:47.471Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T10:42:49.632Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:42:53.924730+00:00\"}]}}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 365893, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:43:36.147Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:43:38.311Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:43:46.527772+00:00\"}]}}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_reconvla_seed47.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 322337, \"seed\": 47, \"model_name\": \"SmolVLA_argmin_K10\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:51:45.356Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:51:50.389646+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T10:54:02.630Z\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 2, \"model_name\": \"crm_perdof_norm01\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve: seed42=11%, seed44=deploying. 3rd seed for perdof low-norm baseline.\", \"pid\": 309151}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-17T10:22:14.184Z\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_perdof_norm01_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"388460\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:11.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"N/A (killed before completion)\", \"wall_clock_seconds\": 12316.3, \"gpu_hours\": 3.42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:19:28.338Z\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_reconvla_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"reconvla\", \"hypothesis\": \"argmin baseline K=10 seed=46 on LIBERO object. 5th seed for Fisher test. Pairs with eval-obs-only-object-norm02-seed46 (bjb1-18228:cuda:3).\", \"data_path\": \"\", \"data_count\": 0, \"checkpoint_source\": \"\", \"eval_data\": \"object\", \"pid\": 295478, \"log_path\": \"logs/eval_argmin_object_seed46.log\", \"checkpoint_path\": \"N/A (eval-only, reconvla baseline)\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed46.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:19:26.819Z\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"272762\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T15:24:08.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:3\", \"model_name\": \"crm_obs_only_norm03\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"wall_clock_seconds\": 56321.1, \"gpu_hours\": 15.64}, \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:00:25.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:00:32.829645+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:02:49.285Z\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"spec\": {\"model_name\": \"smolvla_libero_vla_mean\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 45 --output_file logs/eval_object_vla_mean_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"248652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:45Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 70783.9, \"gpu_hours\": 19.66}, \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:29:41.019Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T03:29:45.978517+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T06:54:28.933Z\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_argmin_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"215932\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed45.log\", \"submitted_at\": \"2026-05-16T07:45:06.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"reconvla_argmin_baseline\", \"hypothesis\": \"argmin baseline K=10 seed=45 on LIBERO object. 4th seed baseline for Fisher test. Paired with eval-obs-only-object-norm02-seed45.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 60530.4, \"gpu_hours\": 16.81}, \"reproduce\": {\"finished_at\": \"2026-05-17T00:31:27.579Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T00:31:32.330885+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval-only)\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\", \"completed_at\": \"2026-05-17T00:33:57.260Z\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"tmux_session\": \"eval-dc-r2\", \"note\": \"Code patched: print every rollout instead of every 5. Root cause of prev failures: workers killed working processes because output interval was 7.5min (5 rollouts x 90s each).\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_direct_correction_object_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}, \"completed_at\": \"2026-05-17T04:48:50.296Z\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"505419\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed44.log\", \"submitted_at\": \"2026-05-16T15:24:11.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:2\", \"model_name\": \"crm_perdof_norm03\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 48060.4, \"gpu_hours\": 13.35}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"reproduce\": {\"finished_at\": \"2026-05-17T04:41:11.191Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T04:41:18.547308+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}, \"completed_at\": \"2026-05-17T04:45:11.458Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"spec\": {\"parent\": \"eval-acr-object-v4-perdof\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.2, K=10, n_rollouts=10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"127732\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log\"}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:45.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:48.447852+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T07:12:35.145Z\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:07:28.510451+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:10:02.679Z\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:5\", \"pid\": 15190, \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:03:26.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:03:29.305763+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm02.log\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-15T16:06:23.063Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log\"}, \"gpu\": \"bjb2-28827:cuda:3\", \"pid\": 14260, \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:53:04.031Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:53:08.939326+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:17:49.711Z\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"gpu\": \"bjb2-28827:cuda:1\", \"pid\": 13456, \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:52:50.451Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:52:53.898813+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:24:59.482Z\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm003.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:0\", \"pid\": 13185, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:32:37.390Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:32:42.080703+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm003.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:40:16.878Z\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:12:39.100Z\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\", \"checkpoint_path\": \"N/A (eval experiment)\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"spec\": {\"hypothesis\": \"obs-only CRM with norm=0.2 on object benchmark. Cross-benchmark norm sensitivity test — paired with eval-mag-obsonly-norm02 on spatial. If obs-only at norm=0.2 > norm=0.1 on both benchmarks → robust 'observation-conditioned correction' story.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 44270, \"tmux_session\": \"eval-acr-object-obs-only-norm02\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark, 10 tasks x 10 rollouts\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\"}, \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:35:34.272Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:35:39.374197+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\", \"completed_at\": \"2026-05-15T17:37:08.420Z\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"123761\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v7.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T01:45:58.391Z\", \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T03:10:30.457Z\", \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 2 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"180480\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard2.log\", \"submitted_at\": \"2026-05-14T07:56:37.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 2 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5491.8, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:09.308Z\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 1 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"180400\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard1.log\", \"submitted_at\": \"2026-05-14T07:56:35.789Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 1 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5492.1, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:07.934Z\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 0 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"180251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard0.log\", \"submitted_at\": \"2026-05-14T07:56:33.414Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 0 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5493.2, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:06.626Z\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"69937\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard2.log\", \"submitted_at\": \"2026-05-13T18:58:14.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173960.7, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:09:25.582Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:09:26.379476+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:35.000Z\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"69793\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log\", \"submitted_at\": \"2026-05-13T18:58:12.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173961.1, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:22.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:23.366356+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:33.288Z\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"69647\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log\", \"submitted_at\": \"2026-05-13T18:58:09.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173962.3, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:45.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:50.222546+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:32.128Z\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:32:23.773Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T11:07:49.901Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:14.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:15.524386+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:07:51.915540+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"118108\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean argmin)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"SampleConsensus scalar baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"186964\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"submitted_at\": \"2026-05-14T09:30:43.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM scalar-unc v2 (327K params, 8D state fix)\", \"seed\": 42, \"hypothesis\": \"Scalar CRM v2 ablation — per-DOF expected to outperform on task success rate despite similar val_loss\", \"wall_clock_seconds\": 9977.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"completed_at\": \"2026-05-14T12:17:01.093Z\", \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"186823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"submitted_at\": \"2026-05-14T09:30:40.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM per-DOF v2 (337K params, 8D state fix, argmin base, L2 clip)\", \"seed\": 42, \"hypothesis\": \"Per-DOF CRM v2 with D016 fixes (8D state, argmin base, alpha=0.5, L2 clipping) improves over pre-fix version\", \"wall_clock_seconds\": 9979.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"completed_at\": \"2026-05-14T12:17:00.195Z\", \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"187913\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"submitted_at\": \"2026-05-14T09:41:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM obs_only v2\", \"seed\": 42, \"wall_clock_seconds\": 9366.4, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"completed_at\": \"2026-05-14T12:17:42.122Z\", \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"47186\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard2.log\", \"submitted_at\": \"2026-05-13T11:57:48.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.4, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:07.463Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"47044\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard1.log\", \"submitted_at\": \"2026-05-13T11:57:46.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.8, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:06.485Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"46966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard0.log\", \"submitted_at\": \"2026-05-13T11:57:45.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12500.2, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:05.433Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:09:33.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:09:34.396952+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"completed_at\": \"2026-05-13T22:12:39.543Z\", \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial object --n_rollouts 20 --seed 42\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"50790\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_014-reconvla-baseline.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"20 tasks x 20 rollouts = 400 episodes\", \"model_name\": \"SmolVLA (450M) + ReconVLA argmin selection\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin selection) as baseline for ACR-VLA comparison\", \"fixes_applied\": [\"BDDL path: use benchmark_instance.get_task_bddl_file_path()\", \"LIBERO assets copied from GitHub repo\"]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T11:07:20.019Z\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --auto --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --K 10\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32811\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_001-crm-smolvla.log\", \"submitted_at\": \"2026-05-13T04:54:14.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": 1000, \"model_name\": \"CRM (337K) + SmolVLA (450M)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\", \"hypothesis\": \"Per-DOF conformal features enable dimension-selective action correction on LIBERO\", \"wall_clock_seconds\": 2992.2, \"gpu_hours\": 0.83}, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-13T05:44:07.131Z\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"43809\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)\", \"seed\": 42, \"hypothesis\": \"Validate smolvla_libero checkpoint with fixed wrapper (correct state repr, 256x256 images, 7D action) achieves >50% success on libero_spatial\", \"log_path\": \"/tmp/eval_spatial_full.log\", \"checkpoint_source\": \"lerobot/smolvla_libero (HuggingFace community checkpoint)\", \"failure_reason\": \"smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization, state 6D→8D, state normalization, action denormalization all missing\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T15:45:51.082Z\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"197596\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log\", \"submitted_at\": \"2026-05-14T12:17:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D input, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"evaluate.py has no crm_obs_only mode. --mode acr_vla loads CRM expecting 1030D input but obs_only checkpoint has 990D (no conformal features). Replaced by eval-obs-only-spatial-v2.\", \"wall_clock_seconds\": 1392.5, \"gpu_hours\": 0.39}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"completed_at\": \"2026-05-14T12:40:23.205Z\", \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"229751\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:13:41.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 48315.0, \"gpu_hours\": 13.42}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:36:24.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:36:28.363366+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T20:38:56.577Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"gpu\": \"1\", \"pid\": 109650, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object (10 tasks x 10 rollouts)\", \"log_path\": \"logs/nohup_eval_object_perdof_norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:33.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:36:35.355Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:40.842032+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"144504\"}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:39:30.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:39:33.739829+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm02_seed43_r3.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:41:59.362Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 140759, \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:10:32.044Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:10:33.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:10:39.747200+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:08.945Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"wall_clock_seconds\": 70039.8, \"gpu_hours\": 19.46}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\", \"completed_at\": \"2026-05-16T00:48:05.254Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:35:42.126Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:35:43.889Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:35:47.235304+00:00\"}]}, \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}, \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"logs/eval_object_obs_only_norm005.json\", \"completed_at\": \"2026-05-16T08:19:41.189Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"note\": \"Code patched to print every rollout (was every 5). Prev attempts killed working processes due to misinterpreting silence as stuck.\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T02:58:54.670Z\"}, \"failure_reason\": \"Agent误杀：wchar未增长30s被误判为stuck，实际是每5 rollout打印一次（~7.5min间隔）且MuJoCo/CUDA使用memory-mapped I/O不被/proc/PID/io追踪。进程实际正常运行中。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:58:57.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T02:59:01.101476+00:00\"}]}}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"1\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"obs_only CRM v3-norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"pid\": 353384, \"tmux_session\": \"eval-direct-correction-object-seed42\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:38:55.611Z\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"226878\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T07:11:59.066Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_scalar_unc\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 51470.5, \"gpu_hours\": 14.3}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:11:40.494Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:11:48.900516+00:00\"}]}, \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-16T21:29:49.586Z\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:04.525Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 44 --n_rollouts 10 --output_file logs/eval_object_perdof_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:13:35.112Z\", \"training_hours\": 13.28}, \"spec\": {\"data_path\": \"LIBERO_object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\"}, \"pid\": \"452982\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:13:38.573783+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:27.956Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"501420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log\", \"submitted_at\": \"2026-05-16T14:49:19.300Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"pid\": 501420, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T15:21:56.018Z\", \"failure_reason\": \"r2 data valid (16%), r4 redundant. PID 501420 killed by worker at 2026-05-16T15:09.\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:32:36.214Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T15:28:27.588Z\", \"training_hours\": 13.93}, \"completed_at\": \"2026-05-16T01:34:17.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:28:32.358640+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"428117\", \"seed\": 44, \"model_name\": \"reconvla_argmin\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"spec\": {\"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"248860\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:47Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 972.5, \"gpu_hours\": 0.27}, \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\", \"failure_reason\": \"killed to resolve cuda:3 GPU conflict\", \"completed_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"390936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log\", \"submitted_at\": \"2026-05-16T02:11:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 24535.3, \"gpu_hours\": 6.82}, \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 105938, \"log_path\": \"logs/eval_object_perdof_norm003.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"parent\": \"eval-acr-object-v4-perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.14, \"per_task_range\": \"0.0-0.4\"}}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:09:00.286Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:09:03.327886+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\", \"completed_at\": \"2026-05-16T08:11:39.117Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 134094, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log\", \"submitted_at\": \"2026-05-15T17:38:21.517Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"wall_clock_seconds\": 48640.4, \"gpu_hours\": 13.51}, \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:19.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:22.516205+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"114664\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log\", \"submitted_at\": \"2026-05-15T16:03:30.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_scalar\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 50435.3, \"gpu_hours\": 14.01}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:01:42.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:01:45.993724+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"completed_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 121325, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10\", \"parent\": \"eval-acr-object-v4-obs-only\"}, \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:35:17.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:35:20.742243+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:02:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T05:05:30.084Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"310854\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"submitted_at\": \"2026-05-16T05:25:05.983Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"309346\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:05:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:05:34.587431+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"431189\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:30.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.0, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:20.095Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"430985\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:27.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.3, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"111709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log\", \"submitted_at\": \"2026-05-15T15:47:37.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"libero/object\", \"data_count\": 10, \"checkpoint_source\": null, \"eval_data\": \"object\", \"wall_clock_seconds\": 47139.2, \"gpu_hours\": 13.09}, \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:48:28.380Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:48:31.493092+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_object_perdof_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 365925, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log\", \"submitted_at\": \"2026-05-15T13:21:00.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO_object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 50078.9, \"gpu_hours\": 13.91}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:12:36.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:12:39.589841+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:29:36.987Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T01:30:26.640Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127 (command not found) — bash -c wrapping 或环境激活路径错误，bjb2-40593 上系统性问题，三个 seed44 实验全部同样失败\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:33.143Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:38.635650+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:29:31.218Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:14.217Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:20.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:23.773246+00:00\"}]}}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:29:25.990Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:04.115Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (argmin baseline)\", \"seed\": 44, \"checkpoint_source\": \"N/A (no CRM)\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:06.598Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:09.864458+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356490\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"submitted_at\": \"2026-05-15T12:00:38.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 46070.8, \"gpu_hours\": 12.8, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:41:25.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:42:01.902179+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"completed_at\": \"2026-05-16T00:48:29.446Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20250.8, \"gpu_hours\": 5.63}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}, \"completed_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"356696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log\", \"submitted_at\": \"2026-05-15T12:00:40.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (reconvla baseline)\", \"seed\": 43, \"checkpoint_source\": \"N/A (no CRM, pure VLA baseline)\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 45422.6, \"gpu_hours\": 12.62}, \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:35:16.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:19.825582+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"138858\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T19:19:36.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed — GPU conflict on cuda:2, replaced by eval-mag-perdof-norm02-seed43-object-r3)\", \"wall_clock_seconds\": 951.1, \"gpu_hours\": 0.26}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:35:27.220Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T06:44:02.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (EXIT_CODE=127, retried as eval-mag-obsonly-norm03-r2)\", \"wall_clock_seconds\": 46287.3, \"gpu_hours\": 12.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:44:32.019Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:44:35.317393+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\", \"completed_at\": \"2026-05-15T19:35:29.718Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 141024, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"checkpoint_path\": \"N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"132816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log\", \"submitted_at\": \"2026-05-15T19:14:01.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 809.4, \"gpu_hours\": 0.22}, \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"134532\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log\", \"submitted_at\": \"2026-05-15T19:14:52.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 755.5, \"gpu_hours\": 0.21}, \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. Paired with obs_only norm=0.2 seed=43 for statistical comparison at the best obs_only norm.\", \"parent\": \"eval-mag-perdof-norm02-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\", \"completed_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Retry of killed eval-mag-perdof-norm0p3-object. Completes perdof 5-point magnitude curve on object domain.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\", \"completed_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"7017\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log\", \"submitted_at\": \"2026-05-15T02:55:02.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58959.5, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"6746\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log\", \"submitted_at\": \"2026-05-15T02:54:59.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58960.3, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"69379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log\", \"submitted_at\": \"2026-05-13T18:58:07.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D015: evaluate.py env_args 缺少 camera_names，SmolVLA 只收到单摄像头输入，结果系统性偏低\", \"wall_clock_seconds\": 173971.8, \"gpu_hours\": 48.33}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-13T19:36:15.749Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:36:19.370112+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:26:37.521060+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:59:44.694612+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"63218\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard2.log\", \"submitted_at\": \"2026-05-13T17:39:04.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178705.9, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"63075\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard1.log\", \"submitted_at\": \"2026-05-13T17:39:02.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178706.7, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:29.293Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && rm -rf /root/autodl-tmp/crm_cache_v3 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"62930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard0.log\", \"submitted_at\": \"2026-05-13T17:39:00.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178707.5, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"57846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard2.log\", \"submitted_at\": \"2026-05-13T16:11:04.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.1, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"57706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard1.log\", \"submitted_at\": \"2026-05-13T16:11:02.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.5, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && rm -rf /root/autodl-tmp/crm_cache/spatial /root/autodl-tmp/crm_cache/object && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"57628\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard0.log\", \"submitted_at\": \"2026-05-13T16:11:01.605Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.0, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"127570\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log\", \"submitted_at\": \"2026-05-15T18:58:29.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"crm_perdof_v3_norm\", \"seed\": 42, \"wall_clock_seconds\": 885.6, \"gpu_hours\": 0.25}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:13:15.247Z\", \"failure_reason\": \"Duplicate of eval-mag-perdof-norm03-object (PID 118886 on bjb2-28827:cuda:3, identical params). Killed to free cuda:2.\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"144887\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log\", \"submitted_at\": \"2026-05-15T18:37:26.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1245.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\", \"failure_reason\": \"GPU conflict on bjb1-32546:cuda:4 (shared with obs-only-default). Killed lower priority perdof. Migrating to bjb2-28827:cuda:2 as r2.\", \"completed_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43.json\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Crashed after 1 task on bjb1-32546:cuda:3 (PID 118214). Reviewer confirmed. Restarting as r2.\", \"completed_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"107658\", \"log_path\": \"logs/eval_object_perdof_default_norm.log\", \"submitted_at\": \"2026-05-16T00:51:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 325264, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"submitted_at\": \"2026-05-15T06:50:02.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 37969.2, \"gpu_hours\": 10.55}, \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:20:31.567Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:20:34.907634+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"completed_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"spec\": {\"command\": \"python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\"}, \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\", \"gpu\": \"bjb1-32546:cuda:5\", \"pid\": 18808, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\", \"completed_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\", \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\"}, \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"13797\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"submitted_at\": \"2026-05-15T02:53:41.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47312.8, \"gpu_hours\": 13.14}, \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:59:31.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:59:34.042176+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:14.366Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"11116\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log\"}, \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --start_task 3\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 311881, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log\", \"submitted_at\": \"2026-05-15T05:14:33.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 70, \"model_name\": \"ACR-VLA CRM scalar_unc v3-norm (restart from T3)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 3-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 29034.3, \"gpu_hours\": 8.07}, \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:15:46.765Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:49.226583+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:18:27.853Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 312420, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"submitted_at\": \"2026-05-15T05:14:38.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 40, \"model_name\": \"ACR-VLA CRM obs_only v3-norm (restart from T6)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 6-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 21633.2, \"gpu_hours\": 6.01}, \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:15:39.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:15:44.340640+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"completed_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_spatial_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"341873\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-15T09:09:23.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 3117.4, \"gpu_hours\": 0.87}, \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_task 7\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 312150, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"submitted_at\": \"2026-05-15T05:14:36.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 30, \"model_name\": \"ACR-VLA CRM perdof v3-norm (restart from T7)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 7-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"wall_clock_seconds\": 14053.7, \"gpu_hours\": 3.9}, \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:05:27.552Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:05:31.321347+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"completed_at\": \"2026-05-15T09:08:50.017Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"N/A (stale duplicate entry)\", \"server\": \"bjb1-18228\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (stale duplicate entry, never ran)\", \"log_path\": \"N/A\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\", \"completed_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"329871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"submitted_at\": \"2026-05-15T07:11:15.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 360.6, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\", \"checkpoint_path\": \"N/A (killed before completion)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"completed_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint output)\", \"completed_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": 225144, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45Z\", \"submitted_via\": \"tmux (manual)\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:32:10.962Z\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --baseline_mode single --benchmark object --n_rollouts 10 --seed 42 --K 1 --output_file logs/eval_object_vla_only_k1.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"39397\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log\", \"submitted_at\": \"2026-05-15T05:11:22.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only K=1 single sample)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_source\": \"N/A (no CRM, single VLA sample)\", \"wall_clock_seconds\": 311.9, \"gpu_hours\": 0.09}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:16:34.574Z\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"212685\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log\", \"submitted_at\": \"2026-05-15T01:49:35.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, default max_correction_norm)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 6030.8, \"gpu_hours\": 1.68}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:31:26.353Z\", \"failure_reason\": \"D021: v2 checkpoint invalidated by crm_cache_v5 retraining. Replaced by eval-acr-spatial-v4-scalar on bjb1:2.\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"203217\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log\", \"submitted_at\": \"2026-05-14T22:29:03.489Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\", \"failure_reason\": \"Superseded by D020 plan. Default norm=1.42 already proven to degrade (v4-default: 0/5). Not needed. Process killed on bjb2 (PID 203222 confirmed dead).\", \"completed_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3 obs_only, default max_correction_norm=1.42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log\", \"tmux_session\": \"eval-acr-spatial-v4-obs-only\", \"pid\": 199257}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:16:04.414Z\", \"failure_reason\": \"Wrong checkpoint (crm_v3 not crm_v3_norm) + wrong max_correction_norm (1.42 not 0.1). Killed and replaced by eval-acr-spatial-v4-obs-only-r2.\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, default correction)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Process died. D019: 0/5 on task 1 confirmed default norm=1.42 still degrades. Replaced by eval-acr-spatial-v4-obs-only on cuda:0.\", \"completed_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (scalar_unc)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"/tmp/crm_train_scalar_unc.log\", \"completed_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (obs_only)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/tmp/crm_train_obs_only.log\", \"completed_at\": \"2026-05-14T22:05:28.289Z\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-337K-Normalized\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"no log file (tee failed, output was in tmux pane only)\", \"completed_at\": \"2026-05-14T20:05:20.181Z\", \"results\": {\"best_epoch\": 47, \"best_val_loss\": 0.03578, \"final_train_loss\": 0.04992, \"final_val_loss\": 0.03578, \"total_epochs\": 50, \"normalization\": \"per-feature input normalization (mean/std stored in crm_best.pt as input_mean/input_std tensors)\"}}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181896\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-scalar-unc.log\", \"submitted_at\": \"2026-05-14T18:05:00.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1917.7, \"gpu_hours\": 0.53}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:15.107Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:19.071535+00:00\"}]}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:36:58.566Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181973\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"submitted_at\": \"2026-05-14T18:05:02.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/spatial\", \"data_count\": 2402, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1802.8, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:22.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:25.410071+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"completed_at\": \"2026-05-14T18:35:05.626Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181668\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"submitted_at\": \"2026-05-14T18:04:54.446Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1510.3, \"gpu_hours\": 0.42}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:11.506Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:13.038696+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:30:04.713Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"211961\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:49:43.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:2 for eval-tiny-correction-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"wall_clock_seconds\": 17890.8, \"gpu_hours\": 4.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"197324\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:17:08.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"CRM v2 scalar-uncertainty + SmolVLA K=10\", \"seed\": 42, \"hypothesis\": \"Scalar uncertainty CRM ablation — tests whether per-DOF conformal is superior to scalar aggregated uncertainty for action correction.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:1 for eval-argmin-only-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"wall_clock_seconds\": 19844.9, \"gpu_hours\": 5.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:53.188Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"121984\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty)\", \"seed\": 42, \"hypothesis\": \"CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001 (bs=32/lr=1e-3).\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"conclusion_note\": \"Training converged. scalar val_loss 0.008379 < per-DOF 0.009046 — original hypothesis (scalar w
```

---

### Large event (continued)

````text
orse) NOT confirmed on val_loss. Hypothesis pending eval-scalar-unc-spatial task success rate validation.\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}, \"completed_at\": \"2026-05-14T02:21:00.891Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 --input_mode obs_only --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-obs_only\", \"seed\": 42, \"hypothesis\": \"CRM without conformal features (obs_only, 990D input) performs significantly worse than full CRM (1030D), validating that per-DOF conformal features are necessary for effective correction\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:43:51.534Z\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"78520\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v1.log\", \"data_path\": \"/root/autodl-tmp/crm_cache/ (spatial: 12167 + object: 14570 = 26737 samples)\", \"data_count\": 26737, \"model_name\": \"CRM MLP (337K params, 1030D→256→256→30D)\", \"seed\": 42, \"hypothesis\": \"CRM with per-DOF conformal features (1030D input) learns dimension-selective correction, achieving lower action MSE than scalar/no-uncertainty ablations\", \"checkpoint_source\": \"precompute-v4 (spatial+object)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:40:27.930Z\"}, \"failure_reason\": \"RESOLVED: EXIT_CODE=129 was SIGHUP after training completed (50/50 epochs). Not a real failure.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T22:40:28.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:40:29.429643+00:00\"}]}, \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ --output_dir /root/autodl-tmp/checkpoints/crm/k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"139839\", \"data_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"data_count\": 26737, \"model_name\": \"CRM (K=5, 337K params)\", \"seed\": 42, \"hypothesis\": \"CRM with K=5 conformal samples for K sensitivity ablation (K=10 baseline val_loss=0.009046)\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/k5/train.log\", \"checkpoint_source\": \"from_scratch\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:12:42.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:12:44.286094+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}, \"completed_at\": \"2026-05-14T07:21:32.072Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"spec\": {\"hypothesis\": \"Scalar CRM (3D unc) vs per-DOF CRM (40D unc) on spatial task success rate. Val_loss favored scalar (0.008 vs 0.009) but per-DOF expected to win on task success via dimension-selective correction.\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty, 327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"143206\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch). Scalar CRM trained on wrong features. Replaced by eval-scalar-unc-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:15.933Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:31:30.005Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:31:31.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:31:32.734610+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"117814\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM per-DOF)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log\", \"hypothesis\": \"ACR-VLA per-DOF correction improves over SmolVLA baseline on spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM trained on wrong features + CGS quantile wrong. Replaced by eval-acr-spatial-v3.\"}, \"conclusion\": \"killed\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"spec\": {\"command\": \"MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"154189\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA K=5 (CRM 337K + SmolVLA 450M)\", \"seed\": 42, \"hypothesis\": \"K=5 vs K=10 ACR-VLA on task success rate.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-k5-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM K=5 trained on wrong features. Replaced by eval-k5-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:14.685Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (single inference per step)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\", \"failure_reason\": \"Duplicate entry — same PID 125830 tracked by eval-object-v8-full. Cleaning up.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:03:28.470Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:09.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:11.481851+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:03:30.351859+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"117486\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v6-full.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with fixed evaluate.py (reset→set_init_state→zero-action)\", \"failure_reason\": \"vla_only mode running K=10 instead of K=1, wasting GPU. Killed and restarted with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:43:52.899Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T23:43:53.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:43:56.187212+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 117697, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"gpu\": \"cuda:0\", \"note\": \"restored from false DONE/failed — cron misdetected tmux pipe buffering as process exit\", \"failure_reason\": \"vla_only mode running K=10 multi-sampling (should be K=1). Killed by Director order, replaced by eval-object-v7-full with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/acr_vla_spatial_v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO spatial benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM perdof)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial, 10 tasks x 10 rollouts\", \"parent\": \"train-crm-v1\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信。已被 eval-acr-spatial-v2 替代\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:13:00.422Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-acr-spatial-v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:38.077Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:40.252Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified-deployed wrapper achieves meaningful success rate on libero_object\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.017Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"73756\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified wrapper + dual camera (agentview + eye_in_hand) achieves >50% on libero_spatial\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.445Z\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"62654\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log\", \"submitted_at\": \"2026-05-13T17:38:57.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, rewritten wrapper aligned with lerobot pipeline)\", \"seed\": 42, \"hypothesis\": \"Rewritten wrapper (fully aligned with lerobot SmolVLAPolicy) achieves >50% on libero_spatial with 10 rollouts\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 5403.4, \"gpu_hours\": 1.5}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"87385\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned)\", \"seed\": 42, \"hypothesis\": \"Fixed wrapper (7 bugs) achieves >50% on libero_spatial\", \"log_path\": \"/tmp/eval_spatial.log\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"Killed by Director - wrapper not fully fixed, 55.6% result unreliable. Redirected to full wrapper rewrite aligned with lerobot pipeline.\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T16:14:40.934Z\"}}, \"count\": 850, \"total\": 850, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2039}}"
    }
  }
}
```

&lt;/details>

---


````

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cy8emmaHUsGLHrhSgHhLnL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt | python3 -c \"\nimport json,sys\nd = json.load(sys.stdin)\nres = json.loads(d['result']) if isinstance(d.get('result'),str) else d['result']\nprint(f'total experiments: {len(res)}')\n# Filter Goal/Object\nfor e in res:\n    name = e.get('name','')\n    if 'goal' in name.lower() or 'object' in name.lower():\n        print(name)\n\" | head -100",
  "description": "Parse registry for Goal/Object experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "d6ba7e99-77e8-45ce-9e82-59fb289af2b1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QiVYFHdu7vd6N98LmW1BUL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 37402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 683
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-25T01:51:18.743Z_

<details><summary>↩ Tool result · `toolu_01Cy8emmaHUsGLHrhSgHhLnL`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    name = e.get('name','')
           ^^^^^
AttributeError: 'str' object has no attribute 'get'
total experiments: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "1ac459ab-9c28-4284-a87f-232e3f0572b6",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    name = e.get('name','')\n           ^^^^^\nAttributeError: 'str' object has no attribute 'get'\ntotal experiments: 4",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01T5JWNKMpm3xuKmbnPn3Tss`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt | python3 -c \"\nimport json,sys\nd = json.load(sys.stdin)\nprint(type(d), list(d.keys()) if isinstance(d, dict) else 'list')\nprint(d.get('result') if isinstance(d,dict) else d)\" 2>&1 | head -50",
  "description": "Inspect file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7367ef61-1644-4d8c-9293-0133523cbd5b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Gqc9oTgwE7D91G1b8QwYjA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 38085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-25T01:51:23.124Z_

<details><summary>↩ Tool result · `toolu_01T5JWNKMpm3xuKmbnPn3Tss`</summary>

```text
&lt;persisted-output>
Output too large (1.1MB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bzssvbyrc.txt

Preview (first 2KB):
&lt;class 'dict'> ['result']
{"success": true, "data": {"experiments": {"eval-k2-tau020-spatial-s42": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-24T21:37:23.017Z", "updated_at": "2026-05-25T01:04:28.781Z", "hypothesis": "K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).", "spec": {"command": "python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20", "server": "bjb1-32546", "gpu": ["cuda:1"], "pid": "788081", "log_path": "~/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log", "submitted_at": "2026-05-24T21:57:59.368Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "model_name": "SmolVLA+CRM", "seed": 42, "data_path": "LIBERO-Spatial", "data_count": 200, "wall_clock_seconds": 10936.2, "gpu_hours": 3.04}, "reproduce": {"finished_at": "2026-05-25T01:00:11.989Z"}, "failure_reason": "", "conclusion": "success", "completed_at": "2026-05-25T01:00:15.617Z", "extra": {"hook_events": [{"event": "on_failed", "action": "agent", "ts": "2026-05-25T01:00:41.988514+00:00"}]}, "metrics": {"SR": 0.805, "trigger_rate": 0.262, "mean_unc": 0.1862}, "notes": "Cron 报告 EXIT_CODE=124，但日志分析显示 τ=0.20 eval 已完成 (SR=80.5%, 161/200)。超时发生在同 tmux session 继续跑 τ=0.25 时。数据完整，纠正为 success。", "log_path": "bjb1-32546:/root/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log", "checkpoint_path": "N/A (eval only)"}, "eval-k2-tau030-spatial-s42": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-24T21:37:30.605Z", "updated_at": "2026-05-25T00:52:29.111Z", "hypothesis": "K=2 τ-sweep: τ=0.30 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.", "spec": {"command": "python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.30 --benchmark spatial --seed 42 --n_rollouts 20", "server": "bjb2-28827", "gpu": ["cuda:1
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "792de43f-8c76-4162-9a57-56c8d7489b32",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'> ['result']\n{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T21:37:23.017Z\", \"updated_at\": \"2026-05-25T01:04:28.781Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\", \"spec\": {\"command\": \"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"788081\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-24T21:57:59.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"wall_clock_seconds\": 10936.2, \"gpu_hours\": 3.04}, \"reproduce\": {\"finished_at\": \"2026-05-25T01:00:11.989Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T01:00:15.617Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T01:00:41.988514+00:00\"}]}, \"metrics\": {\"SR\": 0.805, \"trigger_rate\": 0.262, \"mean_unc\": 0.1862}, \"notes\": \"Cron 报告 EXIT_CODE=124，但日志分析显示 τ=0.20 eval 已完成 (SR=80.5%, 161/200)。超时发生在同 tmux session 继续跑 τ=0.25 时。数据完整，纠正为 success。\", \"log_path\": \"bjb1-32546:/root/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T21:37:30.605Z\", \"updated_at\": \"2026-05-25T00:52:29.111Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.30 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\", \"spec\": {\"command\": \"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.30 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"475008\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-k2-tau030-spatial-s42.log\", \"submitted_at\": \"2026-05-24T21:58:05.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"wall_clock_seconds\": 10455.0, \"gpu_hours\": 2.9}, \"conclusion\": \"success\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau030-spatial-s42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-25T00:52:20.968Z\", \"metrics\": {\"SR\": 0.8, \"success\": 160, \"total\": 200, \"mean_unc\": 0.1924, \"trigger_rate\": 0.169}}, \"eval-k2-tau010-spatial-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:28:29.356Z\", \"updated_at\": \"2026-05-25T00:52:12.177Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. Retry after first attempt failed (conda not activated). Expect high trigger rate at low τ.\", \"spec\": {\"command\": \"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.10 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"327574\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-k2-tau010-spatial-s42-r2.log\", \"submitted_at\": \"2026-05-24T23:28:41.167Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"wall_clock_seconds\": 5011.0, \"gpu_hours\": 1.39}, \"conclusion\": \"killed\", \"log_path\": \"bjb2-40593:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-25T00:52:12.177Z\"}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:44:07.720Z\", \"updated_at\": \"2026-05-25T00:46:32.035Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial (seed 45, 20 rollouts). Replicate seed for variance estimation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 45 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 45}, \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\", \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"metrics\": {\"overall_success_rate\": 0.85, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:46:32.035Z\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:44:04.114Z\", \"updated_at\": \"2026-05-25T00:46:23.539Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object (seed 44, 20 rollouts). Replicate seed for variance estimation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 44}, \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\", \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:46:23.539Z\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T00:43:50.844Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object (seed 43, 20 rollouts). Replicate seed for variance estimation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"388306\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\", \"submitted_at\": \"2026-05-24T18:18:30.109Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"wall_clock_seconds\": 23120.7, \"gpu_hours\": 6.42}, \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\", \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:43:50.844Z\"}, \"eval-k2-tau015-spatial-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T21:37:19.297Z\", \"updated_at\": \"2026-05-25T00:42:00.480Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.15 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\", \"spec\": {\"command\": \"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.15 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"319989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-k2-tau015-spatial-s42.log\", \"submitted_at\": \"2026-05-24T22:41:32.830Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"wall_clock_seconds\": 7227.6, \"gpu_hours\": 2.01}, \"reproduce\": {\"finished_at\": \"2026-05-25T00:41:48.995Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-25T00:42:00.480Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T00:42:18.633856+00:00\"}]}}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:20.358Z\", \"updated_at\": \"2026-05-25T00:37:52.191Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal (seed 43, 20 rollouts). Replicate seed for variance estimation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"574597\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s43.log\", \"submitted_at\": \"2026-05-24T18:18:17.275Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 22774.9, \"gpu_hours\": 6.33}, \"reproduce\": {\"finished_at\": \"2026-05-24T23:54:22.850Z\"}, \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:37:52.191Z\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:16.938Z\", \"updated_at\": \"2026-05-25T00:37:45.363Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal (seed 42, 20 rollouts). Establishes pi0.5 goal-conditioned baseline for ablation against conformal refinement.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"574188\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s42.log\", \"submitted_at\": \"2026-05-24T18:18:09.640Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 22775.7, \"gpu_hours\": 6.33}, \"reproduce\": {\"finished_at\": \"2026-05-24T23:54:12.290Z\"}, \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:37:45.363Z\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:23.924Z\", \"updated_at\": \"2026-05-25T00:37:38.379Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object (seed 42, 20 rollouts). Establishes pi0.5 object-manipulation baseline.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"574940\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42.log\", \"submitted_at\": \"2026-05-24T18:18:23.857Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 22754.5, \"gpu_hours\": 6.32}, \"reproduce\": {\"finished_at\": \"2026-05-24T23:54:33.223Z\"}, \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:37:38.379Z\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:13.434Z\", \"updated_at\": \"2026-05-25T00:37:31.347Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial (seed 43, 20 rollouts). Replicate seed for variance estimation of pi0.5 baseline.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"573908\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s43.log\", \"submitted_at\": \"2026-05-24T18:18:00.844Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 22770.5, \"gpu_hours\": 6.33}, \"reproduce\": {\"finished_at\": \"2026-05-24T23:54:01.363Z\"}, \"metrics\": {\"overall_success_rate\": 0.96, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:37:31.347Z\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:09.880Z\", \"updated_at\": \"2026-05-25T00:35:32.912Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial (seed 42, 20 rollouts). Establishes pi0.5 baseline success rate without conformal refinement, for comparison against reconvla/adaptive modes. Tests whether evaluate.py correctly handles --model pi05 with obs_dim=2048.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"573629\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s42.log\", \"submitted_at\": \"2026-05-24T18:17:54.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 19898.5, \"gpu_hours\": 5.53}, \"metrics\": {\"overall_success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-spatial-s42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T23:49:32.815Z\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:39.365Z\", \"updated_at\": \"2026-05-25T00:35:13.584Z\", \"hypothesis\": \"SmolVLA crm_obs_only baseline on LIBERO-Goal seed48 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 48 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": 5, \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"tmux_session\": \"eval-crm-goal-s48\", \"log_path\": \"logs/eval-supp-crm-norm005-goal-s48.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T23:57:48.080Z\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:35.264Z\", \"updated_at\": \"2026-05-25T00:35:09.845Z\", \"hypothesis\": \"SmolVLA crm_obs_only baseline on LIBERO-Spatial seed49 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 49 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": 4, \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"tmux_session\": \"eval-crm-spatial-s49\", \"log_path\": \"logs/eval-supp-crm-norm005-spatial-s49.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T23:57:34.278Z\", \"metrics\": {\"overall_success_rate\": 0.785, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:31.569Z\", \"updated_at\": \"2026-05-25T00:35:06.130Z\", \"hypothesis\": \"SmolVLA crm_obs_only baseline on LIBERO-Spatial seed48 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": 0, \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"tmux_session\": \"eval-crm-spatial-s48\", \"log_path\": \"logs/eval-supp-crm-norm005-spatial-s48.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T23:57:20.702Z\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}, \"eval-supp-long-vla-only-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:21:06.247Z\", \"updated_at\": \"2026-05-24T23:58:15.416Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Long seed43 (re-run after previous killed). Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark long --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": 5, \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"tmux_session\": \"eval-long-vla-s43\", \"log_path\": \"logs/eval-supp-long-vla-only-s43.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:58:15.416Z\"}, \"eval-supp-goal-vla-only-s42-bjb1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:21:02.585Z\", \"updated_at\": \"2026-05-24T23:58:01.748Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal seed42, parallel re-run on bjb1 (original at cqa1-32758 still running). Provides redundant data for Table 1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": 4, \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"tmux_session\": \"eval-goal-vla-s42\", \"log_path\": \"logs/eval-supp-goal-vla-only-s42.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:58:01.748Z\"}, \"crm-norm005-goal-s49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:18.196Z\", \"updated_at\": \"2026-05-24T23:57:07.110Z\", \"hypothesis\": \"SmolVLA CRM (obs_only, ε=0.05) on LIBERO-Goal seed49. Fills CRM coverage gap for Table 1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 49 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": \"2\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-goal-s49.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:57:07.110Z\"}, \"eval-supp-obj-vla-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:13.529Z\", \"updated_at\": \"2026-05-24T23:56:53.275Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object seed44. Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": 3, \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"tmux_session\": \"eval-obj-vla-s44\", \"log_path\": \"logs/eval-supp-obj-vla-only-s44.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:56:53.275Z\"}, \"crm-norm005-object-s48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:08.294Z\", \"updated_at\": \"2026-05-24T23:56:39.546Z\", \"hypothesis\": \"SmolVLA CRM (obs_only, ε=0.05) on LIBERO-Object seed48. Fills CRM coverage gap for Table 1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 48 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": \"1\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-obj-s48.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:56:39.546Z\"}, \"eval-supp-obj-vla-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:19:02.892Z\", \"updated_at\": \"2026-05-24T23:56:25.825Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object seed43. Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode vla_only --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": 2, \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"tmux_session\": \"eval-obj-vla-s43\", \"log_path\": \"logs/eval-supp-obj-vla-only-s43.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:56:25.825Z\"}, \"eval-supp-obj-vla-only-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:18:57.232Z\", \"updated_at\": \"2026-05-24T23:56:12.064Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object seed42. Fills Table 1 data gap for multi-seed statistical analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": 0, \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"tmux_session\": \"eval-obj-vla-s42\", \"log_path\": \"logs/eval-supp-obj-vla-only-s42.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:56:12.065Z\"}, \"eval-supp-long-vla-only-s48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:42:16.585Z\", \"updated_at\": \"2026-05-24T23:55:58.423Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 48. Long baseline sweep is complete for s42-s47; s48 extends to high seed for additional statistical power on the hardest benchmark.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark long --seed 48 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": 5, \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_long\", \"tmux_session\": \"eval-long-vla-only-s48\", \"log_path\": \"logs/eval-supp-long-vla-only-s48.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:55:58.423Z\"}, \"eval-supp-goal-vla-only-s50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:42:13.100Z\", \"updated_at\": \"2026-05-24T23:55:44.927Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 50. Extension high seed beyond s42-s49 sweep for additional Goal baseline statistical power; pairs with potential future Adaptive Goal s50.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 50 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": 4, \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_goal\", \"tmux_session\": \"eval-goal-vla-only-s50\", \"log_path\": \"logs/eval-supp-goal-vla-only-s50.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:55:44.927Z\"}, \"eval-supp-goal-vla-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:38:56.218Z\", \"updated_at\": \"2026-05-24T23:55:31.142Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 44. Goal baseline sweep missing s42-s47; s44 completes mid-range seeds for paired Adaptive vs VLA-only comparison on Goal.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": 3, \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_goal\", \"tmux_session\": \"eval-goal-vla-only-s44\", \"log_path\": \"logs/eval-supp-goal-vla-only-s44.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:55:31.142Z\"}, \"eval-supp-spatial-vla-only-smolvla-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:37:31.823Z\", \"updated_at\": \"2026-05-24T23:55:17.604Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Spatial seed 42. Re-deploy after PREPARING-stuck entry on bjb1-18228 (which actually ran pi05 not smolvla). Missing smolvla spatial s42 baseline for paired CRM/Adaptive comparisons at seed 42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": 1, \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_spatial\", \"tmux_session\": \"eval-spatial-vla-only-s42\", \"log_path\": \"logs/eval-spatial-vla-only-s42-cqa1.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:55:17.604Z\"}, \"eval-supp-goal-vla-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:35:37.364Z\", \"updated_at\": \"2026-05-24T23:55:03.748Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 43. Replicate seed for Goal baseline variance estimation; needed to support paired Adaptive vs VLA-only statistical comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": 2, \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_goal\", \"tmux_session\": \"eval-goal-vla-only-s43\", \"log_path\": \"logs/eval-supp-goal-vla-only-s43.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T23:55:03.748Z\"}, \"ev",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bzssvbyrc.txt",
    "persistedOutputSize": 1147407
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01U9hyEwiJftmBeZQEytjqmv`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt | python3 -c \"\nimport json,sys\nd = json.load(sys.stdin)\nr = json.loads(d['result'])\nexps = r['data']['experiments']\nprint(f'total: {len(exps)}')\n# Filter Goal/Object\nfor k,e in exps.items():\n    if 'goal' in k.lower() or 'object' in k.lower():\n        print(k)\n\" 2>&1 | head -200",
  "description": "List Goal/Object experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "bef60f59-76cb-4ac9-a944-46f42060af16",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01ACP6WqKTMuHDzdm6Ei7Va8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 38535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1543
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-25T01:51:28.169Z_

<details><summary>↩ Tool result · `toolu_01U9hyEwiJftmBeZQEytjqmv`</summary>

```text
total: 850
eval-pi05-vla-only-object-s44
eval-pi05-vla-only-object-s43
eval-pi05-vla-only-goal-s43
eval-pi05-vla-only-goal-s42
eval-pi05-vla-only-object-s42
eval-supp-crm-norm005-goal-s48
eval-supp-goal-vla-only-s42-bjb1
crm-norm005-goal-s49
crm-norm005-object-s48
eval-supp-goal-vla-only-s50
eval-supp-goal-vla-only-s44
eval-supp-goal-vla-only-s43
eval-supp-goal-vla-only-s42
eval-supp-vla-only-goal-s49
eval-supp-vla-only-goal-s48
eval-supp-goal-vla-only-s45
eval-pi05-vla-only-object-seed43-r4
eval-a1-baseline-object-s42
eval-supp-goal-k2mean-s47
eval-supp-goal-adapt-tau025-s47
eval-supp-goal-crm-norm005-s47
eval-supp-goal-reconvla-s47
eval-supp-goal-vla-only-s47-r3
precompute-pi05-object-2048-r2
eval-openvla-object-vla-only-seed42-v3
train-crm-pi05-goal-k1
eval-supp-goal-vla-only-s47-r2
eval-supp-goal-vla-only-s47
crm-train-openvla-k1-multiscale-object
precompute-pi05-goal-2048-r2
precompute-smolvla-goal-bjb1-32546
eval-supp-goal-vla-only-s46
eval-supp-goal-reconvla-s46
eval-perdof-object-norm003-seed44
eval-supp-goal-vla-only-wrapper-s44
eval-pi05-vla-only-object-seed42
eval-pi05-vla-only-object-seed43
eval-pi05-vla-only-object-seed44
eval-supp-goal-k2mean-s46
eval-supp-goal-adapt-tau025-s46
eval-supp-goal-crm-norm005-s46
eval-supp-goal-k2mean-s45
eval-supp-goal-reconvla-s45
eval-supp-goal-crm-norm005-s45
eval-supp-goal-adapt-tau025-s45
eval-ablation-tau040-goal-s42
eval-ablation-tau015-goal-s42
eval-supp-k2mean-object-s44
eval-ablation-tau010-goal-s42
eval-supp-goal-vla-only-wrapper-s44-r2
eval-supp-k2mean-goal-s44
eval-supp-goal-vla-only-wrapper-s43
eval-supp-goal-reconvla-s44
eval-supp-crm-norm005-goal-s44
eval-supp-k2mean-object-s43
eval-supp-k2mean-goal-s42-r2
eval-supp-adapt-tau025-goal-s44
eval-supp-adapt-tau025-goal-s43
eval-supp-crm-norm005-goal-s43
eval-supp-goal-reconvla-s43
eval-supp-k2mean-goal-s43
eval-supp-k2mean-object-s42
eval-supp-goal-adapt-tau025-s42
eval-supp-goal-crm005-s42
eval-supp-goal-reconvla-s42
eval-goal-vla-only-wrapper-s42
eval-supp-k2mean-goal-s42
eval-object-vla-only-wrapper-s44-r2
eval-object-vla-only-wrapper-s43-r2
eval-object-vla-only-wrapper-s42-r2
eval-openvla-object-baseline-seed42-r2
eval-obs-only-object-norm02-seed55
precompute-pi05-features-object
precompute-smolvla-goal-shard2
precompute-smolvla-goal-shard1
precompute-smolvla-goal-shard0
eval-smolvla-crm-goal-seed42-v1
eval-smolvla-crm-goal-seed43-v1
eval-smolvla-crm-goal-seed44-v1
eval-object-vla-only-wrapper-s44
eval-object-vla-only-wrapper-s43
eval-object-vla-only-wrapper-s42
precompute-pi05-goal-2048
precompute-pi05-object-2048
eval-smolvla-crm-object-seed43-v1
eval-smolvla-crm-object-seed42-v1
eval-smolvla-crm-object-seed44-v1
eval-smolvla-crm-goal-seed43
eval-smolvla-crm-goal-seed42
eval-smolvla-lerobot-goal-seed44-v3
eval-smolvla-lerobot-goal-seed43-v3
eval-smolvla-lerobot-goal-seed43-v2
eval-smolvla-lerobot-object-seed44-v2
eval-smolvla-lerobot-object-seed43-v2
eval-smolvla-lerobot-goal-seed43
eval-smolvla-lerobot-object-seed44
eval-smolvla-lerobot-object-seed43
eval-pi05-crm-object-seed44
eval-pi05-crm-object-seed43
eval-pi05-crm-object-seed42
eval-pi05-vla-only-goal-seed44-r4-std
eval-pi05-vla-only-goal-seed42-r4-std
eval-pi05-vla-only-goal-seed43-r4-std
eval-pi05-vla-only-goal-seed42-r4
precompute-smolvla-goal-bjb2-28827
eval-pi05-vla-only-goal-seed44-r4
eval-pi05-vla-only-goal-seed43-r4
eval-openvla-oft-official-object
eval-pi05-vla-only-object-seed44-r4
eval-smolvla-lerobot-official-object
eval-pi05-vla-only-object-seed42-r4
eval-loss-perdof-object-seed42
eval-loss-combined-object-seed42
eval-loss-conformal-object-seed42
eval-loss-mse-object-seed42
eval-openvla-oft-object-baseline-seed42
precompute-smolvla-goal-bjb1-18228
eval-smolvla-acr-goal-seed43
eval-smolvla-crm-goal-seed44-v2
eval-smolvla-acr-goal-seed42
crm-train-pi05-object-full
crm-train-pi05-object
eval-pi05-vla-only-object-seed44-r3
eval-pi05-vla-only-object-seed43-r3
eval-pi05-vla-only-object-seed42-r3
eval-k20-obs-only-object-seed45
eval-obs-only-object-norm003-seed66
eval-obs-only-object-norm01-seed66
eval-obs-only-object-norm005-seed66
eval-obs-only-object-norm003-seed67
eval-k20-obs-only-object-seed44
eval-k20-obs-only-object-seed43
eval-k20-obs-only-object-seed42
eval-crm-object-k20-seed44
eval-crm-object-k20-seed42
eval-obs-only-object-norm02-seed53
eval-obs-only-object-norm02-seed52
eval-obs-only-object-norm02-seed51
eval-obs-only-object-norm02-seed50
eval-obs-only-object-norm02-seed48-r2
eval-obs-only-object-norm02-seed47
eval-obs-only-object-norm02-seed46
eval-obs-only-object-norm02-seed45
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed43-r3
eval-obs-only-object-norm02-seed43-r2
eval-obs-only-object-norm005-seed67
eval-obs-only-object-norm01-seed67
eval-vla-only-object-seed50
eval-vla-only-object-seed49
eval-vla-only-object-seed48
eval-vla-only-object-seed46
eval-vla-only-object-seed45
eval-vla-only-object-seed44-r2
eval-plan-a-object-seed42
eval-vla-only-object-seed43
eval-vla-only-object
eval-plan-a-object-seed44
eval-plan-a-object-seed43
eval-random-selection-object-seed44
eval-random-selection-object-seed43
eval-obs-only-object-norm01-seed60
eval-pi05-baseline-object-seed42
eval-obs-only-object-norm01-seed54
eval-obs-only-object-norm01-seed53
eval-obs-only-object-norm01-seed52
eval-obs-only-object-norm01-seed50
eval-obs-only-object-norm01-seed49
eval-obs-only-object-norm01-seed48
eval-obs-only-object-norm01-seed47
eval-obs-only-object-norm01-seed45-r2
eval-obs-only-object-norm01-seed44
eval-obs-only-object-norm005-seed55
eval-obs-only-object-norm005-seed50
eval-obs-only-object-norm005-seed49
eval-obs-only-object-norm005-seed48
eval-obs-only-object-norm005-seed47
eval-obs-only-object-norm005-seed44
eval-obs-only-object-norm005-seed43-r2
eval-obs-only-object-norm005-seed43
eval-obs-only-object-norm003-seed48
eval-obs-only-object-norm003-seed47-r2
eval-obs-only-object-norm003-seed46
eval-obs-only-object-norm003-seed45
eval-obs-only-object-norm003-seed44-bjb2
eval-obs-only-object-norm003-seed44
eval-obs-only-object-norm003-seed43-r2
eval-obs-only-object-norm003-seed43
eval-obs-only-object-norm01-seed57
eval-obs-only-object-norm005-seed65
eval-obs-only-object-norm005-seed61
eval-obs-only-object-norm005-seed58
eval-obs-only-object-norm003-seed59
eval-obs-only-object-norm003-seed56
eval-obs-only-object-norm005-seed75
eval-obs-only-object-norm01-seed74
eval-obs-only-object-norm005-seed72
eval-obs-only-object-norm003-seed63-r2
eval-obs-only-object-norm01-seed71
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "cf450dfc-9ae3-4247-a052-57d9b7df7299",
  "tool_use_result": {
    "stdout": "total: 850\neval-pi05-vla-only-object-s44\neval-pi05-vla-only-object-s43\neval-pi05-vla-only-goal-s43\neval-pi05-vla-only-goal-s42\neval-pi05-vla-only-object-s42\neval-supp-crm-norm005-goal-s48\neval-supp-goal-vla-only-s42-bjb1\ncrm-norm005-goal-s49\ncrm-norm005-object-s48\neval-supp-goal-vla-only-s50\neval-supp-goal-vla-only-s44\neval-supp-goal-vla-only-s43\neval-supp-goal-vla-only-s42\neval-supp-vla-only-goal-s49\neval-supp-vla-only-goal-s48\neval-supp-goal-vla-only-s45\neval-pi05-vla-only-object-seed43-r4\neval-a1-baseline-object-s42\neval-supp-goal-k2mean-s47\neval-supp-goal-adapt-tau025-s47\neval-supp-goal-crm-norm005-s47\neval-supp-goal-reconvla-s47\neval-supp-goal-vla-only-s47-r3\nprecompute-pi05-object-2048-r2\neval-openvla-object-vla-only-seed42-v3\ntrain-crm-pi05-goal-k1\neval-supp-goal-vla-only-s47-r2\neval-supp-goal-vla-only-s47\ncrm-train-openvla-k1-multiscale-object\nprecompute-pi05-goal-2048-r2\nprecompute-smolvla-goal-bjb1-32546\neval-supp-goal-vla-only-s46\neval-supp-goal-reconvla-s46\neval-perdof-object-norm003-seed44\neval-supp-goal-vla-only-wrapper-s44\neval-pi05-vla-only-object-seed42\neval-pi05-vla-only-object-seed43\neval-pi05-vla-only-object-seed44\neval-supp-goal-k2mean-s46\neval-supp-goal-adapt-tau025-s46\neval-supp-goal-crm-norm005-s46\neval-supp-goal-k2mean-s45\neval-supp-goal-reconvla-s45\neval-supp-goal-crm-norm005-s45\neval-supp-goal-adapt-tau025-s45\neval-ablation-tau040-goal-s42\neval-ablation-tau015-goal-s42\neval-supp-k2mean-object-s44\neval-ablation-tau010-goal-s42\neval-supp-goal-vla-only-wrapper-s44-r2\neval-supp-k2mean-goal-s44\neval-supp-goal-vla-only-wrapper-s43\neval-supp-goal-reconvla-s44\neval-supp-crm-norm005-goal-s44\neval-supp-k2mean-object-s43\neval-supp-k2mean-goal-s42-r2\neval-supp-adapt-tau025-goal-s44\neval-supp-adapt-tau025-goal-s43\neval-supp-crm-norm005-goal-s43\neval-supp-goal-reconvla-s43\neval-supp-k2mean-goal-s43\neval-supp-k2mean-object-s42\neval-supp-goal-adapt-tau025-s42\neval-supp-goal-crm005-s42\neval-supp-goal-reconvla-s42\neval-goal-vla-only-wrapper-s42\neval-supp-k2mean-goal-s42\neval-object-vla-only-wrapper-s44-r2\neval-object-vla-only-wrapper-s43-r2\neval-object-vla-only-wrapper-s42-r2\neval-openvla-object-baseline-seed42-r2\neval-obs-only-object-norm02-seed55\nprecompute-pi05-features-object\nprecompute-smolvla-goal-shard2\nprecompute-smolvla-goal-shard1\nprecompute-smolvla-goal-shard0\neval-smolvla-crm-goal-seed42-v1\neval-smolvla-crm-goal-seed43-v1\neval-smolvla-crm-goal-seed44-v1\neval-object-vla-only-wrapper-s44\neval-object-vla-only-wrapper-s43\neval-object-vla-only-wrapper-s42\nprecompute-pi05-goal-2048\nprecompute-pi05-object-2048\neval-smolvla-crm-object-seed43-v1\neval-smolvla-crm-object-seed42-v1\neval-smolvla-crm-object-seed44-v1\neval-smolvla-crm-goal-seed43\neval-smolvla-crm-goal-seed42\neval-smolvla-lerobot-goal-seed44-v3\neval-smolvla-lerobot-goal-seed43-v3\neval-smolvla-lerobot-goal-seed43-v2\neval-smolvla-lerobot-object-seed44-v2\neval-smolvla-lerobot-object-seed43-v2\neval-smolvla-lerobot-goal-seed43\neval-smolvla-lerobot-object-seed44\neval-smolvla-lerobot-object-seed43\neval-pi05-crm-object-seed44\neval-pi05-crm-object-seed43\neval-pi05-crm-object-seed42\neval-pi05-vla-only-goal-seed44-r4-std\neval-pi05-vla-only-goal-seed42-r4-std\neval-pi05-vla-only-goal-seed43-r4-std\neval-pi05-vla-only-goal-seed42-r4\nprecompute-smolvla-goal-bjb2-28827\neval-pi05-vla-only-goal-seed44-r4\neval-pi05-vla-only-goal-seed43-r4\neval-openvla-oft-official-object\neval-pi05-vla-only-object-seed44-r4\neval-smolvla-lerobot-official-object\neval-pi05-vla-only-object-seed42-r4\neval-loss-perdof-object-seed42\neval-loss-combined-object-seed42\neval-loss-conformal-object-seed42\neval-loss-mse-object-seed42\neval-openvla-oft-object-baseline-seed42\nprecompute-smolvla-goal-bjb1-18228\neval-smolvla-acr-goal-seed43\neval-smolvla-crm-goal-seed44-v2\neval-smolvla-acr-goal-seed42\ncrm-train-pi05-object-full\ncrm-train-pi05-object\neval-pi05-vla-only-object-seed44-r3\neval-pi05-vla-only-object-seed43-r3\neval-pi05-vla-only-object-seed42-r3\neval-k20-obs-only-object-seed45\neval-obs-only-object-norm003-seed66\neval-obs-only-object-norm01-seed66\neval-obs-only-object-norm005-seed66\neval-obs-only-object-norm003-seed67\neval-k20-obs-only-object-seed44\neval-k20-obs-only-object-seed43\neval-k20-obs-only-object-seed42\neval-crm-object-k20-seed44\neval-crm-object-k20-seed42\neval-obs-only-object-norm02-seed53\neval-obs-only-object-norm02-seed52\neval-obs-only-object-norm02-seed51\neval-obs-only-object-norm02-seed50\neval-obs-only-object-norm02-seed48-r2\neval-obs-only-object-norm02-seed47\neval-obs-only-object-norm02-seed46\neval-obs-only-object-norm02-seed45\neval-obs-only-object-norm02-seed44-r2\neval-obs-only-object-norm02-seed43-r3\neval-obs-only-object-norm02-seed43-r2\neval-obs-only-object-norm005-seed67\neval-obs-only-object-norm01-seed67\neval-vla-only-object-seed50\neval-vla-only-object-seed49\neval-vla-only-object-seed48\neval-vla-only-object-seed46\neval-vla-only-object-seed45\neval-vla-only-object-seed44-r2\neval-plan-a-object-seed42\neval-vla-only-object-seed43\neval-vla-only-object\neval-plan-a-object-seed44\neval-plan-a-object-seed43\neval-random-selection-object-seed44\neval-random-selection-object-seed43\neval-obs-only-object-norm01-seed60\neval-pi05-baseline-object-seed42\neval-obs-only-object-norm01-seed54\neval-obs-only-object-norm01-seed53\neval-obs-only-object-norm01-seed52\neval-obs-only-object-norm01-seed50\neval-obs-only-object-norm01-seed49\neval-obs-only-object-norm01-seed48\neval-obs-only-object-norm01-seed47\neval-obs-only-object-norm01-seed45-r2\neval-obs-only-object-norm01-seed44\neval-obs-only-object-norm005-seed55\neval-obs-only-object-norm005-seed50\neval-obs-only-object-norm005-seed49\neval-obs-only-object-norm005-seed48\neval-obs-only-object-norm005-seed47\neval-obs-only-object-norm005-seed44\neval-obs-only-object-norm005-seed43-r2\neval-obs-only-object-norm005-seed43\neval-obs-only-object-norm003-seed48\neval-obs-only-object-norm003-seed47-r2\neval-obs-only-object-norm003-seed46\neval-obs-only-object-norm003-seed45\neval-obs-only-object-norm003-seed44-bjb2\neval-obs-only-object-norm003-seed44\neval-obs-only-object-norm003-seed43-r2\neval-obs-only-object-norm003-seed43\neval-obs-only-object-norm01-seed57\neval-obs-only-object-norm005-seed65\neval-obs-only-object-norm005-seed61\neval-obs-only-object-norm005-seed58\neval-obs-only-object-norm003-seed59\neval-obs-only-object-norm003-seed56\neval-obs-only-object-norm005-seed75\neval-obs-only-object-norm01-seed74\neval-obs-only-object-norm005-seed72\neval-obs-only-object-norm003-seed63-r2\neval-obs-only-object-norm01-seed71",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "4eb774c9-dfd7-4376-a046-58bbc4fb12c2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019Lx1kHdi6ChA4qcQHXjU1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3967,
      "cache_read_input_tokens": 40078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3967
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017uTbgDxZ44LmEyzz8hfGfX`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "98d38840-bb55-4cd8-aa8c-178aafe50dff",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019Lx1kHdi6ChA4qcQHXjU1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3967,
      "cache_read_input_tokens": 40078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3967
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-25T01:51:34.024Z_

<details><summary>↩ Tool result · `toolu_017uTbgDxZ44LmEyzz8hfGfX`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "18886375-afc9-4364-884f-22d0aaa9c306",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Glob · `toolu_013ksSzA8E8dQaWHwHq9STeL`</summary>

```json
{
  "pattern": "**/ROADMAP*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "819643a4-027b-4087-8af0-6d014d63a3fc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BShqcnNnr9Do54hmr7GDfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 985
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-25T01:51:36.573Z_

<details><summary>↩ Tool result · `toolu_013ksSzA8E8dQaWHwHq9STeL`</summary>

```text
ROADMAP.lock
ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "077efa0d-198d-4be3-ac3b-8f1c217cdbb8",
  "tool_use_result": {
    "filenames": [
      "ROADMAP.lock",
      "ROADMAP.md"
    ],
    "durationMs": 28,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01U75QLJmFj4QjcRmQvhqFj1`</summary>

```json
{
  "command": "grep -n -A 30 -i \"table 1\\|goal.*5.*seed\\|object.*5.*seed\\|goal.*3.*seed\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md 2>/dev/null | head -200",
  "description": "Search ROADMAP for Table 1 context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "10294ceb-10d7-465b-a5bd-299dd31a6fd7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Y3tJadH2P5MLktMHWZrDhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 109,
      "cache_read_input_tokens": 45030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 109
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-25T01:51:42.866Z_

<details><summary>↩ Tool result · `toolu_01U75QLJmFj4QjcRmQvhqFj1`</summary>

```text
14:## Table 1 — 3-seed（待 D139 8-seed 更新）
15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |
16-|-------|---------|-----|----------|--------|--------|
17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |
18-| Goal | 83.7±1.3(3s) | 83.7±1.8(3s) | 85.0±1.3(3s) | **+1.3pp** | +1.3pp |
19-| Object | 77.7±1.3(5s) | 76.5±2.3(3s) | 77.8±2.1(5s) | +0.1pp | +1.3pp |
20-| Long | 58.0±1.5(3s) | 55.8±1.2(3s) | 57.7±1.5(3s) | -0.3pp | **+1.9pp** |
21-
22-## D139 种子扩展 — 部署中 ⏳
23-- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验
24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites
25-- ETA：今晚（5/24）出结果
26-
27-## π0.5 跨模型验证 — 进行中 ⏳
28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**
29-- 训练完成后立即部署 3 suites eval（non-CRM 18 jobs 已审批）
30-- 论文锁定 **SmolVLA (0.4B) + π0.5 (3.6B)** 双模型验证
31-
32-## 补充实验
33-- [x] Mechanism analysis (plan_302) — 完成 ✅ rank-deficient 机制确认
34-- [ ] Spatial τ-sweep — bjb1-32546 运行中
35-- [ ] K-sweep (K=1/2/5) — bjb1-32546 运行中
36-- [ ] CRM Object s47 异常值 re-eval
37-- [x] Long K2mean s47: SR=54.5%（M083 旧代码文件名问题，数据已恢复）
38-
39-## Mechanism Analysis 核心发现（plan_302, Reviewer 审查通过）
40-- K=10 → 30×30 协方差 rank=9, 21/30 维度纯噪声 → per-DOF conditioning 崩溃根因
41-- obs_only 避开问题（960-D embedding 高 SNR）
42-- fig1-fig3 可用于论文 Appendix
43-
44-## GPU 状态
--
56:- [ ] **P0** D139 种子结果 → 更新 Table 1 → 确认叙事升级
57-- [ ] **P0** π0.5 CRM 训练完成(~04:00 UTC) → 部署 eval
58-- [ ] **P0** π0.5 eval 完成 → 汇总双模型数据
59-- [ ] **P0** 5/25 晚：Paper Agent 写最新摘要
60-- [ ] **P1** Mechanism analysis artifacts 拉回 + registry 注册
61-- [ ] **P1** Long K2mean s47 registry 更新(SR=54.5%)
62-- [ ] **P2** 最终论文审稿 → submit_paper_to_review
63-- [x] D138 paper_framing.md 重写 ✅
64-- [x] A1 放弃（D137）✅
65-- [x] s45/s46/s47 seed 扩展 ✅
66-- [x] Fig 1 修正版 ✅
67-
68-## A1 VLA — 已放弃 ❌ (D137)
69-Baseline SR=56.5% vs 官方 99.8%，eval protocol 不兼容。
70-
71-## 关键决策日志
72-
73-| ID | 日期 | 摘要 | 关联实验 |
74-|----|------|------|----------|
75-| D147 | 2026-05-24 | Spatial paired test 必须使用同服务器配对，补跑 cqa1 Adaptive 修复 | — |
76-| D146 | 2026-05-24 | 采用修正版(B) framing：ACR-VLA adaptive gating 为核心贡献，"Ad | spatial-8seed-paired-t, eval-k1-spatial-s42, eval-k5-spatial-s42, eval-k2-tau010-015-spatial-s42 |
77:| D145 | 2026-05-24 | D145: Table 1 Adaptive 确认 K=10；报告策略 n=7 (p<0.01) 为 | Spatial Adaptive s42-s49 |
78-| D144 | 2026-05-24 | D143: Spatial p=0.0049 — claim 策略升级：Spatial magnit | D139 seed extension s48/s49, τ-sweep Spatial s42 |
79-| D143 | 2026-05-24 | D143: Seed extension 确认 Spatial 一致正向，Goal/Object 新 | — |
80-| D142 | 2026-05-24 | D142: 8-seed 统计结果确认——Spatial 显著 (p=0.0418), Goal/O | — |
81-| D141 | 2026-05-24 | D141: Claim 强度确定——mechanism claim + τ-sweep 为主力证据， | — |
82-| D140 | 2026-05-24 | D140: 叙事框架锁定——方案 C（trigger rate ↔ effect size 正相关） | — |
83-| D139 | 2026-05-24 | D139: 用户要求加种子 — Adaptive + VLA-only 在 Spatial/Goal | — |
84:| D138 | 2026-05-24 | D138: paper_framing.md 重写——对齐 Table 1 数字体系，Core Cl | — |
85-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "d1017fb6-ab30-48ce-bd6a-5729cb4319a1",
  "tool_use_result": {
    "stdout": "14:## Table 1 — 3-seed（待 D139 8-seed 更新）\n15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |\n16-|-------|---------|-----|----------|--------|--------|\n17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |\n18-| Goal | 83.7±1.3(3s) | 83.7±1.8(3s) | 85.0±1.3(3s) | **+1.3pp** | +1.3pp |\n19-| Object | 77.7±1.3(5s) | 76.5±2.3(3s) | 77.8±2.1(5s) | +0.1pp | +1.3pp |\n20-| Long | 58.0±1.5(3s) | 55.8±1.2(3s) | 57.7±1.5(3s) | -0.3pp | **+1.9pp** |\n21-\n22-## D139 种子扩展 — 部署中 ⏳\n23-- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验\n24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites\n25-- ETA：今晚（5/24）出结果\n26-\n27-## π0.5 跨模型验证 — 进行中 ⏳\n28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**\n29-- 训练完成后立即部署 3 suites eval（non-CRM 18 jobs 已审批）\n30-- 论文锁定 **SmolVLA (0.4B) + π0.5 (3.6B)** 双模型验证\n31-\n32-## 补充实验\n33-- [x] Mechanism analysis (plan_302) — 完成 ✅ rank-deficient 机制确认\n34-- [ ] Spatial τ-sweep — bjb1-32546 运行中\n35-- [ ] K-sweep (K=1/2/5) — bjb1-32546 运行中\n36-- [ ] CRM Object s47 异常值 re-eval\n37-- [x] Long K2mean s47: SR=54.5%（M083 旧代码文件名问题，数据已恢复）\n38-\n39-## Mechanism Analysis 核心发现（plan_302, Reviewer 审查通过）\n40-- K=10 → 30×30 协方差 rank=9, 21/30 维度纯噪声 → per-DOF conditioning 崩溃根因\n41-- obs_only 避开问题（960-D embedding 高 SNR）\n42-- fig1-fig3 可用于论文 Appendix\n43-\n44-## GPU 状态\n--\n56:- [ ] **P0** D139 种子结果 → 更新 Table 1 → 确认叙事升级\n57-- [ ] **P0** π0.5 CRM 训练完成(~04:00 UTC) → 部署 eval\n58-- [ ] **P0** π0.5 eval 完成 → 汇总双模型数据\n59-- [ ] **P0** 5/25 晚：Paper Agent 写最新摘要\n60-- [ ] **P1** Mechanism analysis artifacts 拉回 + registry 注册\n61-- [ ] **P1** Long K2mean s47 registry 更新(SR=54.5%)\n62-- [ ] **P2** 最终论文审稿 → submit_paper_to_review\n63-- [x] D138 paper_framing.md 重写 ✅\n64-- [x] A1 放弃（D137）✅\n65-- [x] s45/s46/s47 seed 扩展 ✅\n66-- [x] Fig 1 修正版 ✅\n67-\n68-## A1 VLA — 已放弃 ❌ (D137)\n69-Baseline SR=56.5% vs 官方 99.8%，eval protocol 不兼容。\n70-\n71-## 关键决策日志\n72-\n73-| ID | 日期 | 摘要 | 关联实验 |\n74-|----|------|------|----------|\n75-| D147 | 2026-05-24 | Spatial paired test 必须使用同服务器配对，补跑 cqa1 Adaptive 修复 | — |\n76-| D146 | 2026-05-24 | 采用修正版(B) framing：ACR-VLA adaptive gating 为核心贡献，\"Ad | spatial-8seed-paired-t, eval-k1-spatial-s42, eval-k5-spatial-s42, eval-k2-tau010-015-spatial-s42 |\n77:| D145 | 2026-05-24 | D145: Table 1 Adaptive 确认 K=10；报告策略 n=7 (p<0.01) 为 | Spatial Adaptive s42-s49 |\n78-| D144 | 2026-05-24 | D143: Spatial p=0.0049 — claim 策略升级：Spatial magnit | D139 seed extension s48/s49, τ-sweep Spatial s42 |\n79-| D143 | 2026-05-24 | D143: Seed extension 确认 Spatial 一致正向，Goal/Object 新 | — |\n80-| D142 | 2026-05-24 | D142: 8-seed 统计结果确认——Spatial 显著 (p=0.0418), Goal/O | — |\n81-| D141 | 2026-05-24 | D141: Claim 强度确定——mechanism claim + τ-sweep 为主力证据， | — |\n82-| D140 | 2026-05-24 | D140: 叙事框架锁定——方案 C（trigger rate ↔ effect size 正相关） | — |\n83-| D139 | 2026-05-24 | D139: 用户要求加种子 — Adaptive + VLA-only 在 Spatial/Goal | — |\n84:| D138 | 2026-05-24 | D138: paper_framing.md 重写——对齐 Table 1 数字体系，Core Cl | — |\n85-",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01A4F8pfH1UMkMDrh6RanY1N`</summary>

```json
{
  "command": "grep -n -A 5 -i \"goal.*seed\\|object.*seed\\|seed.*goal\\|seed.*object\\|VLA.*only.*goal\\|VLA.*only.*object\\|CRM.*goal\\|CRM.*object\\|adaptive.*goal\\|adaptive.*object\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md 2>/dev/null | head -80",
  "description": "Search for seed listings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "3449cac6-f41b-42a3-bbe0-4b38a6d317c3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Kdeno84ZjLSBU2CcnQeong",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2284,
      "cache_read_input_tokens": 45139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2284
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-25T01:51:48.469Z_

<details><summary>↩ Tool result · `toolu_01A4F8pfH1UMkMDrh6RanY1N`</summary>

```text
12:叙事升级目标：从"harm avoidance"→"CRM + Adaptive 共同作用"（需 Adaptive > VLA-only on Spatial/Goal/Object）。
13-
14-## Table 1 — 3-seed（待 D139 8-seed 更新）
15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |
16-|-------|---------|-----|----------|--------|--------|
17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |
--
23:- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验
24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites
25-- ETA：今晚（5/24）出结果
26-
27-## π0.5 跨模型验证 — 进行中 ⏳
28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**
--
36:- [ ] CRM Object s47 异常值 re-eval
37-- [x] Long K2mean s47: SR=54.5%（M083 旧代码文件名问题，数据已恢复）
38-
39-## Mechanism Analysis 核心发现（plan_302, Reviewer 审查通过）
40-- K=10 → 30×30 协方差 rank=9, 21/30 维度纯噪声 → per-DOF conditioning 崩溃根因
41-- obs_only 避开问题（960-D embedding 高 SNR）
--
79:| D143 | 2026-05-24 | D143: Seed extension 确认 Spatial 一致正向，Goal/Object 新 | — |
80:| D142 | 2026-05-24 | D142: 8-seed 统计结果确认——Spatial 显著 (p=0.0418), Goal/O | — |
81-| D141 | 2026-05-24 | D141: Claim 强度确定——mechanism claim + τ-sweep 为主力证据， | — |
82-| D140 | 2026-05-24 | D140: 叙事框架锁定——方案 C（trigger rate ↔ effect size 正相关） | — |
83:| D139 | 2026-05-24 | D139: 用户要求加种子 — Adaptive + VLA-only 在 Spatial/Goal | — |
84-| D138 | 2026-05-24 | D138: paper_framing.md 重写——对齐 Table 1 数字体系，Core Cl | — |
85-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "826d3831-738b-400b-b9d4-ca6bae0611bf",
  "tool_use_result": {
    "stdout": "12:叙事升级目标：从\"harm avoidance\"→\"CRM + Adaptive 共同作用\"（需 Adaptive > VLA-only on Spatial/Goal/Object）。\n13-\n14-## Table 1 — 3-seed（待 D139 8-seed 更新）\n15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |\n16-|-------|---------|-----|----------|--------|--------|\n17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |\n--\n23:- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验\n24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites\n25-- ETA：今晚（5/24）出结果\n26-\n27-## π0.5 跨模型验证 — 进行中 ⏳\n28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**\n--\n36:- [ ] CRM Object s47 异常值 re-eval\n37-- [x] Long K2mean s47: SR=54.5%（M083 旧代码文件名问题，数据已恢复）\n38-\n39-## Mechanism Analysis 核心发现（plan_302, Reviewer 审查通过）\n40-- K=10 → 30×30 协方差 rank=9, 21/30 维度纯噪声 → per-DOF conditioning 崩溃根因\n41-- obs_only 避开问题（960-D embedding 高 SNR）\n--\n79:| D143 | 2026-05-24 | D143: Seed extension 确认 Spatial 一致正向，Goal/Object 新 | — |\n80:| D142 | 2026-05-24 | D142: 8-seed 统计结果确认——Spatial 显著 (p=0.0418), Goal/O | — |\n81-| D141 | 2026-05-24 | D141: Claim 强度确定——mechanism claim + τ-sweep 为主力证据， | — |\n82-| D140 | 2026-05-24 | D140: 叙事框架锁定——方案 C（trigger rate ↔ effect size 正相关） | — |\n83:| D139 | 2026-05-24 | D139: 用户要求加种子 — Adaptive + VLA-only 在 Spatial/Goal | — |\n84-| D138 | 2026-05-24 | D138: paper_framing.md 重写——对齐 Table 1 数字体系，Core Cl | — |\n85-",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Glob · `toolu_0191yVFXE128cAwQF82CmatH`</summary>

```json
{
  "pattern": "**/table*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "aea7c534-8a73-416c-a993-816598367bad",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01T3rxoGKZrkFttx3oTe3o1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 47423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1180
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-25T01:51:50.963Z_

<details><summary>↩ Tool result · `toolu_0191yVFXE128cAwQF82CmatH`</summary>

```text
artifacts/_project/data/table1_8seed_final.md
artifacts/_project/report/table1_8seed_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "295a8751-bb27-4744-8ea8-ec258f2face6",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/table1_8seed_final.md",
      "artifacts/_project/report/table1_8seed_v2.md"
    ],
    "durationMs": 26,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01VJxgzEDtJRK3hWKa8YcmNU`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md 2>/dev/null | head -200",
  "description": "Read table1 data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "994a16ca-ee13-4fcd-863d-90542d91f39f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VJXkUu5mmb6v3EqUFegjk8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 122,
      "cache_read_input_tokens": 48603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 122
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-25T01:51:57.472Z_

<details><summary>↩ Tool result · `toolu_01VJxgzEDtJRK3hWKa8YcmNU`</summary>

```text
# Table 1 — Multi-seed Results (Clean supp-era data)

Generated: 2026-05-24 20:10 UTC

## Main Table

| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
|-------|---------|-------------|-------------------|--------|--------|
| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |

## Paired t-test: Δ(A-V) = Adaptive - VLA-only

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |
| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |
| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |

## Paired t-test: Δ(A-C) = Adaptive - CRM always-on

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |
| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |
| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |
| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |

## Trigger Rate ↔ Effect Size (D140 key evidence)

| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |
|-------|------------------|--------|-------------|
| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |
| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |
| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |
| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |

## Per-seed Raw Data

### Spatial (8 matched seeds)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | 80.0% | 82.0% | — | +2.0pp |
| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |
| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |
| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |
| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |
| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |
| s48 | 79.5% | 81.0% | — | +1.5pp |
| s49 | 78.5% | 82.0% | — | +3.5pp |

### Goal (7 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | — | 84.0% | 85.5% | — |
| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |
| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |
| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |
| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |
| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |
| s48 | 85.0% | 84.5% | — | -0.5pp |
| s49 | 82.0% | 81.5% | — | -0.5pp |

### Object (5 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | — | 81.0% | 77.0% | — |
| s43 | — | 77.5% | 78.5% | — |
| s44 | — | 75.0% | 74.0% | — |
| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
| s48 | 79.0% | 76.0% | — | -3.0pp |
| s49 | 75.5% | 74.0% | — | -1.5pp |

### Long (5 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
| s43 | — | 58.0% | 54.5% | — |
| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |
| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |

## Data Gaps
- Goal VLA-only s42: missing
- Object VLA-only s42/s43/s44: missing
- Spatial CRM s42/s48/s49: missing
- Goal/Object CRM s48/s49: missing
- Long VLA-only s43/s48/s49: missing
- Long Adaptive s48/s49: missing

## Note on Spatial VLA-only s42
eval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "58d288ed-7971-454f-bbc8-b29d31079d28",
  "tool_use_result": {
    "stdout": "# Table 1 — Multi-seed Results (Clean supp-era data)\n\nGenerated: 2026-05-24 20:10 UTC\n\n## Main Table\n\n| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |\n|-------|---------|-------------|-------------------|--------|--------|\n| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |\n| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |\n| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |\n| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |\n\n## Paired t-test: Δ(A-V) = Adaptive - VLA-only\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |\n| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |\n| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |\n| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |\n\n## Paired t-test: Δ(A-C) = Adaptive - CRM always-on\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |\n| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |\n| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |\n| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |\n\n## Trigger Rate ↔ Effect Size (D140 key evidence)\n\n| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |\n|-------|------------------|--------|-------------|\n| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |\n| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |\n| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |\n| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |\n\n## Per-seed Raw Data\n\n### Spatial (8 matched seeds)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 80.0% | 82.0% | — | +2.0pp |\n| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |\n| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |\n| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |\n| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |\n| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |\n| s48 | 79.5% | 81.0% | — | +1.5pp |\n| s49 | 78.5% | 82.0% | — | +3.5pp |\n\n### Goal (7 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 84.0% | 85.5% | — |\n| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |\n| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |\n| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |\n| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |\n| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |\n| s48 | 85.0% | 84.5% | — | -0.5pp |\n| s49 | 82.0% | 81.5% | — | -0.5pp |\n\n### Object (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 81.0% | 77.0% | — |\n| s43 | — | 77.5% | 78.5% | — |\n| s44 | — | 75.0% | 74.0% | — |\n| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |\n| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |\n| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |\n| s48 | 79.0% | 76.0% | — | -3.0pp |\n| s49 | 75.5% | 74.0% | — | -1.5pp |\n\n### Long (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |\n| s43 | — | 58.0% | 54.5% | — |\n| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |\n| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |\n| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |\n| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |\n\n## Data Gaps\n- Goal VLA-only s42: missing\n- Object VLA-only s42/s43/s44: missing\n- Spatial CRM s42/s48/s49: missing\n- Goal/Object CRM s48/s49: missing\n- Long VLA-only s43/s48/s49: missing\n- Long Adaptive s48/s49: missing\n\n## Note on Spatial VLA-only s42\neval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "1e2c2cf2-6812-4a13-81a5-f8c44af2519c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013ruGMGRCRPZD2QqGki2ZUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 48725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BbdQ6XwTRXsaAVXmNH71VU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "3ecf1b82-a139-43e2-99b4-66a00271b95b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013ruGMGRCRPZD2QqGki2ZUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 48725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-25T01:52:08.344Z_

<details><summary>↩ Tool result · `toolu_01BbdQ6XwTRXsaAVXmNH71VU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "0d2d030b-e99f-48c6-b3e3-80211d365b19",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01RU1CABpzLTC4ZEgZesU3ei`</summary>

```json
{
  "command": "grep -rn -l \"83.7\\|85.0\\|77.7\\|77.8\\|76.5\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/ 2>/dev/null | head -10",
  "description": "Find files with Table 1 3-seed values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "1c242342-2022-4ac7-8e17-66a531da1a04",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01D9A4BTTGhMuf4j76929i9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 51626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-25T01:52:13.647Z_

<details><summary>↩ Tool result · `toolu_01RU1CABpzLTC4ZEgZesU3ei`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig2_main_results.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig1_pipeline.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig3_magnitude_sweep.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval_partial_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary_e015e3.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "bb124f14-9c93-4806-b268-ede920459b02",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig2_main_results.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig1_pipeline.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig3_magnitude_sweep.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval_partial_results.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary_e015e3.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01KSiM8kE7A6zEr2zUEfQW2j`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json 2>/dev/null | head -200",
  "description": "Read summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "a6e518f3-5bfb-4925-b99d-0043c676689c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0177BGuxN1R4VfEdqKZNsoCx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 906
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-25T01:52:18.054Z_

<details><summary>↩ Tool result · `toolu_01KSiM8kE7A6zEr2zUEfQW2j`</summary>

```text
{
  "meta": {
    "suite": "object",
    "K_max": 64,
    "n_tasks": 5,
    "n_init_states": 4,
    "H_eff": 5,
    "pose_dim": 6,
    "flat_dim": 30,
    "seed": 42
  },
  "n_decision_points": 20,
  "n_bootstrap_per_K": 32,
  "K_grid": [
    6,
    10,
    16,
    20,
    32,
    50
  ],
  "K_max": 64,
  "rank": {
    "6": {
      "mean": 5.0,
      "median": 5.0,
      "max": 5,
      "min": 5
    },
    "10": {
      "mean": 9.0,
      "median": 9.0,
      "max": 9,
      "min": 9
    },
    "16": {
      "mean": 15.0,
      "median": 15.0,
      "max": 15,
      "min": 15
    },
    "20": {
      "mean": 19.0,
      "median": 19.0,
      "max": 19,
      "min": 19
    },
    "32": {
      "mean": 29.9921875,
      "median": 30.0,
      "max": 30,
      "min": 29
    },
    "50": {
      "mean": 30.0,
      "median": 30.0,
      "max": 30,
      "min": 30
    },
    "64": {
      "mean": 30.0,
      "median": 30.0,
      "max": 30,
      "min": 30
    }
  },
  "cond_number_log10": {
    "6": {
      "median": 19.319505951782975,
      "p90": 20.206856472773495
    },
    "10": {
      "median": 19.034611732480897,
      "p90": 19.896343082150924
    },
    "16": {
      "median": 18.655276330434113,
      "p90": 19.504748141160338
    },
    "20": {
      "median": 18.505145213879263,
      "p90": 19.367335009575356
    },
    "32": {
      "median": 5.652354587897747,
      "p90": 6.625037978913544
    },
    "50": {
      "median": 4.171016474333227,
      "p90": 4.647836076679067
    },
    "64": {
      "median": 3.9470162478379773,
      "p90": 4.3809091314076065
    }
  },
  "perdof_relative_error": {
    "6": {
      "mean_abs": 0.2582815467237826,
      "median_abs": 0.2226053814209542,
      "p90_abs": 0.5237770856059171
    },
    "10": {
      "mean_abs": 0.18680869744478956,
      "median_abs": 0.15798896493027892,
      "p90_abs": 0.3867095249251528
    },
    "16": {
      "mean_abs": 0.13812100967954197,
      "median_abs": 0.11610700330893065,
      "p90_abs": 0.28557078650817536
    },
    "20": {
      "mean_abs": 0.11761357935512999,
      "median_abs": 0.09885689643503728,
      "p90_abs": 0.24444310748319667
    },
    "32": {
      "mean_abs": 0.07940835432260002,
      "median_abs": 0.06668105827965978,
      "p90_abs": 0.16180068020198815
    },
    "50": {
      "mean_abs": 0.04104854945498445,
      "median_abs": 0.03442979546382717,
      "p90_abs": 0.0815198620777641
    }
  },
  "gt_perdof_std_summary": {
    "mean": 0.0226358915941457,
    "median": 0.013790348985397053,
    "max": 0.11436990502633566,
    "min": 0.0010124623692256147
  },
  "worst_dofs_at_K10": [
    {
      "index": 21,
      "horizon": 4,
      "dof": 4,
      "mean_rel_err": 0.24109260729758528
    },
    {
      "index": 15,
      "horizon": 3,
      "dof": 4,
      "mean_rel_err": 0.22789736980545086
    },
    {
      "index": 27,
      "horizon": 5,
      "dof": 4,
      "mean_rel_err": 0.21648496417755334
    },
    {
      "index": 28,
      "horizon": 5,
      "dof": 5,
      "mean_rel_err": 0.21267205714871906
    },
    {
      "index": 9,
      "horizon": 2,
      "dof": 4,
      "mean_rel_err": 0.2011921875584322
    }
  ],
  "best_dofs_at_K10": [
    {
      "index": 13,
      "horizon": 3,
      "dof": 2,
      "mean_rel_err": 0.1623562021651603
    },
    {
      "index": 7,
      "horizon": 2,
      "dof": 2,
      "mean_rel_err": 0.167029826134513
    },
    {
      "index": 18,
      "horizon": 4,
      "dof": 1,
      "mean_rel_err": 0.1681385540505912
    },
    {
      "index": 14,
      "horizon": 3,
      "dof": 3,
      "mean_rel_err": 0.1681475359447455
    },
    {
      "index": 24,
      "horizon": 5,
      "dof": 1,
      "mean_rel_err": 0.16920295406433788
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "3271451c-b3a7-4231-8ecc-daf3ec8ca214",
  "tool_use_result": {
    "stdout": "{\n  \"meta\": {\n    \"suite\": \"object\",\n    \"K_max\": 64,\n    \"n_tasks\": 5,\n    \"n_init_states\": 4,\n    \"H_eff\": 5,\n    \"pose_dim\": 6,\n    \"flat_dim\": 30,\n    \"seed\": 42\n  },\n  \"n_decision_points\": 20,\n  \"n_bootstrap_per_K\": 32,\n  \"K_grid\": [\n    6,\n    10,\n    16,\n    20,\n    32,\n    50\n  ],\n  \"K_max\": 64,\n  \"rank\": {\n    \"6\": {\n      \"mean\": 5.0,\n      \"median\": 5.0,\n      \"max\": 5,\n      \"min\": 5\n    },\n    \"10\": {\n      \"mean\": 9.0,\n      \"median\": 9.0,\n      \"max\": 9,\n      \"min\": 9\n    },\n    \"16\": {\n      \"mean\": 15.0,\n      \"median\": 15.0,\n      \"max\": 15,\n      \"min\": 15\n    },\n    \"20\": {\n      \"mean\": 19.0,\n      \"median\": 19.0,\n      \"max\": 19,\n      \"min\": 19\n    },\n    \"32\": {\n      \"mean\": 29.9921875,\n      \"median\": 30.0,\n      \"max\": 30,\n      \"min\": 29\n    },\n    \"50\": {\n      \"mean\": 30.0,\n      \"median\": 30.0,\n      \"max\": 30,\n      \"min\": 30\n    },\n    \"64\": {\n      \"mean\": 30.0,\n      \"median\": 30.0,\n      \"max\": 30,\n      \"min\": 30\n    }\n  },\n  \"cond_number_log10\": {\n    \"6\": {\n      \"median\": 19.319505951782975,\n      \"p90\": 20.206856472773495\n    },\n    \"10\": {\n      \"median\": 19.034611732480897,\n      \"p90\": 19.896343082150924\n    },\n    \"16\": {\n      \"median\": 18.655276330434113,\n      \"p90\": 19.504748141160338\n    },\n    \"20\": {\n      \"median\": 18.505145213879263,\n      \"p90\": 19.367335009575356\n    },\n    \"32\": {\n      \"median\": 5.652354587897747,\n      \"p90\": 6.625037978913544\n    },\n    \"50\": {\n      \"median\": 4.171016474333227,\n      \"p90\": 4.647836076679067\n    },\n    \"64\": {\n      \"median\": 3.9470162478379773,\n      \"p90\": 4.3809091314076065\n    }\n  },\n  \"perdof_relative_error\": {\n    \"6\": {\n      \"mean_abs\": 0.2582815467237826,\n      \"median_abs\": 0.2226053814209542,\n      \"p90_abs\": 0.5237770856059171\n    },\n    \"10\": {\n      \"mean_abs\": 0.18680869744478956,\n      \"median_abs\": 0.15798896493027892,\n      \"p90_abs\": 0.3867095249251528\n    },\n    \"16\": {\n      \"mean_abs\": 0.13812100967954197,\n      \"median_abs\": 0.11610700330893065,\n      \"p90_abs\": 0.28557078650817536\n    },\n    \"20\": {\n      \"mean_abs\": 0.11761357935512999,\n      \"median_abs\": 0.09885689643503728,\n      \"p90_abs\": 0.24444310748319667\n    },\n    \"32\": {\n      \"mean_abs\": 0.07940835432260002,\n      \"median_abs\": 0.06668105827965978,\n      \"p90_abs\": 0.16180068020198815\n    },\n    \"50\": {\n      \"mean_abs\": 0.04104854945498445,\n      \"median_abs\": 0.03442979546382717,\n      \"p90_abs\": 0.0815198620777641\n    }\n  },\n  \"gt_perdof_std_summary\": {\n    \"mean\": 0.0226358915941457,\n    \"median\": 0.013790348985397053,\n    \"max\": 0.11436990502633566,\n    \"min\": 0.0010124623692256147\n  },\n  \"worst_dofs_at_K10\": [\n    {\n      \"index\": 21,\n      \"horizon\": 4,\n      \"dof\": 4,\n      \"mean_rel_err\": 0.24109260729758528\n    },\n    {\n      \"index\": 15,\n      \"horizon\": 3,\n      \"dof\": 4,\n      \"mean_rel_err\": 0.22789736980545086\n    },\n    {\n      \"index\": 27,\n      \"horizon\": 5,\n      \"dof\": 4,\n      \"mean_rel_err\": 0.21648496417755334\n    },\n    {\n      \"index\": 28,\n      \"horizon\": 5,\n      \"dof\": 5,\n      \"mean_rel_err\": 0.21267205714871906\n    },\n    {\n      \"index\": 9,\n      \"horizon\": 2,\n      \"dof\": 4,\n      \"mean_rel_err\": 0.2011921875584322\n    }\n  ],\n  \"best_dofs_at_K10\": [\n    {\n      \"index\": 13,\n      \"horizon\": 3,\n      \"dof\": 2,\n      \"mean_rel_err\": 0.1623562021651603\n    },\n    {\n      \"index\": 7,\n      \"horizon\": 2,\n      \"dof\": 2,\n      \"mean_rel_err\": 0.167029826134513\n    },\n    {\n      \"index\": 18,\n      \"horizon\": 4,\n      \"dof\": 1,\n      \"mean_rel_err\": 0.1681385540505912\n    },\n    {\n      \"index\": 14,\n      \"horizon\": 3,\n      \"dof\": 3,\n      \"mean_rel_err\": 0.1681475359447455\n    },\n    {\n      \"index\": 24,\n      \"horizon\": 5,\n      \"dof\": 1,\n      \"mean_rel_err\": 0.16920295406433788\n    }\n  ]\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "e538b013-dd91-40b2-b6ad-5888bd363c7e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01S9iCbVZWTmHCQkmEFdLZTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 53707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2001
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01AVBMUUTRaAn9CivadgzU4h`</summary>

```json
{
  "command": "grep -rln \"83.7\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null | grep -v \".pdf$\\|.png$\" | head -20",
  "description": "Find text files with 83.7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "a88897a2-0de8-4b79-b81c-72a16c704b03",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01S9iCbVZWTmHCQkmEFdLZTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 53707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2001
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-25T01:52:24.123Z_

<details><summary>↩ Tool result · `toolu_01AVBMUUTRaAn9CivadgzU4h`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521_b7ea89.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/trigger_rate_scatter_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitor_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_vla_only_eval_progress_20260521.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_audit_20260521.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "ae4128b1-e99f-4a44-818d-d9ffe8e09735",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521_b7ea89.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/trigger_rate_scatter_data.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitor_analysis.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_vla_only_eval_progress_20260521.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_worst.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_median.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_best.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_worst.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_median.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_best.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_audit_20260521.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01LpQHMWaKQYebhQiJ24gJz6`</summary>

```json
{
  "command": "grep -n -B 2 -A 5 \"83.7\\|85.0\\|77.7\\|77.8\\|76.5\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521_b7ea89.md 2>/dev/null | head -60",
  "description": "Check paper audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "0ea283b1-fbc0-48fd-97b6-cd0463e3f852",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01ScZ6QUAV5yFUXmo7TH5wUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 55708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1312
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-25T01:52:28.932Z_

<details><summary>↩ Tool result · `toolu_01LpQHMWaKQYebhQiJ24gJz6`</summary>

```text
34-| Plan A Object (n=3) | 18.3 ± 2.1% | seeds 42/43/44 = 19/16/20 → 18.33 ± 2.08 | ✅ |
35-| Plan A Spatial (n=3) | 35.0 ± 1.0% | seeds 42/43/44 = 34/35/36 → 35.0 ± 1.0 | ✅ |
36:| Plan A Object trigger rate | 83.7% | seeds 83.8/84.0/83.2 → mean 83.67 | ✅ |
37-| CRM K=5 Object (n=7) | 16.0 ± 2.2% | seeds 42-48 = 14/19/17/15/16/13/18 → 16.0 ± 2.16 | ✅ |
38-| CRM K=5 Spatial (n=4) | 34.5 ± 2.1% | seeds 42/43/44/45 = 35/32/37/34 → 34.5 ± 2.08 | ✅ |
39-| Random K=5 Object (n=4) | 10.5 ± 2.9% | seeds 42/43/44/45 = 14/11/10/7 → 10.5 ± 2.89 | ✅ |
40-| Random K=10 Spatial (n=3) | 29.3 ± 4.2% | seeds 42/43/44 = 34/26/28 → 29.33 ± 4.16 | ✅ |
41-| VLA-only Spatial (n=5) | 29.4 ± 1.5% | seeds 42-46 = 30/29/31/27/30 → 29.4 ± 1.52 | ✅ |
--
47-| Adaptive P25 Object (n=3) | 14.3 ± 1.2% | seeds 42/43/44 = 15/13/15 → 14.33 ± 1.15 | ✅ |
48-| π0.5 VLA-only Object (n=3) | 81.5 ± 0.5% | seeds 42/43/44 (r3) = 82.0/81.5/81.0 → 81.5 ± 0.5 | ✅ |
49:| π0.5 VLA-only Spatial (n=3) | 84.2 ± 1.0% | seeds 42/43/45 = 84.5/83.0/85.0 → 84.17 ± 1.04 | ✅ |
50-| LTO boundary | CRM 2% vs VLA 14% (−12pp) | registry: heldout=0.02, vla-only=0.14 | ✅ |
51-| Argmin K=10 Object (n=6) | 12.3 ± 2.6% | framing: 12/17/13/12/10/10 → 12.33 ± 2.58 | ✅ |
52-| K=1 CRM | 10.3% (below baseline) | framing: 12/9/10 → 10.33 | ✅ |
53-
54-### ⚠️ Issues Found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "567dd396-6bc6-4bb8-8165-2043b5bb73e1",
  "tool_use_result": {
    "stdout": "34-| Plan A Object (n=3) | 18.3 ± 2.1% | seeds 42/43/44 = 19/16/20 → 18.33 ± 2.08 | ✅ |\n35-| Plan A Spatial (n=3) | 35.0 ± 1.0% | seeds 42/43/44 = 34/35/36 → 35.0 ± 1.0 | ✅ |\n36:| Plan A Object trigger rate | 83.7% | seeds 83.8/84.0/83.2 → mean 83.67 | ✅ |\n37-| CRM K=5 Object (n=7) | 16.0 ± 2.2% | seeds 42-48 = 14/19/17/15/16/13/18 → 16.0 ± 2.16 | ✅ |\n38-| CRM K=5 Spatial (n=4) | 34.5 ± 2.1% | seeds 42/43/44/45 = 35/32/37/34 → 34.5 ± 2.08 | ✅ |\n39-| Random K=5 Object (n=4) | 10.5 ± 2.9% | seeds 42/43/44/45 = 14/11/10/7 → 10.5 ± 2.89 | ✅ |\n40-| Random K=10 Spatial (n=3) | 29.3 ± 4.2% | seeds 42/43/44 = 34/26/28 → 29.33 ± 4.16 | ✅ |\n41-| VLA-only Spatial (n=5) | 29.4 ± 1.5% | seeds 42-46 = 30/29/31/27/30 → 29.4 ± 1.52 | ✅ |\n--\n47-| Adaptive P25 Object (n=3) | 14.3 ± 1.2% | seeds 42/43/44 = 15/13/15 → 14.33 ± 1.15 | ✅ |\n48-| π0.5 VLA-only Object (n=3) | 81.5 ± 0.5% | seeds 42/43/44 (r3) = 82.0/81.5/81.0 → 81.5 ± 0.5 | ✅ |\n49:| π0.5 VLA-only Spatial (n=3) | 84.2 ± 1.0% | seeds 42/43/45 = 84.5/83.0/85.0 → 84.17 ± 1.04 | ✅ |\n50-| LTO boundary | CRM 2% vs VLA 14% (−12pp) | registry: heldout=0.02, vla-only=0.14 | ✅ |\n51-| Argmin K=10 Object (n=6) | 12.3 ± 2.6% | framing: 12/17/13/12/10/10 → 12.33 ± 2.58 | ✅ |\n52-| K=1 CRM | 10.3% (below baseline) | framing: 12/9/10 → 10.33 | ✅ |\n53-\n54-### ⚠️ Issues Found",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01PZwndQ8LVetrLwwQJE4AtJ`</summary>

```json
{
  "command": "grep -rln \"table.*1\\|table_1\\|table1\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null | grep -v \".pdf$\" | head -10",
  "description": "Find Table 1 files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "957e3542-b67b-42d6-ac26-a037a2046fa2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017r4ZEcvPh3v7etEt7Rggfr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1196,
      "cache_read_input_tokens": 57020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1196
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-25T01:52:32.532Z_

<details><summary>↩ Tool result · `toolu_01PZwndQ8LVetrLwwQJE4AtJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/precompute_pipeline_status_latest.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft_6d6390.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/conclusion_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/narrative_b_abstract_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/contribution_list.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "703d52d1-95ec-4335-92f5-399cfacc5acd",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/precompute_pipeline_status_latest.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft_6d6390.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/conclusion_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/narrative_b_abstract_final.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/contribution_list.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01J2PyTGM79PnMXM8hxb35Kb`</summary>

```json
{
  "command": "grep -n -A 25 \"Table 1\\|table1\\|## Main Results\\|## Results\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md 2>/dev/null | head -80",
  "description": "Find table 1 in experiments draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "97df4137-a218-46a2-aa79-76e8b92e8f1f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016VbdpQrMuMV3RGfqeeUrzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 58216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 860
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-25T01:52:35.997Z_

<details><summary>↩ Tool result · `toolu_01J2PyTGM79PnMXM8hxb35Kb`</summary>

```text
14:Table 1 presents the primary comparison across all six methods on LIBERO Object. The obs_only CRM achieves the highest mean success rate at 17.5% (seeds 42/43/44/45 = 22/16/16/16%, std=3.0%), representing a +6.7 percentage point improvement over the vla-only baseline (10.8%, std=1.4%) and a +3.5 percentage point improvement over argmin selection alone (14.0%, std=2.6%). The vla-mean aggregation baseline (12.3%, std=2.5%) provides only marginal benefit over single-sample inference, confirming that naive averaging does not address the distributional issues in the action space. [TODO: fill seed45/46/47 for argmin] [TODO: fill seed46/47 for obs_only]
15-
16-The per-DOF and scalar CRM variants fail to improve over the VLA baseline. The perdof CRM (seeds 42/43/44: 11/12/8%, mean=10.3%, std=2.1%) and scalar CRM (seeds 43/44: 10/6%, mean=8.0%, std=2.8%) perform at or below the uncorrected policy. [TODO: fill seed45 for scalar] This negative result is central to our contribution: identical architecture and training produce divergent outcomes depending solely on the conditioning signal. The obs_only CRM succeeds because observation features provide stable directional information for correction, while conformal score features introduce noise that compounds with correction magnitude.
17-
18-The effect size of obs_only over argmin (+3.5pp) is modest in absolute terms. However, the consistent improvement across all evaluated seeds, combined with the robustness analysis in Section 4.3, supports the claim that observation-conditioned corrections provide reliable non-degrading enhancement. A Fisher exact test on pooled trials (700 total across seeds) yields p=0.048 for obs_only vs argmin. [TODO: update with 6-seed pooled test]
19-
20-
21-## 4.3 Magnitude Sensitivity Analysis
22-
23-Figure 2 presents the core mechanistic finding: the interaction between conditioning features and correction magnitude. We sweep the norm bound epsilon across six values (0.03, 0.05, 0.1, 0.2, 0.3, 1.42) for both obs_only and perdof CRM variants on LIBERO Object. The argmin baseline (14%) serves as a reference line, representing the performance ceiling achievable through selection alone without learned correction.
24-
25-The obs_only CRM maintains stable performance across the entire magnitude range. At epsilon=0.03, success rate is 16%; at epsilon=0.2, it peaks at 17.5% (multi-seed); at epsilon=1.42 (effectively uncapped), it remains at 16.5% (seeds 42/44: 17/16%). This flatness demonstrates that observation-conditioned corrections learn a safe residual direction that does not degrade even when the magnitude constraint is fully relaxed. The correction vector aligns with beneficial adjustments regardless of its allowed norm.
26-
27-The perdof CRM exhibits progressive collapse as epsilon increases. Starting at 14% for epsilon=0.03 (matching the argmin baseline, since the correction is negligibly small), performance holds at 14% for epsilon=0.05, then drops to 10% at epsilon=0.1, remains at 10% for epsilon=0.2, falls to 4% at epsilon=0.3, and reaches 0% (complete task failure) at epsilon=1.42. This progressive collapse reveals that per-DOF conformal features generate noisy directional signals. At small magnitudes the noise is harmless; as epsilon grows, the erroneous correction direction overwhelms the base policy's reasonable actions. The mechanism is detailed in Section 3.5: with K=10 samples in a 6-dimensional per-step action space, the per-step covariance estimates carry 30-40% eigenvalue error despite Ledoit-Wolf shrinkage, producing unreliable per-dimension statistics that serve as conditioning inputs to the CRM.
28-
29-
30-## 4.4 Uncapped Correction Ablation
31-
32-To isolate the safety properties of each conditioning strategy, we evaluate both CRM variants with epsilon=1.42, which removes the norm bound entirely and allows the model to apply corrections of arbitrary magnitude. This stress test reveals the intrinsic directional quality of the learned residuals independent of any magnitude safeguard.
33-
34-The obs_only CRM at epsilon=1.42 achieves 17% (seed 42) and 16% (seed 44), with mean 16.5% (std=0.7%). This performance matches the bounded configurations (epsilon=0.2 yields 17.5%), confirming that the observation-conditioned CRM learns corrections that are inherently safe in direction. The model does not exploit the relaxed constraint to produce large, harmful corrections. Even without explicit bounding, the learned residual remains conservative.
35-
36-The perdof CRM at epsilon=1.42 collapses to 0% success rate (seed 42), representing complete task failure across all 100 trials. Every rollout terminates without achieving the goal. This catastrophic outcome, compared to the 11% achieved at epsilon=0.1 with identical model weights, demonstrates that per-DOF conditioning produces residuals whose direction is fundamentally unreliable. The norm bound is the only mechanism preventing total failure for this conditioning strategy. This finding has practical implications: any deployment of per-DOF-conditioned corrections requires strict magnitude control, whereas observation-conditioned corrections can operate safely even without explicit bounds.
37-
38-
39-## 4.5 Cross-Seed Consistency
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "6da60ccd-98ed-4a5d-9281-7263c39f4fbc",
  "tool_use_result": {
    "stdout": "14:Table 1 presents the primary comparison across all six methods on LIBERO Object. The obs_only CRM achieves the highest mean success rate at 17.5% (seeds 42/43/44/45 = 22/16/16/16%, std=3.0%), representing a +6.7 percentage point improvement over the vla-only baseline (10.8%, std=1.4%) and a +3.5 percentage point improvement over argmin selection alone (14.0%, std=2.6%). The vla-mean aggregation baseline (12.3%, std=2.5%) provides only marginal benefit over single-sample inference, confirming that naive averaging does not address the distributional issues in the action space. [TODO: fill seed45/46/47 for argmin] [TODO: fill seed46/47 for obs_only]\n15-\n16-The per-DOF and scalar CRM variants fail to improve over the VLA baseline. The perdof CRM (seeds 42/43/44: 11/12/8%, mean=10.3%, std=2.1%) and scalar CRM (seeds 43/44: 10/6%, mean=8.0%, std=2.8%) perform at or below the uncorrected policy. [TODO: fill seed45 for scalar] This negative result is central to our contribution: identical architecture and training produce divergent outcomes depending solely on the conditioning signal. The obs_only CRM succeeds because observation features provide stable directional information for correction, while conformal score features introduce noise that compounds with correction magnitude.\n17-\n18-The effect size of obs_only over argmin (+3.5pp) is modest in absolute terms. However, the consistent improvement across all evaluated seeds, combined with the robustness analysis in Section 4.3, supports the claim that observation-conditioned corrections provide reliable non-degrading enhancement. A Fisher exact test on pooled trials (700 total across seeds) yields p=0.048 for obs_only vs argmin. [TODO: update with 6-seed pooled test]\n19-\n20-\n21-## 4.3 Magnitude Sensitivity Analysis\n22-\n23-Figure 2 presents the core mechanistic finding: the interaction between conditioning features and correction magnitude. We sweep the norm bound epsilon across six values (0.03, 0.05, 0.1, 0.2, 0.3, 1.42) for both obs_only and perdof CRM variants on LIBERO Object. The argmin baseline (14%) serves as a reference line, representing the performance ceiling achievable through selection alone without learned correction.\n24-\n25-The obs_only CRM maintains stable performance across the entire magnitude range. At epsilon=0.03, success rate is 16%; at epsilon=0.2, it peaks at 17.5% (multi-seed); at epsilon=1.42 (effectively uncapped), it remains at 16.5% (seeds 42/44: 17/16%). This flatness demonstrates that observation-conditioned corrections learn a safe residual direction that does not degrade even when the magnitude constraint is fully relaxed. The correction vector aligns with beneficial adjustments regardless of its allowed norm.\n26-\n27-The perdof CRM exhibits progressive collapse as epsilon increases. Starting at 14% for epsilon=0.03 (matching the argmin baseline, since the correction is negligibly small), performance holds at 14% for epsilon=0.05, then drops to 10% at epsilon=0.1, remains at 10% for epsilon=0.2, falls to 4% at epsilon=0.3, and reaches 0% (complete task failure) at epsilon=1.42. This progressive collapse reveals that per-DOF conformal features generate noisy directional signals. At small magnitudes the noise is harmless; as epsilon grows, the erroneous correction direction overwhelms the base policy's reasonable actions. The mechanism is detailed in Section 3.5: with K=10 samples in a 6-dimensional per-step action space, the per-step covariance estimates carry 30-40% eigenvalue error despite Ledoit-Wolf shrinkage, producing unreliable per-dimension statistics that serve as conditioning inputs to the CRM.\n28-\n29-\n30-## 4.4 Uncapped Correction Ablation\n31-\n32-To isolate the safety properties of each conditioning strategy, we evaluate both CRM variants with epsilon=1.42, which removes the norm bound entirely and allows the model to apply corrections of arbitrary magnitude. This stress test reveals the intrinsic directional quality of the learned residuals independent of any magnitude safeguard.\n33-\n34-The obs_only CRM at epsilon=1.42 achieves 17% (seed 42) and 16% (seed 44), with mean 16.5% (std=0.7%). This performance matches the bounded configurations (epsilon=0.2 yields 17.5%), confirming that the observation-conditioned CRM learns corrections that are inherently safe in direction. The model does not exploit the relaxed constraint to produce large, harmful corrections. Even without explicit bounding, the learned residual remains conservative.\n35-\n36-The perdof CRM at epsilon=1.42 collapses to 0% success rate (seed 42), representing complete task failure across all 100 trials. Every rollout terminates without achieving the goal. This catastrophic outcome, compared to the 11% achieved at epsilon=0.1 with identical model weights, demonstrates that per-DOF conditioning produces residuals whose direction is fundamentally unreliable. The norm bound is the only mechanism preventing total failure for this conditioning strategy. This finding has practical implications: any deployment of per-DOF-conditioned corrections requires strict magnitude control, whereas observation-conditioned corrections can operate safely even without explicit bounds.\n37-\n38-\n39-## 4.5 Cross-Seed Consistency",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "02c8be3a-3fe2-42ae-a9ae-a0cf6f07e2a2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wc1hgb5LDNUDTwFHGeRxDX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2184,
      "cache_read_input_tokens": 59076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2184
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01CeWPV2TKRk65VeZ6wnKunF`</summary>

```json
{
  "command": "grep -rln \"Goal.*83.7\\|Object.*77.7\\|VLA-only.*83.7\\|77.7±1.3\\|85.0±1.3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ 2>/dev/null | grep -v \".pdf$\" | head -20",
  "description": "Find files with the audit Table 1 values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "636cddbc-223a-43fd-8961-95cda4c36aec",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wc1hgb5LDNUDTwFHGeRxDX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2184,
      "cache_read_input_tokens": 59076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2184
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-25T01:52:44.097Z_

<details><summary>↩ Tool result · `toolu_01CeWPV2TKRk65VeZ6wnKunF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_oft-libero-version-fix_20260522T130347.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_table1-long-update-and-trigger-figure_20260523T221950_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_failed-experiments-misdiagnosis_20260520T112559.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_crm-loss-conformal_20260522T062919_retry1_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_design_plan802-openvla-corrector_20260517T224214.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_pi05-long-seed43-44-r4_20260522T164138.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_pi05-baseline-r3-batch_20260521T121613_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_ssh_full-cluster-scan-and-harvest_20260520T054720.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_rewrite-introduction_20260515T194914.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_lerobot-libero-recipes_20260513T094527.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_deploy_precompute-bjb1-18228_20260521T132657_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_vla-baseline-aggregation_20260519T182814.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_cron_register-obj-s47-r2_20260524T134041_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_magnitude-robustness-literature_20260515T155457.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_harvest_pi05-vla-only-baseline-all6_20260521T122006_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_literature-gap-fill_20260515T134355.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_code_stat-analysis-pipeline_20260515T164814.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7c1df558-ed9c-4a3a-b407-7b350af3bd60",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_oft-libero-version-fix_20260522T130347.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_table1-long-update-and-trigger-figure_20260523T221950_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_failed-experiments-misdiagnosis_20260520T112559.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_crm-loss-conformal_20260522T062919_retry1_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_design_plan802-openvla-corrector_20260517T224214.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_pi05-long-seed43-44-r4_20260522T164138.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_pi05-baseline-r3-batch_20260521T121613_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_ssh_full-cluster-scan-and-harvest_20260520T054720.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_rewrite-introduction_20260515T194914.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_lerobot-libero-recipes_20260513T094527.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_deploy_precompute-bjb1-18228_20260521T132657_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_vla-baseline-aggregation_20260519T182814.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_cron_register-obj-s47-r2_20260524T134041_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_magnitude-robustness-literature_20260515T155457.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_harvest_pi05-vla-only-baseline-all6_20260521T122006_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_literature-gap-fill_20260515T134355.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_code_stat-analysis-pipeline_20260515T164814.log",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01KUNTEfrv37jA19cHiRse4t`</summary>

```json
{
  "command": "grep -n -B 3 -A 8 \"83.7\\|85.0\\|77.7\\|77.8\\|76.5\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex 2>/dev/null | head -80",
  "description": "Read experiments tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "e2f5203a-961e-4aaa-bfe5-d1246b98e8a8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AEu7E4fDFtaMeKsAwGYbSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 61260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-25T01:52:47.573Z_

<details><summary>↩ Tool result · `toolu_01KUNTEfrv37jA19cHiRse4t`</summary>

```text
41-\toprule
42-Method & $K$ & Spatial (\%) & Object (\%) & Goal (\%) & Long (\%) \\
43-\midrule
44:VLA-only & 1 & $78.7 \pm 0.3^{(3)}$ & $77.7 \pm 1.3^{(5)}$ & $83.7 \pm 1.3^{(3)}$ & $58.0 \pm 1.5^{(3)}$ \\
45:CRM always-on & 10 & $79.8 \pm 1.3^{(3)}$ & $76.5 \pm 2.3^{(3)}$ & $83.7 \pm 1.8^{(3)}$ & $55.8 \pm 1.2^{(3)}$ \\
46-$K{=}10$ argmin & 10 & $80.3 \pm 1.0^{(3)}$ & $77.3 \pm 1.5^{(3)}$ & $80.8 \pm 0.3^{(3)}$ & $56.5^{(1)}$ \\
47-$K{=}2$ mean & 2 & --- & $77.5 \pm 2.3^{(3)}$ & $83.0 \pm 2.2^{(3)}$ & $57.0^{(1)}$ \\
48-\midrule
49:ACR-VLA & 2 & $80.8 \pm 1.1^{(3)}$ & $77.8 \pm 2.1^{(5)}$ & $85.0 \pm 1.3^{(3)}$ & $57.7 \pm 1.5^{(3)}$ \\
50-\midrule
51-$\Delta$ vs VLA-only & & $+2.1$ & $+0.1$ & $+1.3$ & $-0.3$ \\
52-$\Delta_{\mathrm{CRM}}$ vs CRM & & $+1.0$ & $+1.3$ & $+1.3$ & $+1.9$ \\
53-\bottomrule
54-\end{tabular}
55-\end{table}
56-
57-\begin{figure}[t]
--
63-
64-\looseness=-1 Table~\ref{tab:main} and Figure~\ref{fig:method_bar} report task success rates across all methods and suites. ACR-VLA's adaptive gate correctly modulates intervention intensity: on suites where the VLA shows high uncertainty (trigger rate ${>}$7\%), the gate fires and the CRM applies corrections ($+$2.1\,pp on Spatial, $+$1.3\,pp on Goal, 3 seeds each). On suites where the VLA is already confident (trigger rate ${<}$5\%), the gate rarely fires and the output matches baseline: Object ($\Delta{=}{+}0.1$\,pp, 5 seeds) and Long ($\Delta{=}{-}0.3$\,pp, 3 seeds). This avoids the degradation caused by unconditional correction ($-$1.2\,pp Object, $-$2.2\,pp Long).
65-
66:\looseness=-2 Unconditional correction is unstable across suites. \emph{CRM always-on} ($\varepsilon{=}0.05$) applies correction at every step: $-$2.2\,pp on Long ($55.8 \pm 1.2$\%, 3 seeds), $-$1.2\,pp on Object ($76.5 \pm 2.3$\%, 3 seeds), $\Delta{\approx}0$ on Goal ($83.7 \pm 1.8$\%, 3 seeds), and $+$1.1\,pp on Spatial. Without gating, the CRM hurts on two suites while providing inconsistent benefit elsewhere. \emph{$K{=}10$ argmin} invests $10{\times}$ the VLA forward passes but hurts on Goal ($-$2.9\,pp, $80.8 \pm 0.3$\%, 3 seeds). Selection without correction is insufficient. \emph{$K{=}2$ mean} offers no learned correction mechanism ($-$0.7\,pp Goal, $-$1.0\,pp Long; Long is single-seed preliminary), isolating that multi-sampling alone is not sufficient.
67-
68-\paragraph{Statistical note.}
69-\looseness=-1 Paired differences (Adaptive$-$VLA) are directionally consistent (positive on 3 of 4 suites) but do not reach $p < 0.05$ with $n{=}$5--6 matched seeds. The stronger claim is Adaptive vs.\ CRM always-on: ACR-VLA exceeds unconditional correction on all four suites ($\Delta_{\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\,pp), confirming that gating prevents the degradation caused by unconditional correction.
70-
71-\subsection{Why Gating Is Necessary}
72-\label{sec:failure_modes}
73-
74-\begin{figure}[t]
--
80-
81-\looseness=-1 The main results reveal a core finding: \emph{unconditional correction is unstable across suites}. CRM always-on applies the same learned residual to every step, including the ${\sim}$80--90\% where the VLA is already confident. This produces inconsistent effects: $+$1.1\,pp on Spatial, $\Delta{\approx}0$ on Goal, $-$1.2\,pp on Object (3 seeds), and $-$2.2\,pp on Long (3 seeds). The Object and Long degradation shows that corrections on already-confident steps are harmful noise (Figure~\ref{fig:trigger_scatter}).
82-
83:\looseness=-1 ACR-VLA's adaptive gate resolves this instability. On Object, where the VLA is already confident, the gate triggers on only 3.5\% of steps; the CRM barely fires, and the output matches baseline ($77.8$\%, $\Delta{=}{+}0.1$\,pp, 5 seeds). This is the correct behavior: the gate identifies that Object needs no correction and avoids the $-$1.2\,pp harm of unconditional correction. On Spatial and Goal, where higher uncertainty triggers correction on 7--20\% of steps, the CRM provides targeted improvement ($+$2.1\,pp and $+$1.3\,pp respectively). On Long, the gate triggers on ${\sim}$4\% of steps; ACR-VLA preserves baseline ($57.7 \pm 1.5$\%, $\Delta{=}{-}0.3$\,pp, 3 seeds) while CRM always-on degrades by $-$2.2\,pp.
84-
85-\begin{figure}[t]
86-  \centering
87-  \includegraphics[width=\linewidth]{fig_tau_sweep.pdf}
88-  \caption{Threshold $\tau$ controls trigger rate, which controls improvement: inverted-U on both Goal and Spatial (seed 42, $\varepsilon{=}0.2$). Low $\tau$ overcorrects (${>}$70\% trigger); high $\tau$ disables correction. The optimal region $\tau \in [0.20, 0.25]$ is consistent across suites. Labels show trigger rate at each $\tau$. See Appendix~\ref{sec:tau_sweep} for details.}
89-  \label{fig:tau_sweep}
90-\end{figure}
91-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "2c152cd4-ebac-4f1d-834a-5692b789163c",
  "tool_use_result": {
    "stdout": "41-\\toprule\n42-Method & $K$ & Spatial (\\%) & Object (\\%) & Goal (\\%) & Long (\\%) \\\\\n43-\\midrule\n44:VLA-only & 1 & $78.7 \\pm 0.3^{(3)}$ & $77.7 \\pm 1.3^{(5)}$ & $83.7 \\pm 1.3^{(3)}$ & $58.0 \\pm 1.5^{(3)}$ \\\\\n45:CRM always-on & 10 & $79.8 \\pm 1.3^{(3)}$ & $76.5 \\pm 2.3^{(3)}$ & $83.7 \\pm 1.8^{(3)}$ & $55.8 \\pm 1.2^{(3)}$ \\\\\n46-$K{=}10$ argmin & 10 & $80.3 \\pm 1.0^{(3)}$ & $77.3 \\pm 1.5^{(3)}$ & $80.8 \\pm 0.3^{(3)}$ & $56.5^{(1)}$ \\\\\n47-$K{=}2$ mean & 2 & --- & $77.5 \\pm 2.3^{(3)}$ & $83.0 \\pm 2.2^{(3)}$ & $57.0^{(1)}$ \\\\\n48-\\midrule\n49:ACR-VLA & 2 & $80.8 \\pm 1.1^{(3)}$ & $77.8 \\pm 2.1^{(5)}$ & $85.0 \\pm 1.3^{(3)}$ & $57.7 \\pm 1.5^{(3)}$ \\\\\n50-\\midrule\n51-$\\Delta$ vs VLA-only & & $+2.1$ & $+0.1$ & $+1.3$ & $-0.3$ \\\\\n52-$\\Delta_{\\mathrm{CRM}}$ vs CRM & & $+1.0$ & $+1.3$ & $+1.3$ & $+1.9$ \\\\\n53-\\bottomrule\n54-\\end{tabular}\n55-\\end{table}\n56-\n57-\\begin{figure}[t]\n--\n63-\n64-\\looseness=-1 Table~\\ref{tab:main} and Figure~\\ref{fig:method_bar} report task success rates across all methods and suites. ACR-VLA's adaptive gate correctly modulates intervention intensity: on suites where the VLA shows high uncertainty (trigger rate ${>}$7\\%), the gate fires and the CRM applies corrections ($+$2.1\\,pp on Spatial, $+$1.3\\,pp on Goal, 3 seeds each). On suites where the VLA is already confident (trigger rate ${<}$5\\%), the gate rarely fires and the output matches baseline: Object ($\\Delta{=}{+}0.1$\\,pp, 5 seeds) and Long ($\\Delta{=}{-}0.3$\\,pp, 3 seeds). This avoids the degradation caused by unconditional correction ($-$1.2\\,pp Object, $-$2.2\\,pp Long).\n65-\n66:\\looseness=-2 Unconditional correction is unstable across suites. \\emph{CRM always-on} ($\\varepsilon{=}0.05$) applies correction at every step: $-$2.2\\,pp on Long ($55.8 \\pm 1.2$\\%, 3 seeds), $-$1.2\\,pp on Object ($76.5 \\pm 2.3$\\%, 3 seeds), $\\Delta{\\approx}0$ on Goal ($83.7 \\pm 1.8$\\%, 3 seeds), and $+$1.1\\,pp on Spatial. Without gating, the CRM hurts on two suites while providing inconsistent benefit elsewhere. \\emph{$K{=}10$ argmin} invests $10{\\times}$ the VLA forward passes but hurts on Goal ($-$2.9\\,pp, $80.8 \\pm 0.3$\\%, 3 seeds). Selection without correction is insufficient. \\emph{$K{=}2$ mean} offers no learned correction mechanism ($-$0.7\\,pp Goal, $-$1.0\\,pp Long; Long is single-seed preliminary), isolating that multi-sampling alone is not sufficient.\n67-\n68-\\paragraph{Statistical note.}\n69-\\looseness=-1 Paired differences (Adaptive$-$VLA) are directionally consistent (positive on 3 of 4 suites) but do not reach $p < 0.05$ with $n{=}$5--6 matched seeds. The stronger claim is Adaptive vs.\\ CRM always-on: ACR-VLA exceeds unconditional correction on all four suites ($\\Delta_{\\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\\,pp), confirming that gating prevents the degradation caused by unconditional correction.\n70-\n71-\\subsection{Why Gating Is Necessary}\n72-\\label{sec:failure_modes}\n73-\n74-\\begin{figure}[t]\n--\n80-\n81-\\looseness=-1 The main results reveal a core finding: \\emph{unconditional correction is unstable across suites}. CRM always-on applies the same learned residual to every step, including the ${\\sim}$80--90\\% where the VLA is already confident. This produces inconsistent effects: $+$1.1\\,pp on Spatial, $\\Delta{\\approx}0$ on Goal, $-$1.2\\,pp on Object (3 seeds), and $-$2.2\\,pp on Long (3 seeds). The Object and Long degradation shows that corrections on already-confident steps are harmful noise (Figure~\\ref{fig:trigger_scatter}).\n82-\n83:\\looseness=-1 ACR-VLA's adaptive gate resolves this instability. On Object, where the VLA is already confident, the gate triggers on only 3.5\\% of steps; the CRM barely fires, and the output matches baseline ($77.8$\\%, $\\Delta{=}{+}0.1$\\,pp, 5 seeds). This is the correct behavior: the gate identifies that Object needs no correction and avoids the $-$1.2\\,pp harm of unconditional correction. On Spatial and Goal, where higher uncertainty triggers correction on 7--20\\% of steps, the CRM provides targeted improvement ($+$2.1\\,pp and $+$1.3\\,pp respectively). On Long, the gate triggers on ${\\sim}$4\\% of steps; ACR-VLA preserves baseline ($57.7 \\pm 1.5$\\%, $\\Delta{=}{-}0.3$\\,pp, 3 seeds) while CRM always-on degrades by $-$2.2\\,pp.\n84-\n85-\\begin{figure}[t]\n86-  \\centering\n87-  \\includegraphics[width=\\linewidth]{fig_tau_sweep.pdf}\n88-  \\caption{Threshold $\\tau$ controls trigger rate, which controls improvement: inverted-U on both Goal and Spatial (seed 42, $\\varepsilon{=}0.2$). Low $\\tau$ overcorrects (${>}$70\\% trigger); high $\\tau$ disables correction. The optimal region $\\tau \\in [0.20, 0.25]$ is consistent across suites. Labels show trigger rate at each $\\tau$. See Appendix~\\ref{sec:tau_sweep} for details.}\n89-  \\label{fig:tau_sweep}\n90-\\end{figure}\n91-",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "ebb1dada-76b6-4b8c-8d6e-6141c9a26ed1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EUNgrM3KVge2xiELe8yafX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 63169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2727
      },
      "output_tokens": 94,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01SS1wZugfdc2Cq9mXNnVwpS`</summary>

```json
{
  "command": "grep -rln \"table_data\\|Table 1\\|table 1\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/ 2>/dev/null | grep -v \".pdf$\" | head -20",
  "description": "Find Table 1 data sources"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "aa6ef31f-541a-48c1-93ec-fd208794e2e2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EUNgrM3KVge2xiELe8yafX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 63169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2727
      },
      "output_tokens": 94,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-25T01:52:58.380Z_

<details><summary>↩ Tool result · `toolu_01SS1wZugfdc2Cq9mXNnVwpS`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft_6d6390.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/contribution_list.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/paper_evidence_package.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/norm_sweep_aggregation_20260521.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/a1_vla_survey_and_crm_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/results_tables.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/object_results_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/narrative_b_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/reference_audit_r2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521_b7ea89.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "ba4a1ef3-dc98-49e8-ba32-8fd9cff2f2ff",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft_6d6390.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/contribution_list.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/paper_evidence_package.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/norm_sweep_aggregation_20260521.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/a1_vla_survey_and_crm_analysis.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/results_tables.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/object_results_summary.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/narrative_b_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/reference_audit_r2.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521_b7ea89.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_audit_20260521.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01F9qqGxaiGuMWtHSRFThDSh`</summary>

```json
{
  "command": "grep -n -B 2 -A 10 \"83.7\\|85.0\\|77.7\\|77.8\\|76.5\\|Goal\\|Object\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/results_tables.md 2>/dev/null | head -80",
  "description": "Read results tables"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "37d91190-f02f-4fb1-8ea2-e8edb303ec0f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GTgTjbeMRXw24LXtXpRPf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 65896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-25T01:53:02.151Z_

<details><summary>↩ Tool result · `toolu_01F9qqGxaiGuMWtHSRFThDSh`</summary>

```text
5----
6-
7:## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)
8-
9-| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |
10-|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
11-| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |
12-| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |
13-| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |
14-| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |
15-| perdof (norm=0.1) | `eval-acr-object-v4-perdof` | **11%** | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 |
16-| scalar (norm=0.1) | `eval-acr-object-v4-scalar` | **9%** | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 |
17-
--
81----
82-
83:## Table 4: Object Benchmark — Magnitude Results (mixed status)
84-
85-### FINAL (seed=42, 10/10 tasks)
86-
87-| Method | norm | Overall SR | Exp ID |
88-|--------|:----:|:---------:|--------|
89-| obs_only | 0.1 | **19%** | `eval-acr-object-v4-obs-only` |
90-| obs_only | 0.2 | **22%** | `eval-acr-object-obs-only-norm02` |
91-
92-obs_only norm=0.2 per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=30, bbq_sauce=40, ketchup=20, tomato_sauce=10, butter=10, milk=20, chocolate_pudding=60, orange_juice=30
93-
--
106----
107-
108:## Table 5: Seed=43 Object Benchmark — Progress Tracker
109-
110-| Method | Exp ID | Status | Tasks Done | Partial Per-task SR |
111-|--------|--------|:------:|:----------:|---------------------|
112-| VLA-only (K=1) | `eval-vla-only-object-seed43` | **DONE** | 10/10 | **Overall: 12%** — alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0, butter=0, milk=10, chocolate_pudding=40, orange_juice=20 |
113-| obs_only (norm=0.1) | `eval-obs-only-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0 |
114-| argmin (K=10) | `eval-argmin-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=20, ketchup=10, tomato_sauce=10 |
115-| perdof (norm=0.1) | `eval-perdof-object-seed43` | RUNNING | 4/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=30 |
116-| VLA-mean (K=10) | `eval-vla-mean-object-seed43` | RUNNING | 3/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20 |
117-| scalar (norm=0.1) | `eval-scalar-object-seed43` | RUNNING | 2/10 | alphabet_soup=0, cream_cheese=0 |
118-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "e64e8d02-1a4c-4276-82dc-df2785fb4188",
  "tool_use_result": {
    "stdout": "5----\n6-\n7:## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)\n8-\n9-| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |\n10-|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n11-| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |\n12-| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |\n13-| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |\n14-| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |\n15-| perdof (norm=0.1) | `eval-acr-object-v4-perdof` | **11%** | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 |\n16-| scalar (norm=0.1) | `eval-acr-object-v4-scalar` | **9%** | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 |\n17-\n--\n81----\n82-\n83:## Table 4: Object Benchmark — Magnitude Results (mixed status)\n84-\n85-### FINAL (seed=42, 10/10 tasks)\n86-\n87-| Method | norm | Overall SR | Exp ID |\n88-|--------|:----:|:---------:|--------|\n89-| obs_only | 0.1 | **19%** | `eval-acr-object-v4-obs-only` |\n90-| obs_only | 0.2 | **22%** | `eval-acr-object-obs-only-norm02` |\n91-\n92-obs_only norm=0.2 per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=30, bbq_sauce=40, ketchup=20, tomato_sauce=10, butter=10, milk=20, chocolate_pudding=60, orange_juice=30\n93-\n--\n106----\n107-\n108:## Table 5: Seed=43 Object Benchmark — Progress Tracker\n109-\n110-| Method | Exp ID | Status | Tasks Done | Partial Per-task SR |\n111-|--------|--------|:------:|:----------:|---------------------|\n112-| VLA-only (K=1) | `eval-vla-only-object-seed43` | **DONE** | 10/10 | **Overall: 12%** — alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0, butter=0, milk=10, chocolate_pudding=40, orange_juice=20 |\n113-| obs_only (norm=0.1) | `eval-obs-only-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0 |\n114-| argmin (K=10) | `eval-argmin-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=20, ketchup=10, tomato_sauce=10 |\n115-| perdof (norm=0.1) | `eval-perdof-object-seed43` | RUNNING | 4/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=30 |\n116-| VLA-mean (K=10) | `eval-vla-mean-object-seed43` | RUNNING | 3/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20 |\n117-| scalar (norm=0.1) | `eval-scalar-object-seed43` | RUNNING | 2/10 | alphabet_soup=0, cream_cheese=0 |\n118-",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "f08e5f9d-2443-42f4-bb4a-68d941a124b0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KUPgU6WRe9ge5eyyPRFBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 67664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1816
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01SkjiJf44paFbfVXjRtGxhu`</summary>

```json
{
  "command": "grep -n -B 1 -A 5 \"83.7\\|85.0\\|77.7\\|77.8\\|76.5\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/narrative_b_draft.md 2>/dev/null | head -40",
  "description": "Read narrative B draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7571bc0f-8578-40b2-81bb-0712b034b45c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KUPgU6WRe9ge5eyyPRFBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 67664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1816
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-25T01:53:06.324Z_

<details><summary>↩ Tool result · `toolu_01SkjiJf44paFbfVXjRtGxhu`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "ab3b20a0-72b3-4a67-9c52-de050e9cb82e",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_01UjxQe1c42fA3ArhpaBsRuL`</summary>

```json
{
  "command": "grep -n -B 1 -A 10 \"Goal.*seed.*42\\|Object.*seed.*42\\|table.*seed\\|82.5\\|82.0\\|83.5\\|seeds.*42-44\\|seeds 42.*44\\|seeds=42,43,44\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/paper_evidence_package.md 2>/dev/null | head -80",
  "description": "Search evidence package for seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7d7df378-f56f-4c70-97d5-9369f8606b0a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01REUbTrKXco7SPjnkRqFAdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 69480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-25T01:53:10.909Z_

<details><summary>↩ Tool result · `toolu_01UjxQe1c42fA3ArhpaBsRuL`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "65a49707-85a0-4c8c-a57f-246fb672e78d",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01QUhzHawVdKmFWRcWpCqJQk`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/paper_evidence_package.md 2>/dev/null | head -80",
  "description": "Read evidence package"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "b87a5a3a-cd56-4c1b-b675-cd31a350e945",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DgFxHHvs7uWW4m9jvNKdiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 69757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-25T01:53:14.061Z_

<details><summary>↩ Tool result · `toolu_01QUhzHawVdKmFWRcWpCqJQk`</summary>

```text
# Paper Evidence Package — ACR-VLA Conformal Refinement

> Prepared: 2026-05-18. For Paper Agent startup. Contains locked evidence, data tables, figure inventory, and decision chain summary. No prose — data and facts only.

---

## 1. Method Description (D058 Corrected)

### Pipeline (K=10, primary result)
1. Frozen VLA (SmolVLA 0.4B) generates **K=10 action samples** from flow-matching
2. **Argmin selection**: pick candidate closest to sample mean (L2 distance) — same for all CRM variants
3. **CRM correction**: lightweight MLP (~337K params) takes selected action + conditioning features → outputs refined action
4. Apply correction with norm clipping: `||correction|| ≤ ε`

### CRM Variants (same architecture, different conditioning)
- **obs_only**: VLA observation features only (960D). **Does NOT use conformal statistics.**
- **perdof**: observation features + per-DOF conformal features (40D CGS: 30 per-DOF std + 5 conformal radius + 5 log volume)
- **scalar**: observation features + scalar uncertainty (1D)

### Key Architectural Facts
- CRM is a **correction** module, not a selection/ranking module
- CRM never scores individual candidates — it only refines the one selected by argmin
- The 17.5% vs 12.3% improvement comes from **learned correction**, not ranking
- K-value curve mechanism: more samples → better argmin starting point → more effective correction

### K=1 Mode
- No multi-sample selection (only 1 VLA sample)
- CRM directly corrects single VLA output using observation features
- K=1 CRM ≈ VLA-only baseline (10.3% vs 10.8%) — correction alone without selection is insufficient

---

## 2. Complete Evidence Tables

### 2A. Magnitude Curve (Figure 2 data)

**obs_only (observation-conditioned CRM)**

| ε (norm clip) | Seeds | Mean SR | Std | n |
|---------------|-------|---------|-----|---|
| 0.03 | 42=16% | 16.0% | — | 1 |
| 0.05 | 42=13%, 43=14% | 13.5% | 0.71% | 2 |
| 0.1 | 42=19%, 43=12%, 44=16%, 45=14% | 15.25% | 2.99% | 4 |
| **0.2** | **42=22%, 43=16%, 44=16%, 45=16%, 46=15%, 47=20%** | **17.5%** | **2.81%** | **6** |
| 0.3 | 42=19%, 44=18%, 45=14%, 46=17% | 17.0% | 2.16% | 4 |
| uncapped (1.42) | 44=16%, 45=12%, 46=15% | 14.33% | 2.08% | 3 |

**Narrative**: obs_only is robust across all magnitudes. Peak at ε=0.2 (17.5%), stable 14-17% from ε=0.03 to uncapped.

**perdof (per-DOF conformal-conditioned CRM)**

| ε (norm clip) | Seeds | Mean SR | Std | n |
|---------------|-------|---------|-----|---|
| 0.03 | 42=14% | 14.0% | — | 1 |
| 0.05 | 42=14% | 14.0% | — | 1 |
| 0.1 | 42=11%, 43=12%, 44=8%, 45=11%, 46=10%, 47=14% | 11.0% | 2.0% | 6 |
| 0.2 | 42=11%, 43=9%, 44=10%, 45=9%, 46=9%, 47=11% | 9.83% | 0.98% | 6 |
| 0.3 | 42=4%, 44=4%, 45=6% | 4.67% | 1.15% | 3 |
| uncapped (1.42) | 42=0%, 44=0%(partial 9/10), 46=0% | 0.0% | 0.0% | 3 |

**Narrative**: perdof shows progressive collapse 14% → 11% → 10% → 5% → 0% as magnitude increases. Catastrophic failure at uncapped (all seeds 0%).

### 2B. K-Value Curve

| K | Method | Mean SR | Std | CI 95% | n | Note |
|---|--------|---------|-----|--------|---|------|
| 1 | CRM K=1 multiscale | 10.33% | 1.53% | [8.6%, 12.1%] | 3 | ≈ VLA-only baseline |
| 5 | CRM obs_only ε=0.2 | 14.0% | — | — | 1 | seed42 verified, seed43 running |
| 10 | CRM obs_only ε=0.2 | 17.5% | 2.81% | [15.3%, 19.8%] | 6 | Primary result |

**Alternative K=1**: CRM K=1 ACCG: mean 10.0% (n=3), also ≈ VLA-only.

**Monotonic trend**: K=1 (10.3%) → K=5 (14%) → K=10 (17.5%). More samples = better argmin starting point = more effective correction.

### 2C. Baseline Comparison (LIBERO-Object, K=10)

| Method | Mean SR | Std | n | Note |
|--------|---------|-----|---|------|
| **CRM obs_only ε=0.2** | **17.5%** | **2.81%** | **6** | **Best method** |
| CRM perdof ε=0.1 | 11.0% | 2.0% | 6 | Below VLA-only at higher ε |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "47740914-305b-4a14-aa38-a564efc8a818",
  "tool_use_result": {
    "stdout": "# Paper Evidence Package — ACR-VLA Conformal Refinement\n\n> Prepared: 2026-05-18. For Paper Agent startup. Contains locked evidence, data tables, figure inventory, and decision chain summary. No prose — data and facts only.\n\n---\n\n## 1. Method Description (D058 Corrected)\n\n### Pipeline (K=10, primary result)\n1. Frozen VLA (SmolVLA 0.4B) generates **K=10 action samples** from flow-matching\n2. **Argmin selection**: pick candidate closest to sample mean (L2 distance) — same for all CRM variants\n3. **CRM correction**: lightweight MLP (~337K params) takes selected action + conditioning features → outputs refined action\n4. Apply correction with norm clipping: `||correction|| ≤ ε`\n\n### CRM Variants (same architecture, different conditioning)\n- **obs_only**: VLA observation features only (960D). **Does NOT use conformal statistics.**\n- **perdof**: observation features + per-DOF conformal features (40D CGS: 30 per-DOF std + 5 conformal radius + 5 log volume)\n- **scalar**: observation features + scalar uncertainty (1D)\n\n### Key Architectural Facts\n- CRM is a **correction** module, not a selection/ranking module\n- CRM never scores individual candidates — it only refines the one selected by argmin\n- The 17.5% vs 12.3% improvement comes from **learned correction**, not ranking\n- K-value curve mechanism: more samples → better argmin starting point → more effective correction\n\n### K=1 Mode\n- No multi-sample selection (only 1 VLA sample)\n- CRM directly corrects single VLA output using observation features\n- K=1 CRM ≈ VLA-only baseline (10.3% vs 10.8%) — correction alone without selection is insufficient\n\n---\n\n## 2. Complete Evidence Tables\n\n### 2A. Magnitude Curve (Figure 2 data)\n\n**obs_only (observation-conditioned CRM)**\n\n| ε (norm clip) | Seeds | Mean SR | Std | n |\n|---------------|-------|---------|-----|---|\n| 0.03 | 42=16% | 16.0% | — | 1 |\n| 0.05 | 42=13%, 43=14% | 13.5% | 0.71% | 2 |\n| 0.1 | 42=19%, 43=12%, 44=16%, 45=14% | 15.25% | 2.99% | 4 |\n| **0.2** | **42=22%, 43=16%, 44=16%, 45=16%, 46=15%, 47=20%** | **17.5%** | **2.81%** | **6** |\n| 0.3 | 42=19%, 44=18%, 45=14%, 46=17% | 17.0% | 2.16% | 4 |\n| uncapped (1.42) | 44=16%, 45=12%, 46=15% | 14.33% | 2.08% | 3 |\n\n**Narrative**: obs_only is robust across all magnitudes. Peak at ε=0.2 (17.5%), stable 14-17% from ε=0.03 to uncapped.\n\n**perdof (per-DOF conformal-conditioned CRM)**\n\n| ε (norm clip) | Seeds | Mean SR | Std | n |\n|---------------|-------|---------|-----|---|\n| 0.03 | 42=14% | 14.0% | — | 1 |\n| 0.05 | 42=14% | 14.0% | — | 1 |\n| 0.1 | 42=11%, 43=12%, 44=8%, 45=11%, 46=10%, 47=14% | 11.0% | 2.0% | 6 |\n| 0.2 | 42=11%, 43=9%, 44=10%, 45=9%, 46=9%, 47=11% | 9.83% | 0.98% | 6 |\n| 0.3 | 42=4%, 44=4%, 45=6% | 4.67% | 1.15% | 3 |\n| uncapped (1.42) | 42=0%, 44=0%(partial 9/10), 46=0% | 0.0% | 0.0% | 3 |\n\n**Narrative**: perdof shows progressive collapse 14% → 11% → 10% → 5% → 0% as magnitude increases. Catastrophic failure at uncapped (all seeds 0%).\n\n### 2B. K-Value Curve\n\n| K | Method | Mean SR | Std | CI 95% | n | Note |\n|---|--------|---------|-----|--------|---|------|\n| 1 | CRM K=1 multiscale | 10.33% | 1.53% | [8.6%, 12.1%] | 3 | ≈ VLA-only baseline |\n| 5 | CRM obs_only ε=0.2 | 14.0% | — | — | 1 | seed42 verified, seed43 running |\n| 10 | CRM obs_only ε=0.2 | 17.5% | 2.81% | [15.3%, 19.8%] | 6 | Primary result |\n\n**Alternative K=1**: CRM K=1 ACCG: mean 10.0% (n=3), also ≈ VLA-only.\n\n**Monotonic trend**: K=1 (10.3%) → K=5 (14%) → K=10 (17.5%). More samples = better argmin starting point = more effective correction.\n\n### 2C. Baseline Comparison (LIBERO-Object, K=10)\n\n| Method | Mean SR | Std | n | Note |\n|--------|---------|-----|---|------|\n| **CRM obs_only ε=0.2** | **17.5%** | **2.81%** | **6** | **Best method** |\n| CRM perdof ε=0.1 | 11.0% | 2.0% | 6 | Below VLA-only at higher ε |",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "6a17fe88-c3f0-46b2-a44d-12f41b224020",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01X1CHoLek1u5ycRZXeAzaQa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 70039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2113
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01FXMEjqZrt73RMhZLPrqaPk`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt | python3 -c \"\nimport json,sys\nd = json.load(sys.stdin)\nr = json.loads(d['result'])\nexps = r['data']['experiments']\n# Find Goal VLA-only and Adaptive\npatterns = ['goal-vla-only', 'vla-only-goal', 'goal.*adapt', 'goal.*crm', 'goal.*tau025', 'crm.*norm005.*goal', 'norm005-goal', 'goal-reconvla', 'goal-k2mean', 'goal-crm005']\nfor k,e in exps.items():\n    kl = k.lower()\n    if 'goal' in kl and ('vla-only' in kl or 'adapt' in kl or 'crm' in kl or 'norm005' in kl or 'tau025' in kl or 'reconvla' in kl or 'k2mean' in kl):\n        sr = e.get('metrics',{}).get('SR','?')\n        srv = e.get('spec',{}).get('server','?')\n        seed = e.get('spec',{}).get('seed','?')\n        cmd = e.get('spec',{}).get('command','')[:120]\n        print(f'{k} | seed={seed} | server={srv} | SR={sr} | cmd={cmd}')\n\" 2>&1 | sort | head -120",
  "description": "List Goal experiments by category"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "2bd2dfa0-9c2c-4083-86e7-03da259c2e50",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01X1CHoLek1u5ycRZXeAzaQa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 70039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2113
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-25T01:53:32.126Z_

<details><summary>↩ Tool result · `toolu_01FXMEjqZrt73RMhZLPrqaPk`</summary>

```text
crm-norm005-goal-s49 | seed=49 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 49 --n_rollouts 20 --K 10 -
eval-crm-goal-seed42 | seed=42 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 42 --K 10 -
eval-crm-goal-seed43 | seed=43 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 43 --K 10 -
eval-crm-goal-seed44 | seed=44 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 
eval-crm-goal-seed44-r2 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 44 --K 10 --max_correction_norm 0.2 --checkpoint /
eval-crm-goal-seed45 | seed=45 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 
eval-crm-goal-seed45-r2 | seed=45 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 45 --K 10 --max_correction_norm 0.2 --checkpoint /
eval-crm-goal-seed46 | seed=? | server=bjb2-28827 | SR=? | cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
eval-goal-vla-only-wrapper-s42 | seed=42 | server=bjb2-28827 | SR=? | cmd=bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark
eval-pi05-vla-only-goal-s42 | seed=42 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20
eval-pi05-vla-only-goal-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_rollouts 20
eval-pi05-vla-only-goal-seed42-r4 | seed=? | server=bjb1-18228 | SR=? | cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement 
eval-pi05-vla-only-goal-seed42-r4-std | seed=42 | server=N/A | SR=? | cmd=N/A - phantom entry
eval-pi05-vla-only-goal-seed43-r4 | seed=43 | server=bjb1-32546 | SR=? | cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/
eval-pi05-vla-only-goal-seed43-r4-std | seed=43 | server=N/A | SR=? | cmd=N/A - phantom entry
eval-pi05-vla-only-goal-seed44-r4 | seed=44 | server=bjb1-32546 | SR=? | cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/
eval-pi05-vla-only-goal-seed44-r4-std | seed=44 | server=N/A | SR=? | cmd=N/A - phantom entry
eval-smolvla-crm-goal-seed42 | seed=42 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/c
eval-smolvla-crm-goal-seed42-v1 | seed=? | server=? | SR=? | cmd=
eval-smolvla-crm-goal-seed43 | seed=43 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/c
eval-smolvla-crm-goal-seed43-v1 | seed=? | server=? | SR=? | cmd=
eval-smolvla-crm-goal-seed44-v1 | seed=? | server=? | SR=? | cmd=
eval-smolvla-crm-goal-seed44-v2 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint crm_best.pt
eval-supp-adapt-tau025-goal-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite
eval-supp-adapt-tau025-goal-s44 | seed=44 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpo
eval-supp-crm-norm005-goal-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_be
eval-supp-crm-norm005-goal-s44 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_be
eval-supp-crm-norm005-goal-s48 | seed=48 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 48 --n_rollouts 20 --K 10 -
eval-supp-goal-adapt-tau025-s42 | seed=? | server=? | SR=? | cmd=
eval-supp-goal-adapt-tau025-s45 | seed=45 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 45 --n_rollouts 2
eval-supp-goal-adapt-tau025-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 46 --n_rollouts 2
eval-supp-goal-adapt-tau025-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 2
eval-supp-goal-crm-norm005-s45 | seed=? | server=? | SR=? | cmd=
eval-supp-goal-crm-norm005-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 46 --n_rollouts 20 --max_co
eval-supp-goal-crm-norm005-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 -
eval-supp-goal-crm005-s42 | seed=42 | server=bjb2-28827 | SR=? | cmd=evaluate.py --mode crm_obs_only --max_correction_norm 0.05 --benchmark goal
eval-supp-goal-k2mean-s45 | seed=45 | server=cqa1-32758 | SR=0.81 | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 45 -
eval-supp-goal-k2mean-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 46 -
eval-supp-goal-k2mean-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --seed 47 --n_rol
eval-supp-goal-reconvla-s42 | seed=42 | server=bjb2-28827 | SR=? | cmd=bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --crm_check
eval-supp-goal-reconvla-s43 | seed=43 | server=cqa1-32758 | SR=? | cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_V
eval-supp-goal-reconvla-s44 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode reconvla --K 10 --benchmark goal --seed 44 --n_rollouts 20
eval-supp-goal-reconvla-s45 | seed=45 | server=bjb2-28827 | SR=0.855 | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm
eval-supp-goal-reconvla-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm
eval-supp-goal-reconvla-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 47 --n_rollouts 20 --K 2
eval-supp-goal-vla-only-s42 | seed=42 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 42 --n_rollouts 20
eval-supp-goal-vla-only-s42-bjb1 | seed=42 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 42 --n_rollouts 20
eval-supp-goal-vla-only-s43 | seed=43 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20
eval-supp-goal-vla-only-s44 | seed=44 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20
eval-supp-goal-vla-only-s45 | seed=45 | server=bjb2-28827 | SR=0.835 | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 45 --n_rollouts 20 --K 1
eval-supp-goal-vla-only-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 46 --n_rollouts 20 --K 1
eval-supp-goal-vla-only-s47 | seed=47 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1
eval-supp-goal-vla-only-s47-r2 | seed=47 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1
eval-supp-goal-vla-only-s47-r3 | seed=47 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1
eval-supp-goal-vla-only-s50 | seed=50 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 50 --n_rollouts 20
eval-supp-goal-vla-only-wrapper-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20
eval-supp-goal-vla-only-wrapper-s44 | seed=44 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20
eval-supp-goal-vla-only-wrapper-s44-r2 | seed=44 | server=bjb1-32546 | SR=0.85 | cmd=CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark goal --mode vla_only --seed 44 --n_rollouts 20 --K 1
eval-supp-k2mean-goal-s42 | seed=42 | server=bjb2-40593 | SR=? | cmd=bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --baseline_
eval-supp-k2mean-goal-s42-r2 | seed=42 | server=bjb2-40593 | SR=? | cmd=python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42
eval-supp-k2mean-goal-s43 | seed=43 | server=cqa1-32758 | SR=? | cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_V
eval-supp-k2mean-goal-s44 | seed=44 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20
eval-supp-vla-only-goal-s48 | seed=48 | server=cqa1-32758 | SR=? | cmd=python evaluate.py --mode vla_only --benchmark goal --seed 48 --n_rollouts 20
eval-supp-vla-only-goal-s49 | seed=49 | server=cqa1-32758 | SR=? | cmd=python evaluate.py --mode vla_only --benchmark goal --seed 49 --n_rollouts 20
eval-vla-only-goal-seed42 | seed=42 | server=bjb1-32546 | SR=? | cmd=bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --bench
eval-vla-only-goal-seed43 | seed=43 | server=bjb1-32546 | SR=? | cmd=bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --bench
eval-vla-only-goal-seed44 | seed=44 | server=bjb2-28827 | SR=? | cmd=bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --bench
eval-vla-only-goal-seed44-r2 | seed=44 | server=bjb2-28827 | SR=? | cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement 
eval-vla-only-goal-seed45 | seed=? | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 45 --K 1 --output_file logs/eval_goal_
eval-vla-only-goal-seed46 | seed=46 | server=bjb1-32546 | SR=? | cmd=bash -c "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py 
eval-vla-only-goal-seed47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 ... python -u src/evaluate.py --mode vla_only --benchmark goal --seed 47 --n_rollouts 10
eval-vla-only-goal-seed47-r2 | seed=47 | server=bjb1-32546 | SR=? | cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
eval-vla-only-goal-seed48 | seed=48 | server=bjb2-28827 | SR=? | cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
eval-vla-only-goal-seed48-r2 | seed=48 | server=bjb1-32546 | SR=? | cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
eval-vla-only-goal-seed49 | seed=49 | server=bjb1-18228 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 49
eval-vla-only-goal-seed51 | seed=? | server=bjb1-32546 | SR=? | cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement 
train-crm-pi05-goal-k1 | seed=42 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/train_crm_k1.py --benchmark goal --reuse_merged_cache --merged_cache_dir /root/auto
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "a6ea9896-d43e-4d16-8b72-4b6fdb5ec805",
  "tool_use_result": {
    "stdout": "crm-norm005-goal-s49 | seed=49 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 49 --n_rollouts 20 --K 10 -\neval-crm-goal-seed42 | seed=42 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 42 --K 10 -\neval-crm-goal-seed43 | seed=43 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 43 --K 10 -\neval-crm-goal-seed44 | seed=44 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts \neval-crm-goal-seed44-r2 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 44 --K 10 --max_correction_norm 0.2 --checkpoint /\neval-crm-goal-seed45 | seed=45 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts \neval-crm-goal-seed45-r2 | seed=45 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 45 --K 10 --max_correction_norm 0.2 --checkpoint /\neval-crm-goal-seed46 | seed=? | server=bjb2-28827 | SR=? | cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\neval-goal-vla-only-wrapper-s42 | seed=42 | server=bjb2-28827 | SR=? | cmd=bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark\neval-pi05-vla-only-goal-s42 | seed=42 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20\neval-pi05-vla-only-goal-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\neval-pi05-vla-only-goal-seed42-r4 | seed=? | server=bjb1-18228 | SR=? | cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement \neval-pi05-vla-only-goal-seed42-r4-std | seed=42 | server=N/A | SR=? | cmd=N/A - phantom entry\neval-pi05-vla-only-goal-seed43-r4 | seed=43 | server=bjb1-32546 | SR=? | cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/\neval-pi05-vla-only-goal-seed43-r4-std | seed=43 | server=N/A | SR=? | cmd=N/A - phantom entry\neval-pi05-vla-only-goal-seed44-r4 | seed=44 | server=bjb1-32546 | SR=? | cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/\neval-pi05-vla-only-goal-seed44-r4-std | seed=44 | server=N/A | SR=? | cmd=N/A - phantom entry\neval-smolvla-crm-goal-seed42 | seed=42 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/c\neval-smolvla-crm-goal-seed42-v1 | seed=? | server=? | SR=? | cmd=\neval-smolvla-crm-goal-seed43 | seed=43 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/c\neval-smolvla-crm-goal-seed43-v1 | seed=? | server=? | SR=? | cmd=\neval-smolvla-crm-goal-seed44-v1 | seed=? | server=? | SR=? | cmd=\neval-smolvla-crm-goal-seed44-v2 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint crm_best.pt\neval-supp-adapt-tau025-goal-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite\neval-supp-adapt-tau025-goal-s44 | seed=44 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpo\neval-supp-crm-norm005-goal-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_be\neval-supp-crm-norm005-goal-s44 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_be\neval-supp-crm-norm005-goal-s48 | seed=48 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 48 --n_rollouts 20 --K 10 -\neval-supp-goal-adapt-tau025-s42 | seed=? | server=? | SR=? | cmd=\neval-supp-goal-adapt-tau025-s45 | seed=45 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 45 --n_rollouts 2\neval-supp-goal-adapt-tau025-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 46 --n_rollouts 2\neval-supp-goal-adapt-tau025-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 2\neval-supp-goal-crm-norm005-s45 | seed=? | server=? | SR=? | cmd=\neval-supp-goal-crm-norm005-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 46 --n_rollouts 20 --max_co\neval-supp-goal-crm-norm005-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 -\neval-supp-goal-crm005-s42 | seed=42 | server=bjb2-28827 | SR=? | cmd=evaluate.py --mode crm_obs_only --max_correction_norm 0.05 --benchmark goal\neval-supp-goal-k2mean-s45 | seed=45 | server=cqa1-32758 | SR=0.81 | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 45 -\neval-supp-goal-k2mean-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 46 -\neval-supp-goal-k2mean-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --seed 47 --n_rol\neval-supp-goal-reconvla-s42 | seed=42 | server=bjb2-28827 | SR=? | cmd=bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --crm_check\neval-supp-goal-reconvla-s43 | seed=43 | server=cqa1-32758 | SR=? | cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_V\neval-supp-goal-reconvla-s44 | seed=44 | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode reconvla --K 10 --benchmark goal --seed 44 --n_rollouts 20\neval-supp-goal-reconvla-s45 | seed=45 | server=bjb2-28827 | SR=0.855 | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm\neval-supp-goal-reconvla-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm\neval-supp-goal-reconvla-s47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 47 --n_rollouts 20 --K 2\neval-supp-goal-vla-only-s42 | seed=42 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 42 --n_rollouts 20\neval-supp-goal-vla-only-s42-bjb1 | seed=42 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 42 --n_rollouts 20\neval-supp-goal-vla-only-s43 | seed=43 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\neval-supp-goal-vla-only-s44 | seed=44 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\neval-supp-goal-vla-only-s45 | seed=45 | server=bjb2-28827 | SR=0.835 | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 45 --n_rollouts 20 --K 1\neval-supp-goal-vla-only-s46 | seed=46 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 46 --n_rollouts 20 --K 1\neval-supp-goal-vla-only-s47 | seed=47 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\neval-supp-goal-vla-only-s47-r2 | seed=47 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\neval-supp-goal-vla-only-s47-r3 | seed=47 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\neval-supp-goal-vla-only-s50 | seed=50 | server=cqa1-32758 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 50 --n_rollouts 20\neval-supp-goal-vla-only-wrapper-s43 | seed=43 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\neval-supp-goal-vla-only-wrapper-s44 | seed=44 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\neval-supp-goal-vla-only-wrapper-s44-r2 | seed=44 | server=bjb1-32546 | SR=0.85 | cmd=CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark goal --mode vla_only --seed 44 --n_rollouts 20 --K 1\neval-supp-k2mean-goal-s42 | seed=42 | server=bjb2-40593 | SR=? | cmd=bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --baseline_\neval-supp-k2mean-goal-s42-r2 | seed=42 | server=bjb2-40593 | SR=? | cmd=python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42\neval-supp-k2mean-goal-s43 | seed=43 | server=cqa1-32758 | SR=? | cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_V\neval-supp-k2mean-goal-s44 | seed=44 | server=bjb1-32546 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\neval-supp-vla-only-goal-s48 | seed=48 | server=cqa1-32758 | SR=? | cmd=python evaluate.py --mode vla_only --benchmark goal --seed 48 --n_rollouts 20\neval-supp-vla-only-goal-s49 | seed=49 | server=cqa1-32758 | SR=? | cmd=python evaluate.py --mode vla_only --benchmark goal --seed 49 --n_rollouts 20\neval-vla-only-goal-seed42 | seed=42 | server=bjb1-32546 | SR=? | cmd=bash -c \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --bench\neval-vla-only-goal-seed43 | seed=43 | server=bjb1-32546 | SR=? | cmd=bash -c \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --bench\neval-vla-only-goal-seed44 | seed=44 | server=bjb2-28827 | SR=? | cmd=bash -c \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --bench\neval-vla-only-goal-seed44-r2 | seed=44 | server=bjb2-28827 | SR=? | cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement \neval-vla-only-goal-seed45 | seed=? | server=bjb2-28827 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 45 --K 1 --output_file logs/eval_goal_\neval-vla-only-goal-seed46 | seed=46 | server=bjb1-32546 | SR=? | cmd=bash -c \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py \neval-vla-only-goal-seed47 | seed=47 | server=bjb2-28827 | SR=? | cmd=CUDA_VISIBLE_DEVICES=4 ... python -u src/evaluate.py --mode vla_only --benchmark goal --seed 47 --n_rollouts 10\neval-vla-only-goal-seed47-r2 | seed=47 | server=bjb1-32546 | SR=? | cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\neval-vla-only-goal-seed48 | seed=48 | server=bjb2-28827 | SR=? | cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\neval-vla-only-goal-seed48-r2 | seed=48 | server=bjb1-32546 | SR=? | cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\neval-vla-only-goal-seed49 | seed=49 | server=bjb1-18228 | SR=? | cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 49\neval-vla-only-goal-seed51 | seed=? | server=bjb1-32546 | SR=? | cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement \ntrain-crm-pi05-goal-k1 | seed=42 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/train_crm_k1.py --benchmark goal --reuse_merged_cache --merged_cache_dir /root/auto",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "e0b94257-c25e-45bd-bb4c-2deb5b3ae34e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013zmuvJ9RpQbZGDrWd7grD5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8653,
      "cache_read_input_tokens": 72152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8653
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01K7yb6SjdTpjxFgMq1T8gtG`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt | python3 << 'EOF'\nimport json,sys\nd = json.load(open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt'))\nr = json.loads(d['result'])\nexps = r['data']['experiments']\n# Show all goal-related experiments with full metrics + notes + log_path\ndef matches_goal(k, e):\n    kl=k.lower()\n    return 'goal' in kl and any(x in kl for x in ['vla-only','vla_only','adapt','crm','norm005','tau025','reconvla','k2mean','k1-multiscale','smolvla'])\nfor k,e in sorted(exps.items()):\n    if not matches_goal(k,e): continue\n    metrics = e.get('metrics',{})\n    spec = e.get('spec',{})\n    seed = spec.get('seed','?')\n    srv = spec.get('server','?')\n    cmd = spec.get('command','')\n    log_path = e.get('log_path','?')\n    sr = metrics.get('SR','?')\n    notes = e.get('notes','')[:60]\n    print(f'{k}|seed={seed}|server={srv}|SR={sr}|cmd={cmd[:90]}|notes={notes}')\nEOF",
  "description": "Goal experiments full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "d53ab9ae-90ea-41b2-a25d-8b3f6b42a5ef",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013zmuvJ9RpQbZGDrWd7grD5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8653,
      "cache_read_input_tokens": 72152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8653
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-25T01:53:58.226Z_

<details><summary>↩ Tool result · `toolu_01K7yb6SjdTpjxFgMq1T8gtG`</summary>

```text
crm-norm005-goal-s49|seed=49|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --se|notes=
eval-crm-goal-seed42|seed=42|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=
eval-crm-goal-seed43|seed=43|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=
eval-crm-goal-seed44|seed=44|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only |notes=
eval-crm-goal-seed44-r2|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 44 --K 10 --max_corr|notes=
eval-crm-goal-seed45|seed=45|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only |notes=
eval-crm-goal-seed45-r2|seed=45|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 45 --K 10 --max_corr|notes=
eval-crm-goal-seed46|seed=?|server=bjb2-28827|SR=?|cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=
eval-goal-vla-only-wrapper-s42|seed=42|server=bjb2-28827|SR=?|cmd=bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.|notes=
eval-pi05-vla-only-goal-s42|seed=42|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_roll|notes=
eval-pi05-vla-only-goal-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_roll|notes=
eval-pi05-vla-only-goal-seed42-r4|seed=?|server=bjb1-18228|SR=?|cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=
eval-pi05-vla-only-goal-seed42-r4-std|seed=42|server=N/A|SR=?|cmd=N/A - phantom entry|notes=
eval-pi05-vla-only-goal-seed43-r4|seed=43|server=bjb1-32546|SR=?|cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=
eval-pi05-vla-only-goal-seed43-r4-std|seed=43|server=N/A|SR=?|cmd=N/A - phantom entry|notes=Phantom experiment entry — never submitted (status was PREPA
eval-pi05-vla-only-goal-seed44-r4|seed=44|server=bjb1-32546|SR=?|cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=
eval-pi05-vla-only-goal-seed44-r4-std|seed=44|server=N/A|SR=?|cmd=N/A - phantom entry|notes=
eval-smolvla-acr-goal-seed42|seed=42|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 42 --K 2 |notes=
eval-smolvla-acr-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 43 --K 2 |notes=
eval-smolvla-crm-goal-seed42|seed=42|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm|notes=
eval-smolvla-crm-goal-seed42-v1|seed=?|server=?|SR=?|cmd=|notes=
eval-smolvla-crm-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm|notes=
eval-smolvla-crm-goal-seed43-v1|seed=?|server=?|SR=?|cmd=|notes=
eval-smolvla-crm-goal-seed44-v1|seed=?|server=?|SR=?|cmd=|notes=
eval-smolvla-crm-goal-seed44-v2|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 44 --K 2 |notes=
eval-smolvla-lerobot-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero -|notes=M059: 并行过多崩溃，需重跑
eval-smolvla-lerobot-goal-seed43-v2|seed=43|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero -|notes=
eval-smolvla-lerobot-goal-seed43-v3|seed=43|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -m lerobot.scripts.eval --policy.path=lerobot/smolvla_libero|notes=
eval-smolvla-lerobot-goal-seed44-v3|seed=44|server=bjb1-32546|SR=?|cmd=lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.|notes=
eval-supp-adapt-tau025-goal-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/|notes=
eval-supp-adapt-tau025-goal-s44|seed=44|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_check|notes=
eval-supp-crm-norm005-goal-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoint|notes=
eval-supp-crm-norm005-goal-s44|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoint|notes=
eval-supp-crm-norm005-goal-s48|seed=48|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --se|notes=
eval-supp-goal-adapt-tau025-s42|seed=?|server=?|SR=?|cmd=|notes=
eval-supp-goal-adapt-tau025-s45|seed=45|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conforma|notes=
eval-supp-goal-adapt-tau025-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conforma|notes=
eval-supp-goal-adapt-tau025-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conforma|notes=
eval-supp-goal-crm-norm005-s45|seed=?|server=?|SR=?|cmd=|notes=实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果
eval-supp-goal-crm-norm005-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --se|notes=
eval-supp-goal-crm-norm005-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --se|notes=
eval-supp-goal-crm005-s42|seed=42|server=bjb2-28827|SR=?|cmd=evaluate.py --mode crm_obs_only --max_correction_norm 0.05 --benchmark goal|notes=
eval-supp-goal-k2mean-s45|seed=45|server=cqa1-32758|SR=0.81|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --baseli|notes=
eval-supp-goal-k2mean-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode vla_only --baseli|notes=
eval-supp-goal-k2mean-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseli|notes=
eval-supp-goal-reconvla-s42|seed=42|server=bjb2-28827|SR=?|cmd=bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.|notes=
eval-supp-goal-reconvla-s43|seed=43|server=cqa1-32758|SR=?|cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-|notes=Reconvla Goal seed43: SR=81.0% (162/200). s42=81.0%, s43=81.
eval-supp-goal-reconvla-s44|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode reconvla --K 10 --benchmark goal --seed 44 --n_rollouts 2|notes=
eval-supp-goal-reconvla-s45|seed=45|server=bjb2-28827|SR=0.855|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 4|notes=实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果
eval-supp-goal-reconvla-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 4|notes=
eval-supp-goal-reconvla-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 4|notes=
eval-supp-goal-vla-only-s42|seed=42|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=
eval-supp-goal-vla-only-s42-bjb1|seed=42|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=
eval-supp-goal-vla-only-s43|seed=43|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=
eval-supp-goal-vla-only-s44|seed=44|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=
eval-supp-goal-vla-only-s45|seed=45|server=bjb2-28827|SR=0.835|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果
eval-supp-goal-vla-only-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=
eval-supp-goal-vla-only-s47|seed=47|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=
eval-supp-goal-vla-only-s47-r2|seed=47|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=
eval-supp-goal-vla-only-s47-r3|seed=47|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=
eval-supp-goal-vla-only-s50|seed=50|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 5|notes=
eval-supp-goal-vla-only-wrapper-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20|notes=
eval-supp-goal-vla-only-wrapper-s44|seed=44|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20|notes=
eval-supp-goal-vla-only-wrapper-s44-r2|seed=44|server=bjb1-32546|SR=0.85|cmd=CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark goal --mode vla_only --seed 44 -|notes=
eval-supp-k2mean-goal-s42|seed=42|server=bjb2-40593|SR=?|cmd=bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.|notes=
eval-supp-k2mean-goal-s42-r2|seed=42|server=bjb2-40593|SR=?|cmd=python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rol|notes=
eval-supp-k2mean-goal-s43|seed=43|server=cqa1-32758|SR=?|cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-|notes=
eval-supp-k2mean-goal-s44|seed=44|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --se|notes=
eval-supp-vla-only-goal-s48|seed=48|server=cqa1-32758|SR=?|cmd=python evaluate.py --mode vla_only --benchmark goal --seed 48 --n_rollouts 20|notes=
eval-supp-vla-only-goal-s49|seed=49|server=cqa1-32758|SR=?|cmd=python evaluate.py --mode vla_only --benchmark goal --seed 49 --n_rollouts 20|notes=
eval-vla-only-goal-seed42|seed=42|server=bjb1-32546|SR=?|cmd=bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evalu|notes=
eval-vla-only-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evalu|notes=
eval-vla-only-goal-seed44|seed=44|server=bjb2-28827|SR=?|cmd=bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evalu|notes=
eval-vla-only-goal-seed44-r2|seed=44|server=bjb2-28827|SR=?|cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=
eval-vla-only-goal-seed45|seed=?|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 45 --K 1|notes=
eval-vla-only-goal-seed46|seed=46|server=bjb1-32546|SR=?|cmd=bash -c "cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/|notes=Cron false positive: eval completed normally (71.0%), but no
eval-vla-only-goal-seed47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 ... python -u src/evaluate.py --mode vla_only --benchmark goal --se|notes=
eval-vla-only-goal-seed47-r2|seed=47|server=bjb1-32546|SR=?|cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=
eval-vla-only-goal-seed48|seed=48|server=bjb2-28827|SR=?|cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=
eval-vla-only-goal-seed48-r2|seed=48|server=bjb1-32546|SR=?|cmd=bash -c "source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=
eval-vla-only-goal-seed49|seed=49|server=bjb1-18228|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 49|notes=
eval-vla-only-goal-seed51|seed=?|server=bjb1-32546|SR=?|cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=
precompute-smolvla-goal-bjb1-18228|seed=42|server=bjb1-18228|SR=?|cmd=python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/|notes=
precompute-smolvla-goal-bjb1-32546|seed=?|server=bjb1-32546|SR=?|cmd=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=
precompute-smolvla-goal-bjb2-28827|seed=42|server=bjb2-28827|SR=?|cmd=python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/|notes=
precompute-smolvla-goal-shard0|seed=?|server=?|SR=?|cmd=|notes=
precompute-smolvla-goal-shard1|seed=?|server=?|SR=?|cmd=|notes=
precompute-smolvla-goal-shard2|seed=?|server=?|SR=?|cmd=|notes=
train-crm-pi05-goal-k1|seed=42|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/train_crm_k1.py --benchmark goal --reuse_merged_cache|notes=
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "84f9654a-1857-4c3c-9200-1e3a5c4afd2d",
  "tool_use_result": {
    "stdout": "crm-norm005-goal-s49|seed=49|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --se|notes=\neval-crm-goal-seed42|seed=42|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=\neval-crm-goal-seed43|seed=43|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=\neval-crm-goal-seed44|seed=44|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only |notes=\neval-crm-goal-seed44-r2|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 44 --K 10 --max_corr|notes=\neval-crm-goal-seed45|seed=45|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only |notes=\neval-crm-goal-seed45-r2|seed=45|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 45 --K 10 --max_corr|notes=\neval-crm-goal-seed46|seed=?|server=bjb2-28827|SR=?|cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=\neval-goal-vla-only-wrapper-s42|seed=42|server=bjb2-28827|SR=?|cmd=bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.|notes=\neval-pi05-vla-only-goal-s42|seed=42|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_roll|notes=\neval-pi05-vla-only-goal-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_roll|notes=\neval-pi05-vla-only-goal-seed42-r4|seed=?|server=bjb1-18228|SR=?|cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=\neval-pi05-vla-only-goal-seed42-r4-std|seed=42|server=N/A|SR=?|cmd=N/A - phantom entry|notes=\neval-pi05-vla-only-goal-seed43-r4|seed=43|server=bjb1-32546|SR=?|cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=\neval-pi05-vla-only-goal-seed43-r4-std|seed=43|server=N/A|SR=?|cmd=N/A - phantom entry|notes=Phantom experiment entry — never submitted (status was PREPA\neval-pi05-vla-only-goal-seed44-r4|seed=44|server=bjb1-32546|SR=?|cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=\neval-pi05-vla-only-goal-seed44-r4-std|seed=44|server=N/A|SR=?|cmd=N/A - phantom entry|notes=\neval-smolvla-acr-goal-seed42|seed=42|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 42 --K 2 |notes=\neval-smolvla-acr-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 43 --K 2 |notes=\neval-smolvla-crm-goal-seed42|seed=42|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm|notes=\neval-smolvla-crm-goal-seed42-v1|seed=?|server=?|SR=?|cmd=|notes=\neval-smolvla-crm-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm|notes=\neval-smolvla-crm-goal-seed43-v1|seed=?|server=?|SR=?|cmd=|notes=\neval-smolvla-crm-goal-seed44-v1|seed=?|server=?|SR=?|cmd=|notes=\neval-smolvla-crm-goal-seed44-v2|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 44 --K 2 |notes=\neval-smolvla-lerobot-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero -|notes=M059: 并行过多崩溃，需重跑\neval-smolvla-lerobot-goal-seed43-v2|seed=43|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero -|notes=\neval-smolvla-lerobot-goal-seed43-v3|seed=43|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -m lerobot.scripts.eval --policy.path=lerobot/smolvla_libero|notes=\neval-smolvla-lerobot-goal-seed44-v3|seed=44|server=bjb1-32546|SR=?|cmd=lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.|notes=\neval-supp-adapt-tau025-goal-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/|notes=\neval-supp-adapt-tau025-goal-s44|seed=44|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_check|notes=\neval-supp-crm-norm005-goal-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoint|notes=\neval-supp-crm-norm005-goal-s44|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoint|notes=\neval-supp-crm-norm005-goal-s48|seed=48|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --se|notes=\neval-supp-goal-adapt-tau025-s42|seed=?|server=?|SR=?|cmd=|notes=\neval-supp-goal-adapt-tau025-s45|seed=45|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conforma|notes=\neval-supp-goal-adapt-tau025-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conforma|notes=\neval-supp-goal-adapt-tau025-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conforma|notes=\neval-supp-goal-crm-norm005-s45|seed=?|server=?|SR=?|cmd=|notes=实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果\neval-supp-goal-crm-norm005-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --se|notes=\neval-supp-goal-crm-norm005-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --se|notes=\neval-supp-goal-crm005-s42|seed=42|server=bjb2-28827|SR=?|cmd=evaluate.py --mode crm_obs_only --max_correction_norm 0.05 --benchmark goal|notes=\neval-supp-goal-k2mean-s45|seed=45|server=cqa1-32758|SR=0.81|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --baseli|notes=\neval-supp-goal-k2mean-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode vla_only --baseli|notes=\neval-supp-goal-k2mean-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseli|notes=\neval-supp-goal-reconvla-s42|seed=42|server=bjb2-28827|SR=?|cmd=bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.|notes=\neval-supp-goal-reconvla-s43|seed=43|server=cqa1-32758|SR=?|cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-|notes=Reconvla Goal seed43: SR=81.0% (162/200). s42=81.0%, s43=81.\neval-supp-goal-reconvla-s44|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode reconvla --K 10 --benchmark goal --seed 44 --n_rollouts 2|notes=\neval-supp-goal-reconvla-s45|seed=45|server=bjb2-28827|SR=0.855|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 4|notes=实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果\neval-supp-goal-reconvla-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 4|notes=\neval-supp-goal-reconvla-s47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 4|notes=\neval-supp-goal-vla-only-s42|seed=42|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=\neval-supp-goal-vla-only-s42-bjb1|seed=42|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=\neval-supp-goal-vla-only-s43|seed=43|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=\neval-supp-goal-vla-only-s44|seed=44|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 4|notes=\neval-supp-goal-vla-only-s45|seed=45|server=bjb2-28827|SR=0.835|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果\neval-supp-goal-vla-only-s46|seed=46|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=\neval-supp-goal-vla-only-s47|seed=47|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=\neval-supp-goal-vla-only-s47-r2|seed=47|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=\neval-supp-goal-vla-only-s47-r3|seed=47|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 4|notes=\neval-supp-goal-vla-only-s50|seed=50|server=cqa1-32758|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark goal --seed 5|notes=\neval-supp-goal-vla-only-wrapper-s43|seed=43|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20|notes=\neval-supp-goal-vla-only-wrapper-s44|seed=44|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20|notes=\neval-supp-goal-vla-only-wrapper-s44-r2|seed=44|server=bjb1-32546|SR=0.85|cmd=CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark goal --mode vla_only --seed 44 -|notes=\neval-supp-k2mean-goal-s42|seed=42|server=bjb2-40593|SR=?|cmd=bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.|notes=\neval-supp-k2mean-goal-s42-r2|seed=42|server=bjb2-40593|SR=?|cmd=python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rol|notes=\neval-supp-k2mean-goal-s43|seed=43|server=cqa1-32758|SR=?|cmd=source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-|notes=\neval-supp-k2mean-goal-s44|seed=44|server=bjb1-32546|SR=?|cmd=python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --se|notes=\neval-supp-vla-only-goal-s48|seed=48|server=cqa1-32758|SR=?|cmd=python evaluate.py --mode vla_only --benchmark goal --seed 48 --n_rollouts 20|notes=\neval-supp-vla-only-goal-s49|seed=49|server=cqa1-32758|SR=?|cmd=python evaluate.py --mode vla_only --benchmark goal --seed 49 --n_rollouts 20|notes=\neval-vla-only-goal-seed42|seed=42|server=bjb1-32546|SR=?|cmd=bash -c \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evalu|notes=\neval-vla-only-goal-seed43|seed=43|server=bjb1-32546|SR=?|cmd=bash -c \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evalu|notes=\neval-vla-only-goal-seed44|seed=44|server=bjb2-28827|SR=?|cmd=bash -c \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evalu|notes=\neval-vla-only-goal-seed44-r2|seed=44|server=bjb2-28827|SR=?|cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=\neval-vla-only-goal-seed45|seed=?|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 45 --K 1|notes=\neval-vla-only-goal-seed46|seed=46|server=bjb1-32546|SR=?|cmd=bash -c \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/|notes=Cron false positive: eval completed normally (71.0%), but no\neval-vla-only-goal-seed47|seed=47|server=bjb2-28827|SR=?|cmd=CUDA_VISIBLE_DEVICES=4 ... python -u src/evaluate.py --mode vla_only --benchmark goal --se|notes=\neval-vla-only-goal-seed47-r2|seed=47|server=bjb1-32546|SR=?|cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=\neval-vla-only-goal-seed48|seed=48|server=bjb2-28827|SR=?|cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=\neval-vla-only-goal-seed48-r2|seed=48|server=bjb1-32546|SR=?|cmd=bash -c \"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinemen|notes=\neval-vla-only-goal-seed49|seed=49|server=bjb1-18228|SR=?|cmd=python -u src/evaluate.py --mode vla_only --benchmark goal --seed 49|notes=\neval-vla-only-goal-seed51|seed=?|server=bjb1-32546|SR=?|cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=\nprecompute-smolvla-goal-bjb1-18228|seed=42|server=bjb1-18228|SR=?|cmd=python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/|notes=\nprecompute-smolvla-goal-bjb1-32546|seed=?|server=bjb1-32546|SR=?|cmd=bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root|notes=\nprecompute-smolvla-goal-bjb2-28827|seed=42|server=bjb2-28827|SR=?|cmd=python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/|notes=\nprecompute-smolvla-goal-shard0|seed=?|server=?|SR=?|cmd=|notes=\nprecompute-smolvla-goal-shard1|seed=?|server=?|SR=?|cmd=|notes=\nprecompute-smolvla-goal-shard2|seed=?|server=?|SR=?|cmd=|notes=\ntrain-crm-pi05-goal-k1|seed=42|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/train_crm_k1.py --benchmark goal --reuse_merged_cache|notes=",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "9c133f63-be5d-43e0-ac4b-0a9aba1207ca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012VtdXebhM8gSXh7yKnEGrk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9704,
      "cache_read_input_tokens": 80805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9704
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_015kq7M39qatWQxemkGCiv7r`</summary>

```json
{
  "command": "grep -rln \"goal.*vla.*only.*42\\|vla_only.*goal.*seed.*42\\|s42.*goal.*vla\\|VLA-only.*s42.*Goal\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/ 2>/dev/null | head -10",
  "description": "Find Goal VLA-only s42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "66e0e658-9a0d-49ca-954c-4dfc2e204a33",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012VtdXebhM8gSXh7yKnEGrk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9704,
      "cache_read_input_tokens": 80805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9704
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-25T01:54:33.599Z_

<details><summary>↩ Tool result · `toolu_015kq7M39qatWQxemkGCiv7r`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7_9dfa78.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "6884cdf7-2f84-4c02-908e-ae950682e48c",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7_9dfa78.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_01UQdva9wjhGXncQNz7NMUfH`</summary>

```json
{
  "command": "grep -rln \"Goal.*42\\|seed.*42.*Goal\\|VLA-only.*goal.*83\\.\\|table_data\\|table1_3seed\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null | grep -v \".pdf$\" | head -10",
  "description": "Search for Table 1 source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "af9ea7bb-7561-48dd-b7d2-7e58dd71c3aa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HmFHowtq7a5Wa9pMkU8E7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 90509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2799
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-25T01:54:40.168Z_

<details><summary>↩ Tool result · `toolu_01UQdva9wjhGXncQNz7NMUfH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_results_harvest.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_coverage_libero10_goal.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/experiment_status_20260523_session25.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_fix_status.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/crm_eval_results_harvest.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "0de515c5-0c40-4f89-8cda-7d0b8f101f09",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_results_harvest.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_coverage_libero10_goal.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/experiment_status_20260523_session25.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_fix_status.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/crm_eval_results_harvest.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_worst.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_median.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/logs/review_best.log",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01VgMuxGgWY5cvwDXfCpyLw7`</summary>

```json
{
  "command": "grep -n -B 3 -A 30 \"Goal\\|3.*seed\\|table.*1\\|Table 1\\|## Object\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md 2>/dev/null | head -150",
  "description": "Read table1_8seed_v2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "49bf709f-ab58-48aa-9f5a-eaebd7f53b11",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015h9Q3yW37jm31C4yTGXwYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 93308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-25T01:54:44.520Z_

<details><summary>↩ Tool result · `toolu_01VgMuxGgWY5cvwDXfCpyLw7`</summary>

```text
1:# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)
2-
3-## Per-Seed Detail
4-
5-### SPATIAL (8/8 VLA-only, 8/8 Adaptive)
6-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
7-|------|----------|----------|-----|--------|-----------|
8-| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |
9-| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |
10-| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |
11-| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |
12-| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |
13-| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |
14-| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |
15-| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |
16-
17-**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*
18-
19-### OBJECT (3/8 VLA-only, 6/8 Adaptive)
20-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
21-|------|----------|----------|-----|--------|-----------|
22-| s42 | --- | 81.0% | 77.0% | | 3.5% |
23-| s43 | --- | 77.5% | 78.5% | | 3.7% |
24-| s44 | --- | 75.0% | 74.0% | | 3.6% |
25-| s45 | --- | --- | 76.5% | | |
26-| s46 | --- | --- | 79.5% | | |
27-| s47 | 75.5% | 77.0% | 82.5% | +1.5% | 4.0% |
28-| s48 | 79.0% | 76.0% | --- | -3.0% | 3.9% |
29-| s49 | 75.5% | 74.0% | --- | -1.5% | 4.2% |
30-
31:**Stats (3-seed paired):** VLA 76.7%±2.0% → Adaptive 75.7%±1.5%, Δ=-1.0%, p=0.53 ns
32-**Note:** s42/43/44 VLA-only currently running on bjb1-32546
33-
34-### GOAL (6/8 VLA-only, 8/8 Adaptive)
35-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
36-|------|----------|----------|-----|--------|-----------|
37-| s42 | --- | 84.0% | 85.5% | | 8.3% |
38-| s43 | 82.5% | 84.5% | 82.0% | +2.0% | 8.8% |
39-| s44 | 82.0% | 86.5% | 83.5% | +4.5% | 6.8% |
40-| s45 | --- | 81.0% | 81.0% | | 9.4% |
41-| s46 | 83.0% | 83.5% | 82.0% | +0.5% | 9.1% |
42-| s47 | 82.5% | 82.0% | 82.0% | -0.5% | 8.9% |
43-| s48 | 85.0% | 84.5% | --- | -0.5% | 8.9% |
44-| s49 | 82.0% | 81.5% | --- | -0.5% | 8.9% |
45-
46-**Stats (6-seed paired):** VLA 82.8%±1.1% → Adaptive 83.8%±1.8%, Δ=+0.9%, p=0.31 ns
47-
48-### LONG (3/8 each)
49-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
50-|------|----------|----------|-----|--------|-----------|
51-| s42 | 58.0% | 59.0% | 56.5% | +1.0% | 3.9% |
52-| s46 | 60.5% | 58.5% | 54.0% | -2.0% | |
53-| s47 | 59.5% | 55.0% | 56.5% | -4.5% | 3.7% |
54-
55:**Stats (3-seed paired):** VLA 59.3%±1.3% → Adaptive 57.5%±2.2%, Δ=-1.8%, p=0.37 ns
56-
57-## Summary Table
58-
59-| Suite | VLA-only | Adaptive | CRM | Δ(A-V) | p(A-V) | n |
60-|-------|----------|----------|-----|--------|--------|---|
61-| Spatial | 79.5%±0.8% | 80.9%±0.9% | 80.3%±1.0% | +1.4% | 0.0168* | 8 |
62-| Object | 76.7%±2.0% | 75.7%±1.5% | 78.0% (6s) | -1.0% | 0.53 | 3 |
63:| Goal | 82.8%±1.1% | 83.8%±1.8% | 82.4%±0.8% | +0.9% | 0.31 | 6 |
64-| Long | 59.3%±1.3% | 57.5%±2.2% | 55.7%±1.4% | -1.8% | 0.37 | 3 |
65-
66-## Trigger Rate ↔ Effect Size (D140 方案C evidence)
67-
68-| Suite | trigger_rate | Δ(A-V) | Direction |
69-|-------|-------------|--------|-----------|
70-| Spatial | 19.8% | +1.4%* | Positive (significant) |
71:| Goal | 8.6% | +0.9% | Positive (trend) |
72-| Object | 3.8% | -1.0% | Negligible |
73-| Long | 3.8% | -1.8% | Negligible |
74-
75-Perfect monotonic: higher trigger → larger positive effect.
76-
77-## Data Gaps (being filled)
78-- Object VLA-only s42/43/44: running on bjb1-32546
79:- Goal VLA-only s42/s45: s42 running on bjb1-32546
80-- Spatial CRM s48/s49: running on bjb2-28827
81:- Goal CRM s48/s49: running on bjb2-28827 + bjb1-18228
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "31d2ac84-bc5d-42e2-b2c8-7348efd7e0c8",
  "tool_use_result": {
    "stdout": "1:# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)\n2-\n3-## Per-Seed Detail\n4-\n5-### SPATIAL (8/8 VLA-only, 8/8 Adaptive)\n6-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n7-|------|----------|----------|-----|--------|-----------|\n8-| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |\n9-| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |\n10-| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |\n11-| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |\n12-| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |\n13-| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |\n14-| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |\n15-| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |\n16-\n17-**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*\n18-\n19-### OBJECT (3/8 VLA-only, 6/8 Adaptive)\n20-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n21-|------|----------|----------|-----|--------|-----------|\n22-| s42 | --- | 81.0% | 77.0% | | 3.5% |\n23-| s43 | --- | 77.5% | 78.5% | | 3.7% |\n24-| s44 | --- | 75.0% | 74.0% | | 3.6% |\n25-| s45 | --- | --- | 76.5% | | |\n26-| s46 | --- | --- | 79.5% | | |\n27-| s47 | 75.5% | 77.0% | 82.5% | +1.5% | 4.0% |\n28-| s48 | 79.0% | 76.0% | --- | -3.0% | 3.9% |\n29-| s49 | 75.5% | 74.0% | --- | -1.5% | 4.2% |\n30-\n31:**Stats (3-seed paired):** VLA 76.7%±2.0% → Adaptive 75.7%±1.5%, Δ=-1.0%, p=0.53 ns\n32-**Note:** s42/43/44 VLA-only currently running on bjb1-32546\n33-\n34-### GOAL (6/8 VLA-only, 8/8 Adaptive)\n35-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n36-|------|----------|----------|-----|--------|-----------|\n37-| s42 | --- | 84.0% | 85.5% | | 8.3% |\n38-| s43 | 82.5% | 84.5% | 82.0% | +2.0% | 8.8% |\n39-| s44 | 82.0% | 86.5% | 83.5% | +4.5% | 6.8% |\n40-| s45 | --- | 81.0% | 81.0% | | 9.4% |\n41-| s46 | 83.0% | 83.5% | 82.0% | +0.5% | 9.1% |\n42-| s47 | 82.5% | 82.0% | 82.0% | -0.5% | 8.9% |\n43-| s48 | 85.0% | 84.5% | --- | -0.5% | 8.9% |\n44-| s49 | 82.0% | 81.5% | --- | -0.5% | 8.9% |\n45-\n46-**Stats (6-seed paired):** VLA 82.8%±1.1% → Adaptive 83.8%±1.8%, Δ=+0.9%, p=0.31 ns\n47-\n48-### LONG (3/8 each)\n49-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n50-|------|----------|----------|-----|--------|-----------|\n51-| s42 | 58.0% | 59.0% | 56.5% | +1.0% | 3.9% |\n52-| s46 | 60.5% | 58.5% | 54.0% | -2.0% | |\n53-| s47 | 59.5% | 55.0% | 56.5% | -4.5% | 3.7% |\n54-\n55:**Stats (3-seed paired):** VLA 59.3%±1.3% → Adaptive 57.5%±2.2%, Δ=-1.8%, p=0.37 ns\n56-\n57-## Summary Table\n58-\n59-| Suite | VLA-only | Adaptive | CRM | Δ(A-V) | p(A-V) | n |\n60-|-------|----------|----------|-----|--------|--------|---|\n61-| Spatial | 79.5%±0.8% | 80.9%±0.9% | 80.3%±1.0% | +1.4% | 0.0168* | 8 |\n62-| Object | 76.7%±2.0% | 75.7%±1.5% | 78.0% (6s) | -1.0% | 0.53 | 3 |\n63:| Goal | 82.8%±1.1% | 83.8%±1.8% | 82.4%±0.8% | +0.9% | 0.31 | 6 |\n64-| Long | 59.3%±1.3% | 57.5%±2.2% | 55.7%±1.4% | -1.8% | 0.37 | 3 |\n65-\n66-## Trigger Rate ↔ Effect Size (D140 方案C evidence)\n67-\n68-| Suite | trigger_rate | Δ(A-V) | Direction |\n69-|-------|-------------|--------|-----------|\n70-| Spatial | 19.8% | +1.4%* | Positive (significant) |\n71:| Goal | 8.6% | +0.9% | Positive (trend) |\n72-| Object | 3.8% | -1.0% | Negligible |\n73-| Long | 3.8% | -1.8% | Negligible |\n74-\n75-Perfect monotonic: higher trigger → larger positive effect.\n76-\n77-## Data Gaps (being filled)\n78-- Object VLA-only s42/43/44: running on bjb1-32546\n79:- Goal VLA-only s42/s45: s42 running on bjb1-32546\n80-- Spatial CRM s48/s49: running on bjb2-28827\n81:- Goal CRM s48/s49: running on bjb2-28827 + bjb1-18228",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 77_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "cf540105-b3a8-4210-80f5-46d0b324903b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SB8UUBNMhsAqRw6LgpgbiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2529,
      "cache_read_input_tokens": 94251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2529
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01VZhjwfmSQqhKBDhH1NUv7g`</summary>

```json
{
  "command": "grep -n -B 1 -A 30 \"Object.*5.*seed\\|object.*adaptive.*77.8\\|77.8.*object\\|VLA.*only.*Object\\|Adaptive.*Object\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md 2>/dev/null | head -40",
  "description": "Search 8seed table for Object"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "f4cab443-120f-449c-834f-824744f61858",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SB8UUBNMhsAqRw6LgpgbiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2529,
      "cache_read_input_tokens": 94251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2529
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-25T01:55:14.158Z_

<details><summary>↩ Tool result · `toolu_01VZhjwfmSQqhKBDhH1NUv7g`</summary>

```text
66-
67:### Object (5 matched seeds for A-V)
68-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
69-|------|---------|----------|-----|--------|
70-| s42 | — | 81.0% | 77.0% | — |
71-| s43 | — | 77.5% | 78.5% | — |
72-| s44 | — | 75.0% | 74.0% | — |
73-| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
74-| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
75-| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
76-| s48 | 79.0% | 76.0% | — | -3.0pp |
77-| s49 | 75.5% | 74.0% | — | -1.5pp |
78-
79-### Long (5 matched seeds for A-V)
80-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
81-|------|---------|----------|-----|--------|
82-| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
83-| s43 | — | 58.0% | 54.5% | — |
84-| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
85-| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
86-| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |
87-| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |
88-
89-## Data Gaps
90-- Goal VLA-only s42: missing
91-- Object VLA-only s42/s43/s44: missing
92-- Spatial CRM s42/s48/s49: missing
93-- Goal/Object CRM s48/s49: missing
94-- Long VLA-only s43/s48/s49: missing
95-- Long Adaptive s48/s49: missing
96-
97-## Note on Spatial VLA-only s42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "125f64f1-7dd7-4efb-a6cb-1b68edafcffb",
  "tool_use_result": {
    "stdout": "66-\n67:### Object (5 matched seeds for A-V)\n68-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n69-|------|---------|----------|-----|--------|\n70-| s42 | — | 81.0% | 77.0% | — |\n71-| s43 | — | 77.5% | 78.5% | — |\n72-| s44 | — | 75.0% | 74.0% | — |\n73-| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |\n74-| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |\n75-| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |\n76-| s48 | 79.0% | 76.0% | — | -3.0pp |\n77-| s49 | 75.5% | 74.0% | — | -1.5pp |\n78-\n79-### Long (5 matched seeds for A-V)\n80-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n81-|------|---------|----------|-----|--------|\n82-| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |\n83-| s43 | — | 58.0% | 54.5% | — |\n84-| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |\n85-| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |\n86-| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |\n87-| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |\n88-\n89-## Data Gaps\n90-- Goal VLA-only s42: missing\n91-- Object VLA-only s42/s43/s44: missing\n92-- Spatial CRM s42/s48/s49: missing\n93-- Goal/Object CRM s48/s49: missing\n94-- Long VLA-only s43/s48/s49: missing\n95-- Long Adaptive s48/s49: missing\n96-\n97-## Note on Spatial VLA-only s42",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 80_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "6543b0c5-2faa-4768-a546-3544f80f8e37",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011PzxHVt7mG1rZ3g8MwkF4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3046,
      "cache_read_input_tokens": 96780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3046
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01P876cMqS1AnHqpkpTUZ1ki`</summary>

```json
{
  "command": "grep -rln \"77.7\\|85.0\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null | grep -v \".pdf$\\|.png$\" | head -10\necho \"---\"\ngrep -rln \"Object.*5\\b\\|5.*seed.*object\\|85.0.*1.3\\|77.7.*1.3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ 2>/dev/null | grep -v \".pdf$\" | head -10",
  "description": "Find Table 1 source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "90ae89a0-64e7-4771-be2f-0b9d6c9a8a43",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011PzxHVt7mG1rZ3g8MwkF4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3046,
      "cache_read_input_tokens": 96780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3046
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-25T01:55:35.393Z_

<details><summary>↩ Tool result · `toolu_01P876cMqS1AnHqpkpTUZ1ki`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/gpu_scan_r7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval_partial_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary_e015e3.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_results_harvest.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.registry_3rh2tyz0.tmp
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/figures/fig_magnitude_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_oft-libero-version-fix_20260522T130347.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_pi05-wrapper-vision-tower-final_20260521T063854_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_vla-mean-seed43-results_20260516T045302_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_collect_smolvla-long-reseed-results_20260522T153712.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_multiscale-eval-crons_20260517T183642.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "b542f9c2-48f7-45c5-a881-81147623e08e",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/gpu_scan_r7.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval_partial_results.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary_e015e3.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/gpu_scan_r7.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_results_harvest.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md\n---\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.registry_3rh2tyz0.tmp\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/figures/fig_magnitude_curve.py\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_oft-libero-version-fix_20260522T130347.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_pi05-wrapper-vision-tower-final_20260521T063854_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_vla-mean-seed43-results_20260516T045302_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_collect_smolvla-long-reseed-results_20260522T153712.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_multiscale-eval-crons_20260517T183642.log",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01FHB4WXRqnnHJ3uzFVuiUhP`</summary>

```json
{
  "command": "grep -n -B 2 -A 8 \"77.7\\|85.0\\|77.8.*2.1\\|83.7.*1.3\\|83.7.*1.8\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py 2>/dev/null | head -40\necho \"---\"\ngrep -n -B 2 -A 8 \"77.7\\|85.0\\|77.8.*2.1\\|83.7.*1.3\\|83.7.*1.8\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/figures/fig_magnitude_curve.py 2>/dev/null | head -40",
  "description": "Check magnitude curve scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "ff3bb8e5-b498-4ce1-a81c-fa8855d04f43",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014Qj5fQevXeZn1c6BUDt3Wv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2793,
      "cache_read_input_tokens": 99826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2793
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-25T01:55:41.127Z_

<details><summary>↩ Tool result · `toolu_01FHB4WXRqnnHJ3uzFVuiUhP`</summary>

```text
46-
47-# Baselines — both at 12%, use single line with combined label
48:ax.axhline(argmin_baseline, color='#777777', linestyle=':', linewidth=0.9,
49-           label='argmin / VLA-only (12%)', zorder=2)
50-
51-# Mark optimal point ε=0.2
52-ax.axvline(0.2, color='#888888', linestyle='--', linewidth=0.5, alpha=0.4, zorder=1)
53-ax.plot(0.2, 22, '*', color='#2166ac', markersize=11, markeredgecolor='white',
54-        markeredgewidth=0.4, zorder=6)
55-
56-# Annotations: gap between obs_only and perdof
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "111675c7-6adb-4b9e-abf7-89b54638fcf0",
  "tool_use_result": {
    "stdout": "46-\n47-# Baselines — both at 12%, use single line with combined label\n48:ax.axhline(argmin_baseline, color='#777777', linestyle=':', linewidth=0.9,\n49-           label='argmin / VLA-only (12%)', zorder=2)\n50-\n51-# Mark optimal point ε=0.2\n52-ax.axvline(0.2, color='#888888', linestyle='--', linewidth=0.5, alpha=0.4, zorder=1)\n53-ax.plot(0.2, 22, '*', color='#2166ac', markersize=11, markeredgecolor='white',\n54-        markeredgewidth=0.4, zorder=6)\n55-\n56-# Annotations: gap between obs_only and perdof\n---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_01YF5Gi6HckcxDojTfQuLZaF`</summary>

```json
{
  "command": "grep -rln \"table1.*py\\|table_1.*py\\|gen_table\\|compute_table\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ 2>/dev/null | grep -v \".pdf$\\|.txt$\" | head -10\necho \"---\"\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/scripts/ 2>/dev/null | head -30",
  "description": "Find table generation scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "512aab04-2326-4556-a376-75ff10de91c8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015Yd5inLUyZAjHAdV9CpB2A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 102619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 629
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bdswl12ej",
  "tool_use_id": "toolu_01YF5Gi6HckcxDojTfQuLZaF",
  "description": "Find table generation scripts",
  "task_type": "local_bash",
  "uuid": "7eb115e9-8ff3-46f6-84a4-e26bac7199ee",
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473"
}
```

---


### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bdswl12ej",
  "tool_use_id": "toolu_01YF5Gi6HckcxDojTfQuLZaF",
  "status": "completed",
  "output_file": "",
  "summary": "Find table generation scripts",
  "uuid": "d570a238-8317-4c38-a098-d7a4d21568f4",
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473"
}
```

---


### Tool result

_source line 88 · 2026-05-25T01:55:54.511Z_

<details><summary>↩ Tool result · `toolu_01YF5Gi6HckcxDojTfQuLZaF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_retry1_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-K-values_20260524T213618_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/worker_analysis_per-task-spatial-breakdown_20260524T222035.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/archive/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer_20260515T163317_290457.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/archive/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director_20260515T170345_843511.jsonl
---
parse_log_to_json.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "bf5569de-3330-409f-b0c1-4ed440bfc63c",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_retry1_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-K-values_20260524T213618_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/worker_analysis_per-task-spatial-breakdown_20260524T222035.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/archive/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer_20260515T163317_290457.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/archive/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director_20260515T170345_843511.jsonl\n---\nparse_log_to_json.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mem7GhUbXGvyP1JyE59jdh`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log 2>/dev/null | head -300",
  "description": "Read prior audit log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "af43e8fa-32f7-4fe1-942e-63f5f126c162",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CdWVMZ95LdztxaR9E8X9fq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1096,
      "cache_read_input_tokens": 103248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1096
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-25T01:55:57.964Z_

<details><summary>↩ Tool result · `toolu_01Mem7GhUbXGvyP1JyE59jdh`</summary>

```text
&lt;persisted-output>
Output too large (1.5MB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt

Preview (first 2KB):
Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.
{"type":"system","subtype":"init","cwd":"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement","session_id":"085b74a0-965d-415e-b60e-2ccc9bf1b473","tools":["Task","AskUserQuestion","Bash","CronCreate","CronDelete","CronList","Edit","EnterPlanMode","EnterWorktree","ExitPlanMode","ExitWorktree","Glob","Grep","ListMcpResourcesTool","Monitor","NotebookEdit","PushNotification","Read","ReadMcpResourceTool","RemoteTrigger","ScheduleWakeup","Skill","TaskOutput","TaskStop","TodoWrite","ToolSearch","WebFetch","WebSearch","Write","mcp__agent-ml-research__detect_image","mcp__agent-ml-research__kill_job","mcp__agent-ml-research__read_registry","mcp__agent-ml-research__register_artifact","mcp__agent-ml-research__ssh_execute","mcp__agent-ml-research__ssh_read_only","mcp__agent-ml-research__update_registry"],"mcp_servers":[{"name":"agent-ml-research","status":"connected"}],"model":"claude-opus-4-7[1m]","permissionMode":"bypassPermissions","slash_commands":["update-config","debug","simplify","batch","fewer-permission-prompts","loop","schedule","claude-api","clear","compact","context","heapdump","init","review","security-review","extra-usage","usage","insights","team-onboarding"],"apiKeySource":"none","claude_code_version":"2.1.126","output_style":"default","agents":["claude","Explore","general-purpose","Plan","statusline-setup"],"skills":["update-config","debug","simplify","batch","fewer-permission-prompts","loop","schedule","claude-api"],"plugins":[],"analytics_disabled":false,"uuid":"40284446-a60c-4bc4-89ae-4719a6a59ade","memory_paths":{"auto":"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"},"fast_mode_state":"off"}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7b92cd35-bf93-4965-b038-554904f13141",
  "tool_use_result": {
    "stdout": "Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.\n{\"type\":\"system\",\"subtype\":\"init\",\"cwd\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement\",\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"tools\":[\"Task\",\"AskUserQuestion\",\"Bash\",\"CronCreate\",\"CronDelete\",\"CronList\",\"Edit\",\"EnterPlanMode\",\"EnterWorktree\",\"ExitPlanMode\",\"ExitWorktree\",\"Glob\",\"Grep\",\"ListMcpResourcesTool\",\"Monitor\",\"NotebookEdit\",\"PushNotification\",\"Read\",\"ReadMcpResourceTool\",\"RemoteTrigger\",\"ScheduleWakeup\",\"Skill\",\"TaskOutput\",\"TaskStop\",\"TodoWrite\",\"ToolSearch\",\"WebFetch\",\"WebSearch\",\"Write\",\"mcp__agent-ml-research__detect_image\",\"mcp__agent-ml-research__kill_job\",\"mcp__agent-ml-research__read_registry\",\"mcp__agent-ml-research__register_artifact\",\"mcp__agent-ml-research__ssh_execute\",\"mcp__agent-ml-research__ssh_read_only\",\"mcp__agent-ml-research__update_registry\"],\"mcp_servers\":[{\"name\":\"agent-ml-research\",\"status\":\"connected\"}],\"model\":\"claude-opus-4-7[1m]\",\"permissionMode\":\"bypassPermissions\",\"slash_commands\":[\"update-config\",\"debug\",\"simplify\",\"batch\",\"fewer-permission-prompts\",\"loop\",\"schedule\",\"claude-api\",\"clear\",\"compact\",\"context\",\"heapdump\",\"init\",\"review\",\"security-review\",\"extra-usage\",\"usage\",\"insights\",\"team-onboarding\"],\"apiKeySource\":\"none\",\"claude_code_version\":\"2.1.126\",\"output_style\":\"default\",\"agents\":[\"claude\",\"Explore\",\"general-purpose\",\"Plan\",\"statusline-setup\"],\"skills\":[\"update-config\",\"debug\",\"simplify\",\"batch\",\"fewer-permission-prompts\",\"loop\",\"schedule\",\"claude-api\"],\"plugins\":[],\"analytics_disabled\":false,\"uuid\":\"40284446-a60c-4bc4-89ae-4719a6a59ade\",\"memory_paths\":{\"auto\":\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/\"},\"fast_mode_state\":\"off\"}\n{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1779682200,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"90bc3ca9-dda6-4082-b7e4-a4c154cb9d8c\",\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\"}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_01JPszutAwc6k5oSeJkSEReS\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"thinking\",\"thinking\":\"\",\"signature\":\"Er0FCmMIDhgCKkBXwhfOBiVbpoXU5ECsCnKrfHEfmj7p8jbQw9kxfgHNiXQJlL65wnioyjGTPQa1gUJdZukTv0ZAIIJsH0aRxJ7CMg9jbGF1ZGUtb3B1cy00LTc4AEIIdGhpbmtpbmcSDCwTHYwuFIsbrTF4gRoMecndAPGwDfQkmjXwIjD3EtOPKsOmCOXGws/WB4CLCPHr5J+MMjqaGokdw41grqukRpfGhkAmLdX+/UGEY3MqhwQJ5YNfIVTdhuSy1X3RklZ5gAMFGepJJLYW32YSwUjXuPoePntJ9sOe6KJTfD05oLw+ZQg8EZ46+7KON2KvZLUqmyZr8WwAD6hpQUrjOhNhq9K28d4XcbGanUCM9fEyIDt3dlZGMVUOPMjEvYaLBVFQqFzb3LWkHS9N/miYub9HDoLzRDtI0uvKmKdbyIdmhGm28DDXdd8n7ybf7P9Glj+4ypgpKksKZuhOuWPv00WGx6CBEQhjxrijwhAPEEAtDJE1+fJbn4fwmvOMm9TR1wJwS7Vm7ErM+TuEDYFTKEfUIXuIjkHaSXidvr/K8ROgeu5RCF3Uophl5+oeLwCIHXTkfJhTl9bnqIjlQlWBO1/Jrw1SUXVyOdXnnSpMkT1Gqk8TWvy6N7jgpx1aXc3uZ3lu2eHmtYVMBW/9JuuJrauhJ++NmR46OzFpmJ3o63xb1elVj/2MUWztAdkNQytBB0f81bMyMokRhYem8bW1xWDwfils7u1MG42S4iBFVMYVK7OnjlRkuBrwb585h1tJ/roBdXVv5ZYfED+npezImJ/ya3i4wtt6eUlmDUBa5DdsBTPk1/DGWUTzQ2RC8Sxx4ZRWSwu5S7o5kpUAy3sDVezXtx1GChpsDO9fYHQ1/O2FbP7gK5fYze2U749oiCTgdKVIr1G0uOxDM92mLZscDmK8PZRZtBo1SmUYAQ==\"}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":15471,\"cache_read_input_tokens\":16241,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":15471},\"output_tokens\":0,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"21138cd5-d7c0-4df1-841a-ce4a79574b93\"}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_01JPszutAwc6k5oSeJkSEReS\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_017FPfSLh9a3js5UchPLEo19\",\"name\":\"ToolSearch\",\"input\":{\"query\":\"select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,TodoWrite\",\"max_results\":10},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":15471,\"cache_read_input_tokens\":16241,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":15471},\"output_tokens\":0,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"4129dd72-b60d-4e28-9dfc-5e8174810511\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"type\":\"tool_result\",\"tool_use_id\":\"toolu_017FPfSLh9a3js5UchPLEo19\",\"content\":[{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__read_registry\"},{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__ssh_read_only\"},{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__ssh_execute\"},{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__detect_image\"},{\"type\":\"tool_reference\",\"tool_name\":\"TodoWrite\"}]}]},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"f771656c-93d9-4747-ad36-0548d414eb83\",\"timestamp\":\"2026-05-25T01:51:00.186Z\",\"tool_use_result\":{\"matches\":[\"mcp__agent-ml-research__read_registry\",\"mcp__agent-ml-research__ssh_read_only\",\"mcp__agent-ml-research__ssh_execute\",\"mcp__agent-ml-research__detect_image\",\"TodoWrite\"],\"query\":\"select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,TodoWrite\",\"total_deferred_tools\":26}}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_018W326SwSHnZkA6FvDEFLMf\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"thinking\",\"thinking\":\"\",\"signature\":\"EpsCCmMIDhgCKkDDGd9vAb/yvxJcEUB95E/UKCZEeKmG3S2QnccpAgYSnXEXGUWyWX4B00mx8YMi4WgYirGrE4QnRngIkveXpaD0Mg9jbGF1ZGUtb3B1cy00LTc4AEIIdGhpbmtpbmcSDC8RX2//idAtzuRfghoMx4Sq7TYwnFF48KdyIjAT5feEmlF9iHeYslqBOaparXxWqHhEGMlrumPbcAyGdTsf0A6lm2x+VGellk8eFv0qZpcifynK4hY91i+TNzj8eHH7di0VhgGeA7jrGPUFktjQ5bMt0UyEbdPrOY4UZL00Dh2GDlmilblFAm3a7z42J/N/CrqAUiOtCyJF9VNv1H+ZWxOvr2ezZGE8ECvjH8tzL19wvXkjChgB\"}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":20658,\"cache_read_input_tokens\":16334,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":20658},\"output_tokens\":8,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":{\"cache_miss_reason\":{\"type\":\"tools_changed\",\"cache_missed_input_tokens\":29069}},\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"70a0fa63-0080-4b6a-b945-785385f0e328\"}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_018W326SwSHnZkA6FvDEFLMf\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_01AANouoHGBbEBrwu2pjJqCD\",\"name\":\"TodoWrite\",\"input\":{\"todos\":[{\"content\":\"Query registry for Goal/Object DONE experiments\",\"activeForm\":\"Querying registry\",\"status\":\"in_progress\"},{\"content\":\"SSH to servers and verify JSON files (Goal)\",\"activeForm\":\"Verifying Goal JSONs\",\"status\":\"pending\"},{\"content\":\"SSH to servers and verify JSON files (Object)\",\"activeForm\":\"Verifying Object JSONs\",\"status\":\"pending\"},{\"content\":\"Cross-validate and recompute mean±std\",\"activeForm\":\"Recomputing statistics\",\"status\":\"pending\"},{\"content\":\"Generate audit report\",\"activeForm\":\"Generating report\",\"status\":\"pending\"}]},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":20658,\"cache_read_input_tokens\":16334,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":20658},\"output_tokens\":8,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":{\"cache_miss_reason\":{\"type\":\"tools_changed\",\"cache_missed_input_tokens\":29069}},\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"62f5e81e-6da4-4d0f-a0e0-1b8bef01597d\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01AANouoHGBbEBrwu2pjJqCD\",\"type\":\"tool_result\",\"content\":\"Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable\"}]},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"9457cd9d-71c2-4859-be90-f8da1f352969\",\"timestamp\":\"2026-05-25T01:51:07.074Z\",\"tool_use_result\":{\"oldTodos\":[],\"newTodos\":[{\"content\":\"Query registry for Goal/Object DONE experiments\",\"status\":\"in_progress\",\"activeForm\":\"Querying registry\"},{\"content\":\"SSH to servers and verify JSON files (Goal)\",\"status\":\"pending\",\"activeForm\":\"Verifying Goal JSONs\"},{\"content\":\"SSH to servers and verify JSON files (Object)\",\"status\":\"pending\",\"activeForm\":\"Verifying Object JSONs\"},{\"content\":\"Cross-validate and recompute mean±std\",\"status\":\"pending\",\"activeForm\":\"Recomputing statistics\"},{\"content\":\"Generate audit report\",\"status\":\"pending\",\"activeForm\":\"Generating report\"}],\"verificationNudgeNeeded\":false}}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_01LAoXTLdcLAXcGMKqz9KSa5\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_01FMRQqPY3VVRMKfwc1Dfhkr\",\"name\":\"mcp__agent-ml-research__read_registry\",\"input\":{\"project\":\"acr-vla-conformal-refinement\",\"filters\":{\"status\":\"DONE\"},\"fields\":[\"*\"],\"limit\":0},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":1,\"cache_creation_input_tokens\":410,\"cache_read_input_tokens\":36992,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":410},\"output_tokens\":49,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"ac1cf229-a5ea-4812-a659-99d054bc77fe\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01FMRQqPY3VVRMKfwc1Dfhkr\",\"type\":\"tool_result\",\"content\":\"Error: result (1,220,377 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt.\\nFormat: JSON with schema: {result: string}\\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt in sequential chunks until 100% of the content has been read.\\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\\n\"}]},\"parent_tool_use_id\":null,\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"uuid\":\"7cf49c43-36da-448c-9e20-6e7aa3af05b0\",\"timestamp\":\"2026-05-25T01:51:13.329Z\",\"tool_use_result\":{\"content\":\"Error: result (1,220,377 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt.\\nFormat: JSON with schema: {result: string}\\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/mcp-agent-ml-research-read_registry-1779673873308.txt in sequential chunks until 100% of the content has been read.\\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\\n\",\"structuredContent\":{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-k2-tau020-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T21:37:23.017Z\\\", \\\"updated_at\\\": \\\"2026-05-25T01:04:28.781Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"788081\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T21:57:59.368Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"wall_clock_seconds\\\": 10936.2, \\\"gpu_hours\\\": 3.04}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-25T01:00:11.989Z\\\"}, \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T01:00:15.617Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-25T01:00:41.988514+00:00\\\"}]}, \\\"metrics\\\": {\\\"SR\\\": 0.805, \\\"trigger_rate\\\": 0.262, \\\"mean_unc\\\": 0.1862}, \\\"notes\\\": \\\"Cron 报告 EXIT_CODE=124，但日志分析显示 τ=0.20 eval 已完成 (SR=80.5%, 161/200)。超时发生在同 tmux session 继续跑 τ=0.25 时。数据完整，纠正为 success。\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"eval-k2-tau030-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T21:37:30.605Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:52:29.111Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.30 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.30 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"475008\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-k2-tau030-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T21:58:05.975Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"wall_clock_seconds\\\": 10455.0, \\\"gpu_hours\\\": 2.9}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau030-spatial-s42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"completed_at\\\": \\\"2026-05-25T00:52:20.968Z\\\", \\\"metrics\\\": {\\\"SR\\\": 0.8, \\\"success\\\": 160, \\\"total\\\": 200, \\\"mean_unc\\\": 0.1924, \\\"trigger_rate\\\": 0.169}}, \\\"eval-k2-tau010-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T23:28:29.356Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:52:12.177Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. Retry after first attempt failed (conda not activated). Expect high trigger rate at low τ.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.10 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"327574\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-k2-tau010-spatial-s42-r2.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:28:41.167Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"wall_clock_seconds\\\": 5011.0, \\\"gpu_hours\\\": 1.39}, \\\"conclusion\\\": \\\"killed\\\", \\\"log_path\\\": \\\"bjb2-40593:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"completed_at\\\": \\\"2026-05-25T00:52:12.177Z\\\"}, \\\"eval-pi05-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:44:07.720Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:46:32.035Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial (seed 45, 20 rollouts). Replicate seed for variance estimation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 45 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 45}, \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.85, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:46:32.035Z\\\"}, \\\"eval-pi05-vla-only-object-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:44:04.114Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:46:23.539Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object (seed 44, 20 rollouts). Replicate seed for variance estimation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 44}, \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:46:23.539Z\\\"}, \\\"eval-pi05-vla-only-object-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T18:17:27.320Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:43:50.844Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object (seed 43, 20 rollouts). Replicate seed for variance estimation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"388306\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T18:18:30.109Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"wall_clock_seconds\\\": 23120.7, \\\"gpu_hours\\\": 6.42}, \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.815, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:43:50.844Z\\\"}, \\\"eval-k2-tau015-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T21:37:19.297Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:42:00.480Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.15 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.15 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"319989\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-k2-tau015-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T22:41:32.830Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"wall_clock_seconds\\\": 7227.6, \\\"gpu_hours\\\": 2.01}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-25T00:41:48.995Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-25T00:42:00.480Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-25T00:42:18.633856+00:00\\\"}]}}, \\\"eval-pi05-vla-only-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T18:17:20.358Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:37:52.191Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Goal (seed 43, 20 rollouts). Replicate seed for variance estimation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"574597\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T18:18:17.275Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 20 rollouts)\\\", \\\"wall_clock_seconds\\\": 22774.9, \\\"gpu_hours\\\": 6.33}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T23:54:22.850Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.97, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:37:52.191Z\\\"}, \\\"eval-pi05-vla-only-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T18:17:16.938Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:37:45.363Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Goal (seed 42, 20 rollouts). Establishes pi0.5 goal-conditioned baseline for ablation against conformal refinement.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"574188\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T18:18:09.640Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 20 rollouts)\\\", \\\"wall_clock_seconds\\\": 22775.7, \\\"gpu_hours\\\": 6.33}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T23:54:12.290Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.955, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:37:45.363Z\\\"}, \\\"eval-pi05-vla-only-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T18:17:23.924Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:37:38.379Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object (seed 42, 20 rollouts). Establishes pi0.5 object-manipulation baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"574940\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T18:18:23.857Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts)\\\", \\\"wall_clock_seconds\\\": 22754.5, \\\"gpu_hours\\\": 6.32}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T23:54:33.223Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.965, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:37:38.379Z\\\"}, \\\"eval-pi05-vla-only-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T18:17:13.434Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:37:31.347Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial (seed 43, 20 rollouts). Replicate seed for variance estimation of pi0.5 baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"573908\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T18:18:00.844Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"wall_clock_seconds\\\": 22770.5, \\\"gpu_hours\\\": 6.33}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T23:54:01.363Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.96, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"checkpoint_path\\\": \\\"N/A (eval only, pi05_libero_finetuned)\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T00:37:31.347Z\\\"}, \\\"eval-pi05-vla-only-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T18:17:09.880Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:35:32.912Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial (seed 42, 20 rollouts). Establishes pi0.5 baseline success rate without conformal refinement, for comparison against reconvla/adaptive modes. Tests whether evaluate.py correctly handles --model pi05 with obs_dim=2048.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"573629\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T18:17:54.298Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"wall_clock_seconds\\\": 19898.5, \\\"gpu_hours\\\": 5.53}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.98, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-spatial-s42.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T23:49:32.815Z\\\"}, \\\"eval-supp-crm-norm005-goal-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T20:19:39.365Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:35:13.584Z\\\", \\\"hypothesis\\\": \\\"SmolVLA crm_obs_only baseline on LIBERO-Goal seed48 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 48 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt",
    "persistedOutputSize": 1537149
  }
}
```

</details>

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_017fTnws71L3atyw4PHgV76S`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt | grep -oE '\"text\":\"[^\"]*\"' | grep -iE \"goal|object|seed|83\\.|85\\.|77\\.|76\\.\" | head -50",
  "description": "Extract text from prior audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "9def47f6-62e9-4854-8f43-94afeede3254",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EXKKEQ4p7VtWqkTA8xVyZJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1223,
      "cache_read_input_tokens": 104344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1223
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-25T01:56:03.321Z_

<details><summary>↩ Tool result · `toolu_017fTnws71L3atyw4PHgV76S`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "499b456b-77cb-4e6d-a6ad-6d8ca50a98c3",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01FAfDBzwvCLUBTK9CE6xMgJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt | python3 -c \"\nimport json,sys\nfor line in sys.stdin:\n  line=line.strip()\n  if not line: continue\n  try:\n    j=json.loads(line)\n    msg = j.get('message',{})\n    content = msg.get('content',[])\n    if isinstance(content,list):\n      for c in content:\n        if isinstance(c, dict) and c.get('type')=='text':\n          t = c.get('text','')\n          if any(x in t.lower() for x in ['goal','object','83.7','85.0','77.7','seed','table']):\n            print(t[:500])\n            print('---')\n  except: pass\n\" 2>&1 | head -200",
  "description": "Parse prior worker log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "31658cb9-cffd-4b35-bf73-2f8a00684d2c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0156FoUDb9qBFBG7tdPmJty5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 105567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-25T01:56:10.997Z_

<details><summary>↩ Tool result · `toolu_01FAfDBzwvCLUBTK9CE6xMgJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "bf827f05-8e27-4c17-9817-42315e63cea3",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Bash · `toolu_01DFVrEDsdgN6LoJYec29tad`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt\nhead -3 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt | cut -c1-200",
  "description": "Check file format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "757d65dd-21fe-44ed-b55a-d67e862079ab",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Gwe832T8SEw6k5nun6hnuk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 105842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 431
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-25T01:56:15.699Z_

<details><summary>↩ Tool result · `toolu_01DFVrEDsdgN6LoJYec29tad`</summary>

```text
89 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt
Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.
{"type":"system","subtype":"init","cwd":"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement","session_id":"085b74a0-965d-415e-b60e-2ccc9bf1b473","tools":["Task","Ask
{"type":"rate_limit_event","rate_limit_info":{"status":"allowed","resetsAt":1779682200,"rateLimitType":"five_hour","overageStatus":"rejected","overageDisabledReason":"org_level_disabled","isUsingOvera
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "3c28bcce-f296-42c2-ac8d-ccbe25e917d7",
  "tool_use_result": {
    "stdout": "89 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt\nWarning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.\n{\"type\":\"system\",\"subtype\":\"init\",\"cwd\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement\",\"session_id\":\"085b74a0-965d-415e-b60e-2ccc9bf1b473\",\"tools\":[\"Task\",\"Ask\n{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1779682200,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOvera",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_011nBCQA4tTdqAoWhmE1sGHn`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt < /dev/null | python3 << 'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bc0cfmls9.txt') as f:\n    for i, line in enumerate(f):\n        line=line.strip()\n        if not line.startswith('{'): continue\n        try:\n            j = json.loads(line)\n            t = j.get('type','')\n            msg = j.get('message',{})\n            content = msg.get('content','')\n            if isinstance(content, str) and any(x in content for x in ['goal','83.7','85.0','77.7','85.5','75.5','79.0']):\n                print(f'L{i}: {content[:800]}')\n                print('---')\n            if isinstance(content, list):\n                for c in content:\n                    if isinstance(c, dict):\n                        text = c.get('text','') or c.get('content','')\n                        if isinstance(text,str) and any(x in text for x in ['goal','83.7','85.0','77.7','85.5','75.5','79.0','Object','seed','json']):\n                            print(f'L{i} ({t}): {text[:800]}')\n                            print('---')\n        except Exception as e:\n            pass\nEOF",
  "description": "Parse prior audit jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "41e18ab5-411d-4dc5-88ea-c00601eb5f31",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NDEjgTM8CZDAzFMqmE8tXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 106273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 700
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-25T01:56:25.024Z_

<details><summary>↩ Tool result · `toolu_011nBCQA4tTdqAoWhmE1sGHn`</summary>

```text
L14 (user): &lt;persisted-output>
Output too large (1.1MB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bzssvbyrc.txt

Preview (first 2KB):
&lt;class 'dict'> ['result']
{"success": true, "data": {"experiments": {"eval-k2-tau020-spatial-s42": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-24T21:37:23.017Z", "updated_at": "2026-05-25T01:04:28.781Z", "hypothesis": "K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).", "spec": {"command": "python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.20 --benchmark spatial --se
---
L16 (user): total: 850
eval-pi05-vla-only-object-s44
eval-pi05-vla-only-object-s43
eval-pi05-vla-only-goal-s43
eval-pi05-vla-only-goal-s42
eval-pi05-vla-only-object-s42
eval-supp-crm-norm005-goal-s48
eval-supp-goal-vla-only-s42-bjb1
crm-norm005-goal-s49
crm-norm005-object-s48
eval-supp-goal-vla-only-s50
eval-supp-goal-vla-only-s44
eval-supp-goal-vla-only-s43
eval-supp-goal-vla-only-s42
eval-supp-vla-only-goal-s49
eval-supp-vla-only-goal-s48
eval-supp-goal-vla-only-s45
eval-pi05-vla-only-object-seed43-r4
eval-a1-baseline-object-s42
eval-supp-goal-k2mean-s47
eval-supp-goal-adapt-tau025-s47
eval-supp-goal-crm-norm005-s47
eval-supp-goal-reconvla-s47
eval-supp-goal-vla-only-s47-r3
precompute-pi05-object-2048-r2
eval-openvla-object-vla-only-seed42-v3
train-crm-pi05-goal-k1
eval-supp-goal-vla-only-s47-r2
eva
---
L23 (user): 14:## Table 1 — 3-seed（待 D139 8-seed 更新）
15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |
16-|-------|---------|-----|----------|--------|--------|
17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |
18-| Goal | 83.7±1.3(3s) | 83.7±1.8(3s) | 85.0±1.3(3s) | **+1.3pp** | +1.3pp |
19-| Object | 77.7±1.3(5s) | 76.5±2.3(3s) | 77.8±2.1(5s) | +0.1pp | +1.3pp |
20-| Long | 58.0±1.5(3s) | 55.8±1.2(3s) | 57.7±1.5(3s) | -0.3pp | **+1.9pp** |
21-
22-## D139 种子扩展 — 部署中 ⏳
23-- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验
24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites
25-- ETA：今晚（5/24）出结果
26-
27-## π0.5 跨模型验证 — 进行中 ⏳
28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**
29-- 训练完成后立即部署 3 suites eval（non-CRM 18 jobs 已审批）
30-- 论文锁定 *
---
L25 (user): 12:叙事升级目标：从"harm avoidance"→"CRM + Adaptive 共同作用"（需 Adaptive > VLA-only on Spatial/Goal/Object）。
13-
14-## Table 1 — 3-seed（待 D139 8-seed 更新）
15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |
16-|-------|---------|-----|----------|--------|--------|
17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |
--
23:- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验
24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites
25-- ETA：今晚（5/24）出结果
26-
27-## π0.5 跨模型验证 — 进行中 ⏳
28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**
--
36:- [ ] CRM Object s47 异常值 re-eval
37-- [x] Long K2mean s47: SR=54.5%（M083 旧代码文件名问题，数据已恢复）
38-
39-## Mechanism Analysis 核心发现（plan_302, Reviewer 审查通过）
40-- K=10 → 30×30 协方差 rank=9, 21/30 维度纯噪声 → per-DOF conditioning 崩
---
L27 (user): artifacts/_project/data/table1_8seed_final.md
artifacts/_project/report/table1_8seed_v2.md
---
L29 (user): # Table 1 — Multi-seed Results (Clean supp-era data)

Generated: 2026-05-24 20:10 UTC

## Main Table

| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
|-------|---------|-------------|-------------------|--------|--------|
| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |

## Paired t-test: Δ(A-V) = Adaptive - VLA-only

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
| G
---
L34 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig2_main_results.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig1_pipeline.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig3_magnitude_sweep.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval
---
L36 (user): {
  "meta": {
    "suite": "object",
    "K_max": 64,
    "n_tasks": 5,
    "n_init_states": 4,
    "H_eff": 5,
    "pose_dim": 6,
    "flat_dim": 30,
    "seed": 42
  },
  "n_decision_points": 20,
  "n_bootstrap_per_K": 32,
  "K_grid": [
    6,
    10,
    16,
    20,
    32,
    50
  ],
  "K_max": 64,
  "rank": {
    "6": {
      "mean": 5.0,
      "median": 5.0,
      "max": 5,
      "min": 5
    },
    "10": {
      "mean": 9.0,
      "median": 9.0,
      "max": 9,
      "min": 9
    },
    "16": {
      "mean": 15.0,
      "median": 15.0,
      "max": 15,
      "min": 15
    },
    "20": {
      "mean": 19.0,
      "median": 19.0,
      "max": 19,
      "min": 19
    },
    "32": {
      "mean": 29.9921875,
      "median": 30.0,
      "max": 30,
      "min": 29
    },
    "50": {
    
---
L41 (user): 34-| Plan A Object (n=3) | 18.3 ± 2.1% | seeds 42/43/44 = 19/16/20 → 18.33 ± 2.08 | ✅ |
35-| Plan A Spatial (n=3) | 35.0 ± 1.0% | seeds 42/43/44 = 34/35/36 → 35.0 ± 1.0 | ✅ |
36:| Plan A Object trigger rate | 83.7% | seeds 83.8/84.0/83.2 → mean 83.67 | ✅ |
37-| CRM K=5 Object (n=7) | 16.0 ± 2.2% | seeds 42-48 = 14/19/17/15/16/13/18 → 16.0 ± 2.16 | ✅ |
38-| CRM K=5 Spatial (n=4) | 34.5 ± 2.1% | seeds 42/43/44/45 = 35/32/37/34 → 34.5 ± 2.08 | ✅ |
39-| Random K=5 Object (n=4) | 10.5 ± 2.9% | seeds 42/43/44/45 = 14/11/10/7 → 10.5 ± 2.89 | ✅ |
40-| Random K=10 Spatial (n=3) | 29.3 ± 4.2% | seeds 42/43/44 = 34/26/28 → 29.33 ± 4.16 | ✅ |
41-| VLA-only Spatial (n=5) | 29.4 ± 1.5% | seeds 42-46 = 30/29/31/27/30 → 29.4 ± 1.52 | ✅ |
--
47-| Adaptive P25 Object (n=3) | 14.3 ± 1.2% | seeds 42/43/44 = 1
---
L45 (user): 14:Table 1 presents the primary comparison across all six methods on LIBERO Object. The obs_only CRM achieves the highest mean success rate at 17.5% (seeds 42/43/44/45 = 22/16/16/16%, std=3.0%), representing a +6.7 percentage point improvement over the vla-only baseline (10.8%, std=1.4%) and a +3.5 percentage point improvement over argmin selection alone (14.0%, std=2.6%). The vla-mean aggregation baseline (12.3%, std=2.5%) provides only marginal benefit over single-sample inference, confirming that naive averaging does not address the distributional issues in the action space. [TODO: fill seed45/46/47 for argmin] [TODO: fill seed46/47 for obs_only]
15-
16-The per-DOF and scalar CRM variants fail to improve over the VLA baseline. The perdof CRM (seeds 42/43/44: 11/12/8%, mean=10.3%, std=2.
---
L48 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_oft-libero-version-fix_20260522T130347.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_table1-long-update-and-trigger-figure_20260523T221950_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_failed-experiments-misdiagnosis_20260520T112559.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_crm-loss-conformal_20260522T062919_retry1_retry2.log
/home/ubuntu/.agent-ml-re
---
L50 (user): 41-\toprule
42-Method & $K$ & Spatial (\%) & Object (\%) & Goal (\%) & Long (\%) \\
43-\midrule
44:VLA-only & 1 & $78.7 \pm 0.3^{(3)}$ & $77.7 \pm 1.3^{(5)}$ & $83.7 \pm 1.3^{(3)}$ & $58.0 \pm 1.5^{(3)}$ \\
45:CRM always-on & 10 & $79.8 \pm 1.3^{(3)}$ & $76.5 \pm 2.3^{(3)}$ & $83.7 \pm 1.8^{(3)}$ & $55.8 \pm 1.2^{(3)}$ \\
46-$K{=}10$ argmin & 10 & $80.3 \pm 1.0^{(3)}$ & $77.3 \pm 1.5^{(3)}$ & $80.8 \pm 0.3^{(3)}$ & $56.5^{(1)}$ \\
47-$K{=}2$ mean & 2 & --- & $77.5 \pm 2.3^{(3)}$ & $83.0 \pm 2.2^{(3)}$ & $57.0^{(1)}$ \\
48-\midrule
49:ACR-VLA & 2 & $80.8 \pm 1.1^{(3)}$ & $77.8 \pm 2.1^{(5)}$ & $85.0 \pm 1.3^{(3)}$ & $57.7 \pm 1.5^{(3)}$ \\
50-\midrule
51-$\Delta$ vs VLA-only & & $+2.1$ & $+0.1$ & $+1.3$ & $-0.3$ \\
52-$\Delta_{\mathrm{CRM}}$ vs CRM & & $+1.0$ & $+1.3$ & $+1.3$ & $+1.9$ \\
5
---
L53 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft_6d6390.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/contribution_list.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/paper_evidence_packa
---
L55 (user): 5----
6-
7:## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)
8-
9-| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |
10-|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
11-| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |
12-| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |
13-| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |
14-| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |
15-| perdof (norm=0.1) | `eval-ac
---
L62 (user): # Paper Evidence Package — ACR-VLA Conformal Refinement

> Prepared: 2026-05-18. For Paper Agent startup. Contains locked evidence, data tables, figure inventory, and decision chain summary. No prose — data and facts only.

---

## 1. Method Description (D058 Corrected)

### Pipeline (K=10, primary result)
1. Frozen VLA (SmolVLA 0.4B) generates **K=10 action samples** from flow-matching
2. **Argmin selection**: pick candidate closest to sample mean (L2 distance) — same for all CRM variants
3. **CRM correction**: lightweight MLP (~337K params) takes selected action + conditioning features → outputs refined action
4. Apply correction with norm clipping: `||correction|| ≤ ε`

### CRM Variants (same architecture, different conditioning)
- **obs_only**: VLA observation features only (960D). **D
---
L65 (user): crm-norm005-goal-s49 | seed=49 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 49 --n_rollouts 20 --K 10 -
eval-crm-goal-seed42 | seed=42 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 42 --K 10 -
eval-crm-goal-seed43 | seed=43 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 43 --K 10 -
eval-crm-goal-seed44 | seed=44 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 
eval-crm-goal-seed44-r2 | seed=44 | server=bjb2-28827 | SR=?
---
L68 (user): crm-norm005-goal-s49|seed=49|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --se|notes=
eval-crm-goal-seed42|seed=42|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=
eval-crm-goal-seed43|seed=43|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=
eval-crm-goal-seed44|seed=44|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only |notes=
eval-crm-goal-seed44-r2|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 44 --K 10 --max_corr|notes=
eval-crm-goal-seed45|seed=4
---
L73 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_results_harvest.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_coverage_libero10_goal.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/experiment_status_20260523_session25.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_projec
---
L75 (user): 1:# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)
2-
3-## Per-Seed Detail
4-
5-### SPATIAL (8/8 VLA-only, 8/8 Adaptive)
6-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
7-|------|----------|----------|-----|--------|-----------|
8-| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |
9-| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |
10-| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |
11-| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |
12-| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |
13-| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |
14-| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |
15-| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |
16-
17-**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*
18-
19-### OBJECT (3/8 VLA-only, 6/8 Adaptive)
20-| Seed | VLA-
---
L78 (user): 66-
67:### Object (5 matched seeds for A-V)
68-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
69-|------|---------|----------|-----|--------|
70-| s42 | — | 81.0% | 77.0% | — |
71-| s43 | — | 77.5% | 78.5% | — |
72-| s44 | — | 75.0% | 74.0% | — |
73-| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
74-| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
75-| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
76-| s48 | 79.0% | 76.0% | — | -3.0pp |
77-| s49 | 75.5% | 74.0% | — | -1.5pp |
78-
79-### Long (5 matched seeds for A-V)
80-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
81-|------|---------|----------|-----|--------|
82-| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
83-| s43 | — | 58.0% | 54.5% | — |
84-| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
85-| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
86-| s46 | 60.5% | 58.5% | 54.0% | -
---
L81 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/gpu_scan_r7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval_partial_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary_e015e3.json
/home/ubuntu/.agent-m
---
L87 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_retry1_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-K-va
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "459b46d1-0832-4c2b-af91-dc783ed57336",
  "tool_use_result": {
    "stdout": "L14 (user): &lt;persisted-output>\nOutput too large (1.1MB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/085b74a0-965d-415e-b60e-2ccc9bf1b473/tool-results/bzssvbyrc.txt\n\nPreview (first 2KB):\n&lt;class 'dict'> ['result']\n{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T21:37:23.017Z\", \"updated_at\": \"2026-05-25T01:04:28.781Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\", \"spec\": {\"command\": \"python evaluate.py --mode adaptive_conformal_crm --K 2 --conformal_threshold 0.20 --benchmark spatial --se\n---\nL16 (user): total: 850\neval-pi05-vla-only-object-s44\neval-pi05-vla-only-object-s43\neval-pi05-vla-only-goal-s43\neval-pi05-vla-only-goal-s42\neval-pi05-vla-only-object-s42\neval-supp-crm-norm005-goal-s48\neval-supp-goal-vla-only-s42-bjb1\ncrm-norm005-goal-s49\ncrm-norm005-object-s48\neval-supp-goal-vla-only-s50\neval-supp-goal-vla-only-s44\neval-supp-goal-vla-only-s43\neval-supp-goal-vla-only-s42\neval-supp-vla-only-goal-s49\neval-supp-vla-only-goal-s48\neval-supp-goal-vla-only-s45\neval-pi05-vla-only-object-seed43-r4\neval-a1-baseline-object-s42\neval-supp-goal-k2mean-s47\neval-supp-goal-adapt-tau025-s47\neval-supp-goal-crm-norm005-s47\neval-supp-goal-reconvla-s47\neval-supp-goal-vla-only-s47-r3\nprecompute-pi05-object-2048-r2\neval-openvla-object-vla-only-seed42-v3\ntrain-crm-pi05-goal-k1\neval-supp-goal-vla-only-s47-r2\neva\n---\nL23 (user): 14:## Table 1 — 3-seed（待 D139 8-seed 更新）\n15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |\n16-|-------|---------|-----|----------|--------|--------|\n17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |\n18-| Goal | 83.7±1.3(3s) | 83.7±1.8(3s) | 85.0±1.3(3s) | **+1.3pp** | +1.3pp |\n19-| Object | 77.7±1.3(5s) | 76.5±2.3(3s) | 77.8±2.1(5s) | +0.1pp | +1.3pp |\n20-| Long | 58.0±1.5(3s) | 55.8±1.2(3s) | 57.7±1.5(3s) | -0.3pp | **+1.9pp** |\n21-\n22-## D139 种子扩展 — 部署中 ⏳\n23-- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验\n24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites\n25-- ETA：今晚（5/24）出结果\n26-\n27-## π0.5 跨模型验证 — 进行中 ⏳\n28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**\n29-- 训练完成后立即部署 3 suites eval（non-CRM 18 jobs 已审批）\n30-- 论文锁定 *\n---\nL25 (user): 12:叙事升级目标：从\"harm avoidance\"→\"CRM + Adaptive 共同作用\"（需 Adaptive > VLA-only on Spatial/Goal/Object）。\n13-\n14-## Table 1 — 3-seed（待 D139 8-seed 更新）\n15-| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | Δ(A-C) |\n16-|-------|---------|-----|----------|--------|--------|\n17-| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |\n--\n23:- s48/s49 × Adaptive + VLA-only × Spatial/Goal/Object = 12 实验\n24-- 目标：8-seed Adaptive > VLA-only mean on all 3 suites\n25-- ETA：今晚（5/24）出结果\n26-\n27-## π0.5 跨模型验证 — 进行中 ⏳\n28-- CRM 3-suite 统一训练: bjb1-18228 GPU 0, **ETA 5/25 ~04:00 UTC**\n--\n36:- [ ] CRM Object s47 异常值 re-eval\n37-- [x] Long K2mean s47: SR=54.5%（M083 旧代码文件名问题，数据已恢复）\n38-\n39-## Mechanism Analysis 核心发现（plan_302, Reviewer 审查通过）\n40-- K=10 → 30×30 协方差 rank=9, 21/30 维度纯噪声 → per-DOF conditioning 崩\n---\nL27 (user): artifacts/_project/data/table1_8seed_final.md\nartifacts/_project/report/table1_8seed_v2.md\n---\nL29 (user): # Table 1 — Multi-seed Results (Clean supp-era data)\n\nGenerated: 2026-05-24 20:10 UTC\n\n## Main Table\n\n| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |\n|-------|---------|-------------|-------------------|--------|--------|\n| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |\n| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |\n| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |\n| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |\n\n## Paired t-test: Δ(A-V) = Adaptive - VLA-only\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |\n| G\n---\nL34 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig2_main_results.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig1_pipeline.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/figures/fig3_magnitude_sweep.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval\n---\nL36 (user): {\n  \"meta\": {\n    \"suite\": \"object\",\n    \"K_max\": 64,\n    \"n_tasks\": 5,\n    \"n_init_states\": 4,\n    \"H_eff\": 5,\n    \"pose_dim\": 6,\n    \"flat_dim\": 30,\n    \"seed\": 42\n  },\n  \"n_decision_points\": 20,\n  \"n_bootstrap_per_K\": 32,\n  \"K_grid\": [\n    6,\n    10,\n    16,\n    20,\n    32,\n    50\n  ],\n  \"K_max\": 64,\n  \"rank\": {\n    \"6\": {\n      \"mean\": 5.0,\n      \"median\": 5.0,\n      \"max\": 5,\n      \"min\": 5\n    },\n    \"10\": {\n      \"mean\": 9.0,\n      \"median\": 9.0,\n      \"max\": 9,\n      \"min\": 9\n    },\n    \"16\": {\n      \"mean\": 15.0,\n      \"median\": 15.0,\n      \"max\": 15,\n      \"min\": 15\n    },\n    \"20\": {\n      \"mean\": 19.0,\n      \"median\": 19.0,\n      \"max\": 19,\n      \"min\": 19\n    },\n    \"32\": {\n      \"mean\": 29.9921875,\n      \"median\": 30.0,\n      \"max\": 30,\n      \"min\": 29\n    },\n    \"50\": {\n    \n---\nL41 (user): 34-| Plan A Object (n=3) | 18.3 ± 2.1% | seeds 42/43/44 = 19/16/20 → 18.33 ± 2.08 | ✅ |\n35-| Plan A Spatial (n=3) | 35.0 ± 1.0% | seeds 42/43/44 = 34/35/36 → 35.0 ± 1.0 | ✅ |\n36:| Plan A Object trigger rate | 83.7% | seeds 83.8/84.0/83.2 → mean 83.67 | ✅ |\n37-| CRM K=5 Object (n=7) | 16.0 ± 2.2% | seeds 42-48 = 14/19/17/15/16/13/18 → 16.0 ± 2.16 | ✅ |\n38-| CRM K=5 Spatial (n=4) | 34.5 ± 2.1% | seeds 42/43/44/45 = 35/32/37/34 → 34.5 ± 2.08 | ✅ |\n39-| Random K=5 Object (n=4) | 10.5 ± 2.9% | seeds 42/43/44/45 = 14/11/10/7 → 10.5 ± 2.89 | ✅ |\n40-| Random K=10 Spatial (n=3) | 29.3 ± 4.2% | seeds 42/43/44 = 34/26/28 → 29.33 ± 4.16 | ✅ |\n41-| VLA-only Spatial (n=5) | 29.4 ± 1.5% | seeds 42-46 = 30/29/31/27/30 → 29.4 ± 1.52 | ✅ |\n--\n47-| Adaptive P25 Object (n=3) | 14.3 ± 1.2% | seeds 42/43/44 = 1\n---\nL45 (user): 14:Table 1 presents the primary comparison across all six methods on LIBERO Object. The obs_only CRM achieves the highest mean success rate at 17.5% (seeds 42/43/44/45 = 22/16/16/16%, std=3.0%), representing a +6.7 percentage point improvement over the vla-only baseline (10.8%, std=1.4%) and a +3.5 percentage point improvement over argmin selection alone (14.0%, std=2.6%). The vla-mean aggregation baseline (12.3%, std=2.5%) provides only marginal benefit over single-sample inference, confirming that naive averaging does not address the distributional issues in the action space. [TODO: fill seed45/46/47 for argmin] [TODO: fill seed46/47 for obs_only]\n15-\n16-The per-DOF and scalar CRM variants fail to improve over the VLA baseline. The perdof CRM (seeds 42/43/44: 11/12/8%, mean=10.3%, std=2.\n---\nL48 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_oft-libero-version-fix_20260522T130347.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_table1-long-update-and-trigger-figure_20260523T221950_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_failed-experiments-misdiagnosis_20260520T112559.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_crm-loss-conformal_20260522T062919_retry1_retry2.log\n/home/ubuntu/.agent-ml-re\n---\nL50 (user): 41-\\toprule\n42-Method & $K$ & Spatial (\\%) & Object (\\%) & Goal (\\%) & Long (\\%) \\\\\n43-\\midrule\n44:VLA-only & 1 & $78.7 \\pm 0.3^{(3)}$ & $77.7 \\pm 1.3^{(5)}$ & $83.7 \\pm 1.3^{(3)}$ & $58.0 \\pm 1.5^{(3)}$ \\\\\n45:CRM always-on & 10 & $79.8 \\pm 1.3^{(3)}$ & $76.5 \\pm 2.3^{(3)}$ & $83.7 \\pm 1.8^{(3)}$ & $55.8 \\pm 1.2^{(3)}$ \\\\\n46-$K{=}10$ argmin & 10 & $80.3 \\pm 1.0^{(3)}$ & $77.3 \\pm 1.5^{(3)}$ & $80.8 \\pm 0.3^{(3)}$ & $56.5^{(1)}$ \\\\\n47-$K{=}2$ mean & 2 & --- & $77.5 \\pm 2.3^{(3)}$ & $83.0 \\pm 2.2^{(3)}$ & $57.0^{(1)}$ \\\\\n48-\\midrule\n49:ACR-VLA & 2 & $80.8 \\pm 1.1^{(3)}$ & $77.8 \\pm 2.1^{(5)}$ & $85.0 \\pm 1.3^{(3)}$ & $57.7 \\pm 1.5^{(3)}$ \\\\\n50-\\midrule\n51-$\\Delta$ vs VLA-only & & $+2.1$ & $+0.1$ & $+1.3$ & $-0.3$ \\\\\n52-$\\Delta_{\\mathrm{CRM}}$ vs CRM & & $+1.0$ & $+1.3$ & $+1.3$ & $+1.9$ \\\\\n5\n---\nL53 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft_6d6390.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/contribution_list.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/paper_evidence_packa\n---\nL55 (user): 5----\n6-\n7:## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)\n8-\n9-| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |\n10-|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n11-| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |\n12-| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |\n13-| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |\n14-| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |\n15-| perdof (norm=0.1) | `eval-ac\n---\nL62 (user): # Paper Evidence Package — ACR-VLA Conformal Refinement\n\n> Prepared: 2026-05-18. For Paper Agent startup. Contains locked evidence, data tables, figure inventory, and decision chain summary. No prose — data and facts only.\n\n---\n\n## 1. Method Description (D058 Corrected)\n\n### Pipeline (K=10, primary result)\n1. Frozen VLA (SmolVLA 0.4B) generates **K=10 action samples** from flow-matching\n2. **Argmin selection**: pick candidate closest to sample mean (L2 distance) — same for all CRM variants\n3. **CRM correction**: lightweight MLP (~337K params) takes selected action + conditioning features → outputs refined action\n4. Apply correction with norm clipping: `||correction|| ≤ ε`\n\n### CRM Variants (same architecture, different conditioning)\n- **obs_only**: VLA observation features only (960D). **D\n---\nL65 (user): crm-norm005-goal-s49 | seed=49 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 49 --n_rollouts 20 --K 10 -\neval-crm-goal-seed42 | seed=42 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 42 --K 10 -\neval-crm-goal-seed43 | seed=43 | server=bjb1-18228 | SR=? | cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 43 --K 10 -\neval-crm-goal-seed44 | seed=44 | server=bjb1-32546 | SR=? | cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts \neval-crm-goal-seed44-r2 | seed=44 | server=bjb2-28827 | SR=?\n---\nL68 (user): crm-norm005-goal-s49|seed=49|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --se|notes=\neval-crm-goal-seed42|seed=42|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=\neval-crm-goal-seed43|seed=43|server=bjb1-18228|SR=?|cmd=CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_|notes=\neval-crm-goal-seed44|seed=44|server=bjb1-32546|SR=?|cmd=CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only |notes=\neval-crm-goal-seed44-r2|seed=44|server=bjb2-28827|SR=?|cmd=python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 44 --K 10 --max_corr|notes=\neval-crm-goal-seed45|seed=4\n---\nL73 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_eval_results_harvest.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_coverage_libero10_goal.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/experiment_status_20260523_session25.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_projec\n---\nL75 (user): 1:# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)\n2-\n3-## Per-Seed Detail\n4-\n5-### SPATIAL (8/8 VLA-only, 8/8 Adaptive)\n6-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n7-|------|----------|----------|-----|--------|-----------|\n8-| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |\n9-| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |\n10-| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |\n11-| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |\n12-| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |\n13-| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |\n14-| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |\n15-| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |\n16-\n17-**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*\n18-\n19-### OBJECT (3/8 VLA-only, 6/8 Adaptive)\n20-| Seed | VLA-\n---\nL78 (user): 66-\n67:### Object (5 matched seeds for A-V)\n68-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n69-|------|---------|----------|-----|--------|\n70-| s42 | — | 81.0% | 77.0% | — |\n71-| s43 | — | 77.5% | 78.5% | — |\n72-| s44 | — | 75.0% | 74.0% | — |\n73-| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |\n74-| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |\n75-| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |\n76-| s48 | 79.0% | 76.0% | — | -3.0pp |\n77-| s49 | 75.5% | 74.0% | — | -1.5pp |\n78-\n79-### Long (5 matched seeds for A-V)\n80-| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n81-|------|---------|----------|-----|--------|\n82-| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |\n83-| s43 | — | 58.0% | 54.5% | — |\n84-| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |\n85-| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |\n86-| s46 | 60.5% | 58.5% | 54.0% | -\n---\nL81 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/gpu_scan_r7.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/magnitude_curve.py\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/crm_eval_partial_results.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/trigger_rate_scatter_data.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/summary_e015e3.json\n/home/ubuntu/.agent-m\n---\nL87 (user): /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_retry1_retry2.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-K-va\n---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7a698734-fca1-478a-97ff-180caf3613ce",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014JpdDSr5NYiuhrrVWF41wJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10766,
      "cache_read_input_tokens": 106973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10766
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01SPK5xyb4tRCq6qTnQ3FWuG`</summary>

```json
{
  "todos": [
    {
      "content": "Query registry for Goal/Object DONE experiments",
      "activeForm": "Querying registry",
      "status": "completed"
    },
    {
      "content": "SSH to servers and find Goal eval JSONs",
      "activeForm": "Finding Goal JSONs",
      "status": "in_progress"
    },
    {
      "content": "SSH to servers and find Object eval JSONs",
      "activeForm": "Finding Object JSONs",
      "status": "pending"
    },
    {
      "content": "Cross-validate against Table 1 and recompute mean±std",
      "activeForm": "Recomputing statistics",
      "status": "pending"
    },
    {
      "content": "Generate audit report",
      "activeForm": "Generating report",
      "status": "pending"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "085b74a0-965d-415e-b60e-2ccc9bf1b473",
  "uuid": "7dcf8dad-6d9d-4ea7-a00c-c3e31e2bebd0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014JpdDSr5NYiuhrrVWF41wJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10766,
      "cache_read_input_tokens": 106973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10766
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
