# audit table1 goal object provenance 20260525T015038 retry2 — Part 3 of 4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../audit-table1-goal-object-provenance-20260525t015038-retry2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/c5/c545ede7cd21aa2cae98.json)

## Before a recorded user message

### Large event (continued)

```text
eated_at\": \"2026-05-19T15:30:26.607Z\", \"updated_at\": \"2026-05-19T16:31:06.453Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-random-selection-object-k5-seed42\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 5 --output_file logs/eval_object_random_selection_k5_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 10, \"model_name\": \"SmolVLA\", \"seed\": 42, \"gpu\": \"cuda:5\", \"pid\": 939548, \"checkpoint_source\": \"N/A (random selection baseline)\", \"eval_data\": \"LIBERO-Object\", \"tmux_session\": \"eval-random-selection-object-k5-seed42\", \"output_file\": \"logs/eval_object_random_selection_k5_seed42.json\", \"log_file\": \"logs/eval_object_random_selection_k5_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:18:49.960Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:18:51.282Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T16:19:03.242474+00:00\"}]}, \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:30:32.306Z\", \"updated_at\": \"2026-05-19T16:30:37.908Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed44\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed44.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 10, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"gpu\": \"cuda:2\", \"pid\": 843594, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-spatial\", \"output_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed44.json\", \"log_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed44.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:24:46.925Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:24:38.292Z\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:30:33.621Z\", \"updated_at\": \"2026-05-19T16:30:18.549Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed45\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed45.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 10, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"gpu\": \"cuda:5\", \"pid\": 845019, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-spatial\", \"output_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed45.json\", \"log_file\": \"logs/eval_spatial_obs_only_norm02_k5_seed45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:25:51.927Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:25:54.177Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T16:26:43.837743+00:00\"}]}, \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:13:57.251Z\", \"updated_at\": \"2026-05-19T16:17:38.007Z\", \"hypothesis\": \"Latency profiling: 正式测量 VLA+CRM pipeline 各组件 wall-clock time，覆盖 K=1/5/10/20 batched vs sequential，生成论文 Table 级结果。预期 CRM overhead < 1ms，pipeline 主要 bottleneck 在 VLA flow-matching sampling。\", \"spec\": {\"command\": \"python profile_latency.py\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"107232\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"submitted_at\": \"2026-05-19T16:14:41.817Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 1, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 171.9, \"gpu_hours\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:17:33.738Z\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"spec\": {\"checkpoint_path\": \"N/A (vla_only baseline)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": \"932535\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 45 --output_file logs/eval_spatial_vla_only_seed45.json\", \"finished_at\": \"2026-05-19T15:17:27.081Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:17:34.738444+00:00\"}]}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-19T15:47:20.192Z\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:50:49.193Z\", \"updated_at\": \"2026-05-19T16:06:07.907Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve perdof ε=0.05 (当前 n=2)。timeout=16h。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"eval-perdof-norm005-seed45-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"conclusion\": \"success\", \"log_path\": \"logs/eval_object_perdof_norm005_seed45.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-19T15:29:57.924Z\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:24:44.727Z\", \"updated_at\": \"2026-05-19T15:30:01.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed44. Spatial benchmark 第三个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 44, \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 44 --output_file logs/eval_spatial_vla_only_seed44.json\"}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:4\", \"pid\": \"835806\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed44.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 44 --output_file logs/eval_spatial_vla_only_seed44.json\", \"finished_at\": \"2026-05-19T15:27:05.121Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:27:13.496164+00:00\"}]}, \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint produced)\", \"completed_at\": \"2026-05-19T15:30:01.540Z\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:50:51.880Z\", \"updated_at\": \"2026-05-19T14:58:17.531Z\", \"hypothesis\": \"obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (当前 n=3)。timeout=16h。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"eval-obs-only-default-seed48-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:55:24.359Z\"}, \"failure_reason\": \"Process gone (cron miss 4/5), no sentinel, no W&B output detected\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:55:30.658Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:55:41.674404+00:00\"}]}, \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"notes\": \"误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 output JSON 完整（59 行，10 tasks × 10 rollouts）。success_rate=0.17，与原 seed48 (bjb2-28827) 一致。\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:01:28.636Z\", \"updated_at\": \"2026-05-19T14:43:19.646Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed43. P1 缺口：与 Spatial K=5 CRM seed43=32% 配对，计算 per-seed improvement。没有此 baseline 无法报告 Spatial 改进幅度。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 43 --output_file logs/eval_spatial_vla_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"80076\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-19T13:01:37.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 43, \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6102.3, \"gpu_hours\": 1.7}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:40:35.939Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:40:44.096497+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\", \"completed_at\": \"2026-05-19T14:43:19.646Z\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:55:51.909Z\", \"updated_at\": \"2026-05-19T14:38:29.599Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed42. P1 缺口：Spatial benchmark 需要 VLA-only baseline 才能报告 CRM 的改进幅度。对标 obs_only spatial K=10 seed42=35%。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"917724\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed42.log\", \"submitted_at\": \"2026-05-19T12:57:06.478Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6083.1, \"gpu_hours\": 1.69}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:36:03.209Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:36:10.920946+00:00\"}]}, \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed42.log\", \"completed_at\": \"2026-05-19T14:38:29.600Z\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:40.507Z\", \"updated_at\": \"2026-05-19T14:32:21.490Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed45.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 5, \"max_correction_norm\": 0.2}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:21.490Z\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:39.233Z\", \"updated_at\": \"2026-05-19T14:32:16.468Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_k5_seed44.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 5, \"max_correction_norm\": 0.2}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:16.468Z\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:37.093Z\", \"updated_at\": \"2026-05-19T14:32:11.343Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed45\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 45 --K 5 --output_file logs/eval_object_random_selection_k5_seed45.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 45, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"HuggingFaceM4/SmolVLA-base\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:11.343Z\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:00:34.934Z\", \"updated_at\": \"2026-05-19T14:32:06.313Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-argmin-object-k5-seed44\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 44 --K 5 --output_file logs/eval_object_random_selection_k5_seed44.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 44, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"HuggingFaceM4/SmolVLA-base\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:06.313Z\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:57:11.028Z\", \"updated_at\": \"2026-05-19T14:32:01.561Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed43\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 43 --K 5 --output_file logs/eval_object_random_selection_k5_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 43, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"SmolVLA pretrained (random K=5 selection baseline, no fine-tuning)\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:32:01.561Z\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:43:11.414Z\", \"updated_at\": \"2026-05-19T14:31:56.882Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-argmin-object-k5-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 5 --output_file logs/eval_object_random_selection_k5_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection_K5\", \"seed\": 42, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"smolvla_libero (pretrained, no finetuning)\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:31:56.882Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:49:54.536Z\", \"updated_at\": \"2026-05-19T14:26:11.536Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"eval-spatial-obs-only-norm02-seed44\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:12:36.942Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:12:33.705Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:12:43.426190+00:00\"}]}, \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:29:55.249Z\", \"updated_at\": \"2026-05-19T13:39:15.552Z\", \"spec\": {\"command\": \"crm_perdof --seed 43 --K 10 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"571010\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed43.log\", \"submitted_at\": \"2026-05-18T01:29:54.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 130160.9, \"gpu_hours\": 36.16}, \"reproduce\": {\"finished_at\": \"2026-05-18T16:26:03.341Z\"}, \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed43.log\", \"hypothesis\": \"per-DoF CRM with max_correction_norm=0.1 on LIBERO-Object (seed43, K=10, n_rollouts=10) should achieve comparable SR to obs_only default, as tighter norm constraint limits correction magnitude per joint.\", \"completed_at\": \"2026-05-19T13:39:15.552Z\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:05:53.834Z\", \"updated_at\": \"2026-05-19T13:35:23.895Z\", \"hypothesis\": \"obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=12%)，需标准化。obs_only default 当前 n=3 (seed42/43/44)。\", \"parent\": \"eval-obs-only-object-default-seed45\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"579212\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed45-r2.log\", \"submitted_at\": \"2026-05-18T13:24:59.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 87024.8, \"gpu_hours\": 24.17}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": \"579212\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed45-r2.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45_r2.json\", \"finished_at\": \"2026-05-19T04:22:06.623Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:22:13.278219+00:00\"}]}, \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:35:23.895Z\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:30.602Z\", \"updated_at\": \"2026-05-19T13:30:16.050Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 42 --K 5 --output_file logs/eval_object_argmin_k5_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"883706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed42.log\", \"submitted_at\": \"2026-05-19T11:36:06.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_reconvla_argmin\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6679.2, \"gpu_hours\": 1.86}, \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed42 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"reproduce\": {\"finished_at\": \"2026-05-19T13:26:43.546Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:26:53.401549+00:00\"}]}, \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:27:25.720Z\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:36:13.145Z\", \"updated_at\": \"2026-05-19T13:26:50.930Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 5 --output_file logs/eval_object_argmin_k5_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"884249\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed45.log\", \"submitted_at\": \"2026-05-19T11:36:12.365Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_reconvla_argmin\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6638.6, \"gpu_hours\": 1.84}, \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed45 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:26:50.930Z\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:15.812Z\", \"updated_at\": \"2026-05-19T13:26:46.918Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 5 --output_file logs/eval_object_argmin_k5_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"883975\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed43.log\", \"submitted_at\": \"2026-05-19T11:36:09.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_reconvla_argmin\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 6637.5, \"gpu_hours\": 1.84}, \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed43 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T13:26:46.918Z\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:18:03.763Z\", \"updated_at\": \"2026-05-19T13:24:40.192Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed43 on LIBERO-Object. 补 magnitude curve：perdof ε=0.3 当前 n=3 (seed42:4%, seed44:4%, seed45:6%)，mean=4.67%。增加第 4 个 seed 强化 error bars。\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-18T15:18:23.972Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed43.json\", \"finished_at\": \"2026-05-18T21:19:30.796Z\", \"training_hours\": 6.02}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"594147\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed43.log\", \"submitted_at\": \"2026-05-18T15:18:27.012Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21673.4, \"gpu_hours\": 6.02}, \"pid\": \"594147\", \"log_path\": \"/root/logs/eval_object_perdof_norm03_seed43.json\", \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:19:40.460Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:20:00.703434+00:00\"}]}, \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:49:55.654Z\", \"updated_at\": \"2026-05-19T13:12:13.645Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"eval-spatial-obs-only-norm02-seed45\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T12:50:07.643Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:50:11.303Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:50:17.204819+00:00\"}]}, \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:40:51.279Z\", \"updated_at\": \"2026-05-19T12:48:29.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=0 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-multistage-object --auto 2>&1 | tee /root/acr-vla-conformal-refinement/logs/train_crm_k1_full.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"434871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42-full.log\", \"submitted_at\": \"2026-05-17T15:40:50.814Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 162458.5, \"gpu_hours\": 45.13}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1_accg_full/crm_best.pt\", \"hypothesis\": \"K=1 CRM full training with multi-stage VLA feature fusion + composite loss (L2 + contrastive + uncertainty-weighted) on full object benchmark dataset. Scaled-up version of train-crm-k1-accg-object-seed42-v2 with complete training data.\", \"completed_at\": \"2026-05-19T12:48:29.290Z\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:11:43.484Z\", \"updated_at\": \"2026-05-19T12:48:27.021Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/precompute_k1.py --benchmark spatial --batch_size 4 --cache_dir /root/autodl-tmp/crm_cache_k1/ 2>&1 | tee logs/precompute_k1.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"649967\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_701-precompute-k1-spatial.log\", \"submitted_at\": \"2026-05-17T14:11:42.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 167804.3, \"gpu_hours\": 46.61}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/precomputed/k1_spatial/\", \"hypothesis\": \"K=1 spatial benchmark precomputation: generate single-sample VLA action predictions and features for CRM K=1 training. Required preprocessing step before K=1 CRM can be trained on spatial tasks.\", \"completed_at\": \"2026-05-19T12:48:27.021Z\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:04:14.203Z\", \"updated_at\": \"2026-05-19T12:48:10.176Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p /root/autodl-tmp/checkpoints/crm_k1 && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm_k1.py --auto --benchmark spatial --epochs 50 --batch_size 512 --lr 1e-3 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-train-spatial --precompute_batch_size 4 --output_dir /root/autodl-tmp/checkpoints/crm_k1/ 2>&1 | tee logs/train_crm_k1.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"422526\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_701-crm-k1-train.log\", \"submitted_at\": \"2026-05-17T14:04:13.752Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 168236.4, \"gpu_hours\": 46.73}, \"hypothesis\": \"K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_best.pt\", \"completed_at\": \"2026-05-19T12:48:10.176Z\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:53.216Z\", \"updated_at\": \"2026-05-19T12:48:06.312Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"774538\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\", \"submitted_at\": \"2026-05-17T22:59:52.629Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 136093.7, \"gpu_hours\": 37.8}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.3 至 n=7。\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:44:29.475Z\"}, \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}, \"completed_at\": \"2026-05-19T12:48:06.312Z\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:51.090Z\", \"updated_at\": \"2026-05-19T12:48:03.869Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"774337\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\", \"submitted_at\": \"2026-05-17T22:59:50.463Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 136093.4, \"gpu_hours\": 37.8}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.1 至 n=7。\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:44:25.580Z\"}, \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}, \"completed_at\": \"2026-05-19T12:48:03.869Z\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:56:16.472Z\", \"updated_at\": \"2026-05-19T12:48:01.446Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file /root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"989694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-vla-only-r3.log\", \"submitted_at\": \"2026-05-19T05:56:15.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24705.6, \"gpu_hours\": 6.86}, \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks r3 rerun. Second reproduction of LTO baseline SR=14%. Confirms v2 result consistency.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"completed_at\": \"2026-05-19T12:48:01.446Z\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:55:29.003Z\", \"updated_at\": \"2026-05-19T12:47:58.882Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file logs/eval_lto_splitA_vla_only_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"976974\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-vla-only-r2.log\", \"submitted_at\": \"2026-05-19T04:55:28.251Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28350.6, \"gpu_hours\": 7.88}, \"hypothesis\": \"VLA-only baseline on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"completed_at\": \"2026-05-19T12:47:58.882Z\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:55:26.507Z\", \"updated_at\": \"2026-05-19T12:47:56.312Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode crm_obs_only --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --K 5 --max_correction_norm 0.2 --output_file logs/eval_lto_splitA_heldout_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"976768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-heldout-r2.log\", \"submitted_at\": \"2026-05-19T04:55:25.815Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28350.5, \"gpu_hours\": 7.88}, \"hypothesis\": \"LTO split-A CRM (K=5, ε=0.2, obs_only) on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"completed_at\": \"2026-05-19T12:47:56.312Z\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:13:30.382Z\", \"updated_at\": \"2026-05-19T12:47:52.436Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 python train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_v3 --input_mode obs_only --task_indices 0,1,2,3,4 --epochs 50 --batch_size 256 --lr 0.008 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_lto_splitA/obs_only/ --hidden_dim 256 --val_split 0.1 --log_every 20 2>&1 | tee /root/runs/acr-vla-conformal-refinement/crm-lto-splitA-train.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"953358\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-lto-splitA-train.log\", \"submitted_at\": \"2026-05-19T03:13:29.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 34462.7, \"gpu_hours\": 9.57}, \"conclusion\": \"success\", \"hypothesis\": \"LTO Split A CRM training (obs_only, 5 tasks, task_indices 0-4). Predecessor to eval-lto-splitA-heldout experiments. Superseded by crm-lto-splitA-train-fixed (task_names matching).\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA/crm_best.pt\", \"completed_at\": \"2026-05-19T12:47:52.436Z\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:31:15.780Z\", \"updated_at\": \"2026-05-19T12:23:18.801Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed48 on LIBERO-Object. 补 magnitude curve 最薄点 perdof ε=0.03 (当前 n=1)。timeout=16h。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.03 --n_rollouts 10 --timeout 57600\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\", \"submitted_at\": \"2026-05-18T21:31:00Z\"}, \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:59:18.061Z\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:22:25.439Z\", \"updated_at\": \"2026-05-19T11:45:28.182Z\", \"hypothesis\": \"Scalar CRM seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current scalar: [9,10,6,9] mean=8.5%\", \"parent\": \"eval-scalar-object-seed45\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed45_r2.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"464950\", \"log_path\": \"logs/eval_object_scalar_seed45_r2.json\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T11:45:28.182Z\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:33.036Z\", \"updated_at\": \"2026-05-19T11:34:16.077Z\", \"spec\": {\"command\": \"K=5 obs_only spatial ε=0.2 seed43\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"786306\", \"log_path\": \"logs/eval_spatial_obs_only_norm02_k5_seed43.json\", \"submitted_at\": \"2026-05-19T04:08:32.396Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"wall_clock_seconds\": 26743.7, \"gpu_hours\": 7.43}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:34:16.077Z\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:04:44.384Z\", \"updated_at\": \"2026-05-19T11:34:12.397Z\", \"spec\": {\"command\": \"K=5 obs_only ε=0.2 seed48\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"784377\", \"log_path\": \"logs/eval_object_obs_only_norm02_k5_seed48.json\", \"submitted_at\": \"2026-05-19T04:04:42.324Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"wall_clock_seconds\": 26970.1, \"gpu_hours\": 7.49}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration 补种到 n=7 统计力度增强。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:34:12.398Z\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:08:18.656Z\", \"updated_at\": \"2026-05-19T11:31:39.191Z\", \"spec\": {\"command\": \"K=5 obs_only spatial seed42\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"717974\", \"log_path\": \"logs/eval_spatial_obs_only_norm02_k5_seed42.json\", \"submitted_at\": \"2026-05-19T04:08:17.987Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"wall_clock_seconds\": 26601.2, \"gpu_hours\": 7.39}, \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"completed_at\": \"2026-05-19T11:31:39.191Z\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:29:24.718Z\", \"updated_at\": \"2026-05-19T11:30:55.300Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"956475\", \"log_path\": \"logs/eval_object_obs_only_norm02_k5_seed46.json\", \"submitted_at\": \"2026-05-19T03:31:41.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-obs-only-object-norm02-k5-seed46\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 28569.4, \"gpu_hours\": 7.94}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 n≥5。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:27:50.610Z\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:19:21.005Z\", \"updated_at\": \"2026-05-19T11:30:43.198Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval. Retry after .replace task matching bug fix.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file logs/eval_lto_splitA_vla_only_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"log_path\": \"/root/acr-vla-conformal-refinement/src/logs/eval_lto_splitA_vla_only_r2.json\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-lto-splitA-vla-only-r2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:27:47.248Z\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:19:18.968Z\", \"updated_at\": \"2026-05-19T11:30:33.951Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. Retry after .replace task matching bug fix.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode crm_obs_only --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --K 5 --max_correction_norm 0.2 --output_file logs/eval_lto_splitA_heldout_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/acr-vla-conformal-refinement/src/logs/eval_lto_splitA_heldout_r2.json\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-lto-splitA-heldout-r2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA+CRM_lto_splitA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T11:27:43.439Z\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:44.467Z\", \"updated_at\": \"2026-05-19T11:30:18.282Z\", \"hypothesis\": \"Per-DoF CRM (ε=default/unlimited) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed47.json\", \"server\": \"bjb2-28827\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_default_seed47.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T11:24:52.163Z\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束, success_rate=0%\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:47.310Z\", \"updated_at\": \"2026-05-19T11:30:17.012Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed47.json\", \"server\": \"bjb2-28827\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm03_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:49.647Z\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:41.596Z\", \"updated_at\": \"2026-05-19T11:30:15.785Z\", \"hypothesis\": \"Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed48.json\", \"server\": \"bjb2-28827\", \"seed\": 48, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_obs_only\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_default_seed48.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:56.050Z\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:35.770Z\", \"updated_at\": \"2026-05-19T11:30:14.493Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed46.json\", \"server\": \"bjb2-28827\", \"seed\": 46, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm003_seed46.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:58.897Z\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:29:18.036Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"notes\": \"bjb1-32546 GPU process dead, no JSON output\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:23.296Z\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-18T15:16:48.731Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\"}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"652406\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-18T15:16:51.497Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"notes\": \"bjb1-32546 GPU process dead, no JSON output\", \"wall_clock_seconds\": 72677.9, \"gpu_hours\": 20.19}, \"pid\": \"652406\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed45.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:28:09.358Z\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:29:27.251Z\", \"updated_at\": \"2026-05-19T11:27:53.132Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed47.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"956741\", \"log_path\": \"logs/eval_object_obs_only_norm02_k5_seed47.json\", \"submitted_at\": \"2026-05-19T03:31:43.769Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-obs-only-object-norm02-k5-seed47\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 28569.4, \"gpu_hours\": 7.94}, \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 n≥6。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:27:53.132Z\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:25:28.189Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.1 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/logs/eval_object_perdof_norm01_seed48.json\"}, \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:28.189Z\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:25:18.480Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_default_seed47.log\"}, \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:18.480Z\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:25:13.541Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm03_seed46.log\"}, \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:25:11.008Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_norm03_seed46.log\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:25:07.860Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed46.log\"}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:07.860Z\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:44:44.161Z\", \"updated_at\": \"2026-05-19T05:16:02.877Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. Retry with timeout=16h after r1 timed out. 补 magnitude curve 最薄点 ε=0.03。\", \"spec\": {\"command\": \"timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed45.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"eval-obs-only-norm003-seed45-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T04:44:28.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:44:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:44:37.585122+00:00\"}]}, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/logs/eval_object_obs_only_norm003_seed45.log\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:35:02.089Z\", \"updated_at\": \"2026-05-19T05:13:20.212Z\", \"spec\": {\"command\": \"killed (buggy .replace task matching)\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"970894\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-19T04:35:01.423Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval-only, killed due to task matching bug)\", \"wall_clock_seconds\": 1469.7, \"gpu_hours\": 0.41}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:59:31.167Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval.\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:34:59.607Z\", \"updated_at\": \"2026-05-19T05:13:18.481Z\", \"spec\": {\"command\": \"killed (buggy .replace task matching)\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"970686\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-19T04:34:58.943Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA+CRM_lto_splitA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval-only, killed due to task matching bug)\", \"wall_clock_seconds\": 1469.4, \"gpu_hours\": 0.41}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:59:28.321Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. If SR > VLA-only on held-out tasks, CRM generalizes beyond training distribution.\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:53:33.612Z\", \"updated_at\": \"2026-05-19T04:58:44.483Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 obs_only ε=0.05 seed (n=4→5)。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm005_seed46.log\", \"server\": \"bjb1-18228\", \"seed\": 46, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:58:44.483Z\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:14.835Z\", \"updated_at\": \"2026-05-19T04:58:40.993Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed48 on LIBERO-Object. 补 perdof ε=0.3 至 n=7。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"seed\": 48, \"model_name\": \"crm_v3_norm_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:58:40.993Z\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:09:03.172Z\", \"updated_at\": \"2026-05-19T04:58:36.864Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed49 on LIBERO-Object. 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)，第 6 个 seed 确保极低 norm 端统计可靠。\", \"spec\": {\"command\": \"crm_obs_only --benchmark object --seed 49 --K 10 --max_correction_norm 0.03 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 49, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:58:36.864Z\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:27:23.594Z\", \"updated_at\": \"2026-05-19T04:32:49.103Z\", \"spec\": {\"command\": \"python train_crm.py --benchmark object --task_names alphabet_soup,bbq_sauce,butter,chocolate_pudding,cream_cheese --input_mode obs_only --epochs 50 --output_dir /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"955547\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-lto-splitA-train-fixed.log\", \"submitted_at\": \"2026-05-19T03:27:22.886Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Uses --task_names string matching (bug-fixed, no numeric index).\", \"data_path\": \"/root/autodl-tmp/crm_cache_v3/object/\", \"data_count\": 7499, \"model_name\": \"crm_obs_only_lto_splitA\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt\", \"metrics\": {\"best_val_loss\": 0.091861}, \"wall_clock_seconds\": 3926.2, \"gpu_hours\": 1.09}, \"conclusion\": \"success\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks. Uses task_names string matching.\", \"completed_at\": \"2026-05-19T04:32:49.103Z\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:10.585Z\", \"updated_at\": \"2026-05-19T04:32:33.294Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. 补 magnitude curve ε=0.03 至 n=6。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed47.json\", \"server\": \"bjb1-18228\", \"seed\": 47, \"model_name\": \"crm_v3_norm_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only, killed)\", \"log_path\": \"N/A (killed before completion)\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T04:32:33.295Z\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"submitted_at\": \"2026-05-18T13:25:05.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A-eval\", \"wall_clock_seconds\": 50627.1, \"gpu_hours\": 14.06}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"finished_at\": \"2026-05-19T03:25:56.586Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:26:06.809444+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:28:52.476Z\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"submitted_at\": \"2026-05-18T13:28:51.027Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"max_correction_norm\": 0.05, \"seed\": 43, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"wall_clock_seconds\": 48429.6, \"gpu_hours\": 13.45}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"finished_at\": \"2026-05-19T02:35:05.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:35:13.418956+00:00\"}]}, \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:56:00.676Z\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:17:50.362Z\", \"updated_at\": \"2026-05-19T01:44:05.704Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed43 confirms cross-seed consistency of collapse.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"832702\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-default-seed43.log\", \"submitted_at\": \"2026-05-18T10:31:01.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 54783.7, \"gpu_hours\": 15.22}, \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"log_path\": \"bjb1-18228:/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\", \"completed_at\": \"2026-05-19T01:44:05.704Z\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-19T01:38:34.712Z\", \"completed_at\": \"2026-05-17T02:54:38.157Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed45 confirms cross-seed consistency of collapse.\", \"parent\": \"crm-train-v2-perdof\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"metrics\": {\"kill_reason\": \"Sacrificed for P0 direct-correction experiment (no free GPU). Was at task 5/10 after 6h. Expected result: 0% (confirmed by seed42=0%, seed44 running on autodl-4090).\", \"partial_progress\": \"5/10 tasks, bbq_sauce 0% success\"}}}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"626277\", \"tmux_session\": \"eval_perdof_default_seed45\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof_uncapped\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.log\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:38.704Z\", \"updated_at\": \"2026-05-19T01:33:59.345Z\", \"hypothesis\": \"Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b+crm_obs_only\"}, \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.log\", \"completed_at\": \"2026-05-19T01:33:59.345Z\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:51:08.830Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"finished_at\": \"2026-05-18T21:53:11.259Z\", \"training_hours\": 6.03}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"submitted_at\": \"2026-05-18T15:51:11.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21723.3, \"gpu_hours\": 6.03}, \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T21:53:14.790Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:53:20.362616+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:27:12.596Z\", \"updated_at\": \"2026-05-18T21:05:50.448Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=19%, mean=16.5%). Variance 大 (5pp gap), 第三个 seed 对 K-value scaling narrative 至关重要。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"575334\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed44.log\", \"submitted_at\": \"2026-05-18T13:02:07.891Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 29022.6, \"gpu_hours\": 8.06}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": \"575334\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed44.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed44.json\", \"finished_at\": \"2026-05-18T20:50:04.112Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:50:11.696653+00:00\"}]}, \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"completed_at\": \"2026-05-18T21:05:50.448Z\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:31:41.748Z\", \"updated_at\": \"2026-05-18T19:14:55.968Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。重试 r2 修正 python 路径。\", \"parent\": \"eval-perdof-object-norm003-seed44\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"855046\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44-r2.log\", \"submitted_at\": \"2026-05-18T13:32:24.693Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20543.8, \"gpu_hours\": 5.71}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": \"855046\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44-r2.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\", \"finished_at\": \"2026-05-18T19:14:49.922Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T19:14:48.505Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:14:58.108020+00:00\"}]}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:33:39.698Z\", \"updated_at\": \"2026-05-18T16:48:10.654Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.\", \"spec\": {\"command\": \"crm_obs_only --seed 46 --K 10 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"562396\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:26:17.222Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T15:18:13.193Z\", \"spec\": {\"command\": \"crm_perdof --seed 44 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"553052\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-17T23:31:56.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 56776.9, \"gpu_hours\": 15.77}, \"hypothesis\": \"perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。\", \"reproduce\": {\"finished_at\": \"2026-05-18T12:34:49.939Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T12:34:56.300941+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-18T15:18:13.193Z\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:44:42.438Z\", \"updated_at\": \"2026-05-18T14:17:30.462Z\", \"hypothesis\": \"VLA-only baseline seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current VLA-only: [12,12,10,9,13] mean=11.2%\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 45 --K 1 --output_file logs/eval_object_vla_only_seed45_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA (VLA-only)\", \"seed\": 45, \"pid\": 839546, \"tmux_session\": \"eval_vla_only_seed45_r2\"}, \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:17:30.462Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:02:40.444Z\", \"updated_at\": \"2026-05-18T13:27:03.418Z\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 774538, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T13:20:28.460Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:20:31.564Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:20:37.041564+00:00\"}]}, \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A (eval only)\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T04:37:18.401Z\", \"updated_at\": \"2026-05-18T12:39:30.555Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"527465\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed43.log\", \"submitted_at\": \"2026-05-18T04:37:17.870Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 28932.7, \"gpu_hours\": 8.04}, \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.\", \"reproduce\": {\"finished_at\": \"2026-05-18T12:33:47.520Z\"}, \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T12:39:30.555Z\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:32:26.297Z\", \"updated_at\": \"2026-05-18T12:33:45.335Z\", \"hypothesis\": \"perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52 UTC.\", \"parent\": \"eval-perdof-object-norm01-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T12:33:45.336Z\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:32:25.342Z\", \"updated_at\": \"2026-05-18T12:33:41.666Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 07:52 UTC.\", \"parent\": \"eval-obs-only-object-norm01-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T12:33:41.666Z\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:36:46.839Z\", \"updated_at\": \"2026-05-18T10:56:45.558Z\", \"hypothesis\": \"Perdof CRM with norm clipping ε=0.2 provides controlled corrections that preserve baseline policy behavior on LIBERO-Object. Expected SR ~10% (similar to other seeds 42/44/45/46/47 at 9-12%).\", \"spec\": {\"command\": \"crm_perdof --seed 43 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"535595\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:56:45.558Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-18T07:05:38.605Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"393633\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\", \"submitted_at\": \"2026-05-17T06:51:36.171Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof_v3_norm\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 87240.0, \"gpu_hours\": 24.23}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T07:05:36.145Z\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-18T07:05:03.603Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode crm_obs_only --max_correction_norm 0.1 --k 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_norm01_seed45.json > logs/eval_object_obs_only_norm01_seed45.log 2>&1\", \"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"model_name\": \"crm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": -1, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"obs_only CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve data point. seed42=19%.\"}, \"pid\": 474319, \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\", \"conclusion\": \"success\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"completed_at\": \"2026-05-17T13:31:33.316Z\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-18T07:05:02.646Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:32:21.424Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-17T18:32:28.770Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:40.928533+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:54.338Z\", \"updated_at\": \"2026-05-18T07:05:01.672Z\", \"hypothesis\": \"perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": 423767, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T01:27:04.768Z\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-18T06:19:59.229Z\", \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:20:12.857Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-17T07:20:15.008Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:20:19.307187+00:00\"}], \"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Task 10 not started due to 24h timeout. 0/90 rollouts succeeded. Catastrophic collapse at unclipped norm.\", \"seed\": 44, \"mode\": \"crm_perdof\", \"benchmark\": \"object\", \"max_correction_norm\": \"default (~1.42)\"}, \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\"}}, \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"partial results from previous run, 0/90 rollouts across 9/10 tasks\", \"server\": \"autodl-4090 (previous run)\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"model_name\": \"crm_perdof\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 90}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-18T05:54:22.364Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:2\", \"pid\": 13728, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:14.331Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:30:15.807Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:23.476790+00:00\"}]}, \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-18T05:54:21.341Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 288939, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\", \"gpu_ids\": [\"cuda:2\"]}, \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:54.647Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T04:57:55.887Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:57.857060+00:00\"}]}}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-18T05:54:20.300Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:04:16.712Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 7/10 tasks 后在 task 8 启动前被 kill。\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-18T05:54:19.300Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 24161.7, \"gpu_hours\": 6.71}, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:04:17.448Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 6/10 tasks，第 7 个 task (next_to_cookie_box) rollout 5/10 时被 kill。\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-18T05:54:18.227Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 40187.5, \"gpu_hours\": 11.16}, \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:45.148Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T04:57:46.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:50.175181+00:00\"}]}, \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-18T05:54:17.209Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"197057\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:17:05.974Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28899.4, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:44.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:45.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:46.631294+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-18T05:54:16.171Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"197803\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log\", \"submitted_at\": \"2026-05-14T12:17:13.006Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction generalizes from spatial to object benchmark — cross-benchmark validation of ACR-VLA.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28901.2, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:53.408Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:54.185Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:55.466058+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:56:51.046Z\", \"updated_at\": \"2026-05-18T05:54:15.084Z\", \"spec\": {\"command\": \"python -u src/openvla_eval.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --K 1 --gpu 0 --model_path /root/autodl-tmp/models/openvla-libero-object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"667642\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log\", \"submitted_at\": \"2026-05-17T15:57:37.232Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7512.0, \"gpu_hours\": 2.09}, \"hypothesis\": \"OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40.1 in isolated conda env. Dry-run verified 80% SR on libero_spatial. Awaiting GPU for full LIBERO-Object eval.\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:01:16.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:01:26.464150+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}, \"completed_at\": \"2026-05-17T18:02:49.250Z\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log\", \"notes\": \"NEEDS INVESTIGATION: 0% success rate vs OpenVLA paper 88.4% (LIBERO-Object). 100% confirmed code bug. Suspected action tokenization/detokenization or unnormalize issue. Do NOT treat as valid baseline.\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:28.585Z\", \"updated_at\": \"2026-05-18T04:37:10.886Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"404983\", \"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed47.json\", \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T04:37:04.589Z\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:21.870Z\", \"updated_at\": \"2026-05-18T03:04:35.124Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"796895\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed48.log\", \"submitted_at\": \"2026-05-18T03:04:34.555Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:12:19.723Z\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:52.326Z\", \"updated_at\": \"2026-05-18T03:03:50.286Z\", \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 422357, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:20:44.089Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T00:20:46.904Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:20:52.370655+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-18T02:24:22.787Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 389051, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:24:14.354Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-18T01:01:03.202Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --output_file logs/eval_object_obs_only_norm01_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"590833\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.log\", \"submitted_at\": \"2026-05-17T06:54:14.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"seed\": 46, \"wall_clock_seconds\": 65208.4, \"gpu_hours\": 18.11}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-18T01:00:59.710Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T01:01:03.202Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:01:13.372128+00:00\"}]}}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:31.864Z\", \"updated_at\": \"2026-05-17T23:47:05.521Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"448773\", \"log_path\": \"N/A (killed as orphan)\", \"submitted_at\": \"2026-05-17T18:04:30.652Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 47, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 20554.9, \"gpu_hours\": 5.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:47:05.521Z\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:34.999Z\", \"updated_at\": \"2026-05-17T23:47:03.765Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"449059\", \"log_path\": \"N/A (killed as orphan)\", \"submitted_at\": \"2026-05-17T18:04:34.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 46, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 20549.5, \"gpu_hours\": 5.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:47:03.765Z\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T23:17:06.378Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"N/A (killed as duplicate)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:02:21.019Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T23:10:07.386Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"449330\", \"log_path\": \"N/A (killed)\", \"submitted_at\": \"2026-05-17T18:04:36.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_perdof + SmolVLA\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 18330.9, \"gpu_hours\": 5.09}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:10:07.386Z\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T23:00:33.671Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"spec\": {\"command\": \"cd /root/autodl-tmp/acr-vla && python evaluate.py --model smolvla --mode crm_perdof --benchmark object --seed 47 --n_rollouts 10 --norm_limit 0.1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 414817, \"data_path\": \"/root/autodl-tmp/acr-vla/libero/data\", \"data_count\": 100, \"model_name\": \"SmolVLA-450M + CRM-perdof\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks × 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:00:33.671Z\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:06:55.243Z\", \"updated_at\": \"2026-05-17T22:39:25.302Z\", \"hypothesis\": \"OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.\", \"spec\": {\"command\": \"bash -c \\\"source /root/autodl-tmp/conda_envs/openvla/bin/activate && cd /root/autodl-tmp/openvla && MUJOCO_GL=egl python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --num_trials_per_task 10 --seed 42 --local_log_dir /root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 747644, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 10 trials = 100 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}, \"completed_at\": \"2026-05-17T22:39:25.302Z\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T21:14:35.625Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu_id\": \"cuda:3\", \"tmux_session\": \"eval-k1-seed44\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:14:35.625Z\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T21:02:09.738Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 504682, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 44, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:09.738Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:11.800Z\", \"updated_at\": \"2026-05-17T21:02:08.069Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": 503178, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 43, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed43.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:08.069Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:09.846Z\", \"updated_at\": \"2026-05-17T21:02:06.052Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 455518, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 42, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:06.052Z\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T21:01:12.153Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 393646, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"log_path\": \"logs/eval_object_perdof_norm01_seed46.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-17T21:01:12.153Z\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T20:55:55.430Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_multiscale\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu_id\": \"cuda:1\", \"tmux_session\": \"eval-k1-seed43\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"completed_at\": \"2026-05-17T20:55:55.430Z\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:18.289Z\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"634427\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r2.log\", \"submitted_at\": \"2026-05-17T13:35:38.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 17779.9, \"gpu_hours\": 4.94}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:31:54.940Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:31:57.991Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:03.172248+00:00\"}]}}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:34:38.488Z\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"633631\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed43-r3.log\", \"submitted_at\": \"2026-05-17T13:35:14.715Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 17815.3, \"gpu_hours\": 4.95}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:32:06.590Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:32:10.053Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:15.088162+00:00\"}]}}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:20.097Z\", \"updated_at\": \"2026-05-17T18:35:42.842Z\", \"hypothesis\": \"Measure wall-clock latency of ACR-VLA pipeline components: VLA encode, VLA K-sampling (K=1/5/10/20), CGS scoring, CRM forward pass, and full pipeline. Quantify overhead of conformal refinement relative to VLA sampling cost.\", \"spec\": {\"command\": \"python -u src/latency_profile.py\", \"server\": \"bjb2-28827\", \"seed\": 42, \"data_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"completed_at\": \"2026-05-17T18:35:42.842Z\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T15:51:14.367Z\", \"updated_at\": \"2026-05-17T18:31:23.291Z\", \"hypothesis\": \"K=1 CRM with ACCG using full multi-scale features (4×960D from SmolVLA layers [3,7,11,15]). Multi-scale should capture richer correction signals than single-stage 960D fallback (val_loss=0.006505). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:01:06.354Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:01:12.607135+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"HDF5 corruption report was false alarm - all 10 files verified intact (md5 match, h5py OK). Training continued past crash point. Precompute running: 7500/72507, ~75 min remaining. conclusion=failed was set prematurely; training is actually running.\"}}, \"completed_at\": \"2026-05-17T18:01:40.220Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42-v2.log\"}, \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:01.165Z\", \"updated_at\": \"2026-05-17T18:22:02.272Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed44. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460733, \"gpu\": [\"cuda:5\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed44.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"completed_at\": \"2026-05-17T18:02:47.296Z\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:27:59.825Z\", \"updated_at\": \"2026-05-17T18:22:01.354Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460729, \"gpu\": [\"cuda:4\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed43.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"completed_at\": \"2026-05-17T18:02:45.640Z\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:27:58.213Z\", \"updated_at\": \"2026-05-17T18:22:00.464Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460724, \"gpu\": [\"cuda:1\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed42.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T18:02:43.637Z\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T17:32:15.936Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 242264, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 45}, \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-17T17:32:15.936Z\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T17:29:34.723Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_scalar --max_correction_norm 0.1 --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --output_file logs/eval_object_scalar_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 224623, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed45.log\"}, \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}, \"completed_at\": \"2026-05-17T17:29:34.723Z\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T17:03:14.729Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --K 10 --seed 45 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:1\", \"pid\": 222824, \"seed\": 45, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"Perdof CRM norm=0.2 seed=45 on LIBERO object. Additional perdof data point for cross-seed comparison. Expected ~11% based on seed42 data.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\", \"completed_at\": \"2026-05-17T17:03:14.729Z\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T16:52:17.419Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"326081\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"submitted_at\": \"2026-05-17T08:36:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 29777.4, \"gpu_hours\": 8.27}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"checkpoint_path\": \"logs/eval_object_perdof_norm02_seed44.json\", \"completed_at\": \"2026-05-17T16:52:17.419Z\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:02:35.790Z\", \"updated_at\": \"2026-05-17T15:19:16.626Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --reuse_k10_cache --k10_cache_dir /root/autodl-tmp/crm_cache_v5/ --auto --no_wandb\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 456622, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/train_crm_k1_fallback.log\", \"submitted_at\": \"2026-05-17T15:02:35.104Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:4\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 4857, \"model_name\": \"crm_k1_accg_fallback\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/\", \"wall_clock_seconds\": 914.9, \"gpu_hours\": 0.25}, \"hypothesis\": \"CRM K=1 with ACCG architecture trained on K=10 single-stage cache (960D fallback) can learn effective corrections for object benchmark, achieving low val_loss comparable to multi-scale approach\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T15:17:49.965Z\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:48:22.459Z\", \"updated_at\": \"2026-05-17T14:53:10.162Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=0 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-object --auto\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"427856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42.log\", \"submitted_at\": \"2026-05-17T14:48:21.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"CRM_K1_ACCG_v2\", \"data_path\": \"LIBERO-Object precomputed K=1 features\", \"data_count\": -1, \"wall_clock_seconds\": 174.4, \"gpu_hours\": 0.05}, \"hypothesis\": \"K=1 CRM 训练（ACCG 架构）：使用 Action-Conditioned Correction Gating 替代 FiLM，多阶段 VLA 特征融合 + 组合损失函数（L2 + directional + triplet + magnitude），训练专用于 K=1 单采样纠正的 CRM。目标超越 K=1 VLA-only baseline (10.8%)。ACCG 用 action 本身计算动态 gate 选择 correction 维度。\", \"reproduce\": {\"finished_at\": \"2026-05-17T14:49:15.593Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:49:21.444858+00:00\"}]}, \"conclusion\": \"failed\", \"failure_reason\": \"LIBERO HDF5 demo data missing on bjb2-28827. Precompute requires raw demo trajectories but only K=10 cache exists.\", \"completed_at\": \"2026-05-17T14:51:16.090Z\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:34:09.564Z\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45.json 2>&1 | tee logs/eval_object_perdof_norm02_seed45.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"632156\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-deploy.log\", \"submitted_at\": \"2026-05-17T13:34:09.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1025.8, \"gpu_hours\": 0.28}, \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:47:18.573Z\"}, \"failure_reason\": \"**根因**: MuJoCo EGL 渲染初始化 segfault（native crash）。\\n\\n**证据**:\\n- tmux 日志和应用日志均在 `[eval] 10 tasks loaded.` 后中断，无 Python traceback、无 segfault handler 输出\\n- 代码中有 SIGSEGV handler 但未被触发，说明崩溃发生在 native code（MuJoCo/EGL）且 handler 未能执行\\n- 同服务器多个实验表现相同模式（eval_object_obs_only_norm03_seed47、eval_object_perdof_norm01_seed47 等均在 \\\"10 tasks loaded\\\" 后死亡）\\n- 非 OOM：系统 RAM 454GB 空闲，GPU VRAM 仅用 5.6GB/24GB\\n- 崩溃点：第一个 rollout_single() → env.reset() 触发 MuJoCo EGL context 创建\\n\\n**关键日志（最后一行有效输出）**:\\n`[eval] 10 tasks loaded.`\\n（之后无任何输出，进程静默死亡）\\n\\n**可能触发因素**: 4 张 GPU 同时运行 4 个 eval 进程，并发 EGL context 初始化存在 driver 层竞争。较早的单卡实验（seed44/45/46）正常完成。\\n\\n**建议**: PID 634438 已在 GPU 0 上重启并处于 Running 状态，等待其完成。若再次失败，考虑串行执行（不并发跑 4 个 EGL 进程）或降低并发数。\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:47:28.347997+00:00\"}]}, \"completed_at\": \"2026-05-17T13:51:14.936Z\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T13:31:57.433Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 588037, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T13:31:55.004Z\", \"notes\": \"Worker batch7 误杀, 4/10 tasks 完成\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T12:04:17.540Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed45_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"319463\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T21:33:52.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 45, \"wall_clock_seconds\": 48204.7, \"gpu_hours\": 13.39}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:54:49.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:54:55.730176+00:00\"}]}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:57:16.754Z\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:22:10.412Z\", \"updated_at\": \"2026-05-17T12:00:58.173Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 421086, \"seed\": 44, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-17T11:50:26.264Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T11:50:20.975Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:50:33.595081+00:00\"}]}, \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:56.645Z\", \"updated_at\": \"2026-05-17T11:50:09.879Z\", \"hypothesis\": \"obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 error bar。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed47.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 612853, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-17T11:50:06.763Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T11:50:09.879Z\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:28:13.840Z\", \"updated_at\": \"2026-05-17T11:36:55.536Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 392856, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T11:36:55.536Z\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed44.json\", \"server\": \"bjb1-18228\", \"gpu_id\": 1, \"model_name\": \"crm_perdof_norm01\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=44 on LIBERO object. Multi-seed magnitude curve: seed42=11%, expecting similar. Fills the biggest gap in perdof magnitude data (norm=0.1 only has 1 seed).\", \"pid\": 531963}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:48:36.650Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:48:39.951Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:48:45.826946+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 363223, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (killed duplicate)\", \"log_path\": \"N/A (killed duplicate)\"}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:42:47.471Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T10:42:49.632Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:42:53.924730+00:00\"}]}}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 365893, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:43:36.147Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:43:38.311Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:43:46.527772+00:00\"}]}}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_reconvla_seed47.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 322337, \"seed\": 47, \"model_name\": \"SmolVLA_argmin_K10\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:51:45.356Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:51:50.389646+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T10:54:02.630Z\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 2, \"model_name\": \"crm_perdof_norm01\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve: seed42=11%, seed44=deploying. 3rd seed for perdof low-norm baseline.\", \"pid\": 309151}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-17T10:22:14.184Z\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_perdof_norm01_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"388460\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:11.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"N/A (killed before completion)\", \"wall_clock_seconds\": 12316.3, \"gpu_hours\": 3.42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:19:28.338Z\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_reconvla_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"reconvla\", \"hypothesis\": \"argmin baseline K=10 seed=46 on LIBERO object. 5th seed for Fisher test. Pairs with eval-obs-only-object-norm02-seed46 (bjb1-18228:cuda:3).\", \"data_path\": \"\", \"data_count\": 0, \"checkpoint_source\": \"\", \"eval_data\": \"object\", \"pid\": 295478, \"log_path\": \"logs/eval_argmin_object_seed46.log\", \"checkpoint_path\": \"N/A (eval-only, reconvla baseline)\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed46.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:19:26.819Z\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"272762\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T15:24:08.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:3\", \"model_name\": \"crm_obs_only_norm03\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"wall_clock_seconds\": 56321.1, \"gpu_hours\": 15.64}, \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:00:25.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:00:32.829645+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:02:49.285Z\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"spec\": {\"model_name\": \"smolvla_libero_vla_mean\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 45 --output_file logs/eval_object_vla_mean_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"248652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:45Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 70783.9, \"gpu_hours\": 19.66}, \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:29:41.019Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T03:29:45.978517+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T06:54:28.933Z\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_argmin_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"215932\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed45.log\", \"submitted_at\": \"2026-05-16T07:45:06.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"reconvla_argmin_baseline\", \"hypothesis\": \"argmin baseline K=10 seed=45 on LIBERO object. 4th seed baseline for Fisher test. Paired with eval-obs-only-object-norm02-seed45.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 60530.4, \"gpu_hours\": 16.81}, \"reproduce\": {\"finished_at\": \"2026-05-17T00:31:27.579Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T00:31:32.330885+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval-only)\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\", \"completed_at\": \"2026-05-17T00:33:57.260Z\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"tmux_session\": \"eval-dc-r2\", \"note\": \"Code patched: print every rollout instead of every 5. Root cause of prev failures: workers killed working processes because output interval was 7.5min (5 rollouts x 90s each).\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_direct_correction_object_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}, \"completed_at\": \"2026-05-17T04:48:50.296Z\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"505419\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed44.log\", \"submitted_at\": \"2026-05-16T15:24:11.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:2\", \"model_name\": \"crm_perdof_norm03\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 48060.4, \"gpu_hours\": 13.35}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"reproduce\": {\"finished_at\": \"2026-05-17T04:41:11.191Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T04:41:18.547308+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}, \"completed_at\": \"2026-05-17T04:45:11.458Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"spec\": {\"parent\": \"eval-acr-object-v4-perdof\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.2, K=10, n_rollouts=10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"127732\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log\"}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:45.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:48.447852+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T07:12:35.145Z\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:07:28.510451+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:10:02.679Z\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:5\", \"pid\": 15190, \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:03:26.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:03:29.305763+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm02.log\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-15T16:06:23.063Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log\"}, \"gpu\": \"bjb2-28827:cuda:3\", \"pid\": 14260, \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:53:04.031Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:53:08.939326+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:17:49.711Z\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"gpu\": \"bjb2-28827:cuda:1\", \"pid\": 13456, \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:52:50.451Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:52:53.898813+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:24:59.482Z\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm003.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:0\", \"pid\": 13185, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:32:37.390Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:32:42.080703+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm003.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:40:16.878Z\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:12:39.100Z\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\", \"checkpoint_path\": \"N/A (eval experiment)\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"spec\": {\"hypothesis\": \"obs-only CRM with norm=0.2 on object benchmark. Cross-benchmark norm sensitivity test — paired with eval-mag-obsonly-norm02 on spatial. If obs-only at norm=0.2 > norm=0.1 on both benchmarks → robust 'observation-conditioned correction' story.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 44270, \"tmux_session\": \"eval-acr-object-obs-only-norm02\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark, 10 tasks x 10 rollouts\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\"}, \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:35:34.272Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:35:39.374197+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\", \"completed_at\": \"2026-05-15T17:37:08.420Z\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"123761\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v7.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T01:45:58.391Z\", \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T03:10:30.457Z\", \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 2 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"180480\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard2.log\", \"submitted_at\": \"2026-05-14T07:56:37.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 2 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5491.8, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:09.308Z\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 1 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"180400\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard1.log\", \"submitted_at\": \"2026-05-14T07:56:35.789Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 1 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5492.1, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:07.934Z\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 0 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"180251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard0.log\", \"submitted_at\": \"2026-05-14T07:56:33.414Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 0 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5493.2, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:06.626Z\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"69937\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard2.log\", \"submitted_at\": \"2026-05-13T18:58:14.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173960.7, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:09:25.582Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:09:26.379476+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:35.000Z\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"69793\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log\", \"submitted_at\": \"2026-05-13T18:58:12.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173961.1, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:22.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:23.366356+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:33.288Z\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"69647\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log\", \"submitted_at\": \"2026-05-13T18:58:09.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173962.3, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:45.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:50.222546+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:32.128Z\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:32:23.773Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T11:07:49.901Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:14.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:15.524386+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:07:51.915540+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"118108\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean argmin)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"SampleConsensus scalar baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"186964\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"submitted_at\": \"2026-05-14T09:30:43.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM scalar-unc v2 (327K params, 8D state fix)\", \"seed\": 42, \"hypothesis\": \"Scalar CRM v2 ablation — per-DOF expected to outperform on task success rate despite similar val_loss\", \"wall_clock_seconds\": 9977.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"completed_at\": \"2026-05-14T12:17:01.093Z\", \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"186823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"submitted_at\": \"2026-05-14T09:30:40.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM per-DOF v2 (337K params, 8D state fix, argmin base, L2 clip)\", \"seed\": 42, \"hypothesis\": \"Per-DOF CRM v2 with D016 fixes (8D state, argmin base, alpha=0.5, L2 clipping) improves over pre-fix version\", \"wall_clock_seconds\": 9979.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"completed_at\": \"2026-05-14T12:17:00.195Z\", \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"187913\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"submitted_at\": \"2026-05-14T09:41:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM obs_only v2\", \"seed\": 42, \"wall_clock_seconds\": 9366.4, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"completed_at\": \"2026-05-14T12:17:42.122Z\", \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"47186\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard2.log\", \"submitted_at\": \"2026-05-13T11:57:48.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.4, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:07.463Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"47044\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard1.log\", \"submitted_at\": \"2026-05-13T11:57:46.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.8, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:06.485Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"46966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard0.log\", \"submitted_at\": \"2026-05-13T11:57:45.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12500.2, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:05.433Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:09:33.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:09:34.396952+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"completed_at\": \"2026-05-13T22:12:39.543Z\", \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial object --n_rollouts 20 --seed 42\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"50790\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_014-reconvla-baseline.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"20 tasks x 20 rollouts = 400 episodes\", \"model_name\": \"SmolVLA (450M) + ReconVLA argmin selection\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin selection) as baseline for ACR-VLA comparison\", \"fixes_applied\": [\"BDDL path: use benchmark_instance.get_task_bddl_file_path()\", \"LIBERO assets copied from GitHub repo\"]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T11:07:20.019Z\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --auto --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --K 10\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32811\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_001-crm-smolvla.log\", \"submitted_at\": \"2026-05-13T04:54:14.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": 1000, \"model_name\": \"CRM (337K) + SmolVLA (450M)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\", \"hypothesis\": \"Per-DOF conformal features enable dimension-selective action correction on LIBERO\", \"wall_clock_seconds\": 2992.2, \"gpu_hours\": 0.83}, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-13T05:44:07.131Z\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"43809\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)\", \"seed\": 42, \"hypothesis\": \"Validate smolvla_libero checkpoint with fixed wrapper (correct state repr, 256x256 images, 7D action) achieves >50% success on libero_spatial\", \"log_path\": \"/tmp/eval_spatial_full.log\", \"checkpoint_source\": \"lerobot/smolvla_libero (HuggingFace community checkpoint)\", \"failure_reason\": \"smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization, state 6D→8D, state normalization, action denormalization all missing\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T15:45:51.082Z\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"197596\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log\", \"submitted_at\": \"2026-05-14T12:17:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D input, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"evaluate.py has no crm_obs_only mode. --mode acr_vla loads CRM expecting 1030D input but obs_only checkpoint has 990D (no conformal features). Replaced by eval-obs-only-spatial-v2.\", \"wall_clock_seconds\": 1392.5, \"gpu_hours\": 0.39}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"completed_at\": \"2026-05-14T12:40:23.205Z\", \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"229751\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:13:41.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 48315.0, \"gpu_hours\": 13.42}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:36:24.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:36:28.363366+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T20:38:56.577Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"gpu\": \"1\", \"pid\": 109650, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object (10 tasks x 10 rollouts)\", \"log_path\": \"logs/nohup_eval_object_perdof_norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:33.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:36:35.355Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:40.842032+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"144504\"}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:39:30.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:39:33.739829+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm02_seed43_r3.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:41:59.362Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 140759, \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:10:32.044Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:10:33.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:10:39.747200+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:08.945Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"wall_clock_seconds\": 70039.8, \"gpu_hours\": 19.46}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\", \"completed_at\": \"2026-05-16T00:48:05.254Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:35:42.126Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:35:43.889Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:35:47.235304+00:00\"}]}, \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}, \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"logs/eval_object_obs_only_norm005.json\", \"completed_at\": \"2026-05-16T08:19:41.189Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"note\": \"Code patched to print every rollout (was every 5). Prev attempts killed working processes due to misinterpreting silence as stuck.\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T02:58:54.670Z\"}, \"failure_reason\": \"Agent误杀：wchar未增长30s被误判为stuck，实际是每5 rollout打印一次（~7.5min间隔）且MuJoCo/CUDA使用memory-mapped I/O不被/proc/PID/io追踪。进程实际正常运行中。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:58:57.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T02:59:01.101476+00:00\"}]}}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"1\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"obs_only CRM v3-norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"pid\": 353384, \"tmux_session\": \"eval-direct-correction-object-seed42\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:38:55.611Z\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"226878\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T07:11:59.066Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_scalar_unc\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 51470.5, \"gpu_hours\": 14.3}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:11:40.494Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:11:48.900516+00:00\"}]}, \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-16T21:29:49.586Z\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:04.525Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 44 --n_rollouts 10 --output_file logs/eval_object_perdof_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:13:35.112Z\", \"training_hours\": 13.28}, \"spec\": {\"data_path\": \"LIBERO_object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\"}, \"pid\": \"452982\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:13:38.573783+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:27.956Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"501420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log\", \"submitted_at\": \"2026-05-16T14:49:19.300Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"pid\": 501420, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T15:21:56.018Z\", \"failure_reason\": \"r2 data valid (16%), r4 redundant. PID 501420 killed by worker at 2026-05-16T15:09.\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:32:36.214Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T15:28:27.588Z\", \"training_hours\": 13.93}, \"completed_at\": \"2026-05-16T01:34:17.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:28:32.358640+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"428117\", \"seed\": 44, \"model_name\": \"reconvla_argmin\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"spec\": {\"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"248860\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:47Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 972.5, \"gpu_hours\": 0.27}, \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\", \"failure_reason\": \"killed to resolve cuda:3 GPU conflict\", \"completed_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"390936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log\", \"submitted_at\": \"2026-05-16T02:11:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 24535.3, \"gpu_hours\": 6.82}, \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 105938, \"log_path\": \"logs/eval_object_perdof_norm003.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"parent\": \"eval-acr-object-v4-perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.14, \"per_task_range\": \"0.0-0.4\"}}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:09:00.286Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:09:03.327886+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\", \"completed_at\": \"2026-05-16T08:11:39.117Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 134094, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log\", \"submitted_at\": \"2026-05-15T17:38:21.517Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"wall_clock_seconds\": 48640.4, \"gpu_hours\": 13.51}, \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:19.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:22.516205+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"114664\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log\", \"submitted_at\": \"2026-05-15T16:03:30.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_scalar\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 50435.3, \"gpu_hours\": 14.01}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:01:42.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:01:45.993724+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"completed_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 121325, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10\", \"parent\": \"eval-acr-object-v4-obs-only\"}, \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:35:17.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:35:20.742243+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:02:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T05:05:30.084Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"310854\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"submitted_at\": \"2026-05-16T05:25:05.983Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"309346\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:05:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:05:34.587431+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"431189\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:30.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.0, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:20.095Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"430985\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:27.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.3, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"111709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log\", \"submitted_at\": \"2026-05-15T15:47:37.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"libero/object\", \"data_count\": 10, \"checkpoint_source\": null, \"eval_data\": \"object\", \"wall_clock_seconds\": 47139.2, \"gpu_hours\": 13.09}, \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:48:28.380Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:48:31.493092+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_object_perdof_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 365925, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log\", \"submitted_at\": \"2026-05-15T13:21:00.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO_object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 50078.9, \"gpu_hours\": 13.91}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:12:36.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:12:39.589841+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:29:36.987Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T01:30:26.640Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127 (command not found) — bash -c wrapping 或环境激活路径错误，bjb2-40593 上系统性问题，三个 seed44 实验全部同样失败\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:33.143Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:38.635650+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:29:31.218Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:14.217Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:20.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:23.773246+00:00\"}]}}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:29:25.990Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:04.115Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (argmin baseline)\", \"seed\": 44, \"checkpoint_source\": \"N/A (no CRM)\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:06.598Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:09.864458+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356490\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"submitted_at\": \"2026-05-15T12:00:38.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 46070.8, \"gpu_hours\": 12.8, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:41:25.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:42:01.902179+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"completed_at\": \"2026-05-16T00:48:29.446Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20250.8, \"gpu_hours\": 5.63}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}, \"completed_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"356696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log\", \"submitted_at\": \"2026-05-15T12:00:40.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (reconvla baseline)\", \"seed\": 43, \"checkpoint_source\": \"N/A (no CRM, pure VLA baseline)\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 45422.6, \"gpu_hours\": 12.62}, \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:35:16.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:19.825582+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"138858\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T19:19:36.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed — GPU conflict on cuda:2, replaced by eval-mag-perdof-norm02-seed43-object-r3)\", \"wall_clock_seconds\": 951.1, \"gpu_hours\": 0.26}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:35:27.220Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T06:44:02.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (EXIT_CODE=127, retried as eval-mag-obsonly-norm03-r2)\", \"wall_clock_seconds\": 46287.3, \"gpu_hours\": 12.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:44:32.019Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:44:35.317393+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\", \"completed_at\": \"2026-05-15T19:35:29.718Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 141024, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"checkpoint_path\": \"N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"132816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log\", \"submitted_at\": \"2026-05-15T19:14:01.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 809.4, \"gpu_hours\": 0.22}, \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"134532\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log\", \"submitted_at\": \"2026-05-15T19:14:52.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 755.5, \"gpu_hours\": 0.21}, \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. Paired with obs_only norm=0.2 seed=43 for statistical comparison at the best obs_only norm.\", \"parent\": \"eval-mag-perdof-norm02-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\", \"completed_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Retry of killed eval-mag-perdof-norm0p3-object. Completes perdof 5-point magnitude curve on object domain.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\", \"completed_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"7017\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log\", \"submitted_at\": \"2026-05-15T02:55:02.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58959.5, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"6746\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log\", \"submitted_at\": \"2026-05-15T02:54:59.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58960.3, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"69379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log\", \"submitted_at\": \"2026-05-13T18:58:07.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D015: evaluate.py env_args 缺少 camera_names，SmolVLA 只收到单摄像头输入，结果系统性偏低\", \"wall_clock_seconds\": 173971.8, \"gpu_hours\": 48.33}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-13T19:36:15.749Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:36:19.370112+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:26:37.521060+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:59:44.694612+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"63218\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard2.log\", \"submitted_at\": \"2026-05-13T17:39:04.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178705.9, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"63075\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard1.log\", \"submitted_at\": \"2026-05-13T17:39:02.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178706.7, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:29.293Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && rm -rf /root/autodl-tmp/crm_cache_v3 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"62930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard0.log\", \"submitted_at\": \"2026-05-13T17:39:00.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178707.5, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"57846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard2.log\", \"submitted_at\": \"2026-05-13T16:11:04.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.1, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"57706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard1.log\", \"submitted_at\": \"2026-05-13T16:11:02.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.5, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && rm -rf /root/autodl-tmp/crm_cache/spatial /root/autodl-tmp/crm_cache/object && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"57628\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard0.log\", \"submitted_at\": \"2026-05-13T16:11:01.605Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.0, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"127570\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log\", \"submitted_at\": \"2026-05-15T18:58:29.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"crm_perdof_v3_norm\", \"seed\": 42, \"wall_clock_seconds\": 885.6, \"gpu_hours\": 0.25}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:13:15.247Z\", \"failure_reason\": \"Duplicate of eval-mag-perdof-norm03-object (PID 118886 on bjb2-28827:cuda:3, identical params). Killed to free cuda:2.\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"144887\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log\", \"submitted_at\": \"2026-05-15T18:37:26.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1245.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\", \"failure_reason\": \"GPU conflict on bjb1-32546:cuda:4 (shared with obs-only-default). Killed lower priority perdof. Migrating to bjb2-28827:cuda:2 as r2.\", \"completed_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43.json\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Crashed after 1 task on bjb1-32546:cuda:3 (PID 118214). Reviewer confirmed. Restarting as r2.\", \"completed_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"107658\", \"log_path\": \"logs/eval_object_perdof_default_norm.log\", \"submitted_at\": \"2026-05-16T00:51:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 325264, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"submitted_at\": \"2026-05-15T06:50:02.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 37969.2, \"gpu_hours\": 10.55}, \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:20:31.567Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:20:34.907634+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"completed_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"spec\": {\"command\": \"python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\"}, \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\", \"gpu\": \"bjb1-32546:cuda:5\", \"pid\": 18808, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\", \"completed_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\", \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\"}, \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"13797\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"submitted_at\": \"2026-05-15T02:53:41.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47312.8, \"gpu_hours\": 13.14}, \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:59:31.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:59:34.042176+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:14.366Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"11116\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log\"}, \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --start_task 3\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 311881, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log\", \"submitted_at\": \"2026-05-15T05:14:33.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 70, \"model_name\": \"ACR-VLA CRM scalar_unc v3-norm (restart from T3)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 3-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 29034.3, \"gpu_hours\": 8.07}, \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:15:46.765Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:49.226583+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:18:27.853Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 312420, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"submitted_at\": \"2026-05-15T05:14:38.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 40, \"model_name\": \"ACR-VLA CRM obs_only v3-norm (restart from T6)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 6-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 21633.2, \"gpu_hours\": 6.01}, \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:15:39.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:15:44.340640+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"completed_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_spatial_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"341873\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-15T09:09:23.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 3117.4, \"gpu_hours\": 0.87}, \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_task 7\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 312150, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"submitted_at\": \"2026-05-15T05:14:36.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 30, \"model_name\": \"ACR-VLA CRM perdof v3-norm (restart from T7)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 7-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"wall_clock_seconds\": 14053.7, \"gpu_hours\": 3.9}, \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:05:27.552Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:05:31.321347+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"completed_at\": \"2026-05-15T09:08:50.017Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"N/A (stale duplicate entry)\", \"server\": \"bjb1-18228\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (stale duplicate entry, never ran)\", \"log_path\": \"N/A\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\", \"completed_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"329871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"submitted_at\": \"2026-05-15T07:11:15.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 360.6, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\", \"checkpoint_path\": \"N/A (killed before completion)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"completed_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint output)\", \"completed_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": 225144, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45Z\", \"submitted_via\": \"tmux (manual)\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:32:10.962Z\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --baseline_mode single --benchmark object --n_rollouts 10 --seed 42 --K 1 --output_file logs/eval_object_vla_only_k1.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"39397\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log\", \"submitted_at\": \"2026-05-15T05:11:22.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only K=1 single sample)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_source\": \"N/A (no CRM, single VLA sample)\", \"wall_clock_seconds\": 311.9, \"gpu_hours\": 0.09}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:16:34.574Z\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"212685\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log\", \"submitted_at\": \"2026-05-15T01:49:35.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, default max_correction_norm)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 6030.8, \"gpu_hours\": 1.68}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:31:26.353Z\", \"failure_reason\": \"D021: v2 checkpoint invalidated by crm_cache_v5 retraining. Replaced by eval-acr-spatial-v4-scalar on bjb1:2.\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"203217\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log\", \"submitted_at\": \"2026-05-14T22:29:03.489Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\", \"failure_reason\": \"Superseded by D020 plan. Default norm=1.42 already proven to degrade (v4-default: 0/5). Not needed. Process killed on bjb2 (PID 203222 confirmed dead).\", \"completed_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3 obs_only, default max_correction_norm=1.42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log\", \"tmux_session\": \"eval-acr-spatial-v4-obs-only\", \"pid\": 199257}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:16:04.414Z\", \"failure_reason\": \"Wrong checkpoint (crm_v3 not crm_v3_norm) + wrong max_correction_norm (1.42 not 0.1). Killed and replaced by eval-acr-spatial-v4-obs-only-r2.\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, default correction)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Process died. D019: 0/5 on task 1 confirmed default norm=1.42 still degrades. Replaced by eval-acr-spatial-v4-obs-only on cuda:0.\", \"completed_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (scalar_unc)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"/tmp/crm_train_scalar_unc.log\", \"completed_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (obs_only)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/tmp/crm_train_obs_only.log\", \"completed_at\": \"2026-05-14T22:05:28.289Z\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-337K-Normalized\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"no log file (tee failed, output was in tmux pane only)\", \"completed_at\": \"2026-05-14T20:05:20.181Z\", \"results\": {\"best_epoch\": 47, \"best_val_loss\": 0.03578, \"final_train_loss\": 0.04992, \"final_val_loss\": 0.03578, \"total_epochs\": 50, \"normalization\": \"per-feature input normalization (mean/std stored in crm_best.pt as input_mean/input_std tensors)\"}}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181896\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-scalar-unc.log\", \"submitted_at\": \"2026-05-14T18:05:00.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1917.7, \"gpu_hours\": 0.53}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:15.107Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:19.071535+00:00\"}]}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:36:58.566Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181973\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"submitted_at\": \"2026-05-14T18:05:02.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/spatial\", \"data_count\": 2402, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1802.8, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:22.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:25.410071+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"completed_at\": \"2026-05-14T18:35:05.626Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181668\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"submitted_at\": \"2026-05-14T18:04:54.446Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1510.3, \"gpu_hours\": 0.42}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:11.506Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:13.038696+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:30:04.713Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"211961\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:49:43.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:2 for eval-tiny-correction-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"wall_clock_seconds\": 17890.8, \"gpu_hours\": 4.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"197324\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:17:08.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"CRM v2 scalar-uncertainty + SmolVLA K=10\", \"seed\": 42, \"hypothesis\": \"Scalar uncertainty CRM ablation — tests whether per-DOF conformal is superior to scalar aggregated uncertainty for action correction.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:1 for eval-argmin-only-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"wall_clock_seconds\": 19844.9, \"gpu_hours\": 5.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:53.188Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"121984\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty)\", \"seed\": 42, \"hypothesis\": \"CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001 (bs=32/lr=1e-3).\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"conclusion_note\": \"Training converged. scalar val_loss 0.008379 < per-DOF 0.009046 — original hypothesis (scalar w
```

---

### Large event (continued)

````text
orse) NOT confirmed on val_loss. Hypothesis pending eval-scalar-unc-spatial task success rate validation.\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}, \"completed_at\": \"2026-05-14T02:21:00.891Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 --input_mode obs_only --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-obs_only\", \"seed\": 42, \"hypothesis\": \"CRM without conformal features (obs_only, 990D input) performs significantly worse than full CRM (1030D), validating that per-DOF conformal features are necessary for effective correction\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:43:51.534Z\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"78520\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v1.log\", \"data_path\": \"/root/autodl-tmp/crm_cache/ (spatial: 12167 + object: 14570 = 26737 samples)\", \"data_count\": 26737, \"model_name\": \"CRM MLP (337K params, 1030D→256→256→30D)\", \"seed\": 42, \"hypothesis\": \"CRM with per-DOF conformal features (1030D input) learns dimension-selective correction, achieving lower action MSE than scalar/no-uncertainty ablations\", \"checkpoint_source\": \"precompute-v4 (spatial+object)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:40:27.930Z\"}, \"failure_reason\": \"RESOLVED: EXIT_CODE=129 was SIGHUP after training completed (50/50 epochs). Not a real failure.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T22:40:28.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:40:29.429643+00:00\"}]}, \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ --output_dir /root/autodl-tmp/checkpoints/crm/k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"139839\", \"data_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"data_count\": 26737, \"model_name\": \"CRM (K=5, 337K params)\", \"seed\": 42, \"hypothesis\": \"CRM with K=5 conformal samples for K sensitivity ablation (K=10 baseline val_loss=0.009046)\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/k5/train.log\", \"checkpoint_source\": \"from_scratch\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:12:42.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:12:44.286094+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}, \"completed_at\": \"2026-05-14T07:21:32.072Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"spec\": {\"hypothesis\": \"Scalar CRM (3D unc) vs per-DOF CRM (40D unc) on spatial task success rate. Val_loss favored scalar (0.008 vs 0.009) but per-DOF expected to win on task success via dimension-selective correction.\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty, 327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"143206\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch). Scalar CRM trained on wrong features. Replaced by eval-scalar-unc-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:15.933Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:31:30.005Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:31:31.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:31:32.734610+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"117814\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM per-DOF)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log\", \"hypothesis\": \"ACR-VLA per-DOF correction improves over SmolVLA baseline on spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM trained on wrong features + CGS quantile wrong. Replaced by eval-acr-spatial-v3.\"}, \"conclusion\": \"killed\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"spec\": {\"command\": \"MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"154189\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA K=5 (CRM 337K + SmolVLA 450M)\", \"seed\": 42, \"hypothesis\": \"K=5 vs K=10 ACR-VLA on task success rate.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-k5-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM K=5 trained on wrong features. Replaced by eval-k5-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:14.685Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (single inference per step)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\", \"failure_reason\": \"Duplicate entry — same PID 125830 tracked by eval-object-v8-full. Cleaning up.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:03:28.470Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:09.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:11.481851+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:03:30.351859+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"117486\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v6-full.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with fixed evaluate.py (reset→set_init_state→zero-action)\", \"failure_reason\": \"vla_only mode running K=10 instead of K=1, wasting GPU. Killed and restarted with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:43:52.899Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T23:43:53.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:43:56.187212+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 117697, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"gpu\": \"cuda:0\", \"note\": \"restored from false DONE/failed — cron misdetected tmux pipe buffering as process exit\", \"failure_reason\": \"vla_only mode running K=10 multi-sampling (should be K=1). Killed by Director order, replaced by eval-object-v7-full with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/acr_vla_spatial_v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO spatial benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM perdof)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial, 10 tasks x 10 rollouts\", \"parent\": \"train-crm-v1\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信。已被 eval-acr-spatial-v2 替代\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:13:00.422Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-acr-spatial-v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:38.077Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:40.252Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified-deployed wrapper achieves meaningful success rate on libero_object\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.017Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"73756\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified wrapper + dual camera (agentview + eye_in_hand) achieves >50% on libero_spatial\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.445Z\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"62654\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log\", \"submitted_at\": \"2026-05-13T17:38:57.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, rewritten wrapper aligned with lerobot pipeline)\", \"seed\": 42, \"hypothesis\": \"Rewritten wrapper (fully aligned with lerobot SmolVLAPolicy) achieves >50% on libero_spatial with 10 rollouts\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 5403.4, \"gpu_hours\": 1.5}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"87385\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned)\", \"seed\": 42, \"hypothesis\": \"Fixed wrapper (7 bugs) achieves >50% on libero_spatial\", \"log_path\": \"/tmp/eval_spatial.log\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"Killed by Director - wrapper not fully fixed, 55.6% result unreliable. Redirected to full wrapper rewrite aligned with lerobot pipeline.\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T16:14:40.934Z\"}}, \"count\": 850, \"total\": 850, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.491}}"
    }
  }
}
```

&lt;/details>

---


````

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The registry is too large. Let me search for Goal and Object related experiments specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "b5776437-44ae-466a-89bc-097c2562714b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8HKoqxpPdvfwrsDvyQ8go",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 24810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
      },
      "output_tokens": 8,
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


### Assistant

_source line 10_

Registry too large. Let me filter for Goal and Object experiments specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "23206cef-fadd-4601-a7da-db8065dd74b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8HKoqxpPdvfwrsDvyQ8go",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 24810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
      },
      "output_tokens": 8,
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01JAcC1M3C9NNWmeiNX7UskJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/mcp-agent-ml-research-read_registry-1779674475741.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\n# Filter for goal and object related experiments\nfor exp in data:\n    exp_id = exp.get('experiment_id','')\n    name = exp.get('name','')\n    conclusion = exp.get('conclusion','')\n    lower = (exp_id + name + conclusion).lower()\n    if 'goal' in lower or 'object' in lower:\n        print(f'ID: {exp_id}')\n        print(f'  name: {name}')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  server: {exp.get(\\\"server\\\")}')\n        print(f'  conclusion: {conclusion[:200]}')\n        metrics = exp.get('metrics', {})\n        if metrics:\n            print(f'  metrics: {json.dumps(metrics)[:300]}')\n        print()\n\" 2>&1 | head -500",
  "description": "Filter registry for Goal/Object experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "7f3f759d-6aa5-4144-beda-877e6255b53f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8HKoqxpPdvfwrsDvyQ8go",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 24810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
      },
      "output_tokens": 8,
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

_source line 12 · 2026-05-25T02:01:25.726Z_

<details><summary>↩ Tool result · `toolu_01JAcC1M3C9NNWmeiNX7UskJ`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    exp_id = exp.get('experiment_id','')
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "2b3fda08-3cd7-42b2-ab77-50dab0758306",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    exp_id = exp.get('experiment_id','')\n             ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
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

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_016LmhTJh3fuhvEdBdkMt35W`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/mcp-agent-ml-research-read_registry-1779674475741.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nparsed = json.loads(raw)\nresult = parsed['result']\n# Check type\nif isinstance(result, str):\n    data = json.loads(result)\nelse:\n    data = result\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    if data:\n        print(f'First item type: {type(data[0])}')\n        if isinstance(data[0], dict):\n            print(f'Keys: {list(data[0].keys())}')\n            print(json.dumps(data[0], indent=2)[:500])\n        else:\n            print(f'First item: {str(data[0])[:200]}')\nelif isinstance(data, dict):\n    print(f'Dict keys: {list(data.keys())}')\n\"\n",
  "description": "Inspect registry data structure",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "72284d5d-5b47-49a6-8289-6eecb1ce2199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbQsysFz6UaCdmHVVWGgh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 25355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
      },
      "output_tokens": 58,
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

_source line 14 · 2026-05-25T02:01:32.764Z_

<details><summary>↩ Tool result · reported error · `toolu_016LmhTJh3fuhvEdBdkMt35W`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    parsed = json.loads(raw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "74841d85-2d1c-42e6-9b83-7e519f1e3e87",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 4, in &lt;module>\n    parsed = json.loads(raw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 361, in raw_decode\n    obj, end = self.scan_once(s, idx)\n               ~~~~~~~~~~~~~~^^^^^^^^\njson.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)"
}
```

</details>

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_013Ps2yiekT2amLnMnWPDw6p`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/mcp-agent-ml-research-read_registry-1779674475741.txt",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "d2fafe13-1829-4b36-a3ba-99fd8413bbb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DecBiY6HQyjK7xZ5bMxcvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 25911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 650
      },
      "output_tokens": 53,
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

_source line 16 · 2026-05-25T02:01:37.071Z_

<details><summary>↩ Tool result · reported error · `toolu_013Ps2yiekT2amLnMnWPDw6p`</summary>

```text
File content (513193 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "4aad4ffd-20f3-4279-8449-5850bde19e19",
  "tool_use_result": "Error: File content (513193 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_012kKp4xgn3EoCfyrYodxHLu`</summary>

```json
{
  "command": "dd if=/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/mcp-agent-ml-research-read_registry-1779674475741.txt bs=1 count=500 2>/dev/null",
  "description": "Read first 500 bytes of registry output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "4477650a-3bf3-4a85-9d4a-753d50ed1b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQMJsmthCNSx9ggmyDrrou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 26561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 226
      },
      "output_tokens": 70,
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

_source line 18 · 2026-05-25T02:01:40.354Z_

<details><summary>↩ Tool result · `toolu_012kKp4xgn3EoCfyrYodxHLu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T21:37:23.017Z\", \"updated_at\": \"2026-05-25T01:04:28.781Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\", \"spec\": {\"command\": \"python evaluate.py --mode adaptive_conformal_crm --K 2 --conform
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "3b5a6121-4cee-4e57-b9e7-744434751f80",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-k2-tau020-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T21:37:23.017Z\\\", \\\"updated_at\\\": \\\"2026-05-25T01:04:28.781Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode adaptive_conformal_crm --K 2 --conform",
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_019rvPXwYFU6DZgNkN8u6Mtr`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/mcp-agent-ml-research-read_registry-1779674475741.txt') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\n\n# Filter for goal/object\nfor eid, exp in exps.items():\n    lower_id = eid.lower()\n    lower_hyp = (exp.get('hypothesis','') or '').lower()\n    lower_conc = (exp.get('conclusion','') or '').lower()\n    \n    if 'goal' in lower_id or 'object' in lower_id:\n        server = exp.get('spec',{}).get('server','?')\n        metrics = exp.get('metrics',{})\n        print(f'{eid} | server={server} | metrics={json.dumps(metrics)[:200]}')\n\" 2>&1",
  "description": "Parse registry and find Goal/Object experiments",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "4ed8ae84-3cc5-4e74-a51f-5b159d5ffadd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrEqUWr7xcQUk7mh9DH2rv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 26787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 20 · 2026-05-25T02:01:46.996Z_

<details><summary>↩ Tool result · `toolu_019rvPXwYFU6DZgNkN8u6Mtr`</summary>

```text
&lt;persisted-output>
Output too large (62.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/bijarzrz0.txt

Preview (first 2KB):
Total experiments: 850
eval-pi05-vla-only-object-s44 | server=bjb1-32546 | metrics={"overall_success_rate": 0.81, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-object-s43 | server=bjb1-32546 | metrics={"overall_success_rate": 0.815, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-goal-s43 | server=bjb1-32546 | metrics={"overall_success_rate": 0.97, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-goal-s42 | server=bjb1-32546 | metrics={"overall_success_rate": 0.955, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-object-s42 | server=bjb1-32546 | metrics={"overall_success_rate": 0.965, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}
eval-supp-crm-norm005-goal-s48 | server=bjb2-28827 | metrics={"overall_success_rate": 0.8, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "crm_obs_only", "max_correction_norm": 0.05, "K": 10}
eval-supp-goal-vla-only-s42-bjb1 | server=bjb1-32546 | metrics={}
crm-norm005-goal-s49 | server=bjb1-18228 | metrics={}
crm-norm005-object-s48 | server=bjb1-18228 | metrics={}
eval-supp-goal-vla-only-s50 | server=cqa1-32758 | metrics={}
eval-supp-goal-vla-only-s44 | server=cqa1-32758 | metrics={}
eval-supp-goal-vla-only-s43 | server=cqa1-32758 | metrics={}
eval-supp-goal-vla-only-s42 | server=cqa1-32758 | metrics={}
eval-supp-vla-only-goal-s49 | server=cqa1-32758 | metrics={"overall_sr": 0.82, "per_task_sr": {"middle_drawer": 0.75, "bowl_stove": 0.95, "wine_cabinet": 0.85, "drawer_bowl": 0.65, "bowl_cabinet": 0.95, "push_plate": 0.85, "cream_cheese": 0.55, "stove_on": 1
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
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "6cda7f5d-2053-44ee-ad8c-04a2c0901c3d",
  "tool_use_result": {
    "stdout": "Total experiments: 850\neval-pi05-vla-only-object-s44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-object-s43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-goal-s43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-goal-s42 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-object-s42 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-supp-crm-norm005-goal-s48 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}\neval-supp-goal-vla-only-s42-bjb1 | server=bjb1-32546 | metrics={}\ncrm-norm005-goal-s49 | server=bjb1-18228 | metrics={}\ncrm-norm005-object-s48 | server=bjb1-18228 | metrics={}\neval-supp-goal-vla-only-s50 | server=cqa1-32758 | metrics={}\neval-supp-goal-vla-only-s44 | server=cqa1-32758 | metrics={}\neval-supp-goal-vla-only-s43 | server=cqa1-32758 | metrics={}\neval-supp-goal-vla-only-s42 | server=cqa1-32758 | metrics={}\neval-supp-vla-only-goal-s49 | server=cqa1-32758 | metrics={\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1\neval-supp-vla-only-goal-s48 | server=cqa1-32758 | metrics={\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl\neval-supp-goal-vla-only-s45 | server=bjb2-28827 | metrics={\"SR\": 0.835}\neval-pi05-vla-only-object-seed43-r4 | server=bjb1-18228 | metrics={\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}\neval-a1-baseline-object-s42 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.565, \"total_successes\": 113, \"total_episodes\": 200, \"official_reported_sr\": 0.998, \"gap_vs_official\": -0.433, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.35, \"sala\neval-supp-goal-k2mean-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}\neval-supp-goal-adapt-tau025-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29\neval-supp-goal-crm-norm005-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}\neval-supp-goal-reconvla-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-supp-goal-vla-only-s47-r3 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}\nprecompute-pi05-object-2048-r2 | server=bjb1-18228 | metrics={\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}\neval-openvla-object-vla-only-seed42-v3 | server=bjb2-28827 | metrics={}\ntrain-crm-pi05-goal-k1 | server=bjb1-18228 | metrics={\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}\neval-supp-goal-vla-only-s47-r2 | server=bjb1-18228 | metrics={}\neval-supp-goal-vla-only-s47 | server=bjb1-18228 | metrics={}\ncrm-train-openvla-k1-multiscale-object | server=bjb2-28827 | metrics={\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}\nprecompute-pi05-goal-2048-r2 | server=bjb1-18228 | metrics={}\nprecompute-smolvla-goal-bjb1-32546 | server=bjb1-32546 | metrics={}\neval-supp-goal-vla-only-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-reconvla-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}\neval-perdof-object-norm003-seed44 | server=bjb1-18228 | metrics={\"success_rate\": 11, \"successes\": 11, \"total\": 100}\neval-supp-goal-vla-only-wrapper-s44 | server=bjb1-32546 | metrics={\"success_rate\": 82, \"successes\": 164, \"total\": 200}\neval-pi05-vla-only-object-seed42 | server=bjb1-32546 | metrics={\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-pi05-vla-only-object-seed43 | server=bjb1-32546 | metrics={\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-pi05-vla-only-object-seed44 | server=bjb1-32546 | metrics={\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-supp-goal-k2mean-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-adapt-tau025-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-crm-norm005-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-k2mean-s45 | server=cqa1-32758 | metrics={\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_insi\neval-supp-goal-reconvla-s45 | server=bjb2-28827 | metrics={\"SR\": 0.855}\neval-supp-goal-crm-norm005-s45 | server=? | metrics={\"success_rate\": 81, \"successes\": 162, \"total\": 200}\neval-supp-goal-adapt-tau025-s45 | server=bjb1-32546 | metrics={\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}\neval-ablation-tau040-goal-s42 | server=bjb2-28827 | metrics={\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}\neval-ablation-tau015-goal-s42 | server=bjb2-28827 | metrics={\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}\neval-supp-k2mean-object-s44 | server=cqa1-32758 | metrics={\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudd\neval-ablation-tau010-goal-s42 | server=bjb2-28827 | metrics={\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}\neval-supp-goal-vla-only-wrapper-s44-r2 | server=bjb1-32546 | metrics={\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_pl\neval-supp-k2mean-goal-s44 | server=bjb1-32546 | metrics={\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wi\neval-supp-goal-vla-only-wrapper-s43 | server=bjb1-32546 | metrics={\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \neval-supp-goal-reconvla-s44 | server=bjb2-28827 | metrics={\"success_rate\": 0.805, \"total_rollouts\": 200, \"total_successes\": 161, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.81, 0.81, 0.805], \"mean\": 0.8083, \"std\": 0.0029}}\neval-supp-crm-norm005-goal-s44 | server=bjb2-28827 | metrics={\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}\neval-supp-k2mean-object-s43 | server=cqa1-32758 | metrics={\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"toma\neval-supp-k2mean-goal-s42-r2 | server=bjb2-40593 | metrics={\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"op\neval-supp-adapt-tau025-goal-s44 | server=bjb1-32546 | metrics={\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}\neval-supp-adapt-tau025-goal-s43 | server=bjb1-32546 | metrics={\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}\neval-supp-crm-norm005-goal-s43 | server=bjb1-32546 | metrics={\"success_rate\": 0.82}\neval-supp-goal-reconvla-s43 | server=cqa1-32758 | metrics={\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.65, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bott\neval-supp-k2mean-goal-s43 | server=cqa1-32758 | metrics={\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"\neval-supp-k2mean-object-s42 | server=bjb2-28827 | metrics={\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"\neval-supp-goal-adapt-tau025-s42 | server=? | metrics={\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bow\neval-supp-goal-crm005-s42 | server=bjb2-28827 | metrics={\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_\neval-supp-goal-reconvla-s42 | server=bjb2-28827 | metrics={}\neval-goal-vla-only-wrapper-s42 | server=bjb2-28827 | metrics={\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}\neval-supp-k2mean-goal-s42 | server=bjb2-40593 | metrics={}\neval-object-vla-only-wrapper-s44-r2 | server=bjb2-28827 | metrics={\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"b\neval-object-vla-only-wrapper-s43-r2 | server=bjb2-28827 | metrics={\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"but\neval-object-vla-only-wrapper-s42-r2 | server=bjb2-28827 | metrics={\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"but\neval-openvla-object-baseline-seed42-r2 | server=n/a | metrics={}\neval-obs-only-object-norm02-seed55 | server=? | metrics={}\nprecompute-pi05-features-object | server=? | metrics={}\nprecompute-smolvla-goal-shard2 | server=? | metrics={}\nprecompute-smolvla-goal-shard1 | server=? | metrics={}\nprecompute-smolvla-goal-shard0 | server=? | metrics={}\neval-smolvla-crm-goal-seed42-v1 | server=? | metrics={}\neval-smolvla-crm-goal-seed43-v1 | server=? | metrics={}\neval-smolvla-crm-goal-seed44-v1 | server=? | metrics={}\neval-object-vla-only-wrapper-s44 | server=bjb2-28827 | metrics={}\neval-object-vla-only-wrapper-s43 | server=bjb2-28827 | metrics={}\neval-object-vla-only-wrapper-s42 | server=bjb2-28827 | metrics={}\nprecompute-pi05-goal-2048 | server=bjb1-18228 | metrics={}\nprecompute-pi05-object-2048 | server=bjb1-18228 | metrics={}\neval-smolvla-crm-object-seed43-v1 | server=bjb2-28827 | metrics={}\neval-smolvla-crm-object-seed42-v1 | server=bjb2-28827 | metrics={}\neval-smolvla-crm-object-seed44-v1 | server=bjb2-28827 | metrics={}\neval-smolvla-crm-goal-seed43 | server=bjb1-32546 | metrics={}\neval-smolvla-crm-goal-seed42 | server=bjb1-32546 | metrics={}\neval-smolvla-lerobot-goal-seed44-v3 | server=bjb1-32546 | metrics={\"success_rate\": 78, \"n_episodes\": 200}\neval-smolvla-lerobot-goal-seed43-v3 | server=bjb1-32546 | metrics={\"success_rate\": 82, \"n_episodes\": 200}\neval-smolvla-lerobot-goal-seed43-v2 | server=bjb1-18228 | metrics={}\neval-smolvla-lerobot-object-seed44-v2 | server=bjb1-32546 | metrics={\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}\neval-smolvla-lerobot-object-seed43-v2 | server=bjb1-32546 | metrics={\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}\neval-smolvla-lerobot-goal-seed43 | server=bjb1-32546 | metrics={}\neval-smolvla-lerobot-object-seed44 | server=bjb1-32546 | metrics={}\neval-smolvla-lerobot-object-seed43 | server=bjb1-32546 | metrics={}\neval-pi05-crm-object-seed44 | server=bjb1-32546 | metrics={}\neval-pi05-crm-object-seed43 | server=bjb1-32546 | metrics={}\neval-pi05-crm-object-seed42 | server=bjb1-32546 | metrics={}\neval-pi05-vla-only-goal-seed44-r4-std | server=N/A | metrics={}\neval-pi05-vla-only-goal-seed42-r4-std | server=N/A | metrics={}\neval-pi05-vla-only-goal-seed43-r4-std | server=N/A | metrics={}\neval-pi05-vla-only-goal-seed42-r4 | server=bjb1-18228 | metrics={\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}\nprecompute-smolvla-goal-bjb2-28827 | server=bjb2-28827 | metrics={}\neval-pi05-vla-only-goal-seed44-r4 | server=bjb1-32546 | metrics={\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}\neval-pi05-vla-only-goal-seed43-r4 | server=bjb1-32546 | metrics={\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}\neval-openvla-oft-official-object | server=bjb2-40593 | metrics={}\neval-pi05-vla-only-object-seed44-r4 | server=bjb1-18228 | metrics={\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}\neval-smolvla-lerobot-official-object | server=bjb1-18228 | metrics={}\neval-pi05-vla-only-object-seed42-r4 | server=bjb1-18228 | metrics={\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100\neval-loss-perdof-object-seed42 | server=bjb1-18228 | metrics={\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"\neval-loss-combined-object-seed42 | server=bjb1-32546 | metrics={\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butt\neval-loss-conformal-object-seed42 | server=bjb1-32546 | metrics={\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0\neval-loss-mse-object-seed42 | server=bjb1-18228 | metrics={\"avg_success_rate\": 7, \"total_successes\": 14, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 10, \"ketchup\": 5, \"tomato_sauce\": 15, \"butt\neval-openvla-oft-object-baseline-seed42 | server=bjb2-40593 | metrics={\"overall_sr\": 0, \"per_task_sr\": \"all 10 tasks 0.0%\", \"n_rollouts\": 20, \"total_episodes\": 200}\nprecompute-smolvla-goal-bjb1-18228 | server=bjb1-18228 | metrics={\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}\neval-smolvla-acr-goal-seed43 | server=bjb1-32546 | metrics={}\neval-smolvla-crm-goal-seed44-v2 | server=bjb2-28827 | metrics={}\neval-smolvla-acr-goal-seed42 | server=bjb1-32546 | metrics={}\ncrm-train-pi05-object-full | server=bjb1-18228 | metrics={\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}\ncrm-train-pi05-object | server=bjb1-18228 | metrics={}\neval-pi05-vla-only-object-seed44-r3 | server=bjb1-32546 | metrics={\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}\neval-pi05-vla-only-object-seed43-r3 | server=bjb1-32546 | metrics={\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}\neval-pi05-vla-only-object-seed42-r3 | server=bjb1-32546 | metrics={\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}\neval-k20-obs-only-object-seed45 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_ob\neval-obs-only-object-norm003-seed66 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}\neval-obs-only-object-norm01-seed66 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}\neval-obs-only-object-norm005-seed66 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}\neval-obs-only-object-norm003-seed67 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.14}\neval-k20-obs-only-object-seed44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.18}\neval-k20-obs-only-object-seed43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.18}\neval-k20-obs-only-object-seed42 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.2}\neval-crm-object-k20-seed44 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.18}\neval-crm-object-k20-seed42 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.2}\neval-obs-only-object-norm02-seed53 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed52 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm02-seed51 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm02-seed50 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.18}\neval-obs-only-object-norm02-seed48-r2 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.18}\neval-obs-only-object-norm02-seed47 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.2}\neval-obs-only-object-norm02-seed46 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm02-seed45 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed44-r2 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed43-r3 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed43-r2 | server=? | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm005-seed67 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.1}\neval-obs-only-object-norm01-seed67 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.14}\neval-vla-only-object-seed50 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.09}\neval-vla-only-object-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.1}\neval-vla-only-object-seed48 | server=bjb2-40593 | metrics={\"overall_success_rate\": 0.1}\neval-vla-only-object-seed46 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.13}\neval-vla-only-object-seed45 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.09}\neval-vla-only-object-seed44-r2 | server=bjb2-40593 | metrics={\"overall_success_rate\": 0.1}\neval-plan-a-object-seed42 | server=bjb1-18228 | metrics={\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}\neval-vla-only-object-seed43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.12}\neval-vla-only-object | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.12}\neval-plan-a-object-seed44 | server=bjb1-18228 | metrics={\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}\neval-plan-a-object-seed43 | server=bjb1-18228 | metrics={\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}\neval-random-selection-object-seed44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"\neval-random-selection-object-seed43 | server=bjb1-32546 | metrics={\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}\neval-obs-only-object-norm01-seed60 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pu\neval-pi05-baseline-object-seed42 | server=bjb2-40593 | metrics={\"overall_success_rate\": 0}\neval-obs-only-object-norm01-seed54 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed53 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.19}\neval-obs-only-object-norm01-seed52 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed50 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm01-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm01-seed48 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm01-seed47 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm01-seed45-r2 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm01-seed44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm005-seed55 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed50 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm005-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed48 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm005-seed47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm005-seed44 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.12}\neval-obs-only-object-norm005-seed43-r2 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm005-seed43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm003-seed48 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed47-r2 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed46 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed45 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed44-bjb2 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed44 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed43-r2 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm003-seed43 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm01-seed57 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.19}\neval-obs-only-object-norm005-seed65 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm005-seed61 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed58 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm003-seed59 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm003-seed56 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed75 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15, \"total_rollouts\": 100}\neval-obs-only-object-norm01-seed74 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13, \"total_rollouts\": 100}\neval-obs-only-object-norm005-seed72 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.11, \"total_rollouts\": 100}\neval-obs-only-object-norm003-seed63-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed71 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16, \"total_rollouts\": 100}\neval-obs-only-object-norm003-seed62-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm003-seed73 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16, \"total_rollouts\": 100}\neval-obs-only-object-norm01-seed51-r3 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.11}\neval-obs-only-object-norm01-seed52-r3 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed65 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed64 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed64 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed65 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm003-seed64 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm005-seed62 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm005-seed63 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm01-seed61 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm003-seed64-bjb2 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm003-seed63 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm003-seed62 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed51-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed52-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed51 | server=bjb1-32546 | metrics={\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}\neval-obs-only-object-norm005-seed49-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm005-seed55-r2 | server=bjb1-18228 | metrics={}\neval-openvla-crm-object-seed42 | server=bjb2-28827 | metrics={\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-obs-only-object-norm003-seed44-r2 | server=bjb2-28827 | metrics={\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-random-selection-object-seed49 | server=bjb1-32546 | metrics={\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-random-selection-object-seed48 | server=bjb2-40593 | metrics={\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-k5-obs-only-object-seed44 | server=bjb1-32546 | metrics={\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-obs-only-object-norm02-seed54 | server=bjb2-28827 | metrics={}\nD088-eval-adaptive-unc-head-object-seed44 | server=bjb2-28827 | metrics={}\nD088-eval-adaptive-unc-head-object-seed43 | server=bjb2-28827 | metrics={}\nD088-eval-adaptive-unc-head-object-seed42 | server=bjb2-28827 | metrics={}\neval-adaptive-unc-head-object-seed42 | server=bjb2-28827 | metrics={\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}\neval-adaptive-unc-head-object-seed43 | server=bjb2-28827 | metrics={\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}\neval-perdof-object-norm02-seed50 | server=bjb1-32546 | metrics={\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}\neval-adaptive-unc-head-object-seed44 | server=bjb2-28827 | metrics={\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}\neval-random-selection-object-seed46-r3 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}\neval-perdof-object-norm02-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}\neval-random-selection-object-seed47 | server=bjb1-18228 | metrics={\"sr\": 7}\neval-k5-obs-only-object-seed43 | server=bjb1-32546 | metrics={\"sr\": 17}\neval-crm-k1-object-seed43-plan702 | server=bjb2-28827 | metrics={\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-crm-k1-object-seed42-plan702 | server=bjb2-28827 | metrics={\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 10",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/bijarzrz0.txt",
    "persistedOutputSize": 64318
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01T7ATYikDyY62tNKzmBEgQL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/bijarzrz0.txt",
  "description": "Read full Goal/Object experiment list",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "22fbebd1-f30b-4e73-aa73-d11e581ea5c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No1tLYw4R1YYCJaCBzk6H3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 27188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1433
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

_source line 22 · 2026-05-25T02:01:50.532Z_

<details><summary>↩ Tool result · `toolu_01T7ATYikDyY62tNKzmBEgQL`</summary>

```text
&lt;persisted-output>
Output too large (62.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/ba75uljfc.txt

Preview (first 2KB):
Total experiments: 850
eval-pi05-vla-only-object-s44 | server=bjb1-32546 | metrics={"overall_success_rate": 0.81, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-object-s43 | server=bjb1-32546 | metrics={"overall_success_rate": 0.815, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-goal-s43 | server=bjb1-32546 | metrics={"overall_success_rate": 0.97, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-goal-s42 | server=bjb1-32546 | metrics={"overall_success_rate": 0.955, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}
eval-pi05-vla-only-object-s42 | server=bjb1-32546 | metrics={"overall_success_rate": 0.965, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}
eval-supp-crm-norm005-goal-s48 | server=bjb2-28827 | metrics={"overall_success_rate": 0.8, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "crm_obs_only", "max_correction_norm": 0.05, "K": 10}
eval-supp-goal-vla-only-s42-bjb1 | server=bjb1-32546 | metrics={}
crm-norm005-goal-s49 | server=bjb1-18228 | metrics={}
crm-norm005-object-s48 | server=bjb1-18228 | metrics={}
eval-supp-goal-vla-only-s50 | server=cqa1-32758 | metrics={}
eval-supp-goal-vla-only-s44 | server=cqa1-32758 | metrics={}
eval-supp-goal-vla-only-s43 | server=cqa1-32758 | metrics={}
eval-supp-goal-vla-only-s42 | server=cqa1-32758 | metrics={}
eval-supp-vla-only-goal-s49 | server=cqa1-32758 | metrics={"overall_sr": 0.82, "per_task_sr": {"middle_drawer": 0.75, "bowl_stove": 0.95, "wine_cabinet": 0.85, "drawer_bowl": 0.65, "bowl_cabinet": 0.95, "push_plate": 0.85, "cream_cheese": 0.55, "stove_on": 1
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
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "b641a241-8b63-4af3-a25b-51c2b053018f",
  "tool_use_result": {
    "stdout": "Total experiments: 850\neval-pi05-vla-only-object-s44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-object-s43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-goal-s43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-goal-s42 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-pi05-vla-only-object-s42 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}\neval-supp-crm-norm005-goal-s48 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}\neval-supp-goal-vla-only-s42-bjb1 | server=bjb1-32546 | metrics={}\ncrm-norm005-goal-s49 | server=bjb1-18228 | metrics={}\ncrm-norm005-object-s48 | server=bjb1-18228 | metrics={}\neval-supp-goal-vla-only-s50 | server=cqa1-32758 | metrics={}\neval-supp-goal-vla-only-s44 | server=cqa1-32758 | metrics={}\neval-supp-goal-vla-only-s43 | server=cqa1-32758 | metrics={}\neval-supp-goal-vla-only-s42 | server=cqa1-32758 | metrics={}\neval-supp-vla-only-goal-s49 | server=cqa1-32758 | metrics={\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1\neval-supp-vla-only-goal-s48 | server=cqa1-32758 | metrics={\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl\neval-supp-goal-vla-only-s45 | server=bjb2-28827 | metrics={\"SR\": 0.835}\neval-pi05-vla-only-object-seed43-r4 | server=bjb1-18228 | metrics={\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}\neval-a1-baseline-object-s42 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.565, \"total_successes\": 113, \"total_episodes\": 200, \"official_reported_sr\": 0.998, \"gap_vs_official\": -0.433, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.35, \"sala\neval-supp-goal-k2mean-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}\neval-supp-goal-adapt-tau025-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29\neval-supp-goal-crm-norm005-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}\neval-supp-goal-reconvla-s47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-supp-goal-vla-only-s47-r3 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}\nprecompute-pi05-object-2048-r2 | server=bjb1-18228 | metrics={\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}\neval-openvla-object-vla-only-seed42-v3 | server=bjb2-28827 | metrics={}\ntrain-crm-pi05-goal-k1 | server=bjb1-18228 | metrics={\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}\neval-supp-goal-vla-only-s47-r2 | server=bjb1-18228 | metrics={}\neval-supp-goal-vla-only-s47 | server=bjb1-18228 | metrics={}\ncrm-train-openvla-k1-multiscale-object | server=bjb2-28827 | metrics={\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}\nprecompute-pi05-goal-2048-r2 | server=bjb1-18228 | metrics={}\nprecompute-smolvla-goal-bjb1-32546 | server=bjb1-32546 | metrics={}\neval-supp-goal-vla-only-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-reconvla-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}\neval-perdof-object-norm003-seed44 | server=bjb1-18228 | metrics={\"success_rate\": 11, \"successes\": 11, \"total\": 100}\neval-supp-goal-vla-only-wrapper-s44 | server=bjb1-32546 | metrics={\"success_rate\": 82, \"successes\": 164, \"total\": 200}\neval-pi05-vla-only-object-seed42 | server=bjb1-32546 | metrics={\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-pi05-vla-only-object-seed43 | server=bjb1-32546 | metrics={\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-pi05-vla-only-object-seed44 | server=bjb1-32546 | metrics={\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}\neval-supp-goal-k2mean-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-adapt-tau025-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-crm-norm005-s46 | server=bjb2-28827 | metrics={\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}\neval-supp-goal-k2mean-s45 | server=cqa1-32758 | metrics={\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_insi\neval-supp-goal-reconvla-s45 | server=bjb2-28827 | metrics={\"SR\": 0.855}\neval-supp-goal-crm-norm005-s45 | server=? | metrics={\"success_rate\": 81, \"successes\": 162, \"total\": 200}\neval-supp-goal-adapt-tau025-s45 | server=bjb1-32546 | metrics={\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}\neval-ablation-tau040-goal-s42 | server=bjb2-28827 | metrics={\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}\neval-ablation-tau015-goal-s42 | server=bjb2-28827 | metrics={\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}\neval-supp-k2mean-object-s44 | server=cqa1-32758 | metrics={\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudd\neval-ablation-tau010-goal-s42 | server=bjb2-28827 | metrics={\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}\neval-supp-goal-vla-only-wrapper-s44-r2 | server=bjb1-32546 | metrics={\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_pl\neval-supp-k2mean-goal-s44 | server=bjb1-32546 | metrics={\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wi\neval-supp-goal-vla-only-wrapper-s43 | server=bjb1-32546 | metrics={\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \neval-supp-goal-reconvla-s44 | server=bjb2-28827 | metrics={\"success_rate\": 0.805, \"total_rollouts\": 200, \"total_successes\": 161, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.81, 0.81, 0.805], \"mean\": 0.8083, \"std\": 0.0029}}\neval-supp-crm-norm005-goal-s44 | server=bjb2-28827 | metrics={\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}\neval-supp-k2mean-object-s43 | server=cqa1-32758 | metrics={\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"toma\neval-supp-k2mean-goal-s42-r2 | server=bjb2-40593 | metrics={\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"op\neval-supp-adapt-tau025-goal-s44 | server=bjb1-32546 | metrics={\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}\neval-supp-adapt-tau025-goal-s43 | server=bjb1-32546 | metrics={\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}\neval-supp-crm-norm005-goal-s43 | server=bjb1-32546 | metrics={\"success_rate\": 0.82}\neval-supp-goal-reconvla-s43 | server=cqa1-32758 | metrics={\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.65, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bott\neval-supp-k2mean-goal-s43 | server=cqa1-32758 | metrics={\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"\neval-supp-k2mean-object-s42 | server=bjb2-28827 | metrics={\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"\neval-supp-goal-adapt-tau025-s42 | server=? | metrics={\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bow\neval-supp-goal-crm005-s42 | server=bjb2-28827 | metrics={\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_\neval-supp-goal-reconvla-s42 | server=bjb2-28827 | metrics={}\neval-goal-vla-only-wrapper-s42 | server=bjb2-28827 | metrics={\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}\neval-supp-k2mean-goal-s42 | server=bjb2-40593 | metrics={}\neval-object-vla-only-wrapper-s44-r2 | server=bjb2-28827 | metrics={\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"b\neval-object-vla-only-wrapper-s43-r2 | server=bjb2-28827 | metrics={\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"but\neval-object-vla-only-wrapper-s42-r2 | server=bjb2-28827 | metrics={\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"but\neval-openvla-object-baseline-seed42-r2 | server=n/a | metrics={}\neval-obs-only-object-norm02-seed55 | server=? | metrics={}\nprecompute-pi05-features-object | server=? | metrics={}\nprecompute-smolvla-goal-shard2 | server=? | metrics={}\nprecompute-smolvla-goal-shard1 | server=? | metrics={}\nprecompute-smolvla-goal-shard0 | server=? | metrics={}\neval-smolvla-crm-goal-seed42-v1 | server=? | metrics={}\neval-smolvla-crm-goal-seed43-v1 | server=? | metrics={}\neval-smolvla-crm-goal-seed44-v1 | server=? | metrics={}\neval-object-vla-only-wrapper-s44 | server=bjb2-28827 | metrics={}\neval-object-vla-only-wrapper-s43 | server=bjb2-28827 | metrics={}\neval-object-vla-only-wrapper-s42 | server=bjb2-28827 | metrics={}\nprecompute-pi05-goal-2048 | server=bjb1-18228 | metrics={}\nprecompute-pi05-object-2048 | server=bjb1-18228 | metrics={}\neval-smolvla-crm-object-seed43-v1 | server=bjb2-28827 | metrics={}\neval-smolvla-crm-object-seed42-v1 | server=bjb2-28827 | metrics={}\neval-smolvla-crm-object-seed44-v1 | server=bjb2-28827 | metrics={}\neval-smolvla-crm-goal-seed43 | server=bjb1-32546 | metrics={}\neval-smolvla-crm-goal-seed42 | server=bjb1-32546 | metrics={}\neval-smolvla-lerobot-goal-seed44-v3 | server=bjb1-32546 | metrics={\"success_rate\": 78, \"n_episodes\": 200}\neval-smolvla-lerobot-goal-seed43-v3 | server=bjb1-32546 | metrics={\"success_rate\": 82, \"n_episodes\": 200}\neval-smolvla-lerobot-goal-seed43-v2 | server=bjb1-18228 | metrics={}\neval-smolvla-lerobot-object-seed44-v2 | server=bjb1-32546 | metrics={\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}\neval-smolvla-lerobot-object-seed43-v2 | server=bjb1-32546 | metrics={\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}\neval-smolvla-lerobot-goal-seed43 | server=bjb1-32546 | metrics={}\neval-smolvla-lerobot-object-seed44 | server=bjb1-32546 | metrics={}\neval-smolvla-lerobot-object-seed43 | server=bjb1-32546 | metrics={}\neval-pi05-crm-object-seed44 | server=bjb1-32546 | metrics={}\neval-pi05-crm-object-seed43 | server=bjb1-32546 | metrics={}\neval-pi05-crm-object-seed42 | server=bjb1-32546 | metrics={}\neval-pi05-vla-only-goal-seed44-r4-std | server=N/A | metrics={}\neval-pi05-vla-only-goal-seed42-r4-std | server=N/A | metrics={}\neval-pi05-vla-only-goal-seed43-r4-std | server=N/A | metrics={}\neval-pi05-vla-only-goal-seed42-r4 | server=bjb1-18228 | metrics={\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}\nprecompute-smolvla-goal-bjb2-28827 | server=bjb2-28827 | metrics={}\neval-pi05-vla-only-goal-seed44-r4 | server=bjb1-32546 | metrics={\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}\neval-pi05-vla-only-goal-seed43-r4 | server=bjb1-32546 | metrics={\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}\neval-openvla-oft-official-object | server=bjb2-40593 | metrics={}\neval-pi05-vla-only-object-seed44-r4 | server=bjb1-18228 | metrics={\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}\neval-smolvla-lerobot-official-object | server=bjb1-18228 | metrics={}\neval-pi05-vla-only-object-seed42-r4 | server=bjb1-18228 | metrics={\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100\neval-loss-perdof-object-seed42 | server=bjb1-18228 | metrics={\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"\neval-loss-combined-object-seed42 | server=bjb1-32546 | metrics={\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butt\neval-loss-conformal-object-seed42 | server=bjb1-32546 | metrics={\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0\neval-loss-mse-object-seed42 | server=bjb1-18228 | metrics={\"avg_success_rate\": 7, \"total_successes\": 14, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 10, \"ketchup\": 5, \"tomato_sauce\": 15, \"butt\neval-openvla-oft-object-baseline-seed42 | server=bjb2-40593 | metrics={\"overall_sr\": 0, \"per_task_sr\": \"all 10 tasks 0.0%\", \"n_rollouts\": 20, \"total_episodes\": 200}\nprecompute-smolvla-goal-bjb1-18228 | server=bjb1-18228 | metrics={\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}\neval-smolvla-acr-goal-seed43 | server=bjb1-32546 | metrics={}\neval-smolvla-crm-goal-seed44-v2 | server=bjb2-28827 | metrics={}\neval-smolvla-acr-goal-seed42 | server=bjb1-32546 | metrics={}\ncrm-train-pi05-object-full | server=bjb1-18228 | metrics={\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}\ncrm-train-pi05-object | server=bjb1-18228 | metrics={}\neval-pi05-vla-only-object-seed44-r3 | server=bjb1-32546 | metrics={\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}\neval-pi05-vla-only-object-seed43-r3 | server=bjb1-32546 | metrics={\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}\neval-pi05-vla-only-object-seed42-r3 | server=bjb1-32546 | metrics={\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}\neval-k20-obs-only-object-seed45 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_ob\neval-obs-only-object-norm003-seed66 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}\neval-obs-only-object-norm01-seed66 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}\neval-obs-only-object-norm005-seed66 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}\neval-obs-only-object-norm003-seed67 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.14}\neval-k20-obs-only-object-seed44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.18}\neval-k20-obs-only-object-seed43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.18}\neval-k20-obs-only-object-seed42 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.2}\neval-crm-object-k20-seed44 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.18}\neval-crm-object-k20-seed42 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.2}\neval-obs-only-object-norm02-seed53 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed52 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm02-seed51 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm02-seed50 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.18}\neval-obs-only-object-norm02-seed48-r2 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.18}\neval-obs-only-object-norm02-seed47 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.2}\neval-obs-only-object-norm02-seed46 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm02-seed45 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed44-r2 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed43-r3 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm02-seed43-r2 | server=? | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm005-seed67 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.1}\neval-obs-only-object-norm01-seed67 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.14}\neval-vla-only-object-seed50 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.09}\neval-vla-only-object-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.1}\neval-vla-only-object-seed48 | server=bjb2-40593 | metrics={\"overall_success_rate\": 0.1}\neval-vla-only-object-seed46 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.13}\neval-vla-only-object-seed45 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.09}\neval-vla-only-object-seed44-r2 | server=bjb2-40593 | metrics={\"overall_success_rate\": 0.1}\neval-plan-a-object-seed42 | server=bjb1-18228 | metrics={\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}\neval-vla-only-object-seed43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.12}\neval-vla-only-object | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.12}\neval-plan-a-object-seed44 | server=bjb1-18228 | metrics={\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}\neval-plan-a-object-seed43 | server=bjb1-18228 | metrics={\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}\neval-random-selection-object-seed44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"\neval-random-selection-object-seed43 | server=bjb1-32546 | metrics={\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}\neval-obs-only-object-norm01-seed60 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pu\neval-pi05-baseline-object-seed42 | server=bjb2-40593 | metrics={\"overall_success_rate\": 0}\neval-obs-only-object-norm01-seed54 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed53 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.19}\neval-obs-only-object-norm01-seed52 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed50 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm01-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm01-seed48 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm01-seed47 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm01-seed45-r2 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm01-seed44 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm005-seed55 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed50 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm005-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed48 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm005-seed47 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm005-seed44 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.12}\neval-obs-only-object-norm005-seed43-r2 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm005-seed43 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm003-seed48 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed47-r2 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed46 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed45 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed44-bjb2 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed44 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed43-r2 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm003-seed43 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm01-seed57 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.19}\neval-obs-only-object-norm005-seed65 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.14}\neval-obs-only-object-norm005-seed61 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed58 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.16}\neval-obs-only-object-norm003-seed59 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.13}\neval-obs-only-object-norm003-seed56 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed75 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.15, \"total_rollouts\": 100}\neval-obs-only-object-norm01-seed74 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.13, \"total_rollouts\": 100}\neval-obs-only-object-norm005-seed72 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.11, \"total_rollouts\": 100}\neval-obs-only-object-norm003-seed63-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed71 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16, \"total_rollouts\": 100}\neval-obs-only-object-norm003-seed62-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm003-seed73 | server=bjb2-28827 | metrics={\"overall_success_rate\": 0.16, \"total_rollouts\": 100}\neval-obs-only-object-norm01-seed51-r3 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.11}\neval-obs-only-object-norm01-seed52-r3 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed65 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm01-seed64 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm005-seed64 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.15}\neval-obs-only-object-norm003-seed65 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm003-seed64 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.17}\neval-obs-only-object-norm005-seed62 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm005-seed63 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm01-seed61 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm003-seed64-bjb2 | server=bjb2-28827 | metrics={}\neval-obs-only-object-norm003-seed63 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm003-seed62 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed51-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed52-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm01-seed51 | server=bjb1-32546 | metrics={\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}\neval-obs-only-object-norm005-seed49-r2 | server=bjb1-32546 | metrics={}\neval-obs-only-object-norm005-seed55-r2 | server=bjb1-18228 | metrics={}\neval-openvla-crm-object-seed42 | server=bjb2-28827 | metrics={\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-obs-only-object-norm003-seed44-r2 | server=bjb2-28827 | metrics={\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-random-selection-object-seed49 | server=bjb1-32546 | metrics={\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-random-selection-object-seed48 | server=bjb2-40593 | metrics={\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-k5-obs-only-object-seed44 | server=bjb1-32546 | metrics={\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-obs-only-object-norm02-seed54 | server=bjb2-28827 | metrics={}\nD088-eval-adaptive-unc-head-object-seed44 | server=bjb2-28827 | metrics={}\nD088-eval-adaptive-unc-head-object-seed43 | server=bjb2-28827 | metrics={}\nD088-eval-adaptive-unc-head-object-seed42 | server=bjb2-28827 | metrics={}\neval-adaptive-unc-head-object-seed42 | server=bjb2-28827 | metrics={\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}\neval-adaptive-unc-head-object-seed43 | server=bjb2-28827 | metrics={\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}\neval-perdof-object-norm02-seed50 | server=bjb1-32546 | metrics={\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}\neval-adaptive-unc-head-object-seed44 | server=bjb2-28827 | metrics={\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}\neval-random-selection-object-seed46-r3 | server=bjb1-18228 | metrics={\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}\neval-perdof-object-norm02-seed49 | server=bjb1-32546 | metrics={\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}\neval-random-selection-object-seed47 | server=bjb1-18228 | metrics={\"sr\": 7}\neval-k5-obs-only-object-seed43 | server=bjb1-32546 | metrics={\"sr\": 17}\neval-crm-k1-object-seed43-plan702 | server=bjb2-28827 | metrics={\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}\neval-crm-k1-object-seed42-plan702 | server=bjb2-28827 | metrics={\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 10",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/ba75uljfc.txt",
    "persistedOutputSize": 64318
  }
}
```

</details>

---


### Assistant

_source line 23_

Let me get a more structured view of all Goal/Object experiments, separating Table 1 candidates from supplementary ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "d400fd6a-c6fe-4379-8d4e-e976505d44b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtT7YmWQdhXopRQYLbqpmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1306,
      "cache_read_input_tokens": 28621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1306
      },
      "output_tokens": 1,
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_012P2CFFsENMdm6on8GPNVS6`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/1bbcf642-be59-4ac1-a0a5-15f36bcc29ff/tool-results/mcp-agent-ml-research-read_registry-1779674475741.txt') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Focus on Table 1 experiments (not pi05, not supp, not norm005 etc)\n# Table 1 uses: vla_only, crm (baseline), adaptive_conformal_crm\n# For goal and object suites\n\ntable1_candidates = []\nfor eid, exp in exps.items():\n    lower_id = eid.lower()\n    if 'goal' not in lower_id and 'object' not in lower_id:\n        continue\n    # Skip pi0.5 experiments\n    if 'pi05' in lower_id:\n        continue\n    # Skip supplementary\n    if 'supp' in lower_id:\n        continue\n    # Skip norm variations (those are ablations)\n    if 'norm0' in lower_id or 'norm1' in lower_id:\n        continue\n    # Skip tau sweep\n    if 'tau0' in lower_id or 'tau-sweep' in lower_id:\n        continue\n    # Skip K variations (k2, k5 etc) unless it's the main Table 1 K\n    if any(x in lower_id for x in ['k2-', 'k5-', 'k20-']):\n        continue\n    \n    server = exp.get('spec',{}).get('server','?')\n    metrics = exp.get('metrics',{})\n    status = exp.get('status','?')\n    conclusion = (exp.get('conclusion','') or '')[:150]\n    \n    table1_candidates.append({\n        'id': eid,\n        'server': server,\n        'status': status,\n        'metrics': metrics,\n        'conclusion': conclusion\n    })\n\n# Sort by id\ntable1_candidates.sort(key=lambda x: x['id'])\nfor c in table1_candidates:\n    m = c['metrics']\n    sr = m.get('overall_success_rate', m.get('overall_sr', '?'))\n    mode = m.get('mode', '?')\n    n_r = m.get('n_rollouts', '?')\n    print(f\\\"{c['id']} | {c['status']} | server={c['server']} | mode={mode} | SR={sr} | n_rollouts={n_r}\\\")\n    if c['conclusion']:\n        print(f\\\"  conclusion: {c['conclusion']}\\\")\n\" 2>&1",
  "description": "Filter Table 1 candidate experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "aea56dad-9392-4ebc-b8fe-30f595a0f420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtT7YmWQdhXopRQYLbqpmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1306,
      "cache_read_input_tokens": 28621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1306
      },
      "output_tokens": 1,
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

_source line 25 · 2026-05-25T02:02:09.016Z_

<details><summary>↩ Tool result · `toolu_012P2CFFsENMdm6on8GPNVS6`</summary>

```text
D088-eval-adaptive-unc-head-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
D088-eval-adaptive-unc-head-object-seed43 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
D088-eval-adaptive-unc-head-object-seed44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
crm-train-openvla-k1-multiscale-object | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-a1-baseline-object-s42 | DONE | server=bjb1-32546 | mode=? | SR=0.565 | n_rollouts=?
  conclusion: negative
eval-acr-object-obs-only-default | DONE | server=bjb1-32546 | mode=? | SR=0.17 | n_rollouts=?
  conclusion: success
eval-acr-object-v3 | DONE | server=bjb1-18228 | mode=? | SR=0 | n_rollouts=?
  conclusion: negative
eval-acr-object-v4-default | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-acr-object-v4-default-r2 | DONE | server=bjb1-18228 | mode=? | SR=0 | n_rollouts=?
  conclusion: success
eval-acr-object-v4-obs-only | DONE | server=bjb1-32546 | mode=obs_only | SR=19.0% (19/100) | n_rollouts=?
  conclusion: success
eval-acr-object-v4-obs-only-b2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-acr-object-v4-perdof | DONE | server=bjb1-32546 | mode=perdof | SR=11.0% (11/100) | n_rollouts=?
  conclusion: success
eval-acr-object-v4-scalar | DONE | server=bjb1-32546 | mode=? | SR=9 | n_rollouts=?
  conclusion: negative
eval-acr-object-v4-scalar-b2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-adaptive-unc-head-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: negative
eval-adaptive-unc-head-object-seed43 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=100
  conclusion: negative
eval-adaptive-unc-head-object-seed44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: negative
eval-argmin-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.17 | n_rollouts=?
  conclusion: success
eval-argmin-object-seed44 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-argmin-object-seed44-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.13 | n_rollouts=?
  conclusion: success
eval-argmin-object-seed44-r3 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-argmin-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: success
eval-argmin-object-seed46 | DONE | server=bjb1-32546 | mode=reconvla | SR=0.1 | n_rollouts=?
  conclusion: success
eval-argmin-object-seed47 | DONE | server=bjb1-32546 | mode=reconvla | SR=0.1 | n_rollouts=?
  conclusion: success
eval-argmin-object-seed48 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-argmin-object-seed49 | DONE | server=bjb1-32546 | mode=reconvla (argmin baseline) | SR=0.16 | n_rollouts=?
  conclusion: success
eval-argmin-object-seed50 | DONE | server=bjb1-32546 | mode=reconvla | SR=0.13 | n_rollouts=?
  conclusion: success
eval-crm-goal-seed42 | DONE | server=bjb1-18228 | mode=? | SR=0.67 | n_rollouts=10
  conclusion: success
eval-crm-goal-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.72 | n_rollouts=10
  conclusion: success
eval-crm-goal-seed44 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-crm-goal-seed44-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-crm-goal-seed45 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-crm-goal-seed45-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-crm-goal-seed46 | DONE | server=bjb2-28827 | mode=? | SR=0.72 | n_rollouts=10
  conclusion: success
eval-crm-k1-object-seed42-plan702 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-crm-k1-object-seed42-plan702-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-crm-k1-object-seed43-plan702 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-crm-k1-object-seed43-plan702-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-crm-k1-object-seed44-plan702 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-crm-k1-object-seed44-plan702-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-direct-correction-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-direct-correction-object-seed42-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-direct-correction-object-seed42-r3 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-goal-vla-only-wrapper-s42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-k1-crm-accg-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=0.11 | n_rollouts=100
  conclusion: negative
eval-k1-crm-accg-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.12 | n_rollouts=100
  conclusion: negative
eval-k1-crm-accg-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.07 | n_rollouts=100
  conclusion: negative
eval-k1-crm-multiscale-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: negative
eval-k1-crm-multiscale-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.09 | n_rollouts=?
  conclusion: negative
eval-k1-crm-multiscale-object-seed43-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.09 | n_rollouts=?
  conclusion: negative
eval-k1-crm-multiscale-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: negative
eval-k1-crm-multiscale-object-seed44-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: negative
eval-loss-combined-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-loss-conformal-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-loss-mse-object-seed42 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-loss-perdof-object-seed42 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-object-v4-full | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-v5-full | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-v6-full | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-v7-full | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-v8-full | DONE | server=bjb2-40593 | mode=? | SR=0.13 | n_rollouts=?
  conclusion: success
eval-object-vla-only-wrapper-s42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-vla-only-wrapper-s42-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-object-vla-only-wrapper-s43 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-vla-only-wrapper-s43-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-object-vla-only-wrapper-s44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-object-vla-only-wrapper-s44-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-obs-only-object-default-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.16 | n_rollouts=?
  conclusion: success
eval-obs-only-object-default-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: success
eval-obs-only-object-default-seed45-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-obs-only-object-default-seed46 | DONE | server=bjb1-32546 | mode=? | SR=0.15 | n_rollouts=?
  conclusion: success
eval-obs-only-object-default-seed47 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-obs-only-object-default-seed48 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-obs-only-object-default-seed48-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-obs-only-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: negative
eval-openvla-crm-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: negative
eval-openvla-object-baseline-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-openvla-object-baseline-seed42-r2 | DONE | server=n/a | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-openvla-object-vla-only-seed42 | DONE | server=bjb1-18228 | mode=? | SR=0 | n_rollouts=?
  conclusion: negative
eval-openvla-object-vla-only-seed42-v2 | DONE | server=bjb1-18228 | mode=? | SR=0.69 | n_rollouts=?
  conclusion: success
eval-openvla-object-vla-only-seed42-v3 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-openvla-oft-object-baseline-seed42 | DONE | server=bjb2-40593 | mode=? | SR=0 | n_rollouts=20
  conclusion: negative
eval-openvla-oft-official-object | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-perdof-object-default-seed43 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-perdof-object-default-seed44 | DONE | server=autodl-4090 (previous run) | mode=? | SR=0 | n_rollouts=?
  conclusion: negative
eval-perdof-object-default-seed45 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-perdof-object-default-seed46 | DONE | server=bjb1-32546 | mode=? | SR=0 | n_rollouts=?
  conclusion: negative
eval-perdof-object-default-seed47 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: negative
eval-perdof-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: success
eval-perdof-object-seed44 | DONE | server=? | mode=? | SR=0.08 | n_rollouts=?
  conclusion: negative
eval-plan-a-object-seed42 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-plan-a-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-plan-a-object-seed44 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-random-selection-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-random-selection-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-random-selection-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.11 | n_rollouts=10
  conclusion: success
eval-random-selection-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-random-selection-object-seed46 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-random-selection-object-seed46-r2 | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-random-selection-object-seed46-r3 | DONE | server=bjb1-18228 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: success
eval-random-selection-object-seed47 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-random-selection-object-seed48 | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-random-selection-object-seed49 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-reconvla-object | DONE | server=? | mode=? | SR=0.12 | n_rollouts=10
  conclusion: success
eval-scalar-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-scalar-object-seed44 | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-scalar-object-seed44-r2 | DONE | server=bjb1-32546 | mode=? | SR=0.06 | n_rollouts=?
  conclusion: negative
eval-scalar-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.09 | n_rollouts=?
  conclusion: success
eval-scalar-object-seed45-r2 | DONE | server=bjb2-40593 | mode=? | SR=0.07 | n_rollouts=?
  conclusion: negative
eval-scalar-object-seed46 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-smolvla-acr-goal-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-smolvla-acr-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-smolvla-crm-goal-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-smolvla-crm-goal-seed42-v1 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-smolvla-crm-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-smolvla-crm-goal-seed43-v1 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-smolvla-crm-goal-seed44-v1 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-smolvla-crm-goal-seed44-v2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-smolvla-crm-object-seed42-v1 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-smolvla-crm-object-seed43-v1 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-smolvla-crm-object-seed44-v1 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: negative
eval-smolvla-lerobot-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-smolvla-lerobot-goal-seed43-v2 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-smolvla-lerobot-goal-seed43-v3 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-smolvla-lerobot-goal-seed44-v3 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-smolvla-lerobot-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-smolvla-lerobot-object-seed43-v2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-smolvla-lerobot-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-smolvla-lerobot-object-seed44-v2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-smolvla-lerobot-official-object | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-vla-mean-object | DONE | server=bjb1-32546 | mode=vla_only | SR=12 | n_rollouts=10
  conclusion: success
eval-vla-mean-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.15 | n_rollouts=?
  conclusion: success
eval-vla-mean-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: success
eval-vla-mean-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.13 | n_rollouts=?
  conclusion: success
eval-vla-only-goal-seed42 | DONE | server=bjb1-32546 | mode=? | SR=0.71 | n_rollouts=?
  conclusion: success
eval-vla-only-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.69 | n_rollouts=?
  conclusion: success
eval-vla-only-goal-seed44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-vla-only-goal-seed44-r2 | DONE | server=bjb2-28827 | mode=vla_only | SR=? | n_rollouts=?
  conclusion: success
eval-vla-only-goal-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.63 | n_rollouts=10
  conclusion: success
eval-vla-only-goal-seed46 | DONE | server=bjb1-32546 | mode=? | SR=0.71 | n_rollouts=?
  conclusion: success
eval-vla-only-goal-seed47 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-vla-only-goal-seed47-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-vla-only-goal-seed48 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
eval-vla-only-goal-seed48-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-vla-only-goal-seed49 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-vla-only-goal-seed51 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10
  conclusion: success
eval-vla-only-object | DONE | server=bjb1-32546 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: success
eval-vla-only-object-k1 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-vla-only-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.12 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed44 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: failed
eval-vla-only-object-seed44-r2 | DONE | server=bjb2-40593 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.09 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed45-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.11 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed46 | DONE | server=bjb1-18228 | mode=? | SR=0.13 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed47 | DONE | server=bjb2-28827 | mode=? | SR=0.1 | n_rollouts=10
  conclusion: success
eval-vla-only-object-seed48 | DONE | server=bjb2-40593 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed48-r2 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed49 | DONE | server=bjb1-32546 | mode=? | SR=0.1 | n_rollouts=?
  conclusion: success
eval-vla-only-object-seed50 | DONE | server=bjb1-32546 | mode=? | SR=0.09 | n_rollouts=?
  conclusion: success
precompute-smolvla-goal-bjb1-18228 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?
  conclusion: success
precompute-smolvla-goal-bjb1-32546 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
precompute-smolvla-goal-bjb2-28827 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: killed
precompute-smolvla-goal-shard0 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
precompute-smolvla-goal-shard1 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
precompute-smolvla-goal-shard2 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: killed
train-crm-k1-accg-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: failed
train-crm-k1-accg-object-seed42-fallback | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?
  conclusion: success
train-crm-k1-accg-object-seed42-full | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?
  conclusion: success
train-crm-k1-accg-object-seed42-v2 | DONE | server=? | mode=? | SR=? | n_rollouts=?
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "43323cc7-c196-48e4-9f40-7b5332450011",
  "tool_use_result": {
    "stdout": "D088-eval-adaptive-unc-head-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\nD088-eval-adaptive-unc-head-object-seed43 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\nD088-eval-adaptive-unc-head-object-seed44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\ncrm-train-openvla-k1-multiscale-object | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-a1-baseline-object-s42 | DONE | server=bjb1-32546 | mode=? | SR=0.565 | n_rollouts=?\n  conclusion: negative\neval-acr-object-obs-only-default | DONE | server=bjb1-32546 | mode=? | SR=0.17 | n_rollouts=?\n  conclusion: success\neval-acr-object-v3 | DONE | server=bjb1-18228 | mode=? | SR=0 | n_rollouts=?\n  conclusion: negative\neval-acr-object-v4-default | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-acr-object-v4-default-r2 | DONE | server=bjb1-18228 | mode=? | SR=0 | n_rollouts=?\n  conclusion: success\neval-acr-object-v4-obs-only | DONE | server=bjb1-32546 | mode=obs_only | SR=19.0% (19/100) | n_rollouts=?\n  conclusion: success\neval-acr-object-v4-obs-only-b2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-acr-object-v4-perdof | DONE | server=bjb1-32546 | mode=perdof | SR=11.0% (11/100) | n_rollouts=?\n  conclusion: success\neval-acr-object-v4-scalar | DONE | server=bjb1-32546 | mode=? | SR=9 | n_rollouts=?\n  conclusion: negative\neval-acr-object-v4-scalar-b2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-adaptive-unc-head-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: negative\neval-adaptive-unc-head-object-seed43 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=100\n  conclusion: negative\neval-adaptive-unc-head-object-seed44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: negative\neval-argmin-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.17 | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed44 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-argmin-object-seed44-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.13 | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed44-r3 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-argmin-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed46 | DONE | server=bjb1-32546 | mode=reconvla | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed47 | DONE | server=bjb1-32546 | mode=reconvla | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed48 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed49 | DONE | server=bjb1-32546 | mode=reconvla (argmin baseline) | SR=0.16 | n_rollouts=?\n  conclusion: success\neval-argmin-object-seed50 | DONE | server=bjb1-32546 | mode=reconvla | SR=0.13 | n_rollouts=?\n  conclusion: success\neval-crm-goal-seed42 | DONE | server=bjb1-18228 | mode=? | SR=0.67 | n_rollouts=10\n  conclusion: success\neval-crm-goal-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.72 | n_rollouts=10\n  conclusion: success\neval-crm-goal-seed44 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-crm-goal-seed44-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-crm-goal-seed45 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-crm-goal-seed45-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-crm-goal-seed46 | DONE | server=bjb2-28827 | mode=? | SR=0.72 | n_rollouts=10\n  conclusion: success\neval-crm-k1-object-seed42-plan702 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-crm-k1-object-seed42-plan702-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-crm-k1-object-seed43-plan702 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-crm-k1-object-seed43-plan702-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-crm-k1-object-seed44-plan702 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-crm-k1-object-seed44-plan702-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-direct-correction-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-direct-correction-object-seed42-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-direct-correction-object-seed42-r3 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-goal-vla-only-wrapper-s42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-k1-crm-accg-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=0.11 | n_rollouts=100\n  conclusion: negative\neval-k1-crm-accg-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.12 | n_rollouts=100\n  conclusion: negative\neval-k1-crm-accg-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.07 | n_rollouts=100\n  conclusion: negative\neval-k1-crm-multiscale-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: negative\neval-k1-crm-multiscale-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.09 | n_rollouts=?\n  conclusion: negative\neval-k1-crm-multiscale-object-seed43-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.09 | n_rollouts=?\n  conclusion: negative\neval-k1-crm-multiscale-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: negative\neval-k1-crm-multiscale-object-seed44-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: negative\neval-loss-combined-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-loss-conformal-object-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-loss-mse-object-seed42 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-loss-perdof-object-seed42 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-object-v4-full | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-v5-full | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-v6-full | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-v7-full | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-v8-full | DONE | server=bjb2-40593 | mode=? | SR=0.13 | n_rollouts=?\n  conclusion: success\neval-object-vla-only-wrapper-s42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-vla-only-wrapper-s42-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-object-vla-only-wrapper-s43 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-vla-only-wrapper-s43-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-object-vla-only-wrapper-s44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-object-vla-only-wrapper-s44-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-obs-only-object-default-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.16 | n_rollouts=?\n  conclusion: success\neval-obs-only-object-default-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: success\neval-obs-only-object-default-seed45-r2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-obs-only-object-default-seed46 | DONE | server=bjb1-32546 | mode=? | SR=0.15 | n_rollouts=?\n  conclusion: success\neval-obs-only-object-default-seed47 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-obs-only-object-default-seed48 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-obs-only-object-default-seed48-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-obs-only-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: negative\neval-openvla-crm-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: negative\neval-openvla-object-baseline-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-openvla-object-baseline-seed42-r2 | DONE | server=n/a | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-openvla-object-vla-only-seed42 | DONE | server=bjb1-18228 | mode=? | SR=0 | n_rollouts=?\n  conclusion: negative\neval-openvla-object-vla-only-seed42-v2 | DONE | server=bjb1-18228 | mode=? | SR=0.69 | n_rollouts=?\n  conclusion: success\neval-openvla-object-vla-only-seed42-v3 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-openvla-oft-object-baseline-seed42 | DONE | server=bjb2-40593 | mode=? | SR=0 | n_rollouts=20\n  conclusion: negative\neval-openvla-oft-official-object | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-perdof-object-default-seed43 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-perdof-object-default-seed44 | DONE | server=autodl-4090 (previous run) | mode=? | SR=0 | n_rollouts=?\n  conclusion: negative\neval-perdof-object-default-seed45 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-perdof-object-default-seed46 | DONE | server=bjb1-32546 | mode=? | SR=0 | n_rollouts=?\n  conclusion: negative\neval-perdof-object-default-seed47 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: negative\neval-perdof-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: success\neval-perdof-object-seed44 | DONE | server=? | mode=? | SR=0.08 | n_rollouts=?\n  conclusion: negative\neval-plan-a-object-seed42 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-plan-a-object-seed43 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-plan-a-object-seed44 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-random-selection-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-random-selection-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-random-selection-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.11 | n_rollouts=10\n  conclusion: success\neval-random-selection-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-random-selection-object-seed46 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-random-selection-object-seed46-r2 | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-random-selection-object-seed46-r3 | DONE | server=bjb1-18228 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-random-selection-object-seed47 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-random-selection-object-seed48 | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-random-selection-object-seed49 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-reconvla-object | DONE | server=? | mode=? | SR=0.12 | n_rollouts=10\n  conclusion: success\neval-scalar-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-scalar-object-seed44 | DONE | server=bjb2-40593 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-scalar-object-seed44-r2 | DONE | server=bjb1-32546 | mode=? | SR=0.06 | n_rollouts=?\n  conclusion: negative\neval-scalar-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.09 | n_rollouts=?\n  conclusion: success\neval-scalar-object-seed45-r2 | DONE | server=bjb2-40593 | mode=? | SR=0.07 | n_rollouts=?\n  conclusion: negative\neval-scalar-object-seed46 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-smolvla-acr-goal-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-smolvla-acr-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-smolvla-crm-goal-seed42 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-smolvla-crm-goal-seed42-v1 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-smolvla-crm-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-smolvla-crm-goal-seed43-v1 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-smolvla-crm-goal-seed44-v1 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-smolvla-crm-goal-seed44-v2 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-smolvla-crm-object-seed42-v1 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-smolvla-crm-object-seed43-v1 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-smolvla-crm-object-seed44-v1 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: negative\neval-smolvla-lerobot-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-smolvla-lerobot-goal-seed43-v2 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-smolvla-lerobot-goal-seed43-v3 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-smolvla-lerobot-goal-seed44-v3 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-smolvla-lerobot-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-smolvla-lerobot-object-seed43-v2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-smolvla-lerobot-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-smolvla-lerobot-object-seed44-v2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-smolvla-lerobot-official-object | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-vla-mean-object | DONE | server=bjb1-32546 | mode=vla_only | SR=12 | n_rollouts=10\n  conclusion: success\neval-vla-mean-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.15 | n_rollouts=?\n  conclusion: success\neval-vla-mean-object-seed44 | DONE | server=bjb1-32546 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-vla-mean-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.13 | n_rollouts=?\n  conclusion: success\neval-vla-only-goal-seed42 | DONE | server=bjb1-32546 | mode=? | SR=0.71 | n_rollouts=?\n  conclusion: success\neval-vla-only-goal-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.69 | n_rollouts=?\n  conclusion: success\neval-vla-only-goal-seed44 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-vla-only-goal-seed44-r2 | DONE | server=bjb2-28827 | mode=vla_only | SR=? | n_rollouts=?\n  conclusion: success\neval-vla-only-goal-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.63 | n_rollouts=10\n  conclusion: success\neval-vla-only-goal-seed46 | DONE | server=bjb1-32546 | mode=? | SR=0.71 | n_rollouts=?\n  conclusion: success\neval-vla-only-goal-seed47 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-vla-only-goal-seed47-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-vla-only-goal-seed48 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\neval-vla-only-goal-seed48-r2 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-vla-only-goal-seed49 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-vla-only-goal-seed51 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=10\n  conclusion: success\neval-vla-only-object | DONE | server=bjb1-32546 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-k1 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-vla-only-object-seed43 | DONE | server=bjb1-32546 | mode=? | SR=0.12 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed44 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\neval-vla-only-object-seed44-r2 | DONE | server=bjb2-40593 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed45 | DONE | server=bjb2-28827 | mode=? | SR=0.09 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed45-r2 | DONE | server=bjb1-18228 | mode=? | SR=0.11 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed46 | DONE | server=bjb1-18228 | mode=? | SR=0.13 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed47 | DONE | server=bjb2-28827 | mode=? | SR=0.1 | n_rollouts=10\n  conclusion: success\neval-vla-only-object-seed48 | DONE | server=bjb2-40593 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed48-r2 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed49 | DONE | server=bjb1-32546 | mode=? | SR=0.1 | n_rollouts=?\n  conclusion: success\neval-vla-only-object-seed50 | DONE | server=bjb1-32546 | mode=? | SR=0.09 | n_rollouts=?\n  conclusion: success\nprecompute-smolvla-goal-bjb1-18228 | DONE | server=bjb1-18228 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\nprecompute-smolvla-goal-bjb1-32546 | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\nprecompute-smolvla-goal-bjb2-28827 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\nprecompute-smolvla-goal-shard0 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\nprecompute-smolvla-goal-shard1 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\nprecompute-smolvla-goal-shard2 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: killed\ntrain-crm-k1-accg-object-seed42 | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: failed\ntrain-crm-k1-accg-object-seed42-fallback | DONE | server=bjb1-32546 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\ntrain-crm-k1-accg-object-seed42-full | DONE | server=bjb2-28827 | mode=? | SR=? | n_rollouts=?\n  conclusion: success\ntrain-crm-k1-accg-object-seed42-v2 | DONE | server=? | mode=? | SR=? | n_rollouts=?\n  conclusion: success",
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

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
This is a lot of experiments. I need to focus on the ones that are actually used for Table 1. The Table 1 values are:
- Goal: VLA-only 83.7±1.3(3s), CRM 83.7±1.8(3s), Adaptive 85.0±1.3(3s)
- Object: VLA-only 77.7±1.3(5s), CRM 76.5±2.3(3s), Adaptive 77.8±2.1(5s)

These success rates are in the 77-85% range, which is quite high. 

But when I look at the registry, most experiments show success rates around 10-15%, with the higher values appearing in wrapper variants or pi0.5 runs. Looking more closely at the specific seed runs, I'm seeing values like 71%, 69%, 67%, and 72% for the goal experiments, which don't align with the 83-85% reported in Table 1.

The object-only experiments show 12% success rates, so those aren't matching either. The Table 1 values must be coming from newer experiments—likely the ones with the "supp" prefix or wrapper variants that I filtered out earlier. I need to search again including those suppressed entries to find where the Table 1 data actually comes from, or check if there's a different experiment set I'm missing. I'm noticing the Object Adaptive result completes the table at 77.8±2.1 with 5 seeds. The SR values in the 80% range for Goal tasks and mid-to-high 70s for Object tasks align with the newer evaluation runs, while older experiments show lower performance in the 60-70% range. I'll search the servers directly by scanning all eval JSON files for matching Goal and Object metrics—that's the most straightforward way to identify which experiments produced these results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "d4973fde-ef5f-465d-b92c-474c2a91d9ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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


### Assistant

_source line 27_

The registry has too many experiments to pinpoint Table 1 sources. Let me go directly to the servers and scan all eval JSON files. I'll hit all 4 servers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "553e6892-5c44-4ae2-a0b0-ff8a684af27c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NUs4dKZwPLBPMSAKRMTXxB`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\" -o -name \"eval_object_*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "7529e700-5972-480a-af17-971ab09a5709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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

_source line 29 · 2026-05-25T02:02:34.950Z_

<details><summary>↩ Tool result · `toolu_01NUs4dKZwPLBPMSAKRMTXxB`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "9dfbb981-bdb6-47f8-ba6e-7fe7d39b3078",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0174bmd7yG9nzPQrnrGPo2nM`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\" -o -name \"eval_object_*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "a4ea43d7-646d-454a-b405-c2336a259244",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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

_source line 31 · 2026-05-25T02:02:35.890Z_

<details><summary>↩ Tool result · `toolu_0174bmd7yG9nzPQrnrGPo2nM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "119002da-ce0c-4ff9-bf94-34234ef6dc2c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YWeGQxSAmDhDv7pahpTZ2r`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\" -o -name \"eval_object_*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "80f76f8d-816b-4849-9b47-6094fc17dbec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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

_source line 33 · 2026-05-25T02:02:36.834Z_

<details><summary>↩ Tool result · `toolu_01YWeGQxSAmDhDv7pahpTZ2r`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "b69cb69e-937b-4cd5-96e2-61c273ef8ea9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SkcCJWCncfG79jn7UXZYQG`</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\" -o -name \"eval_object_*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "dc177180-564c-4b23-bb92-dc9e186c9da0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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

_source line 35 · 2026-05-25T02:02:37.698Z_

<details><summary>↩ Tool result · `toolu_01SkcCJWCncfG79jn7UXZYQG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "1dba97cc-7396-47d0-8c05-b1d9ed5290a1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CKYYmfUKWDqgMTn2M1ZZ2a`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\" -o -name \"eval_object_*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "8c346b43-88b5-44c2-90a9-d3d52e9a58bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hAt71MVXahmei7cDdjWxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8974
      },
      "output_tokens": 8,
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

_source line 37 · 2026-05-25T02:02:38.669Z_

<details><summary>↩ Tool result · `toolu_01CKYYmfUKWDqgMTn2M1ZZ2a`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "a9a24a00-9afc-4238-b14d-af78645966bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
The `-o` flag is being interpreted as a shell metacharacter issue. Let me use a different approach - maybe use `find` with a pattern that doesn't use `-o`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "019e2866-dcc7-441e-8b2d-74222fedf78b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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


### Assistant

_source line 39_

The `-o` flag is being blocked. Let me use separate find commands.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "b9766ed9-35ec-4a50-b714-9b919d156c07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01L1Bio2XkSnvdtbTy6iuMSh`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "f4c3fd8a-00b1-4ec6-a615-8a1681aa1925",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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

_source line 41 · 2026-05-25T02:02:44.390Z_

<details><summary>↩ Tool result · `toolu_01L1Bio2XkSnvdtbTy6iuMSh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "f10cc38b-3cb2-4204-bc46-31b5c78155fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018QGK8d33WHCeRMBqpwiqio`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "45597ffa-4956-45ee-9bfd-14a2d347fba1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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

_source line 43 · 2026-05-25T02:02:45.206Z_

<details><summary>↩ Tool result · `toolu_018QGK8d33WHCeRMBqpwiqio`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "caedec87-fd31-4555-ac8f-53f1daee3229",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.79}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014By9e5iAFh11Ajcd3mXVmu`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "e8954a27-e7c2-408d-b309-acc3f582a07f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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

_source line 45 · 2026-05-25T02:02:46.083Z_

<details><summary>↩ Tool result · `toolu_014By9e5iAFh11Ajcd3mXVmu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "d1c0b747-f525-4b99-bccf-0578f015a5fe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed51.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_tau0.25_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GYctagW7vjnaYu47NFirr6`</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "93425a0d-ead0-4806-94d6-c07c1659d1ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019u3YQfuhTWS5RJneRxf5gr`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_goal_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "7f7840f5-2ea4-4206-ac20-e33bd632e74f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjbSKvGXuhtTN7fHYabTou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 38901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2169
      },
      "output_tokens": 8,
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

_source line 48 · 2026-05-25T02:02:47.138Z_

<details><summary>↩ Tool result · `toolu_01GYctagW7vjnaYu47NFirr6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "366e9f98-1ef7-443a-89c8-88021b4eaff6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.81}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-25T02:02:47.909Z_

<details><summary>↩ Tool result · `toolu_019u3YQfuhTWS5RJneRxf5gr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "6828bc48-2bc7-4e69-b1a8-8aa7128631c1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.76}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Now let me find Object files on all servers too.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "57c40ea0-4146-489d-be11-a32f2e031de3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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


### Assistant

_source line 51_

Now let me find Object files on all servers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "7f777eb0-94df-41f0-b547-53b5fc69df6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E8bjazX4aydve7a1eFenvn`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "a14b38d7-c11a-41eb-9a68-7da403d98b55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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

_source line 53 · 2026-05-25T02:02:56.168Z_

<details><summary>↩ Tool result · `toolu_01E8bjazX4aydve7a1eFenvn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed45.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "ec0eff76-5e8b-4f03-a0cf-80a3b5150fc8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed45.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed45.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HPwTKVZbXJzZf7HVw4XG9Y`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "f25447b2-976d-45a4-8e64-5b40c9693273",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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

_source line 55 · 2026-05-25T02:02:57.198Z_

<details><summary>↩ Tool result · `toolu_01HPwTKVZbXJzZf7HVw4XG9Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_a1_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "802d3c78-a74e-4a21-8bdd-93828b8fdfc6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_a1_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_a1_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0195nFdtvgZ4hbt1bKJubLNg`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "4d164a2a-104c-4b45-94ea-0d540cad28f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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

_source line 57 · 2026-05-25T02:02:58.117Z_

<details><summary>↩ Tool result · `toolu_0195nFdtvgZ4hbt1bKJubLNg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "a7112887-f891-44b4-9879-eaa6a6101fb6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018LkU97dzjvUCACvHpupX8a`</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "15e883ac-5078-4cf6-b634-1b65d4f9b2f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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

_source line 59 · 2026-05-25T02:02:59.171Z_

<details><summary>↩ Tool result · `toolu_018LkU97dzjvUCACvHpupX8a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "bdce1150-cbbc-453b-b2b0-e7fb03d93954",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016pkEK792NZoDnLFRtm3zDh`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "4586bbbd-b549-44fc-bc65-c75fd240ca27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZER9iAPzgdCThvogaKgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 41070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3425
      },
      "output_tokens": 8,
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

_source line 61 · 2026-05-25T02:02:59.793Z_

<details><summary>↩ Tool result · `toolu_016pkEK792NZoDnLFRtm3zDh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed55.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed76.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed77.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "a4eae59f-8384-4d58-8602-015a548f4ec3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed55.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed76.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed77.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed55.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed76.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed77.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Now I need to identify which files are relevant for Table 1. Table 1 uses:

For Goal:
- VLA-only: 83.7±1.3 (3 seeds)
- CRM: 83.7±1.8 (3 seeds)
- Adaptive: 85.0±1.3 (3 seeds)

For Object:
- VLA-only: 77.7±1.3 (5 seeds)
- CRM: 76.5±2.3 (3 seeds)
- Adaptive: 77.8±2.1 (5 seeds)


I'm mapping out the specific evaluation files for each method and metric combination, filtering for the right seed counts and excluding certain variants like pi05 and r2 configurations.

Now I need to verify the actual success rate values stored in these files—whether they're stored as decimals like 0.837 or as percentages like 83.7—and then cross-reference the ROADMAP to confirm which exact experiments contribute to Table 1.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "1b62f1d8-cebe-4f43-b752-1354dd8cef73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwGy3tTVhrsiys9bWKgXUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7759,
      "cache_read_input_tokens": 44495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7759
      },
      "output_tokens": 8,
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


### Assistant

_source line 63_

Let me check the ROADMAP and the table generation script to understand which seeds are used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "6db1bfc8-27f9-48b3-8dbf-e27f9ce95510",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwGy3tTVhrsiys9bWKgXUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7759,
      "cache_read_input_tokens": 44495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7759
      },
      "output_tokens": 8,
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

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01CmVbmaPnqWn9haBQ3yQbid`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ -name \"ROADMAP.md\" -type f 2>/dev/null",
  "description": "Find ROADMAP file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "3dd1a1ae-90a1-4db0-adbf-c8c0c53037aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwGy3tTVhrsiys9bWKgXUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7759,
      "cache_read_input_tokens": 44495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7759
      },
      "output_tokens": 8,
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

_source line 65 · 2026-05-25T02:03:12.181Z_

<details><summary>↩ Tool result · `toolu_01CmVbmaPnqWn9haBQ3yQbid`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "1f3feefd-740c-49be-a912-e24fe63a7c13",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
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

_source line 66_

<details open><summary>🔧 Tool call — Grep · `toolu_011ycU4yzRqvYD9DdWZsv9JC`</summary>

```json
{
  "pattern": "Table.?1|table_1|generate_table|83\\.7|85\\.0|77\\.7|76\\.5|77\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "6d7c484b-b46a-4ab7-a922-d9d8daee2d3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwGy3tTVhrsiys9bWKgXUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7759,
      "cache_read_input_tokens": 44495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7759
      },
      "output_tokens": 8,
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

_source line 67 · 2026-05-25T02:03:14.356Z_

<details><summary>↩ Tool result · `toolu_011ycU4yzRqvYD9DdWZsv9JC`</summary>

```text
Found 250 files limit: 250
logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry2.log
logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry2.log
logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log
logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log
logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log
logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry1.log
logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl
logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl
logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.jsonl
report.md
registry.yaml
logs/workers/worker_fix_cqa1-timeout-resubmit_20260525T011711_retry1.log
mistakes.yaml
logs/chats/cron_hook_eval-k2-tau020-spatial-s42.jsonl
checkpoints/eval-k2-tau025-spatial-s42_QUEUED_20260525T010506.json
checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010351.json
logs/ralph_loop_timeline.jsonl
checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010037.json
checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010031.json
checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010017.json
checkpoints/eval-k2-tau020-spatial-s42_RUNNING_20260525T010009.json
logs/workers/worker_fix_bjb2-40593-k2-tau-overlap_20260525T004500.log
logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_result.json
logs/chats/worker_harvest_14-stale-completed-experiments_20260525T004657.jsonl
logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_retry1.log
logs/workers/worker_harvest_pi05-vla-only-retry_20260525T004709_retry1.log
checkpoints/eval-k2-tau030-spatial-s42_DONE_20260525T005222.json
checkpoints/eval-k2-tau030-spatial-s42_RUNNING_20260525T005133.json
logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_result.json
logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry2.log
logs/workers/worker_diagnose_eval-k2-tau015-spatial-s42_20260525T004449.log
memory.md
logs/chats/cron_hook_eval-k2-tau015-spatial-s42.jsonl
checkpoints/eval-k2-tau015-spatial-s42_DONE_20260525T004202.json
checkpoints/eval-k2-tau015-spatial-s42_RUNNING_20260525T004158.json
logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry1.log
checkpoints/eval-supp-crm-norm005-goal-s48_DONE_20260525T003515.json
checkpoints/eval-supp-crm-norm005-spatial-s49_DONE_20260525T003511.json
checkpoints/eval-supp-crm-norm005-spatial-s48_DONE_20260525T003507.json
checkpoints/eval-supp-long-vla-only-s43-r2_DONE_20260524T235816.json
checkpoints/eval-supp-long-vla-only-s43-r2_RUNNING_20260524T235813.json
checkpoints/eval-supp-goal-vla-only-s42-bjb1_DONE_20260524T235803.json
checkpoints/eval-supp-goal-vla-only-s42-bjb1_RUNNING_20260524T235759.json
checkpoints/eval-supp-crm-norm005-goal-s48_DONE_20260524T235749.json
checkpoints/eval-supp-crm-norm005-goal-s48_RUNNING_20260524T235745.json
checkpoints/eval-supp-crm-norm005-spatial-s49_DONE_20260524T235735.json
checkpoints/eval-supp-crm-norm005-spatial-s49_RUNNING_20260524T235732.json
checkpoints/eval-supp-crm-norm005-spatial-s48_DONE_20260524T235722.json
checkpoints/eval-supp-crm-norm005-spatial-s48_RUNNING_20260524T235718.json
checkpoints/crm-norm005-goal-s49_DONE_20260524T235708.json
checkpoints/crm-norm005-goal-s49_RUNNING_20260524T235705.json
checkpoints/eval-supp-obj-vla-only-s44_DONE_20260524T235654.json
checkpoints/eval-supp-obj-vla-only-s44_RUNNING_20260524T235651.json
checkpoints/crm-norm005-object-s48_DONE_20260524T235640.json
checkpoints/crm-norm005-object-s48_RUNNING_20260524T235637.json
checkpoints/eval-supp-obj-vla-only-s43_DONE_20260524T235627.json
checkpoints/eval-supp-obj-vla-only-s43_RUNNING_20260524T235623.json
checkpoints/eval-supp-obj-vla-only-s42_DONE_20260524T235613.json
checkpoints/eval-supp-obj-vla-only-s42_RUNNING_20260524T235610.json
checkpoints/eval-supp-goal-vla-only-s42_DONE_20260524T235451.json
checkpoints/eval-supp-goal-vla-only-s42_RUNNING_20260524T235448.json
logs/workers/worker_harvest_pi05-vla-only-12-entries_20260524T234439_retry1.log
logs/workers/worker_debug_harvest-worker-registry-bug_20260524T234456_retry1_retry2.log
logs/workers/worker_check_stale-running-cleanup_20260524T234143_result.json
logs/workers/worker_check_stale-running-cleanup_20260524T234143_retry2.log
logs/chats/worker_debug_harvest-worker-registry-bug_20260524T234456.jsonl
logs/workers/worker_debug_harvest-worker-registry-bug_20260524T234456_retry1.log
logs/workers/worker_check_stale-running-cleanup_20260524T234143_retry1.log
logs/workers/worker_check_cqa1-canonical-status_20260524T234136_retry2.log
logs/workers/worker_check_cqa1-canonical-status_20260524T234136_retry1.log
checkpoints/eval-k2-tau010-015-spatial-s42_PREPARING_20260524T234016.json
checkpoints/eval-k2-tau010-spatial-s42_PREPARING_20260524T234012.json
checkpoints/eval-k2-tau030-spatial-s42_RUNNING_20260524T233937.json
checkpoints/eval-k2-tau020-spatial-s42_RUNNING_20260524T233930.json
checkpoints/eval-k2-tau015-spatial-s42_RUNNING_20260524T233922.json
checkpoints/eval-k2-tau035-spatial-s42_QUEUED_20260524T233853.json
checkpoints/eval-k2-tau030-spatial-s42_QUEUED_20260524T233845.json
checkpoints/eval-k2-tau025-spatial-s42_QUEUED_20260524T233838.json
checkpoints/eval-k2-tau020-spatial-s42_QUEUED_20260524T233831.json
checkpoints/eval-k2-tau015-spatial-s42_QUEUED_20260524T233823.json
logs/workers/worker_audit_s47-duplicate-data_20260524T232536_retry1.log
ROADMAP.md
decisions.yaml
logs/chats/worker_audit_canonical-data-protocol_20260524T224440.jsonl
logs/workers/worker_audit_canonical-data-protocol_20260524T224440_retry1.log
logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_result.json
logs/chats/worker_analysis_per-task-spatial-breakdown_20260524T222035.jsonl
logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_retry1_retry2.log
artifacts/spatial_per_task_breakdown.md
logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry2.log
logs/workers/worker_analysis_s42-adaptive-cross-run_20260524T222048_result.json
logs/chats/worker_analysis_s42-adaptive-cross-run_20260524T222048.jsonl
logs/workers/worker_analysis_s42-adaptive-cross-run_20260524T222048_retry1.log
logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry1.log
logs/workers/worker_deploy_k2-tau-sweep-bjb2-40593_20260524T213757_retry1.log
paper_framing.md
logs/workers/worker_audit_table1-K-values_20260524T213618_result.json
logs/workers/worker_audit_table1-K-values_20260524T213618_retry1.log
logs/chats/worker_deploy_tau-sweep-extensions_20260524T212027.jsonl
logs/workers/worker_deploy_tau-sweep-extensions_20260524T212027_retry1.log
logs/workers/worker_verify_spatial-vla-only-s42-model_20260524T211224_result.json
logs/workers/worker_harvest_bjb1-32546-vla-baselines_20260524T210940_retry2.log
logs/workers/worker_verify_spatial-vla-only-s42-model_20260524T211224_retry1.log
logs/workers/worker_harvest_cqa1-32758-vla-baselines_20260524T210954_retry2.log
logs/workers/worker_harvest_cqa1-32758-vla-baselines_20260524T210954_retry1.log
logs/workers/worker_harvest_bjb1-32546-vla-baselines_20260524T210940_retry1.log
artifacts/manifest.yaml
artifacts/_project/report/table1_8seed_v2.md
logs/workers/worker_deploy_cqa1-32758-6gpu_20260524T192742_retry2.log
logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_result.json
logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_retry2.log
logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_retry1.log
logs/workers/worker_deploy_bjb1-18228-gpu12_20260524T201758_retry1.log
checkpoints/crm-norm005-goal-s49_RUNNING_20260524T202925.json
checkpoints/crm-norm005-object-s48_RUNNING_20260524T202918.json
checkpoints/crm-norm005-goal-s49_QUEUED_20260524T202902.json
checkpoints/crm-norm005-object-s48_QUEUED_20260524T202855.json
logs/workers/worker_deploy_fill-idle-gpus-bjb1-bjb2_20260524T201646_retry1.log
checkpoints/eval-supp-crm-norm005-goal-s48_RUNNING_20260524T202432.json
checkpoints/eval-supp-crm-norm005-spatial-s49_RUNNING_20260524T202425.json
checkpoints/eval-supp-crm-norm005-spatial-s48_RUNNING_20260524T202418.json
checkpoints/eval-supp-long-vla-only-s43-r2_RUNNING_20260524T202411.json
checkpoints/eval-supp-goal-vla-only-s42-bjb1_RUNNING_20260524T202404.json
checkpoints/eval-supp-obj-vla-only-s44_RUNNING_20260524T202357.json
checkpoints/eval-supp-obj-vla-only-s43_RUNNING_20260524T202350.json
checkpoints/eval-supp-obj-vla-only-s42_RUNNING_20260524T202342.json
checkpoints/eval-supp-crm-norm005-goal-s48_QUEUED_20260524T202327.json
checkpoints/eval-supp-crm-norm005-spatial-s49_QUEUED_20260524T202320.json
checkpoints/eval-supp-crm-norm005-spatial-s48_QUEUED_20260524T202311.json
logs/chats/worker_code_add-bf16-redeploy-pi05-reconvla_20260524T201900.jsonl
logs/workers/worker_code_add-bf16-redeploy-pi05-reconvla_20260524T201900_retry1.log
checkpoints/eval-supp-long-vla-only-s43-r2_QUEUED_20260524T202303.json
checkpoints/eval-supp-goal-vla-only-s42-bjb1_QUEUED_20260524T202256.json
checkpoints/eval-supp-obj-vla-only-s44_QUEUED_20260524T202249.json
checkpoints/eval-supp-obj-vla-only-s43_QUEUED_20260524T202242.json
checkpoints/eval-supp-obj-vla-only-s42_QUEUED_20260524T202234.json
checkpoints/eval-supp-crm-norm005-goal-s48_PENDING_20260524T202223.json
checkpoints/eval-supp-crm-norm005-spatial-s49_PENDING_20260524T202215.json
checkpoints/eval-supp-crm-norm005-spatial-s48_PENDING_20260524T202208.json
checkpoints/eval-supp-long-vla-only-s43-r2_PENDING_20260524T202159.json
checkpoints/eval-supp-goal-vla-only-s42-bjb1_PENDING_20260524T202149.json
checkpoints/eval-supp-obj-vla-only-s44_PENDING_20260524T202142.json
checkpoints/eval-supp-obj-vla-only-s43_PENDING_20260524T202135.json
checkpoints/eval-supp-obj-vla-only-s42_PENDING_20260524T202127.json
checkpoints/crm-norm005-goal-s49_PENDING_20260524T202012.json
checkpoints/crm-norm005-object-s48_PENDING_20260524T202005.json
artifacts/_project/data/table1_8seed_final.md
logs/chats/worker_scan_tau-k-sweep-k5-status_20260524T201027.jsonl
logs/workers/worker_scan_tau-k-sweep-k5-status_20260524T201027_retry1.log
logs/chats/cron_hook_train-crm-pi05-unified-3suite-r2.jsonl
logs/workers/worker_deploy_cqa1-32758-6gpu_20260524T192742_retry1.log
logs/workers/worker_investigate_pi05-object-s43-conflict_20260524T192714_retry2.log
logs/workers/worker_investigate_pi05-object-s43-conflict_20260524T192714_retry1.log
logs/chats/worker_scan_d139-seed-status-all-servers_20260524T192909.jsonl
logs/workers/worker_scan_d139-seed-status-all-servers_20260524T192909_retry1.log
logs/workers/worker_monitor_gpu-scan-harvest-r7_20260524T192151_retry2.log
artifacts/_project/report/gpu_scan_r7_9dfa78.md
logs/workers/worker_check_bjb1-18228-critical-exps_20260524T192333_retry1.log
logs/workers/worker_monitor_gpu-scan-harvest-r7_20260524T192151_retry1.log
artifacts/_project/report/gpu_scan_r7.md
artifacts/gpu_scan_r7.md
logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_paper_agent.jsonl
.claude/sessions/paper_agent_f11cbd51/AGENTS.md
.claude/sessions/paper_agent_f11cbd51/CLAUDE.md
logs/workers/worker_monitor_harvest-loop-r1_20260524T191135_result.json
logs/workers/worker_monitor_harvest-loop-r1_20260524T191135.log
docs/paper/experiments.tex
docs/paper/appendix.tex
.registry_hp5nas9m.tmp
logs/workers/worker_harvest_eval-supp-long-k2mean-s47-r2_20260524T155120_retry2.log
logs/workers/worker_harvest_eval-supp-long-k2mean-s47-r2_20260524T155120_retry1.log
logs/workers/worker_diagnose_eval-supp-long-k2mean-s47-r2_20260524T154330_retry2.log
logs/workers/worker_diagnose_eval-supp-long-k2mean-s47-r2_20260524T154330_retry1.log
logs/chats/cron_hook_eval-supp-long-k2mean-s47-r2.jsonl
logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_result.json
logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_retry2.log
logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_retry1.log
logs/workers/worker_harvest_spatial-adapt-s47_20260524T132710.log
logs/workers/worker_harvest_spatial-k2mean-s47_20260524T132224.log
logs/chats/cron_hook_eval-supp-obj-reconvla-s47.jsonl
logs/workers/worker_harvest_obj-reconvla-s47_20260524T123141_retry1.log
logs/workers/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937_result.json
logs/chats/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937.jsonl
logs/workers/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937_retry1.log
worker_output.md
logs/workers/worker_harvest_goal-crm-s47_20260524T120138_retry1.log
logs/workers/worker_verify_crm-obj-s47-anomaly_20260524T115755_retry1.log
logs/workers/worker_harvest_goal-reconvla-s47_20260524T120045_retry1.log
logs/workers/worker_diagnose_goal-vla-s47-r3-crash_20260524T112412_retry2.log
logs/workers/worker_diagnose_goal-vla-s47-r3-crash_20260524T112412_retry1.log
logs/chats/worker_fix_registry-s45-s46-cleanup_20260524T110058.jsonl
logs/workers/worker_fix_registry-s45-s46-cleanup_20260524T110058_retry1.log
logs/workers/worker_monitor_scan-all-running-evals_20260524T103511_retry1.log
logs/workers/worker_fix_bjb2-28827-ghost-cleanup_20260524T100348_retry2.log
logs/workers/worker_fix_bjb2-28827-ghost-cleanup_20260524T100348_retry1.log
logs/workers/worker_research_a1-vla-phase1_20260524T091251_retry2.log
artifacts/_project/report/a1_vla_survey_and_crm_analysis.md
logs/workers/worker_deploy_bjb2-28827-6gpu-goal-obj-s47_20260524T094131_retry1.log
logs/workers/worker_health_full-gpu-scan-all-servers_20260524T093345_retry2.log
logs/workers/worker_health_full-gpu-scan-all-servers_20260524T093345_retry1.log
logs/workers/worker_research_a1-vla-phase1_20260524T091251_retry1.log
logs/workers/worker_deploy_bjb1-32546-gpu0-gpu2_20260524T082906_retry2.log
logs/workers/worker_deploy_bjb1-32546-gpu0-gpu2_20260524T082906_retry1.log
logs/workers/worker_monitor_stale-experiments-check_20260524T082347_retry2.log
logs/workers/worker_deploy_cqa1-32758-spatial-s47_20260524T071325_retry1.log
logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_result.json
logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_retry2.log
logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_retry1.log
logs/workers/worker_deploy_cqa1-32758-spatial-seeds_20260524T070703_retry1.log
logs/workers/worker_deploy_bjb2-40593-gpu0_20260524T064404_result.json
logs/workers/worker_deploy_bjb2-40593-gpu0_20260524T064404_retry2.log
logs/workers/worker_deploy_bjb1-18228-gpu12_20260524T064352_retry2.log
logs/chats/worker_deploy_cqa1-32758-seeds_20260524T062601.jsonl
logs/workers/worker_deploy_cqa1-32758-seeds_20260524T062601_retry1.log
logs/workers/worker_ops_register-untracked-processes_20260524T061547_retry1.log
logs/chats/cron_hook_precompute-pi05-spatial-2048-r2.jsonl
logs/workers/worker_harvest_bjb2-40593-bjb1-18228_20260524T035325.log
.registry_3rh2tyz0.tmp
logs/workers/worker_audit_false-failures-bulk_20260524T031957.log
logs/chats/cron_hook_eval-supp-spatial-crm-norm005-s46.jsonl
logs/workers/worker_diagnose_cqa1-32758-failures_20260524T031634.log
checkpoints/eval-supp-spatial-k2mean-s45_DONE_20260524T031745.json
logs/chats/cron_hook_eval-supp-spatial-reconvla-s46.jsonl
logs/chats/cron_hook_eval-supp-k2mean-object-s42.jsonl
logs/chats/cron_hook_eval-supp-obj-adapt-tau025-s42.jsonl
checkpoints/eval-supp-spatial-k2mean-s45_DONE_20260524T022418.json
checkpoints/eval-supp-spatial-k2mean-s45_RUNNING_20260524T022415.json
logs/chats/cron_hook_train-crm-unified-4suite-r6.jsonl
logs/chats/cron_hook_eval-supp-crm-norm005-spatial-s44.jsonl
logs/chats/cron_hook_eval-supp-crm-norm005-spatial-s43.jsonl
logs/chats/cron_hook_eval-supp-reconvla-k2-spatial-s42.jsonl
logs/workers/worker_ssh_scan-bjb1-32546-bjb2-40593_20260524T004828.log
logs/chats/cron_hook_eval-supp-adapt-tau025-spatial-s44.jsonl
task_context/director.md
logs/chats/archive/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director_20260524T005550_264054.jsonl
task_context/agent.md
logs/chats/archive/cron_hook_eval-supp-adapt-tau025-spatial-s44_20260524T005546_856213.jsonl
logs/chats/archive/cron_hook_eval-supp-crm-norm005-spatial-s43_20260524T005536_574438.jsonl
logs/chats/archive/cron_hook_eval-supp-reconvla-k2-spatial-s42_20260524T005531_358713.jsonl
logs/workers/worker_ssh_scan-bjb2-28827-cqa1-32758_20260524T004847.log
logs/workers/worker_ssh_harvest-spatial-vla-s45-deploy_20260524T003005.log
logs/chats/cron_hook_eval-supp-spatial-reconvla-s45.jsonl
logs/workers/worker_ssh_harvest-goal-k2mean-s45-deploy_20260524T001854_result.json
logs/workers/worker_ssh_harvest-goal-k2mean-s45-deploy_20260524T001854.log
logs/workers/worker_ssh_harvest-spatial-reconvla-s45-deploy_20260524T001644.log
logs/workers/worker_ssh_kill-dup-deploy-cqa1-cuda2_20260523T234353.log
logs/workers/worker_ssh_scan-bjb1-bjb2-28827_20260523T233833.log
logs/workers/worker_ssh_scan-cqa1-bjb2-40593_20260523T233806.log
logs/chats/cron_hook_eval-supp-obj-reconvla-s42.jsonl
logs/chats/cron_hook_eval-object-vla-only-wrapper-s43-r2.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "3ee517c9-fbe7-4bb3-af7a-db564e22cdfe",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry2.log",
      "logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry2.log",
      "logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log",
      "logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log",
      "logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log",
      "logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry1.log",
      "logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl",
      "logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl",
      "logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.jsonl",
      "report.md",
      "registry.yaml",
      "logs/workers/worker_fix_cqa1-timeout-resubmit_20260525T011711_retry1.log",
      "mistakes.yaml",
      "logs/chats/cron_hook_eval-k2-tau020-spatial-s42.jsonl",
      "checkpoints/eval-k2-tau025-spatial-s42_QUEUED_20260525T010506.json",
      "checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010351.json",
      "logs/ralph_loop_timeline.jsonl",
      "checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010037.json",
      "checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010031.json",
      "checkpoints/eval-k2-tau020-spatial-s42_DONE_20260525T010017.json",
      "checkpoints/eval-k2-tau020-spatial-s42_RUNNING_20260525T010009.json",
      "logs/workers/worker_fix_bjb2-40593-k2-tau-overlap_20260525T004500.log",
      "logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_result.json",
      "logs/chats/worker_harvest_14-stale-completed-experiments_20260525T004657.jsonl",
      "logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_retry1.log",
      "logs/workers/worker_harvest_pi05-vla-only-retry_20260525T004709_retry1.log",
      "checkpoints/eval-k2-tau030-spatial-s42_DONE_20260525T005222.json",
      "checkpoints/eval-k2-tau030-spatial-s42_RUNNING_20260525T005133.json",
      "logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_result.json",
      "logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry2.log",
      "logs/workers/worker_diagnose_eval-k2-tau015-spatial-s42_20260525T004449.log",
      "memory.md",
      "logs/chats/cron_hook_eval-k2-tau015-spatial-s42.jsonl",
      "checkpoints/eval-k2-tau015-spatial-s42_DONE_20260525T004202.json",
      "checkpoints/eval-k2-tau015-spatial-s42_RUNNING_20260525T004158.json",
      "logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry1.log",
      "checkpoints/eval-supp-crm-norm005-goal-s48_DONE_20260525T003515.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s49_DONE_20260525T003511.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s48_DONE_20260525T003507.json",
      "checkpoints/eval-supp-long-vla-only-s43-r2_DONE_20260524T235816.json",
      "checkpoints/eval-supp-long-vla-only-s43-r2_RUNNING_20260524T235813.json",
      "checkpoints/eval-supp-goal-vla-only-s42-bjb1_DONE_20260524T235803.json",
      "checkpoints/eval-supp-goal-vla-only-s42-bjb1_RUNNING_20260524T235759.json",
      "checkpoints/eval-supp-crm-norm005-goal-s48_DONE_20260524T235749.json",
      "checkpoints/eval-supp-crm-norm005-goal-s48_RUNNING_20260524T235745.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s49_DONE_20260524T235735.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s49_RUNNING_20260524T235732.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s48_DONE_20260524T235722.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s48_RUNNING_20260524T235718.json",
      "checkpoints/crm-norm005-goal-s49_DONE_20260524T235708.json",
      "checkpoints/crm-norm005-goal-s49_RUNNING_20260524T235705.json",
      "checkpoints/eval-supp-obj-vla-only-s44_DONE_20260524T235654.json",
      "checkpoints/eval-supp-obj-vla-only-s44_RUNNING_20260524T235651.json",
      "checkpoints/crm-norm005-object-s48_DONE_20260524T235640.json",
      "checkpoints/crm-norm005-object-s48_RUNNING_20260524T235637.json",
      "checkpoints/eval-supp-obj-vla-only-s43_DONE_20260524T235627.json",
      "checkpoints/eval-supp-obj-vla-only-s43_RUNNING_20260524T235623.json",
      "checkpoints/eval-supp-obj-vla-only-s42_DONE_20260524T235613.json",
      "checkpoints/eval-supp-obj-vla-only-s42_RUNNING_20260524T235610.json",
      "checkpoints/eval-supp-goal-vla-only-s42_DONE_20260524T235451.json",
      "checkpoints/eval-supp-goal-vla-only-s42_RUNNING_20260524T235448.json",
      "logs/workers/worker_harvest_pi05-vla-only-12-entries_20260524T234439_retry1.log",
      "logs/workers/worker_debug_harvest-worker-registry-bug_20260524T234456_retry1_retry2.log",
      "logs/workers/worker_check_stale-running-cleanup_20260524T234143_result.json",
      "logs/workers/worker_check_stale-running-cleanup_20260524T234143_retry2.log",
      "logs/chats/worker_debug_harvest-worker-registry-bug_20260524T234456.jsonl",
      "logs/workers/worker_debug_harvest-worker-registry-bug_20260524T234456_retry1.log",
      "logs/workers/worker_check_stale-running-cleanup_20260524T234143_retry1.log",
      "logs/workers/worker_check_cqa1-canonical-status_20260524T234136_retry2.log",
      "logs/workers/worker_check_cqa1-canonical-status_20260524T234136_retry1.log",
      "checkpoints/eval-k2-tau010-015-spatial-s42_PREPARING_20260524T234016.json",
      "checkpoints/eval-k2-tau010-spatial-s42_PREPARING_20260524T234012.json",
      "checkpoints/eval-k2-tau030-spatial-s42_RUNNING_20260524T233937.json",
      "checkpoints/eval-k2-tau020-spatial-s42_RUNNING_20260524T233930.json",
      "checkpoints/eval-k2-tau015-spatial-s42_RUNNING_20260524T233922.json",
      "checkpoints/eval-k2-tau035-spatial-s42_QUEUED_20260524T233853.json",
      "checkpoints/eval-k2-tau030-spatial-s42_QUEUED_20260524T233845.json",
      "checkpoints/eval-k2-tau025-spatial-s42_QUEUED_20260524T233838.json",
      "checkpoints/eval-k2-tau020-spatial-s42_QUEUED_20260524T233831.json",
      "checkpoints/eval-k2-tau015-spatial-s42_QUEUED_20260524T233823.json",
      "logs/workers/worker_audit_s47-duplicate-data_20260524T232536_retry1.log",
      "ROADMAP.md",
      "decisions.yaml",
      "logs/chats/worker_audit_canonical-data-protocol_20260524T224440.jsonl",
      "logs/workers/worker_audit_canonical-data-protocol_20260524T224440_retry1.log",
      "logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_result.json",
      "logs/chats/worker_analysis_per-task-spatial-breakdown_20260524T222035.jsonl",
      "logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_retry1_retry2.log",
      "artifacts/spatial_per_task_breakdown.md",
      "logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry2.log",
      "logs/workers/worker_analysis_s42-adaptive-cross-run_20260524T222048_result.json",
      "logs/chats/worker_analysis_s42-adaptive-cross-run_20260524T222048.jsonl",
      "logs/workers/worker_analysis_s42-adaptive-cross-run_20260524T222048_retry1.log",
      "logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_retry1.log",
      "logs/workers/worker_deploy_k2-tau-sweep-bjb2-40593_20260524T213757_retry1.log",
      "paper_framing.md",
      "logs/workers/worker_audit_table1-K-values_20260524T213618_result.json",
      "logs/workers/worker_audit_table1-K-values_20260524T213618_retry1.log",
      "logs/chats/worker_deploy_tau-sweep-extensions_20260524T212027.jsonl",
      "logs/workers/worker_deploy_tau-sweep-extensions_20260524T212027_retry1.log",
      "logs/workers/worker_verify_spatial-vla-only-s42-model_20260524T211224_result.json",
      "logs/workers/worker_harvest_bjb1-32546-vla-baselines_20260524T210940_retry2.log",
      "logs/workers/worker_verify_spatial-vla-only-s42-model_20260524T211224_retry1.log",
      "logs/workers/worker_harvest_cqa1-32758-vla-baselines_20260524T210954_retry2.log",
      "logs/workers/worker_harvest_cqa1-32758-vla-baselines_20260524T210954_retry1.log",
      "logs/workers/worker_harvest_bjb1-32546-vla-baselines_20260524T210940_retry1.log",
      "artifacts/manifest.yaml",
      "artifacts/_project/report/table1_8seed_v2.md",
      "logs/workers/worker_deploy_cqa1-32758-6gpu_20260524T192742_retry2.log",
      "logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_result.json",
      "logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_retry2.log",
      "logs/workers/worker_harvest_bjb1-32546-vla-only-results_20260524T205956_retry1.log",
      "logs/workers/worker_deploy_bjb1-18228-gpu12_20260524T201758_retry1.log",
      "checkpoints/crm-norm005-goal-s49_RUNNING_20260524T202925.json",
      "checkpoints/crm-norm005-object-s48_RUNNING_20260524T202918.json",
      "checkpoints/crm-norm005-goal-s49_QUEUED_20260524T202902.json",
      "checkpoints/crm-norm005-object-s48_QUEUED_20260524T202855.json",
      "logs/workers/worker_deploy_fill-idle-gpus-bjb1-bjb2_20260524T201646_retry1.log",
      "checkpoints/eval-supp-crm-norm005-goal-s48_RUNNING_20260524T202432.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s49_RUNNING_20260524T202425.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s48_RUNNING_20260524T202418.json",
      "checkpoints/eval-supp-long-vla-only-s43-r2_RUNNING_20260524T202411.json",
      "checkpoints/eval-supp-goal-vla-only-s42-bjb1_RUNNING_20260524T202404.json",
      "checkpoints/eval-supp-obj-vla-only-s44_RUNNING_20260524T202357.json",
      "checkpoints/eval-supp-obj-vla-only-s43_RUNNING_20260524T202350.json",
      "checkpoints/eval-supp-obj-vla-only-s42_RUNNING_20260524T202342.json",
      "checkpoints/eval-supp-crm-norm005-goal-s48_QUEUED_20260524T202327.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s49_QUEUED_20260524T202320.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s48_QUEUED_20260524T202311.json",
      "logs/chats/worker_code_add-bf16-redeploy-pi05-reconvla_20260524T201900.jsonl",
      "logs/workers/worker_code_add-bf16-redeploy-pi05-reconvla_20260524T201900_retry1.log",
      "checkpoints/eval-supp-long-vla-only-s43-r2_QUEUED_20260524T202303.json",
      "checkpoints/eval-supp-goal-vla-only-s42-bjb1_QUEUED_20260524T202256.json",
      "checkpoints/eval-supp-obj-vla-only-s44_QUEUED_20260524T202249.json",
      "checkpoints/eval-supp-obj-vla-only-s43_QUEUED_20260524T202242.json",
      "checkpoints/eval-supp-obj-vla-only-s42_QUEUED_20260524T202234.json",
      "checkpoints/eval-supp-crm-norm005-goal-s48_PENDING_20260524T202223.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s49_PENDING_20260524T202215.json",
      "checkpoints/eval-supp-crm-norm005-spatial-s48_PENDING_20260524T202208.json",
      "checkpoints/eval-supp-long-vla-only-s43-r2_PENDING_20260524T202159.json",
      "checkpoints/eval-supp-goal-vla-only-s42-bjb1_PENDING_20260524T202149.json",
      "checkpoints/eval-supp-obj-vla-only-s44_PENDING_20260524T202142.json",
      "checkpoints/eval-supp-obj-vla-only-s43_PENDING_20260524T202135.json",
      "checkpoints/eval-supp-obj-vla-only-s42_PENDING_20260524T202127.json",
      "checkpoints/crm-norm005-goal-s49_PENDING_20260524T202012.json",
      "checkpoints/crm-norm005-object-s48_PENDING_20260524T202005.json",
      "artifacts/_project/data/table1_8seed_final.md",
      "logs/chats/worker_scan_tau-k-sweep-k5-status_20260524T201027.jsonl",
      "logs/workers/worker_scan_tau-k-sweep-k5-status_20260524T201027_retry1.log",
      "logs/chats/cron_hook_train-crm-pi05-unified-3suite-r2.jsonl",
      "logs/workers/worker_deploy_cqa1-32758-6gpu_20260524T192742_retry1.log",
      "logs/workers/worker_investigate_pi05-object-s43-conflict_20260524T192714_retry2.log",
      "logs/workers/worker_investigate_pi05-object-s43-conflict_20260524T192714_retry1.log",
      "logs/chats/worker_scan_d139-seed-status-all-servers_20260524T192909.jsonl",
      "logs/workers/worker_scan_d139-seed-status-all-servers_20260524T192909_retry1.log",
      "logs/workers/worker_monitor_gpu-scan-harvest-r7_20260524T192151_retry2.log",
      "artifacts/_project/report/gpu_scan_r7_9dfa78.md",
      "logs/workers/worker_check_bjb1-18228-critical-exps_20260524T192333_retry1.log",
      "logs/workers/worker_monitor_gpu-scan-harvest-r7_20260524T192151_retry1.log",
      "artifacts/_project/report/gpu_scan_r7.md",
      "artifacts/gpu_scan_r7.md",
      "logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_paper_agent.jsonl",
      ".claude/sessions/paper_agent_f11cbd51/AGENTS.md",
      ".claude/sessions/paper_agent_f11cbd51/CLAUDE.md",
      "logs/workers/worker_monitor_harvest-loop-r1_20260524T191135_result.json",
      "logs/workers/worker_monitor_harvest-loop-r1_20260524T191135.log",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex",
      ".registry_hp5nas9m.tmp",
      "logs/workers/worker_harvest_eval-supp-long-k2mean-s47-r2_20260524T155120_retry2.log",
      "logs/workers/worker_harvest_eval-supp-long-k2mean-s47-r2_20260524T155120_retry1.log",
      "logs/workers/worker_diagnose_eval-supp-long-k2mean-s47-r2_20260524T154330_retry2.log",
      "logs/workers/worker_diagnose_eval-supp-long-k2mean-s47-r2_20260524T154330_retry1.log",
      "logs/chats/cron_hook_eval-supp-long-k2mean-s47-r2.jsonl",
      "logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_result.json",
      "logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_retry2.log",
      "logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_retry1.log",
      "logs/workers/worker_harvest_spatial-adapt-s47_20260524T132710.log",
      "logs/workers/worker_harvest_spatial-k2mean-s47_20260524T132224.log",
      "logs/chats/cron_hook_eval-supp-obj-reconvla-s47.jsonl",
      "logs/workers/worker_harvest_obj-reconvla-s47_20260524T123141_retry1.log",
      "logs/workers/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937_result.json",
      "logs/chats/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937.jsonl",
      "logs/workers/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937_retry1.log",
      "worker_output.md",
      "logs/workers/worker_harvest_goal-crm-s47_20260524T120138_retry1.log",
      "logs/workers/worker_verify_crm-obj-s47-anomaly_20260524T115755_retry1.log",
      "logs/workers/worker_harvest_goal-reconvla-s47_20260524T120045_retry1.log",
      "logs/workers/worker_diagnose_goal-vla-s47-r3-crash_20260524T112412_retry2.log",
      "logs/workers/worker_diagnose_goal-vla-s47-r3-crash_20260524T112412_retry1.log",
      "logs/chats/worker_fix_registry-s45-s46-cleanup_20260524T110058.jsonl",
      "logs/workers/worker_fix_registry-s45-s46-cleanup_20260524T110058_retry1.log",
      "logs/workers/worker_monitor_scan-all-running-evals_20260524T103511_retry1.log",
      "logs/workers/worker_fix_bjb2-28827-ghost-cleanup_20260524T100348_retry2.log",
      "logs/workers/worker_fix_bjb2-28827-ghost-cleanup_20260524T100348_retry1.log",
      "logs/workers/worker_research_a1-vla-phase1_20260524T091251_retry2.log",
      "artifacts/_project/report/a1_vla_survey_and_crm_analysis.md",
      "logs/workers/worker_deploy_bjb2-28827-6gpu-goal-obj-s47_20260524T094131_retry1.log",
      "logs/workers/worker_health_full-gpu-scan-all-servers_20260524T093345_retry2.log",
      "logs/workers/worker_health_full-gpu-scan-all-servers_20260524T093345_retry1.log",
      "logs/workers/worker_research_a1-vla-phase1_20260524T091251_retry1.log",
      "logs/workers/worker_deploy_bjb1-32546-gpu0-gpu2_20260524T082906_retry2.log",
      "logs/workers/worker_deploy_bjb1-32546-gpu0-gpu2_20260524T082906_retry1.log",
      "logs/workers/worker_monitor_stale-experiments-check_20260524T082347_retry2.log",
      "logs/workers/worker_deploy_cqa1-32758-spatial-s47_20260524T071325_retry1.log",
      "logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_result.json",
      "logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_retry2.log",
      "logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_retry1.log",
      "logs/workers/worker_deploy_cqa1-32758-spatial-seeds_20260524T070703_retry1.log",
      "logs/workers/worker_deploy_bjb2-40593-gpu0_20260524T064404_result.json",
      "logs/workers/worker_deploy_bjb2-40593-gpu0_20260524T064404_retry2.log",
      "logs/workers/worker_deploy_bjb1-18228-gpu12_20260524T064352_retry2.log",
      "logs/chats/worker_deploy_cqa1-32758-seeds_20260524T062601.jsonl",
      "logs/workers/worker_deploy_cqa1-32758-seeds_20260524T062601_retry1.log",
      "logs/workers/worker_ops_register-untracked-processes_20260524T061547_retry1.log",
      "logs/chats/cron_hook_precompute-pi05-spatial-2048-r2.jsonl",
      "logs/workers/worker_harvest_bjb2-40593-bjb1-18228_20260524T035325.log",
      ".registry_3rh2tyz0.tmp",
      "logs/workers/worker_audit_false-failures-bulk_20260524T031957.log",
      "logs/chats/cron_hook_eval-supp-spatial-crm-norm005-s46.jsonl",
      "logs/workers/worker_diagnose_cqa1-32758-failures_20260524T031634.log",
      "checkpoints/eval-supp-spatial-k2mean-s45_DONE_20260524T031745.json",
      "logs/chats/cron_hook_eval-supp-spatial-reconvla-s46.jsonl",
      "logs/chats/cron_hook_eval-supp-k2mean-object-s42.jsonl",
      "logs/chats/cron_hook_eval-supp-obj-adapt-tau025-s42.jsonl",
      "checkpoints/eval-supp-spatial-k2mean-s45_DONE_20260524T022418.json",
      "checkpoints/eval-supp-spatial-k2mean-s45_RUNNING_20260524T022415.json",
      "logs/chats/cron_hook_train-crm-unified-4suite-r6.jsonl",
      "logs/chats/cron_hook_eval-supp-crm-norm005-spatial-s44.jsonl",
      "logs/chats/cron_hook_eval-supp-crm-norm005-spatial-s43.jsonl",
      "logs/chats/cron_hook_eval-supp-reconvla-k2-spatial-s42.jsonl",
      "logs/workers/worker_ssh_scan-bjb1-32546-bjb2-40593_20260524T004828.log",
      "logs/chats/cron_hook_eval-supp-adapt-tau025-spatial-s44.jsonl",
      "task_context/director.md",
      "logs/chats/archive/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director_20260524T005550_264054.jsonl",
      "task_context/agent.md",
      "logs/chats/archive/cron_hook_eval-supp-adapt-tau025-spatial-s44_20260524T005546_856213.jsonl",
      "logs/chats/archive/cron_hook_eval-supp-crm-norm005-spatial-s43_20260524T005536_574438.jsonl",
      "logs/chats/archive/cron_hook_eval-supp-reconvla-k2-spatial-s42_20260524T005531_358713.jsonl",
      "logs/workers/worker_ssh_scan-bjb2-28827-cqa1-32758_20260524T004847.log",
      "logs/workers/worker_ssh_harvest-spatial-vla-s45-deploy_20260524T003005.log",
      "logs/chats/cron_hook_eval-supp-spatial-reconvla-s45.jsonl",
      "logs/workers/worker_ssh_harvest-goal-k2mean-s45-deploy_20260524T001854_result.json",
      "logs/workers/worker_ssh_harvest-goal-k2mean-s45-deploy_20260524T001854.log",
      "logs/workers/worker_ssh_harvest-spatial-reconvla-s45-deploy_20260524T001644.log",
      "logs/workers/worker_ssh_kill-dup-deploy-cqa1-cuda2_20260523T234353.log",
      "logs/workers/worker_ssh_scan-bjb1-bjb2-28827_20260523T233833.log",
      "logs/workers/worker_ssh_scan-cqa1-bjb2-40593_20260523T233806.log",
      "logs/chats/cron_hook_eval-supp-obj-reconvla-s42.jsonl",
      "logs/chats/cron_hook_eval-object-vla-only-wrapper-s43-r2.jsonl"
    ],
    "numFiles": 250,
    "appliedLimit": 250
  }
}
```

</details>

---


### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Let me look at the table1_8seed_final.md and report.md to understand what seeds were used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "a17ab40c-b6ae-4a8d-b9e7-ed9249bf63be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrT62XPVnBVyhUdotbpk5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7930,
      "cache_read_input_tokens": 52254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7930
      },
      "output_tokens": 8,
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


### Assistant

_source line 69_

Let me check the Table 1 data files and the report to find which seeds are used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "4b607c22-a4dc-4a5b-8bfd-76e5b8f9e6aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrT62XPVnBVyhUdotbpk5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7930,
      "cache_read_input_tokens": 52254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7930
      },
      "output_tokens": 8,
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

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01SFmfKLGSh5Njx4ymtnMyLL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "e8f694d0-88f8-45f0-8573-7127e84f356b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrT62XPVnBVyhUdotbpk5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7930,
      "cache_read_input_tokens": 52254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7930
      },
      "output_tokens": 8,
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

_source line 71 · 2026-05-25T02:03:24.089Z_

<details><summary>↩ Tool result · `toolu_01SFmfKLGSh5Njx4ymtnMyLL`</summary>

```text
1	# Table 1 — Multi-seed Results (Clean supp-era data)
2	
3	Generated: 2026-05-24 20:10 UTC
4	
5	## Main Table
6	
7	| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
8	|-------|---------|-------------|-------------------|--------|--------|
9	| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
10	| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
11	| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
12	| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |
13	
14	## Paired t-test: Δ(A-V) = Adaptive - VLA-only
15	
16	| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
17	|-------|---------|--------|---------|-----------|-------|
18	| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
19	| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |
20	| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |
21	| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |
22	
23	## Paired t-test: Δ(A-C) = Adaptive - CRM always-on
24	
25	| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
26	|-------|---------|--------|---------|-----------|-------|
27	| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |
28	| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |
29	| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |
30	| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |
31	
32	## Trigger Rate ↔ Effect Size (D140 key evidence)
33	
34	| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |
35	|-------|------------------|--------|-------------|
36	| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |
37	| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |
38	| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |
39	| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |
40	
41	## Per-seed Raw Data
42	
43	### Spatial (8 matched seeds)
44	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
45	|------|---------|----------|-----|--------|
46	| s42 | 80.0% | 82.0% | — | +2.0pp |
47	| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |
48	| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |
49	| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |
50	| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |
51	| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |
52	| s48 | 79.5% | 81.0% | — | +1.5pp |
53	| s49 | 78.5% | 82.0% | — | +3.5pp |
54	
55	### Goal (7 matched seeds for A-V)
56	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
57	|------|---------|----------|-----|--------|
58	| s42 | — | 84.0% | 85.5% | — |
59	| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |
60	| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |
61	| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |
62	| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |
63	| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |
64	| s48 | 85.0% | 84.5% | — | -0.5pp |
65	| s49 | 82.0% | 81.5% | — | -0.5pp |
66	
67	### Object (5 matched seeds for A-V)
68	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
69	|------|---------|----------|-----|--------|
70	| s42 | — | 81.0% | 77.0% | — |
71	| s43 | — | 77.5% | 78.5% | — |
72	| s44 | — | 75.0% | 74.0% | — |
73	| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
74	| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
75	| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
76	| s48 | 79.0% | 76.0% | — | -3.0pp |
77	| s49 | 75.5% | 74.0% | — | -1.5pp |
78	
79	### Long (5 matched seeds for A-V)
80	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
81	|------|---------|----------|-----|--------|
82	| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
83	| s43 | — | 58.0% | 54.5% | — |
84	| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
85	| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
86	| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |
87	| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |
88	
89	## Data Gaps
90	- Goal VLA-only s42: missing
91	- Object VLA-only s42/s43/s44: missing
92	- Spatial CRM s42/s48/s49: missing
93	- Goal/Object CRM s48/s49: missing
94	- Long VLA-only s43/s48/s49: missing
95	- Long Adaptive s48/s49: missing
96	
97	## Note on Spatial VLA-only s42
98	eval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "7afba8d6-37cc-4932-8735-03b4901a1e7e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md",
      "content": "# Table 1 — Multi-seed Results (Clean supp-era data)\n\nGenerated: 2026-05-24 20:10 UTC\n\n## Main Table\n\n| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |\n|-------|---------|-------------|-------------------|--------|--------|\n| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |\n| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |\n| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |\n| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |\n\n## Paired t-test: Δ(A-V) = Adaptive - VLA-only\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |\n| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |\n| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |\n| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |\n\n## Paired t-test: Δ(A-C) = Adaptive - CRM always-on\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |\n| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |\n| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |\n| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |\n\n## Trigger Rate ↔ Effect Size (D140 key evidence)\n\n| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |\n|-------|------------------|--------|-------------|\n| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |\n| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |\n| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |\n| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |\n\n## Per-seed Raw Data\n\n### Spatial (8 matched seeds)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 80.0% | 82.0% | — | +2.0pp |\n| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |\n| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |\n| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |\n| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |\n| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |\n| s48 | 79.5% | 81.0% | — | +1.5pp |\n| s49 | 78.5% | 82.0% | — | +3.5pp |\n\n### Goal (7 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 84.0% | 85.5% | — |\n| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |\n| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |\n| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |\n| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |\n| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |\n| s48 | 85.0% | 84.5% | — | -0.5pp |\n| s49 | 82.0% | 81.5% | — | -0.5pp |\n\n### Object (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 81.0% | 77.0% | — |\n| s43 | — | 77.5% | 78.5% | — |\n| s44 | — | 75.0% | 74.0% | — |\n| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |\n| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |\n| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |\n| s48 | 79.0% | 76.0% | — | -3.0pp |\n| s49 | 75.5% | 74.0% | — | -1.5pp |\n\n### Long (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |\n| s43 | — | 58.0% | 54.5% | — |\n| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |\n| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |\n| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |\n| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |\n\n## Data Gaps\n- Goal VLA-only s42: missing\n- Object VLA-only s42/s43/s44: missing\n- Spatial CRM s42/s48/s49: missing\n- Goal/Object CRM s48/s49: missing\n- Long VLA-only s43/s48/s49: missing\n- Long Adaptive s48/s49: missing\n\n## Note on Spatial VLA-only s42\neval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01MA1HeGCCvksWVFsDfibYdc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "fb81298b-2869-4cc8-9cc2-971f7096a0ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrT62XPVnBVyhUdotbpk5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7930,
      "cache_read_input_tokens": 52254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7930
      },
      "output_tokens": 8,
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

_source line 73 · 2026-05-25T02:03:24.347Z_

<details><summary>↩ Tool result · `toolu_01MA1HeGCCvksWVFsDfibYdc`</summary>

```text
1	# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)
2	
3	## Per-Seed Detail
4	
5	### SPATIAL (8/8 VLA-only, 8/8 Adaptive)
6	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
7	|------|----------|----------|-----|--------|-----------|
8	| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |
9	| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |
10	| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |
11	| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |
12	| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |
13	| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |
14	| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |
15	| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |
16	
17	**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*
18	
19	### OBJECT (3/8 VLA-only, 6/8 Adaptive)
20	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
21	|------|----------|----------|-----|--------|-----------|
22	| s42 | --- | 81.0% | 77.0% | | 3.5% |
23	| s43 | --- | 77.5% | 78.5% | | 3.7% |
24	| s44 | --- | 75.0% | 74.0% | | 3.6% |
25	| s45 | --- | --- | 76.5% | | |
26	| s46 | --- | --- | 79.5% | | |
27	| s47 | 75.5% | 77.0% | 82.5% | +1.5% | 4.0% |
28	| s48 | 79.0% | 76.0% | --- | -3.0% | 3.9% |
29	| s49 | 75.5% | 74.0% | --- | -1.5% | 4.2% |
30	
31	**Stats (3-seed paired):** VLA 76.7%±2.0% → Adaptive 75.7%±1.5%, Δ=-1.0%, p=0.53 ns
32	**Note:** s42/43/44 VLA-only currently running on bjb1-32546
33	
34	### GOAL (6/8 VLA-only, 8/8 Adaptive)
35	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
36	|------|----------|----------|-----|--------|-----------|
37	| s42 | --- | 84.0% | 85.5% | | 8.3% |
38	| s43 | 82.5% | 84.5% | 82.0% | +2.0% | 8.8% |
39	| s44 | 82.0% | 86.5% | 83.5% | +4.5% | 6.8% |
40	| s45 | --- | 81.0% | 81.0% | | 9.4% |
41	| s46 | 83.0% | 83.5% | 82.0% | +0.5% | 9.1% |
42	| s47 | 82.5% | 82.0% | 82.0% | -0.5% | 8.9% |
43	| s48 | 85.0% | 84.5% | --- | -0.5% | 8.9% |
44	| s49 | 82.0% | 81.5% | --- | -0.5% | 8.9% |
45	
46	**Stats (6-seed paired):** VLA 82.8%±1.1% → Adaptive 83.8%±1.8%, Δ=+0.9%, p=0.31 ns
47	
48	### LONG (3/8 each)
49	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
50	|------|----------|----------|-----|--------|-----------|
51	| s42 | 58.0% | 59.0% | 56.5% | +1.0% | 3.9% |
52	| s46 | 60.5% | 58.5% | 54.0% | -2.0% | |
53	| s47 | 59.5% | 55.0% | 56.5% | -4.5% | 3.7% |
54	
55	**Stats (3-seed paired):** VLA 59.3%±1.3% → Adaptive 57.5%±2.2%, Δ=-1.8%, p=0.37 ns
56	
57	## Summary Table
58	
59	| Suite | VLA-only | Adaptive | CRM | Δ(A-V) | p(A-V) | n |
60	|-------|----------|----------|-----|--------|--------|---|
61	| Spatial | 79.5%±0.8% | 80.9%±0.9% | 80.3%±1.0% | +1.4% | 0.0168* | 8 |
62	| Object | 76.7%±2.0% | 75.7%±1.5% | 78.0% (6s) | -1.0% | 0.53 | 3 |
63	| Goal | 82.8%±1.1% | 83.8%±1.8% | 82.4%±0.8% | +0.9% | 0.31 | 6 |
64	| Long | 59.3%±1.3% | 57.5%±2.2% | 55.7%±1.4% | -1.8% | 0.37 | 3 |
65	
66	## Trigger Rate ↔ Effect Size (D140 方案C evidence)
67	
68	| Suite | trigger_rate | Δ(A-V) | Direction |
69	|-------|-------------|--------|-----------|
70	| Spatial | 19.8% | +1.4%* | Positive (significant) |
71	| Goal | 8.6% | +0.9% | Positive (trend) |
72	| Object | 3.8% | -1.0% | Negligible |
73	| Long | 3.8% | -1.8% | Negligible |
74	
75	Perfect monotonic: higher trigger → larger positive effect.
76	
77	## Data Gaps (being filled)
78	- Object VLA-only s42/43/44: running on bjb1-32546
79	- Goal VLA-only s42/s45: s42 running on bjb1-32546
80	- Spatial CRM s48/s49: running on bjb2-28827
81	- Goal CRM s48/s49: running on bjb2-28827 + bjb1-18228
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "50defff1-0652-4760-9e43-2e64f8fdac59",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md",
      "content": "# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)\n\n## Per-Seed Detail\n\n### SPATIAL (8/8 VLA-only, 8/8 Adaptive)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |\n| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |\n| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |\n| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |\n| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |\n| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |\n| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |\n| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |\n\n**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*\n\n### OBJECT (3/8 VLA-only, 6/8 Adaptive)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | --- | 81.0% | 77.0% | | 3.5% |\n| s43 | --- | 77.5% | 78.5% | | 3.7% |\n| s44 | --- | 75.0% | 74.0% | | 3.6% |\n| s45 | --- | --- | 76.5% | | |\n| s46 | --- | --- | 79.5% | | |\n| s47 | 75.5% | 77.0% | 82.5% | +1.5% | 4.0% |\n| s48 | 79.0% | 76.0% | --- | -3.0% | 3.9% |\n| s49 | 75.5% | 74.0% | --- | -1.5% | 4.2% |\n\n**Stats (3-seed paired):** VLA 76.7%±2.0% → Adaptive 75.7%±1.5%, Δ=-1.0%, p=0.53 ns\n**Note:** s42/43/44 VLA-only currently running on bjb1-32546\n\n### GOAL (6/8 VLA-only, 8/8 Adaptive)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | --- | 84.0% | 85.5% | | 8.3% |\n| s43 | 82.5% | 84.5% | 82.0% | +2.0% | 8.8% |\n| s44 | 82.0% | 86.5% | 83.5% | +4.5% | 6.8% |\n| s45 | --- | 81.0% | 81.0% | | 9.4% |\n| s46 | 83.0% | 83.5% | 82.0% | +0.5% | 9.1% |\n| s47 | 82.5% | 82.0% | 82.0% | -0.5% | 8.9% |\n| s48 | 85.0% | 84.5% | --- | -0.5% | 8.9% |\n| s49 | 82.0% | 81.5% | --- | -0.5% | 8.9% |\n\n**Stats (6-seed paired):** VLA 82.8%±1.1% → Adaptive 83.8%±1.8%, Δ=+0.9%, p=0.31 ns\n\n### LONG (3/8 each)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | 58.0% | 59.0% | 56.5% | +1.0% | 3.9% |\n| s46 | 60.5% | 58.5% | 54.0% | -2.0% | |\n| s47 | 59.5% | 55.0% | 56.5% | -4.5% | 3.7% |\n\n**Stats (3-seed paired):** VLA 59.3%±1.3% → Adaptive 57.5%±2.2%, Δ=-1.8%, p=0.37 ns\n\n## Summary Table\n\n| Suite | VLA-only | Adaptive | CRM | Δ(A-V) | p(A-V) | n |\n|-------|----------|----------|-----|--------|--------|---|\n| Spatial | 79.5%±0.8% | 80.9%±0.9% | 80.3%±1.0% | +1.4% | 0.0168* | 8 |\n| Object | 76.7%±2.0% | 75.7%±1.5% | 78.0% (6s) | -1.0% | 0.53 | 3 |\n| Goal | 82.8%±1.1% | 83.8%±1.8% | 82.4%±0.8% | +0.9% | 0.31 | 6 |\n| Long | 59.3%±1.3% | 57.5%±2.2% | 55.7%±1.4% | -1.8% | 0.37 | 3 |\n\n## Trigger Rate ↔ Effect Size (D140 方案C evidence)\n\n| Suite | trigger_rate | Δ(A-V) | Direction |\n|-------|-------------|--------|-----------|\n| Spatial | 19.8% | +1.4%* | Positive (significant) |\n| Goal | 8.6% | +0.9% | Positive (trend) |\n| Object | 3.8% | -1.0% | Negligible |\n| Long | 3.8% | -1.8% | Negligible |\n\nPerfect monotonic: higher trigger → larger positive effect.\n\n## Data Gaps (being filled)\n- Object VLA-only s42/43/44: running on bjb1-32546\n- Goal VLA-only s42/s45: s42 running on bjb1-32546\n- Spatial CRM s48/s49: running on bjb2-28827\n- Goal CRM s48/s49: running on bjb2-28827 + bjb1-18228\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  }
}
```

</details>

---


### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Now I see the current data state. But the user's stated Table 1 values are:
- Goal: VLA-only 83.7±1.3(3s), CRM 83.7±1.8(3s), Adaptive 85.0±1.3(3s)
- Object: VLA-only 77.7±1.3(5s), CRM 76.5±2.3(3s), Adaptive 77.8±2.1(5s)

These don't match the 8-seed tables above. The 8-seed data shows:


- Goal: VLA 82.8±1.1 (6s), Adaptive 83.8±1.8 (6s)
- Object: VLA 76.7±2.0 (3s), Adaptive 75.7±1.5 (3s)

There's a discrepancy here, so I need to check the ROADMAP to find the latest Table 1 values the user was referencing, and also look more carefully at the per-seed breakdowns to understand where these numbers are coming from.

Looking at the Goal task data across seeds, VLA-only ranges from 82.0 to 85.0, CRM clusters around 81-85.5, and Adaptive spans 81.0 to 86.5. For Object, the VLA-only seeds are sparse with values between 75.5 and 79.0, while I'm seeing additional data points that might fill in the picture. I'm testing different combinations of seed values to match the reported mean of 83.7 for the VLA-only goal, but none of them are working out. The values I'm checking don't align with what's in Table 1, so either the seeds are different than what I have here, or these numbers are from an earlier version of the data. I should probably check the actual JSON files on the servers or look at what the ROADMAP currently shows to resolve this discrepancy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "ba760308-59a6-4445-9c06-6538921d50cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcusWne6uhcngDrVorytPS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4817,
      "cache_read_input_tokens": 60184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4817
      },
      "output_tokens": 8,
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


### Assistant

_source line 75_

Let me check the ROADMAP for the current Table 1 values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "6726956d-6dc1-46c5-9c4b-8c9887ba4ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcusWne6uhcngDrVorytPS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4817,
      "cache_read_input_tokens": 60184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4817
      },
      "output_tokens": 8,
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

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01B8pDjXTXCS4u6QLpwpXzs4`</summary>

```json
{
  "command": "grep -n -A 30 \"Table 1\\|table.1\\|Goal.*VLA.*83\\|Object.*VLA.*77\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md 2>/dev/null | head -100",
  "description": "Search ROADMAP for Table 1 values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "2d213020-ae4c-4649-8e93-1a4970da9cfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcusWne6uhcngDrVorytPS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4817,
      "cache_read_input_tokens": 60184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4817
      },
      "output_tokens": 8,
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

_source line 77 · 2026-05-25T02:03:47.236Z_

<details><summary>↩ Tool result · `toolu_01B8pDjXTXCS4u6QLpwpXzs4`</summary>

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
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "d8c09ab1-7bd8-4903-bc5a-76fb294820a8",
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


### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Now I see the Table 1 values from ROADMAP:
- Goal: VLA-only 83.7±1.3(3s), CRM 83.7±1.8(3s), Adaptive 85.0±1.3(3s)
- Object: VLA-only 77.7±1.3(5s), CRM 76.5±2.3(3s), Adaptive 77.8±2.1(5s)

This is the "3-seed" version that hasn't been updated to D139 8-seed yet. 

The current report uses 3 seeds for some metrics, so I need to figure out which specific seeds were used to get these numbers. Looking at the Goal VLA-only result of 83.7±1.3, I'm trying to find three seeds from the 8-seed table that would average to 83.7, but the combinations I'm checking don't quite match up. There might be a separate per-seed dataset for the 3-seed version that I need to locate.

Let me try a more systematic approach—I'll extract the raw data directly from the JSON files on the servers and cross-reference them with the Table 1 values to figure out exactly which seeds were used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "1e8e3035-c202-4cea-a588-e6eeaa66dcb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7yDnRJ7BRdi27MnBKapFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2999,
      "cache_read_input_tokens": 65001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2999
      },
      "output_tokens": 8,
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


### Assistant

_source line 79_

Now I know the Table 1 values. Let me extract all JSON data from each server. I'll run the extraction on all relevant servers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "e52575d0-4b4f-4174-875f-2c301c152ca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7yDnRJ7BRdi27MnBKapFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2999,
      "cache_read_input_tokens": 65001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2999
      },
      "output_tokens": 8,
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

_source line 80_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014dbGYLAdmj9TqJ8Mo63eZU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "c7d59d35-fda3-41e4-8f38-ac4bab05723f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7yDnRJ7BRdi27MnBKapFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2999,
      "cache_read_input_tokens": 65001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2999
      },
      "output_tokens": 8,
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

_source line 81 · 2026-05-25T02:04:02.777Z_

<details><summary>↩ Tool result · `toolu_014dbGYLAdmj9TqJ8Mo63eZU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "5fa6cbe5-b3ce-4e4b-a166-8d9700e51488",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TTiFpyhCdELvSKtKQ4p5Yc`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement/logs && python3 -c \"\nimport json, os, glob\nfor pattern in ['eval_goal_*.json', 'eval_object_*.json']:\n    for f in sorted(glob.glob(pattern)):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', d.get('overall_sr', '?'))\n            mode = d.get('mode', '?')\n            bm = d.get('baseline_mode', '?')\n            K = d.get('K', '?')\n            nr = d.get('n_rollouts', '?')\n            seed = d.get('seed', '?')\n            tau = d.get('conformal_threshold', '?')\n            tr = d.get('trigger_rate', '?')\n            norm = d.get('max_correction_norm', '?')\n            mt = os.path.getmtime(f)\n            print(f'{f}|mode={mode}|bm={bm}|K={K}|nr={nr}|SR={sr}|seed={seed}|tau={tau}|tr={tr}|norm={norm}|mtime={mt}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n\"\n",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "71e6f7e4-284a-40f3-8db0-aceae73cb1f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXqYjr7coQRCtxYvyqg9UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 68000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 831
      },
      "output_tokens": 44,
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

_source line 83 · 2026-05-25T02:04:12.711Z_

<details><summary>↩ Tool result · `toolu_01TTiFpyhCdELvSKtKQ4p5Yc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.845|seed=?|tau=?|tr=?|norm=?|mtime=1779532692.0368764\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.865|seed=?|tau=?|tr=?|norm=?|mtime=1779534038.1873076\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779573989.1342785\\neval_goal_crm_obs_only_norm0.05_seed43.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779532615.7577972\\neval_goal_obs_only_norm02_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.64|seed=?|tau=?|tr=?|norm=?|mtime=1779226734.8219275\\neval_goal_obs_only_norm02_seed45.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.65|seed=?|tau=?|tr=?|norm=?|mtime=1779226656.9082208\\neval_goal_vla_only_pi05_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.955|seed=?|tau=?|tr=?|norm=?|mtime=1779648460.4864602\\neval_goal_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.97|seed=?|tau=?|tr=?|norm=?|mtime=1779648408.7665005\\neval_goal_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779660559.46666\\neval_goal_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.825|seed=?|tau=?|tr=?|norm=?|mtime=1779543280.6008415\\neval_goal_vla_only_seed43_r4.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.98|seed=?|tau=?|tr=?|norm=?|mtime=1779466545.5277555\\neval_goal_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.85|seed=?|tau=?|tr=?|norm=?|mtime=1779554057.3608177\\neval_goal_vla_only_seed44_r4.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.975|seed=?|tau=?|tr=?|norm=?|mtime=1779466563.1835966\\neval_goal_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.71|seed=?|tau=?|tr=?|norm=?|mtime=1779217864.568117\\neval_goal_vla_only_seed52.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.68|seed=?|tau=?|tr=?|norm=?|mtime=1779258356.752343\\neval_object_a1_vla_only_seed42.json|mode=vla_only|bm=?|K=?|nr=20|SR=0.565|seed=42|tau=?|tr=?|norm=?|mtime=1779632318.3484762\\neval_object_acr_vla_seed42.json|mode=acr_vla|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779446251.1607614\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779534514.8316638\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.75|seed=?|tau=?|tr=?|norm=?|mtime=1779544967.0937607\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779620684.912818\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.745|seed=?|tau=?|tr=?|norm=?|mtime=1779652744.7301142\\neval_object_argmin_k5_seed42.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1779197179.481897\\neval_object_argmin_k5_seed43.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779197051.5643177\\neval_object_argmin_k5_seed45.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779197072.4012444\\neval_object_crm_obs_only_norm0.05_seed42.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779517904.9530287\\neval_object_crm_obs_only_norm0.05_seed43.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.785|seed=?|tau=?|tr=?|norm=?|mtime=1779534131.8963373\\neval_object_crm_obs_only_norm0.05_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.74|seed=?|tau=?|tr=?|norm=?|mtime=1779545122.824118\\neval_object_crm_obs_only_norm0.05_seed46.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.795|seed=?|tau=?|tr=?|norm=?|mtime=1779575439.2929757\\neval_object_crm_obs_only_norm0.05_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.825|se\\n\\n... [截断: 输出过长，省略 4447 字符] ...\\n\\n?|mtime=1779114756.0048013\\neval_object_perdof_norm01_seed45.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779009838.273586\\neval_object_perdof_norm01_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779051409.6994042\\neval_object_perdof_norm01_seed47_r2.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1779058707.2655356\\neval_object_perdof_norm02.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1778911465.5034993\\neval_object_perdof_norm02_seed43_bjb1-32546.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779100445.6939704\\neval_object_perdof_norm03_seed45_r2.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.06|seed=?|tau=?|tr=?|norm=?|mtime=1779015231.113998\\neval_object_perdof_norm03_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.04|seed=?|tau=?|tr=?|norm=?|mtime=1779171847.8640468\\neval_object_random_selection_k5_seed42.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1779205521.1789782\\neval_object_random_selection_k5_seed44.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779205824.8221142\\neval_object_random_selection_k5_seed45.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.07|seed=?|tau=?|tr=?|norm=?|mtime=1779206238.5938497\\neval_object_reconvla.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778861960.5493712\\neval_object_reconvla_seed45.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.78|seed=?|tau=?|tr=?|norm=?|mtime=1779584340.2720754\\neval_object_reconvla_seed46.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779007276.5154657\\neval_object_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779015057.1953292\\neval_object_scalar_seed43.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1778911280.780721\\neval_object_scalar_seed44_r2.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.06|seed=?|tau=?|tr=?|norm=?|mtime=1778965792.2518973\\neval_object_scalar_seed46.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779173566.5986395\\neval_object_vla_mean.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778864307.5984843\\neval_object_vla_mean_seed43.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1778906889.8088453\\neval_object_vla_mean_seed44.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1778956311.8025947\\neval_object_vla_only.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778820025.433092\\neval_object_vla_only_pi05_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.965|seed=?|tau=?|tr=?|norm=?|mtime=1779648676.4412975\\neval_object_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.815|seed=?|tau=?|tr=?|norm=?|mtime=1779365555.9832056\\neval_object_vla_only_pi05_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779365563.7790554\\neval_object_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779662470.450166\\neval_object_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779662333.9723992\\neval_object_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779662265.775499\\neval_object_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779565205.5899165\\neval_object_vla_only_seed47.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.755|seed=?|tau=?|tr=?|norm=?|mtime=1779620415.3197114\\neval_object_vla_only_seed49.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779231488.4945297\\neval_object_vla_only_seed51.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1779251295.2411811\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "ff0cdf1a-e037-4481-aa79-63d5f6b85329",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.845|seed=?|tau=?|tr=?|norm=?|mtime=1779532692.0368764\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.865|seed=?|tau=?|tr=?|norm=?|mtime=1779534038.1873076\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779573989.1342785\\\\neval_goal_crm_obs_only_norm0.05_seed43.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779532615.7577972\\\\neval_goal_obs_only_norm02_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.64|seed=?|tau=?|tr=?|norm=?|mtime=1779226734.8219275\\\\neval_goal_obs_only_norm02_seed45.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.65|seed=?|tau=?|tr=?|norm=?|mtime=1779226656.9082208\\\\neval_goal_vla_only_pi05_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.955|seed=?|tau=?|tr=?|norm=?|mtime=1779648460.4864602\\\\neval_goal_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.97|seed=?|tau=?|tr=?|norm=?|mtime=1779648408.7665005\\\\neval_goal_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779660559.46666\\\\neval_goal_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.825|seed=?|tau=?|tr=?|norm=?|mtime=1779543280.6008415\\\\neval_goal_vla_only_seed43_r4.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.98|seed=?|tau=?|tr=?|norm=?|mtime=1779466545.5277555\\\\neval_goal_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.85|seed=?|tau=?|tr=?|norm=?|mtime=1779554057.3608177\\\\neval_goal_vla_only_seed44_r4.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.975|seed=?|tau=?|tr=?|norm=?|mtime=1779466563.1835966\\\\neval_goal_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.71|seed=?|tau=?|tr=?|norm=?|mtime=1779217864.568117\\\\neval_goal_vla_only_seed52.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.68|seed=?|tau=?|tr=?|norm=?|mtime=1779258356.752343\\\\neval_object_a1_vla_only_seed42.json|mode=vla_only|bm=?|K=?|nr=20|SR=0.565|seed=42|tau=?|tr=?|norm=?|mtime=1779632318.3484762\\\\neval_object_acr_vla_seed42.json|mode=acr_vla|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779446251.1607614\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779534514.8316638\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.75|seed=?|tau=?|tr=?|norm=?|mtime=1779544967.0937607\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779620684.912818\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.745|seed=?|tau=?|tr=?|norm=?|mtime=1779652744.7301142\\\\neval_object_argmin_k5_seed42.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1779197179.481897\\\\neval_object_argmin_k5_seed43.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779197051.5643177\\\\neval_object_argmin_k5_seed45.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779197072.4012444\\\\neval_object_crm_obs_only_norm0.05_seed42.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779517904.9530287\\\\neval_object_crm_obs_only_norm0.05_seed43.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.785|seed=?|tau=?|tr=?|norm=?|mtime=1779534131.8963373\\\\neval_object_crm_obs_only_norm0.05_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.74|seed=?|tau=?|tr=?|norm=?|mtime=1779545122.824118\\\\neval_object_crm_obs_only_norm0.05_seed46.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.795|seed=?|tau=?|tr=?|norm=?|mtime=1779575439.2929757\\\\neval_object_crm_obs_only_norm0.05_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.825|se\\\\n\\\\n... [截断: 输出过长，省略 4447 字符] ...\\\\n\\\\n?|mtime=1779114756.0048013\\\\neval_object_perdof_norm01_seed45.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779009838.273586\\\\neval_object_perdof_norm01_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779051409.6994042\\\\neval_object_perdof_norm01_seed47_r2.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1779058707.2655356\\\\neval_object_perdof_norm02.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1778911465.5034993\\\\neval_object_perdof_norm02_seed43_bjb1-32546.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779100445.6939704\\\\neval_object_perdof_norm03_seed45_r2.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.06|seed=?|tau=?|tr=?|norm=?|mtime=1779015231.113998\\\\neval_object_perdof_norm03_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.04|seed=?|tau=?|tr=?|norm=?|mtime=1779171847.8640468\\\\neval_object_random_selection_k5_seed42.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1779205521.1789782\\\\neval_object_random_selection_k5_seed44.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779205824.8221142\\\\neval_object_random_selection_k5_seed45.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.07|seed=?|tau=?|tr=?|norm=?|mtime=1779206238.5938497\\\\neval_object_reconvla.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778861960.5493712\\\\neval_object_reconvla_seed45.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.78|seed=?|tau=?|tr=?|norm=?|mtime=1779584340.2720754\\\\neval_object_reconvla_seed46.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779007276.5154657\\\\neval_object_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779015057.1953292\\\\neval_object_scalar_seed43.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1778911280.780721\\\\neval_object_scalar_seed44_r2.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.06|seed=?|tau=?|tr=?|norm=?|mtime=1778965792.2518973\\\\neval_object_scalar_seed46.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779173566.5986395\\\\neval_object_vla_mean.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778864307.5984843\\\\neval_object_vla_mean_seed43.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1778906889.8088453\\\\neval_object_vla_mean_seed44.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1778956311.8025947\\\\neval_object_vla_only.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778820025.433092\\\\neval_object_vla_only_pi05_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.965|seed=?|tau=?|tr=?|norm=?|mtime=1779648676.4412975\\\\neval_object_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.815|seed=?|tau=?|tr=?|norm=?|mtime=1779365555.9832056\\\\neval_object_vla_only_pi05_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779365563.7790554\\\\neval_object_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779662470.450166\\\\neval_object_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779662333.9723992\\\\neval_object_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779662265.775499\\\\neval_object_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779565205.5899165\\\\neval_object_vla_only_seed47.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.755|seed=?|tau=?|tr=?|norm=?|mtime=1779620415.3197114\\\\neval_object_vla_only_seed49.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779231488.4945297\\\\neval_object_vla_only_seed51.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1779251295.2411811\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.845|seed=?|tau=?|tr=?|norm=?|mtime=1779532692.0368764\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.865|seed=?|tau=?|tr=?|norm=?|mtime=1779534038.1873076\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779573989.1342785\\neval_goal_crm_obs_only_norm0.05_seed43.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779532615.7577972\\neval_goal_obs_only_norm02_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.64|seed=?|tau=?|tr=?|norm=?|mtime=1779226734.8219275\\neval_goal_obs_only_norm02_seed45.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.65|seed=?|tau=?|tr=?|norm=?|mtime=1779226656.9082208\\neval_goal_vla_only_pi05_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.955|seed=?|tau=?|tr=?|norm=?|mtime=1779648460.4864602\\neval_goal_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.97|seed=?|tau=?|tr=?|norm=?|mtime=1779648408.7665005\\neval_goal_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779660559.46666\\neval_goal_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.825|seed=?|tau=?|tr=?|norm=?|mtime=1779543280.6008415\\neval_goal_vla_only_seed43_r4.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.98|seed=?|tau=?|tr=?|norm=?|mtime=1779466545.5277555\\neval_goal_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.85|seed=?|tau=?|tr=?|norm=?|mtime=1779554057.3608177\\neval_goal_vla_only_seed44_r4.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.975|seed=?|tau=?|tr=?|norm=?|mtime=1779466563.1835966\\neval_goal_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.71|seed=?|tau=?|tr=?|norm=?|mtime=1779217864.568117\\neval_goal_vla_only_seed52.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.68|seed=?|tau=?|tr=?|norm=?|mtime=1779258356.752343\\neval_object_a1_vla_only_seed42.json|mode=vla_only|bm=?|K=?|nr=20|SR=0.565|seed=42|tau=?|tr=?|norm=?|mtime=1779632318.3484762\\neval_object_acr_vla_seed42.json|mode=acr_vla|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779446251.1607614\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779534514.8316638\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.75|seed=?|tau=?|tr=?|norm=?|mtime=1779544967.0937607\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779620684.912818\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.745|seed=?|tau=?|tr=?|norm=?|mtime=1779652744.7301142\\neval_object_argmin_k5_seed42.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1779197179.481897\\neval_object_argmin_k5_seed43.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779197051.5643177\\neval_object_argmin_k5_seed45.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779197072.4012444\\neval_object_crm_obs_only_norm0.05_seed42.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779517904.9530287\\neval_object_crm_obs_only_norm0.05_seed43.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.785|seed=?|tau=?|tr=?|norm=?|mtime=1779534131.8963373\\neval_object_crm_obs_only_norm0.05_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.74|seed=?|tau=?|tr=?|norm=?|mtime=1779545122.824118\\neval_object_crm_obs_only_norm0.05_seed46.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.795|seed=?|tau=?|tr=?|norm=?|mtime=1779575439.2929757\\neval_object_crm_obs_only_norm0.05_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.825|se\\n\\n... [截断: 输出过长，省略 4447 字符] ...\\n\\n?|mtime=1779114756.0048013\\neval_object_perdof_norm01_seed45.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779009838.273586\\neval_object_perdof_norm01_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779051409.6994042\\neval_object_perdof_norm01_seed47_r2.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1779058707.2655356\\neval_object_perdof_norm02.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1778911465.5034993\\neval_object_perdof_norm02_seed43_bjb1-32546.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779100445.6939704\\neval_object_perdof_norm03_seed45_r2.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.06|seed=?|tau=?|tr=?|norm=?|mtime=1779015231.113998\\neval_object_perdof_norm03_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.04|seed=?|tau=?|tr=?|norm=?|mtime=1779171847.8640468\\neval_object_random_selection_k5_seed42.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1779205521.1789782\\neval_object_random_selection_k5_seed44.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779205824.8221142\\neval_object_random_selection_k5_seed45.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.07|seed=?|tau=?|tr=?|norm=?|mtime=1779206238.5938497\\neval_object_reconvla.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778861960.5493712\\neval_object_reconvla_seed45.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.78|seed=?|tau=?|tr=?|norm=?|mtime=1779584340.2720754\\neval_object_reconvla_seed46.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779007276.5154657\\neval_object_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779015057.1953292\\neval_object_scalar_seed43.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1778911280.780721\\neval_object_scalar_seed44_r2.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.06|seed=?|tau=?|tr=?|norm=?|mtime=1778965792.2518973\\neval_object_scalar_seed46.json|mode=crm_scalar|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779173566.5986395\\neval_object_vla_mean.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778864307.5984843\\neval_object_vla_mean_seed43.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1778906889.8088453\\neval_object_vla_mean_seed44.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1778956311.8025947\\neval_object_vla_only.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.12|seed=?|tau=?|tr=?|norm=?|mtime=1778820025.433092\\neval_object_vla_only_pi05_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.965|seed=?|tau=?|tr=?|norm=?|mtime=1779648676.4412975\\neval_object_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.815|seed=?|tau=?|tr=?|norm=?|mtime=1779365555.9832056\\neval_object_vla_only_pi05_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779365563.7790554\\neval_object_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779662470.450166\\neval_object_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779662333.9723992\\neval_object_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779662265.775499\\neval_object_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779565205.5899165\\neval_object_vla_only_seed47.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.755|seed=?|tau=?|tr=?|norm=?|mtime=1779620415.3197114\\neval_object_vla_only_seed49.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779231488.4945297\\neval_object_vla_only_seed51.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.15|seed=?|tau=?|tr=?|norm=?|mtime=1779251295.2411811\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016jeHXz3BWrA6Pvhp4MvsW6`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cd /root/acr-vla-conformal-refinement/logs && python3 -c \"\nimport json, os, glob\nfor pattern in ['eval_goal_*.json', 'eval_object_*.json']:\n    for f in sorted(glob.glob(pattern)):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', d.get('overall_sr', '?'))\n            mode = d.get('mode', '?')\n            bm = d.get('baseline_mode', '?')\n            K = d.get('K', '?')\n            nr = d.get('n_rollouts', '?')\n            seed = d.get('seed', '?')\n            tau = d.get('conformal_threshold', '?')\n            tr = d.get('trigger_rate', '?')\n            norm = d.get('max_correction_norm', '?')\n            mt = os.path.getmtime(f)\n            print(f'{f}|mode={mode}|bm={bm}|K={K}|nr={nr}|SR={sr}|seed={seed}|tau={tau}|tr={tr}|norm={norm}|mtime={mt}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n\"\n",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "1d2539ea-2744-4084-aa51-4b6d2a0c0bc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXqYjr7coQRCtxYvyqg9UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 68000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 831
      },
      "output_tokens": 44,
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

_source line 85 · 2026-05-25T02:04:16.044Z_

<details><summary>↩ Tool result · `toolu_016jeHXz3BWrA6Pvhp4MvsW6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.85|seed=?|tau=?|tr=?|norm=?|mtime=1779549505.0621097\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779550003.4908967\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.84|seed=?|tau=?|tr=?|norm=?|mtime=1779526362.0417063\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779585591.7900822\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.845|seed=?|tau=?|tr=?|norm=?|mtime=1779645319.0771303\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.815|seed=?|tau=?|tr=?|norm=?|mtime=1779645913.180236\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779549390.4939702\\neval_goal_adaptive_conformal_crm_tau0.25_seed47.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779624214.8184283\\neval_goal_crm_obs_only_norm0.05_seed42.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.855|seed=?|tau=?|tr=?|norm=?|mtime=1779517392.569333\\neval_goal_crm_obs_only_norm0.05_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779539474.0705094\\neval_goal_crm_obs_only_norm0.05_seed45.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779576334.434667\\neval_goal_crm_obs_only_norm0.05_seed46.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779585677.870676\\neval_goal_crm_obs_only_norm0.05_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779623912.9975011\\neval_goal_crm_obs_only_norm0.05_seed48.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.8|seed=?|tau=?|tr=?|norm=?|mtime=1779661966.0933068\\neval_goal_k2mean_seed46.json|mode=vla_only|bm=mean|K=?|nr=20|SR=0.825|seed=?|tau=?|tr=?|norm=?|mtime=1779585432.3525603\\neval_goal_obs_only_norm02_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.69|seed=?|tau=?|tr=?|norm=?|mtime=1779250596.8733935\\neval_goal_obs_only_norm02_seed48.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.68|seed=?|tau=?|tr=?|norm=?|mtime=1779250876.6610563\\neval_goal_obs_only_norm02_seed49.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.62|seed=?|tau=?|tr=?|norm=?|mtime=1779260314.9717753\\neval_goal_obs_only_norm02_seed50.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.67|seed=?|tau=?|tr=?|norm=?|mtime=1779260258.1875696\\neval_goal_reconvla_seed42.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779528564.048699\\neval_goal_reconvla_seed44.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.805|seed=?|tau=?|tr=?|norm=?|mtime=1779539552.3289988\\neval_goal_reconvla_seed45.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.855|seed=?|tau=?|tr=?|norm=?|mtime=1779575953.7916744\\neval_goal_reconvla_seed46.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779586066.3842058\\neval_goal_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779623803.4525318\\neval_goal_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779528693.3852956\\neval_goal_vla_only_seed44_r2.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.73|seed=?|tau=?|tr=?|norm=?|mtime=1779214848.283968\\neval_goal_vla_only_seed45.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779575976.9561207\\neval_goal_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.83|seed=?|tau=?|tr=?|norm=?|mtime=1779585604.1747642\\neval_goal_vla_only_seed47.json|mode=vla_only|bm=mean|K=?|nr=20|S\\n\\n... [截断: 输出过长，省略 4208 字符] ...\\n\\nrm_perdof|bm=single|K=?|nr=10|SR=0.0|seed=?|tau=?|tr=?|norm=?|mtime=1779182777.447817\\neval_object_perdof_norm003.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1778918839.1050653\\neval_object_perdof_norm003_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779177862.2909682\\neval_object_perdof_norm005.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1778920150.0054674\\neval_object_perdof_norm005_seed45.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779197057.5790293\\neval_object_perdof_norm01_seed42.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779117175.6900625\\neval_object_perdof_norm02_seed43_r3.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1778927925.6223562\\neval_object_perdof_norm02_seed44.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779036519.8630602\\neval_object_perdof_norm02_seed45.json|mode=crm_perdof|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779037238.8097897\\neval_object_perdof_norm02_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779070916.6589944\\neval_object_perdof_norm02_seed47.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779078884.6691506\\neval_object_perdof_norm02_seed48.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.07|seed=?|tau=?|tr=?|norm=?|mtime=1779114863.6627562\\neval_object_perdof_norm03_r3.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.04|seed=?|tau=?|tr=?|norm=?|mtime=1778929371.5343606\\neval_object_perdof_norm03_seed47.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.05|seed=?|tau=?|tr=?|norm=?|mtime=1779180058.680503\\neval_object_random_selection_k5_seed43.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779206635.0573328\\neval_object_random_selection_seed42.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779266724.7550728\\neval_object_random_selection_seed43.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779119137.8045802\\neval_object_random_selection_seed44.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779266661.5051854\\neval_object_random_selection_seed45.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779179392.522475\\neval_object_reconvla_k5_seed42.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779193280.5257018\\neval_object_reconvla_seed42.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779519252.2247827\\neval_object_reconvla_seed43.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779536616.4167185\\neval_object_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.765|seed=?|tau=?|tr=?|norm=?|mtime=1779625593.4554389\\neval_object_scalar_seed45.json|mode=crm_scalar|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779038782.577561\\neval_object_vla_mean_seed45.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1778988474.8153772\\neval_object_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.865|seed=?|tau=?|tr=?|norm=?|mtime=1779648601.1655722\\neval_object_vla_only_seed42.json|mode=vla_only|bm=mean|K=?|nr=20|SR=0.795|seed=?|tau=?|tr=?|norm=?|mtime=1779530392.1805253\\neval_object_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779519458.5314624\\neval_object_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779519465.7787242\\neval_object_vla_only_seed45.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.76|seed=?|tau=?|tr=?|norm=?|mtime=1779567131.6725698\\neval_object_vla_only_seed47.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779225251.1051867\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbcf642-be59-4ac1-a0a5-15f36bcc29ff",
  "uuid": "e4b983d4-a1b4-4b4e-9099-f8f7992dc3a7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.85|seed=?|tau=?|tr=?|norm=?|mtime=1779549505.0621097\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779550003.4908967\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.84|seed=?|tau=?|tr=?|norm=?|mtime=1779526362.0417063\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779585591.7900822\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.845|seed=?|tau=?|tr=?|norm=?|mtime=1779645319.0771303\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.815|seed=?|tau=?|tr=?|norm=?|mtime=1779645913.180236\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779549390.4939702\\\\neval_goal_adaptive_conformal_crm_tau0.25_seed47.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779624214.8184283\\\\neval_goal_crm_obs_only_norm0.05_seed42.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.855|seed=?|tau=?|tr=?|norm=?|mtime=1779517392.569333\\\\neval_goal_crm_obs_only_norm0.05_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779539474.0705094\\\\neval_goal_crm_obs_only_norm0.05_seed45.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779576334.434667\\\\neval_goal_crm_obs_only_norm0.05_seed46.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779585677.870676\\\\neval_goal_crm_obs_only_norm0.05_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779623912.9975011\\\\neval_goal_crm_obs_only_norm0.05_seed48.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.8|seed=?|tau=?|tr=?|norm=?|mtime=1779661966.0933068\\\\neval_goal_k2mean_seed46.json|mode=vla_only|bm=mean|K=?|nr=20|SR=0.825|seed=?|tau=?|tr=?|norm=?|mtime=1779585432.3525603\\\\neval_goal_obs_only_norm02_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.69|seed=?|tau=?|tr=?|norm=?|mtime=1779250596.8733935\\\\neval_goal_obs_only_norm02_seed48.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.68|seed=?|tau=?|tr=?|norm=?|mtime=1779250876.6610563\\\\neval_goal_obs_only_norm02_seed49.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.62|seed=?|tau=?|tr=?|norm=?|mtime=1779260314.9717753\\\\neval_goal_obs_only_norm02_seed50.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.67|seed=?|tau=?|tr=?|norm=?|mtime=1779260258.1875696\\\\neval_goal_reconvla_seed42.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779528564.048699\\\\neval_goal_reconvla_seed44.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.805|seed=?|tau=?|tr=?|norm=?|mtime=1779539552.3289988\\\\neval_goal_reconvla_seed45.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.855|seed=?|tau=?|tr=?|norm=?|mtime=1779575953.7916744\\\\neval_goal_reconvla_seed46.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779586066.3842058\\\\neval_goal_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779623803.4525318\\\\neval_goal_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779528693.3852956\\\\neval_goal_vla_only_seed44_r2.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.73|seed=?|tau=?|tr=?|norm=?|mtime=1779214848.283968\\\\neval_goal_vla_only_seed45.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779575976.9561207\\\\neval_goal_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.83|seed=?|tau=?|tr=?|norm=?|mtime=1779585604.1747642\\\\neval_goal_vla_only_seed47.json|mode=vla_only|bm=mean|K=?|nr=20|S\\\\n\\\\n... [截断: 输出过长，省略 4208 字符] ...\\\\n\\\\nrm_perdof|bm=single|K=?|nr=10|SR=0.0|seed=?|tau=?|tr=?|norm=?|mtime=1779182777.447817\\\\neval_object_perdof_norm003.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1778918839.1050653\\\\neval_object_perdof_norm003_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779177862.2909682\\\\neval_object_perdof_norm005.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1778920150.0054674\\\\neval_object_perdof_norm005_seed45.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779197057.5790293\\\\neval_object_perdof_norm01_seed42.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779117175.6900625\\\\neval_object_perdof_norm02_seed43_r3.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1778927925.6223562\\\\neval_object_perdof_norm02_seed44.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779036519.8630602\\\\neval_object_perdof_norm02_seed45.json|mode=crm_perdof|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779037238.8097897\\\\neval_object_perdof_norm02_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779070916.6589944\\\\neval_object_perdof_norm02_seed47.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779078884.6691506\\\\neval_object_perdof_norm02_seed48.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.07|seed=?|tau=?|tr=?|norm=?|mtime=1779114863.6627562\\\\neval_object_perdof_norm03_r3.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.04|seed=?|tau=?|tr=?|norm=?|mtime=1778929371.5343606\\\\neval_object_perdof_norm03_seed47.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.05|seed=?|tau=?|tr=?|norm=?|mtime=1779180058.680503\\\\neval_object_random_selection_k5_seed43.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779206635.0573328\\\\neval_object_random_selection_seed42.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779266724.7550728\\\\neval_object_random_selection_seed43.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779119137.8045802\\\\neval_object_random_selection_seed44.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779266661.5051854\\\\neval_object_random_selection_seed45.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779179392.522475\\\\neval_object_reconvla_k5_seed42.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779193280.5257018\\\\neval_object_reconvla_seed42.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779519252.2247827\\\\neval_object_reconvla_seed43.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779536616.4167185\\\\neval_object_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.765|seed=?|tau=?|tr=?|norm=?|mtime=1779625593.4554389\\\\neval_object_scalar_seed45.json|mode=crm_scalar|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779038782.577561\\\\neval_object_vla_mean_seed45.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1778988474.8153772\\\\neval_object_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.865|seed=?|tau=?|tr=?|norm=?|mtime=1779648601.1655722\\\\neval_object_vla_only_seed42.json|mode=vla_only|bm=mean|K=?|nr=20|SR=0.795|seed=?|tau=?|tr=?|norm=?|mtime=1779530392.1805253\\\\neval_object_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779519458.5314624\\\\neval_object_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779519465.7787242\\\\neval_object_vla_only_seed45.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.76|seed=?|tau=?|tr=?|norm=?|mtime=1779567131.6725698\\\\neval_object_vla_only_seed47.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779225251.1051867\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.85|seed=?|tau=?|tr=?|norm=?|mtime=1779549505.0621097\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779550003.4908967\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.84|seed=?|tau=?|tr=?|norm=?|mtime=1779526362.0417063\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779585591.7900822\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.845|seed=?|tau=?|tr=?|norm=?|mtime=1779645319.0771303\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.815|seed=?|tau=?|tr=?|norm=?|mtime=1779645913.180236\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779549390.4939702\\neval_goal_adaptive_conformal_crm_tau0.25_seed47.json|mode=adaptive_conformal_crm|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779624214.8184283\\neval_goal_crm_obs_only_norm0.05_seed42.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.855|seed=?|tau=?|tr=?|norm=?|mtime=1779517392.569333\\neval_goal_crm_obs_only_norm0.05_seed44.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779539474.0705094\\neval_goal_crm_obs_only_norm0.05_seed45.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779576334.434667\\neval_goal_crm_obs_only_norm0.05_seed46.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779585677.870676\\neval_goal_crm_obs_only_norm0.05_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.82|seed=?|tau=?|tr=?|norm=?|mtime=1779623912.9975011\\neval_goal_crm_obs_only_norm0.05_seed48.json|mode=crm_obs_only|bm=single|K=?|nr=20|SR=0.8|seed=?|tau=?|tr=?|norm=?|mtime=1779661966.0933068\\neval_goal_k2mean_seed46.json|mode=vla_only|bm=mean|K=?|nr=20|SR=0.825|seed=?|tau=?|tr=?|norm=?|mtime=1779585432.3525603\\neval_goal_obs_only_norm02_seed47.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.69|seed=?|tau=?|tr=?|norm=?|mtime=1779250596.8733935\\neval_goal_obs_only_norm02_seed48.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.68|seed=?|tau=?|tr=?|norm=?|mtime=1779250876.6610563\\neval_goal_obs_only_norm02_seed49.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.62|seed=?|tau=?|tr=?|norm=?|mtime=1779260314.9717753\\neval_goal_obs_only_norm02_seed50.json|mode=crm_obs_only|bm=single|K=?|nr=10|SR=0.67|seed=?|tau=?|tr=?|norm=?|mtime=1779260258.1875696\\neval_goal_reconvla_seed42.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.81|seed=?|tau=?|tr=?|norm=?|mtime=1779528564.048699\\neval_goal_reconvla_seed44.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.805|seed=?|tau=?|tr=?|norm=?|mtime=1779539552.3289988\\neval_goal_reconvla_seed45.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.855|seed=?|tau=?|tr=?|norm=?|mtime=1779575953.7916744\\neval_goal_reconvla_seed46.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779586066.3842058\\neval_goal_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779623803.4525318\\neval_goal_vla_only_seed42.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779528693.3852956\\neval_goal_vla_only_seed44_r2.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.73|seed=?|tau=?|tr=?|norm=?|mtime=1779214848.283968\\neval_goal_vla_only_seed45.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.835|seed=?|tau=?|tr=?|norm=?|mtime=1779575976.9561207\\neval_goal_vla_only_seed46.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.83|seed=?|tau=?|tr=?|norm=?|mtime=1779585604.1747642\\neval_goal_vla_only_seed47.json|mode=vla_only|bm=mean|K=?|nr=20|S\\n\\n... [截断: 输出过长，省略 4208 字符] ...\\n\\nrm_perdof|bm=single|K=?|nr=10|SR=0.0|seed=?|tau=?|tr=?|norm=?|mtime=1779182777.447817\\neval_object_perdof_norm003.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1778918839.1050653\\neval_object_perdof_norm003_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779177862.2909682\\neval_object_perdof_norm005.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.14|seed=?|tau=?|tr=?|norm=?|mtime=1778920150.0054674\\neval_object_perdof_norm005_seed45.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779197057.5790293\\neval_object_perdof_norm01_seed42.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779117175.6900625\\neval_object_perdof_norm02_seed43_r3.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1778927925.6223562\\neval_object_perdof_norm02_seed44.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779036519.8630602\\neval_object_perdof_norm02_seed45.json|mode=crm_perdof|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779037238.8097897\\neval_object_perdof_norm02_seed46.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779070916.6589944\\neval_object_perdof_norm02_seed47.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779078884.6691506\\neval_object_perdof_norm02_seed48.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.07|seed=?|tau=?|tr=?|norm=?|mtime=1779114863.6627562\\neval_object_perdof_norm03_r3.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.04|seed=?|tau=?|tr=?|norm=?|mtime=1778929371.5343606\\neval_object_perdof_norm03_seed47.json|mode=crm_perdof|bm=single|K=?|nr=10|SR=0.05|seed=?|tau=?|tr=?|norm=?|mtime=1779180058.680503\\neval_object_random_selection_k5_seed43.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779206635.0573328\\neval_object_random_selection_seed42.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779266724.7550728\\neval_object_random_selection_seed43.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779119137.8045802\\neval_object_random_selection_seed44.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.11|seed=?|tau=?|tr=?|norm=?|mtime=1779266661.5051854\\neval_object_random_selection_seed45.json|mode=random_selection|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779179392.522475\\neval_object_reconvla_k5_seed42.json|mode=reconvla|bm=single|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1779193280.5257018\\neval_object_reconvla_seed42.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.79|seed=?|tau=?|tr=?|norm=?|mtime=1779519252.2247827\\neval_object_reconvla_seed43.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779536616.4167185\\neval_object_reconvla_seed47.json|mode=reconvla|bm=single|K=?|nr=20|SR=0.765|seed=?|tau=?|tr=?|norm=?|mtime=1779625593.4554389\\neval_object_scalar_seed45.json|mode=crm_scalar|bm=single|K=?|nr=20|SR=0.09|seed=?|tau=?|tr=?|norm=?|mtime=1779038782.577561\\neval_object_vla_mean_seed45.json|mode=vla_only|bm=mean|K=?|nr=10|SR=0.13|seed=?|tau=?|tr=?|norm=?|mtime=1778988474.8153772\\neval_object_vla_only_pi05_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.865|seed=?|tau=?|tr=?|norm=?|mtime=1779648601.1655722\\neval_object_vla_only_seed42.json|mode=vla_only|bm=mean|K=?|nr=20|SR=0.795|seed=?|tau=?|tr=?|norm=?|mtime=1779530392.1805253\\neval_object_vla_only_seed43.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.77|seed=?|tau=?|tr=?|norm=?|mtime=1779519458.5314624\\neval_object_vla_only_seed44.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.775|seed=?|tau=?|tr=?|norm=?|mtime=1779519465.7787242\\neval_object_vla_only_seed45.json|mode=vla_only|bm=single|K=?|nr=20|SR=0.76|seed=?|tau=?|tr=?|norm=?|mtime=1779567131.6725698\\neval_object_vla_only_seed47.json|mode=vla_only|bm=single|K=?|nr=10|SR=0.1|seed=?|tau=?|tr=?|norm=?|mtime=1779225251.1051867\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---
