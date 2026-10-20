# ssh rsa method audit — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ssh-rsa-method-audit.md) · [Structured JSON](../../../sessions/89/897db267de81db9c13c1.json)

## Before a recorded user message

### Tool result

_source line 297 · 2026-05-16T02:52:50.828Z_

<details><summary>↩ Tool result · `toolu_01BxD3PLcmeAfsL5kCSXzm5A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"models\\\": {\\n    \\\"dino_cls\\\": {\\n      \\\"method_A\\\": 0.3881,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.4909,\\n        \\\"mid\\\": 0.4132,\\n        \\\"late\\\": 0.2601\\n      },\\n      \\\"method_B\\\": 0.6412,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.2874,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.9224,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.8455,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.6378,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.6839,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.8166,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.242,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.892,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.6084,\\n        \\\"turn_on_the_stove\\\": 0.4763\\n      },\\n      \\\"A_with_euc_act\\\": 0.4148,\\n      \\\"B_with_cos_act\\\": 0.5913,\\n      \\\"C_crosstask_full_euc\\\": 0.4747,\\n      \\\"C_crosstask_full_cos\\\": 0.4518\\n    },\\n    \\\"dino_patch_mean\\\": {\\n      \\\"method_A\\\": 0.3712,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.3688,\\n        \\\"mid\\\": 0.4594,\\n        \\\"late\\\": 0.2855\\n      },\\n      \\\"method_B\\\": 0.5675,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.2158,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.8656,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.8744,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.5863,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.5679,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.7967,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.1336,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.8999,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.4756,\\n        \\\"turn_on_the_stove\\\": 0.2594\\n      },\\n      \\\"A_with_euc_act\\\": 0.419,\\n      \\\"B_with_cos_act\\\": 0.5118,\\n      \\\"C_crosstask_full_euc\\\": 0.521,\\n      \\\"C_crosstask_full_cos\\\": 0.4786\\n    },\\n    \\\"clip_cls\\\": {\\n      \\\"method_A\\\": 0.4565,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.3346,\\n        \\\"mid\\\": 0.5465,\\n        \\\"late\\\": 0.4885\\n      },\\n      \\\"method_B\\\": 0.4818,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.1848,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.7323,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.8913,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.6885,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.0787,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.2386,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.5109,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.847,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.6007,\\n        \\\"turn_on_the_stove\\\": 0.0448\\n      },\\n      \\\"A_with_euc_act\\\": 0.499,\\n      \\\"B_with_cos_act\\\": 0.4648,\\n      \\\"C_crosstask_full_euc\\\": 0.6562,\\n      \\\"C_crosstask_full_cos\\\": 0.6178\\n    },\\n    \\\"clip_patch_mean\\\": {\\n      \\\"method_A\\\": 0.4788,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.3602,\\n        \\\"mid\\\": 0.5874,\\n        \\\"late\\\": 0.4889\\n      },\\n      \\\"method_B\\\": 0.5408,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.1776,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.832,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.9054,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.7235,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.2045,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.4897,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.4646,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.8984,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.5788,\\n        \\\"turn_on_the_stove\\\": 0.1337\\n      },\\n      \\\"A_with_euc_act\\\": 0.5393,\\n      \\\"B_with_cos_act\\\": 0.5209,\\n      \\\"C_crosstask_full_euc\\\": 0.7074,\\n      \\\"C_crosstask_full_cos\\\": 0.6595\\n    },\\n    \\\"siglip_projector\\\": {\\n      \\\"method_A\\\": 0.4509,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.4406,\\n        \\\"mid\\\": 0.5239,\\n        \\\"late\\\": 0.3883\\n      },\\n      \\\"method_B\\\": 0.5645,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.3456,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.804,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.898,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.53,\\n  \\n\\n... [截断: 输出过长，省略 2646 字符] ...\\n\\ntask + full trajectory + cosine (isolates phase effect from A)\\\"\\n  },\\n  \\\"scripts_compared\\\": {\\n    \\\"method_A_script\\\": \\\"rsa_analysis.py (line 1-486, /root/vla-ssd/rsa_analysis.py)\\\",\\n    \\\"method_B_script\\\": \\\"rsa_siglip_only.py + rsa_clip.py (/root/vla-ssd/scripts/)\\\"\\n  },\\n  \\\"three_differences\\\": {\\n    \\\"1_rdm_scope\\\": {\\n      \\\"method_A\\\": \\\"Cross-task: single 100x100 RDM (10 tasks x 10 demos), includes cross-task pairs\\\",\\n      \\\"method_B\\\": \\\"Per-task: 10 separate ~10x10 RDMs, one per task, average across tasks\\\",\\n      \\\"impact\\\": \\\"DOMINANT (~66% of DINO gap). Cross-task dilutes DINO RSA because DINO features across tasks are similar (shared LIBERO-Goal scene) but actions differ greatly.\\\",\\n      \\\"code_location\\\": \\\"rsa_analysis.py:main() builds flat dict with (task,did) keys vs rsa_siglip_only.py iterates tasks independently\\\"\\n    },\\n    \\\"2_temporal\\\": {\\n      \\\"method_A\\\": \\\"Split trajectory into 3 phases (early 0-33%, mid 33-67%, late 67-100%), compute RSA per phase, average\\\",\\n      \\\"method_B\\\": \\\"Full trajectory, uniformly subsample to N_SAMPLE=20 timesteps\\\",\\n      \\\"impact\\\": \\\"MODERATE (~24% of DINO gap). DINO late-phase RSA=0.26 drags average down.\\\",\\n      \\\"code_location\\\": \\\"rsa_analysis.py:TEMPORAL_BINS + get_temporal_indices() vs rsa_siglip_only.py:subsample_to_length()\\\"\\n    },\\n    \\\"3_action_distance\\\": {\\n      \\\"method_A\\\": \\\"Cosine distance on action vectors (7-dim), via build_dissimilarity_matrix()\\\",\\n      \\\"method_B\\\": \\\"Euclidean distance on action vectors, via mean_action_distance()\\\",\\n      \\\"impact\\\": \\\"MINOR (~10% of DINO gap). Cosine on small action vectors has different sensitivity than euclidean.\\\",\\n      \\\"code_location\\\": \\\"rsa_analysis.py:build_dissimilarity_matrix() uses compute_mean_cosine_distance() for both features AND actions; rsa_siglip_only.py has separate mean_action_distance() using np.linalg.norm\\\"\\n    }\\n  },\\n  \\\"fourth_difference_n_demos\\\": {\\n    \\\"description\\\": \\\"rsa_analysis.py uses --n_demos=10 (default), rsa_siglip_only.py/rsa_clip.py load ALL demos (~50/task)\\\",\\n    \\\"effect\\\": \\\"More demos -> more pairs -> slightly different RSA. DINO cls 10demos=0.641 vs 50demos=~0.692.\\\",\\n    \\\"not_root_cause\\\": \\\"This explains the residual gap between our 10-demo Method B (0.641) and previously reported 50-demo (0.692), but is NOT the main methodology issue.\\\"\\n  },\\n  \\\"critical_finding\\\": \\\"The originally reported comparison (SigLIP=0.615 vs VLA_trained=0.488 vs DINO=0.388) mixed Method A and Method B: SigLIP=0.615 was Method B (per-task, 50 demos), while VLA=0.488 and DINO=0.388 were Method A (cross-task, 10 demos, phase split). This is an apples-to-oranges comparison and must be corrected in the paper.\\\",\\n  \\\"unified_table_method_B_10demos\\\": {\\n    \\\"description\\\": \\\"All models computed with Method B (per-task + full trajectory + euclidean action), 10 demos/task\\\",\\n    \\\"results\\\": {\\n      \\\"dino_cls\\\": 0.6412,\\n      \\\"dino_patch_mean\\\": 0.5675,\\n      \\\"clip_cls\\\": 0.4818,\\n      \\\"clip_patch_mean\\\": 0.5408,\\n      \\\"siglip_projector\\\": 0.5645,\\n      \\\"vla_trained_L9\\\": 0.499,\\n      \\\"vla_untrained_L9\\\": 0.5767\\n    },\\n    \\\"ranking\\\": \\\"DINO_cls(0.641) > VLA_untrained(0.577) > DINO_pm(0.568) > SigLIP(0.565) > CLIP_pm(0.541) > VLA_trained(0.499) > CLIP_cls(0.482)\\\"\\n  },\\n  \\\"recommendation\\\": {\\n    \\\"method\\\": \\\"Method B (per-task + full trajectory + euclidean action distance)\\\",\\n    \\\"n_demos\\\": \\\"Use ALL demos (50/task) for maximum statistical power, OR use 10/task for all models consistently\\\",\\n    \\\"rationale\\\": [\\n      \\\"Per-task RSA is standard: measures feature discriminability for execution variants of SAME task\\\",\\n      \\\"Full trajectory avoids arbitrary phase boundaries\\\",\\n      \\\"Euclidean is natural for continuous 7-dim action space\\\",\\n      \\\"SigLIP was already Method B, so Method B achieves backward compatibility\\\"\\n    ],\\n    \\\"action_items\\\": [\\n      \\\"Re-run all models with unified Method B + consistent N_DEMOS\\\",\\n      \\\"Replace all RSA numbers in the paper with unified results\\\",\\n      \\\"DINO is NOT low-RSA baseline (0.641), it is actually HIGHEST RSA \\\\u2014 this changes the narrative\\\"\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ab8e7d-57e0-4fff-8ef0-f0a9a442867b",
  "uuid": "e0e1773e-939f-44fc-89ee-d9bd79a91de7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"models\\\\\\\": {\\\\n    \\\\\\\"dino_cls\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": 0.3881,\\\\n      \\\\\\\"method_A_phases\\\\\\\": {\\\\n        \\\\\\\"early\\\\\\\": 0.4909,\\\\n        \\\\\\\"mid\\\\\\\": 0.4132,\\\\n        \\\\\\\"late\\\\\\\": 0.2601\\\\n      },\\\\n      \\\\\\\"method_B\\\\\\\": 0.6412,\\\\n      \\\\\\\"method_B_per_task\\\\\\\": {\\\\n        \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": 0.2874,\\\\n        \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": 0.9224,\\\\n        \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": 0.8455,\\\\n        \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": 0.6378,\\\\n        \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": 0.6839,\\\\n        \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": 0.8166,\\\\n        \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": 0.242,\\\\n        \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": 0.892,\\\\n        \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": 0.6084,\\\\n        \\\\\\\"turn_on_the_stove\\\\\\\": 0.4763\\\\n      },\\\\n      \\\\\\\"A_with_euc_act\\\\\\\": 0.4148,\\\\n      \\\\\\\"B_with_cos_act\\\\\\\": 0.5913,\\\\n      \\\\\\\"C_crosstask_full_euc\\\\\\\": 0.4747,\\\\n      \\\\\\\"C_crosstask_full_cos\\\\\\\": 0.4518\\\\n    },\\\\n    \\\\\\\"dino_patch_mean\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": 0.3712,\\\\n      \\\\\\\"method_A_phases\\\\\\\": {\\\\n        \\\\\\\"early\\\\\\\": 0.3688,\\\\n        \\\\\\\"mid\\\\\\\": 0.4594,\\\\n        \\\\\\\"late\\\\\\\": 0.2855\\\\n      },\\\\n      \\\\\\\"method_B\\\\\\\": 0.5675,\\\\n      \\\\\\\"method_B_per_task\\\\\\\": {\\\\n        \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": 0.2158,\\\\n        \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": 0.8656,\\\\n        \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": 0.8744,\\\\n        \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": 0.5863,\\\\n        \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": 0.5679,\\\\n        \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": 0.7967,\\\\n        \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": 0.1336,\\\\n        \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": 0.8999,\\\\n        \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": 0.4756,\\\\n        \\\\\\\"turn_on_the_stove\\\\\\\": 0.2594\\\\n      },\\\\n      \\\\\\\"A_with_euc_act\\\\\\\": 0.419,\\\\n      \\\\\\\"B_with_cos_act\\\\\\\": 0.5118,\\\\n      \\\\\\\"C_crosstask_full_euc\\\\\\\": 0.521,\\\\n      \\\\\\\"C_crosstask_full_cos\\\\\\\": 0.4786\\\\n    },\\\\n    \\\\\\\"clip_cls\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": 0.4565,\\\\n      \\\\\\\"method_A_phases\\\\\\\": {\\\\n        \\\\\\\"early\\\\\\\": 0.3346,\\\\n        \\\\\\\"mid\\\\\\\": 0.5465,\\\\n        \\\\\\\"late\\\\\\\": 0.4885\\\\n      },\\\\n      \\\\\\\"method_B\\\\\\\": 0.4818,\\\\n      \\\\\\\"method_B_per_task\\\\\\\": {\\\\n        \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": 0.1848,\\\\n        \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": 0.7323,\\\\n        \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": 0.8913,\\\\n        \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": 0.6885,\\\\n        \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": 0.0787,\\\\n        \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": 0.2386,\\\\n        \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": 0.5109,\\\\n        \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": 0.847,\\\\n        \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": 0.6007,\\\\n        \\\\\\\"turn_on_the_stove\\\\\\\": 0.0448\\\\n      },\\\\n      \\\\\\\"A_with_euc_act\\\\\\\": 0.499,\\\\n      \\\\\\\"B_with_cos_act\\\\\\\": 0.4648,\\\\n      \\\\\\\"C_crosstask_full_euc\\\\\\\": 0.6562,\\\\n      \\\\\\\"C_crosstask_full_cos\\\\\\\": 0.6178\\\\n    },\\\\n    \\\\\\\"clip_patch_mean\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": 0.4788,\\\\n      \\\\\\\"method_A_phases\\\\\\\": {\\\\n        \\\\\\\"early\\\\\\\": 0.3602,\\\\n        \\\\\\\"mid\\\\\\\": 0.5874,\\\\n        \\\\\\\"late\\\\\\\": 0.4889\\\\n      },\\\\n      \\\\\\\"method_B\\\\\\\": 0.5408,\\\\n      \\\\\\\"method_B_per_task\\\\\\\": {\\\\n        \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": 0.1776,\\\\n        \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": 0.832,\\\\n        \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": 0.9054,\\\\n        \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": 0.7235,\\\\n        \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": 0.2045,\\\\n        \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": 0.4897,\\\\n        \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": 0.4646,\\\\n        \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": 0.8984,\\\\n        \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": 0.5788,\\\\n        \\\\\\\"turn_on_the_stove\\\\\\\": 0.1337\\\\n      },\\\\n      \\\\\\\"A_with_euc_act\\\\\\\": 0.5393,\\\\n      \\\\\\\"B_with_cos_act\\\\\\\": 0.5209,\\\\n      \\\\\\\"C_crosstask_full_euc\\\\\\\": 0.7074,\\\\n      \\\\\\\"C_crosstask_full_cos\\\\\\\": 0.6595\\\\n    },\\\\n    \\\\\\\"siglip_projector\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": 0.4509,\\\\n      \\\\\\\"method_A_phases\\\\\\\": {\\\\n        \\\\\\\"early\\\\\\\": 0.4406,\\\\n        \\\\\\\"mid\\\\\\\": 0.5239,\\\\n        \\\\\\\"late\\\\\\\": 0.3883\\\\n      },\\\\n      \\\\\\\"method_B\\\\\\\": 0.5645,\\\\n      \\\\\\\"method_B_per_task\\\\\\\": {\\\\n        \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": 0.3456,\\\\n        \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": 0.804,\\\\n        \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": 0.898,\\\\n        \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": 0.53,\\\\n  \\\\n\\\\n... [截断: 输出过长，省略 2646 字符] ...\\\\n\\\\ntask + full trajectory + cosine (isolates phase effect from A)\\\\\\\"\\\\n  },\\\\n  \\\\\\\"scripts_compared\\\\\\\": {\\\\n    \\\\\\\"method_A_script\\\\\\\": \\\\\\\"rsa_analysis.py (line 1-486, /root/vla-ssd/rsa_analysis.py)\\\\\\\",\\\\n    \\\\\\\"method_B_script\\\\\\\": \\\\\\\"rsa_siglip_only.py + rsa_clip.py (/root/vla-ssd/scripts/)\\\\\\\"\\\\n  },\\\\n  \\\\\\\"three_differences\\\\\\\": {\\\\n    \\\\\\\"1_rdm_scope\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": \\\\\\\"Cross-task: single 100x100 RDM (10 tasks x 10 demos), includes cross-task pairs\\\\\\\",\\\\n      \\\\\\\"method_B\\\\\\\": \\\\\\\"Per-task: 10 separate ~10x10 RDMs, one per task, average across tasks\\\\\\\",\\\\n      \\\\\\\"impact\\\\\\\": \\\\\\\"DOMINANT (~66% of DINO gap). Cross-task dilutes DINO RSA because DINO features across tasks are similar (shared LIBERO-Goal scene) but actions differ greatly.\\\\\\\",\\\\n      \\\\\\\"code_location\\\\\\\": \\\\\\\"rsa_analysis.py:main() builds flat dict with (task,did) keys vs rsa_siglip_only.py iterates tasks independently\\\\\\\"\\\\n    },\\\\n    \\\\\\\"2_temporal\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": \\\\\\\"Split trajectory into 3 phases (early 0-33%, mid 33-67%, late 67-100%), compute RSA per phase, average\\\\\\\",\\\\n      \\\\\\\"method_B\\\\\\\": \\\\\\\"Full trajectory, uniformly subsample to N_SAMPLE=20 timesteps\\\\\\\",\\\\n      \\\\\\\"impact\\\\\\\": \\\\\\\"MODERATE (~24% of DINO gap). DINO late-phase RSA=0.26 drags average down.\\\\\\\",\\\\n      \\\\\\\"code_location\\\\\\\": \\\\\\\"rsa_analysis.py:TEMPORAL_BINS + get_temporal_indices() vs rsa_siglip_only.py:subsample_to_length()\\\\\\\"\\\\n    },\\\\n    \\\\\\\"3_action_distance\\\\\\\": {\\\\n      \\\\\\\"method_A\\\\\\\": \\\\\\\"Cosine distance on action vectors (7-dim), via build_dissimilarity_matrix()\\\\\\\",\\\\n      \\\\\\\"method_B\\\\\\\": \\\\\\\"Euclidean distance on action vectors, via mean_action_distance()\\\\\\\",\\\\n      \\\\\\\"impact\\\\\\\": \\\\\\\"MINOR (~10% of DINO gap). Cosine on small action vectors has different sensitivity than euclidean.\\\\\\\",\\\\n      \\\\\\\"code_location\\\\\\\": \\\\\\\"rsa_analysis.py:build_dissimilarity_matrix() uses compute_mean_cosine_distance() for both features AND actions; rsa_siglip_only.py has separate mean_action_distance() using np.linalg.norm\\\\\\\"\\\\n    }\\\\n  },\\\\n  \\\\\\\"fourth_difference_n_demos\\\\\\\": {\\\\n    \\\\\\\"description\\\\\\\": \\\\\\\"rsa_analysis.py uses --n_demos=10 (default), rsa_siglip_only.py/rsa_clip.py load ALL demos (~50/task)\\\\\\\",\\\\n    \\\\\\\"effect\\\\\\\": \\\\\\\"More demos -> more pairs -> slightly different RSA. DINO cls 10demos=0.641 vs 50demos=~0.692.\\\\\\\",\\\\n    \\\\\\\"not_root_cause\\\\\\\": \\\\\\\"This explains the residual gap between our 10-demo Method B (0.641) and previously reported 50-demo (0.692), but is NOT the main methodology issue.\\\\\\\"\\\\n  },\\\\n  \\\\\\\"critical_finding\\\\\\\": \\\\\\\"The originally reported comparison (SigLIP=0.615 vs VLA_trained=0.488 vs DINO=0.388) mixed Method A and Method B: SigLIP=0.615 was Method B (per-task, 50 demos), while VLA=0.488 and DINO=0.388 were Method A (cross-task, 10 demos, phase split). This is an apples-to-oranges comparison and must be corrected in the paper.\\\\\\\",\\\\n  \\\\\\\"unified_table_method_B_10demos\\\\\\\": {\\\\n    \\\\\\\"description\\\\\\\": \\\\\\\"All models computed with Method B (per-task + full trajectory + euclidean action), 10 demos/task\\\\\\\",\\\\n    \\\\\\\"results\\\\\\\": {\\\\n      \\\\\\\"dino_cls\\\\\\\": 0.6412,\\\\n      \\\\\\\"dino_patch_mean\\\\\\\": 0.5675,\\\\n      \\\\\\\"clip_cls\\\\\\\": 0.4818,\\\\n      \\\\\\\"clip_patch_mean\\\\\\\": 0.5408,\\\\n      \\\\\\\"siglip_projector\\\\\\\": 0.5645,\\\\n      \\\\\\\"vla_trained_L9\\\\\\\": 0.499,\\\\n      \\\\\\\"vla_untrained_L9\\\\\\\": 0.5767\\\\n    },\\\\n    \\\\\\\"ranking\\\\\\\": \\\\\\\"DINO_cls(0.641) > VLA_untrained(0.577) > DINO_pm(0.568) > SigLIP(0.565) > CLIP_pm(0.541) > VLA_trained(0.499) > CLIP_cls(0.482)\\\\\\\"\\\\n  },\\\\n  \\\\\\\"recommendation\\\\\\\": {\\\\n    \\\\\\\"method\\\\\\\": \\\\\\\"Method B (per-task + full trajectory + euclidean action distance)\\\\\\\",\\\\n    \\\\\\\"n_demos\\\\\\\": \\\\\\\"Use ALL demos (50/task) for maximum statistical power, OR use 10/task for all models consistently\\\\\\\",\\\\n    \\\\\\\"rationale\\\\\\\": [\\\\n      \\\\\\\"Per-task RSA is standard: measures feature discriminability for execution variants of SAME task\\\\\\\",\\\\n      \\\\\\\"Full trajectory avoids arbitrary phase boundaries\\\\\\\",\\\\n      \\\\\\\"Euclidean is natural for continuous 7-dim action space\\\\\\\",\\\\n      \\\\\\\"SigLIP was already Method B, so Method B achieves backward compatibility\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"action_items\\\\\\\": [\\\\n      \\\\\\\"Re-run all models with unified Method B + consistent N_DEMOS\\\\\\\",\\\\n      \\\\\\\"Replace all RSA numbers in the paper with unified results\\\\\\\",\\\\n      \\\\\\\"DINO is NOT low-RSA baseline (0.641), it is actually HIGHEST RSA \\\\\\\\u2014 this changes the narrative\\\\\\\"\\\\n    ]\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"models\\\": {\\n    \\\"dino_cls\\\": {\\n      \\\"method_A\\\": 0.3881,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.4909,\\n        \\\"mid\\\": 0.4132,\\n        \\\"late\\\": 0.2601\\n      },\\n      \\\"method_B\\\": 0.6412,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.2874,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.9224,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.8455,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.6378,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.6839,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.8166,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.242,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.892,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.6084,\\n        \\\"turn_on_the_stove\\\": 0.4763\\n      },\\n      \\\"A_with_euc_act\\\": 0.4148,\\n      \\\"B_with_cos_act\\\": 0.5913,\\n      \\\"C_crosstask_full_euc\\\": 0.4747,\\n      \\\"C_crosstask_full_cos\\\": 0.4518\\n    },\\n    \\\"dino_patch_mean\\\": {\\n      \\\"method_A\\\": 0.3712,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.3688,\\n        \\\"mid\\\": 0.4594,\\n        \\\"late\\\": 0.2855\\n      },\\n      \\\"method_B\\\": 0.5675,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.2158,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.8656,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.8744,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.5863,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.5679,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.7967,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.1336,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.8999,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.4756,\\n        \\\"turn_on_the_stove\\\": 0.2594\\n      },\\n      \\\"A_with_euc_act\\\": 0.419,\\n      \\\"B_with_cos_act\\\": 0.5118,\\n      \\\"C_crosstask_full_euc\\\": 0.521,\\n      \\\"C_crosstask_full_cos\\\": 0.4786\\n    },\\n    \\\"clip_cls\\\": {\\n      \\\"method_A\\\": 0.4565,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.3346,\\n        \\\"mid\\\": 0.5465,\\n        \\\"late\\\": 0.4885\\n      },\\n      \\\"method_B\\\": 0.4818,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.1848,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.7323,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.8913,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.6885,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.0787,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.2386,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.5109,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.847,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.6007,\\n        \\\"turn_on_the_stove\\\": 0.0448\\n      },\\n      \\\"A_with_euc_act\\\": 0.499,\\n      \\\"B_with_cos_act\\\": 0.4648,\\n      \\\"C_crosstask_full_euc\\\": 0.6562,\\n      \\\"C_crosstask_full_cos\\\": 0.6178\\n    },\\n    \\\"clip_patch_mean\\\": {\\n      \\\"method_A\\\": 0.4788,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.3602,\\n        \\\"mid\\\": 0.5874,\\n        \\\"late\\\": 0.4889\\n      },\\n      \\\"method_B\\\": 0.5408,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.1776,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.832,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.9054,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.7235,\\n        \\\"put_the_bowl_on_the_stove\\\": 0.2045,\\n        \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.4897,\\n        \\\"put_the_cream_cheese_in_the_bowl\\\": 0.4646,\\n        \\\"put_the_wine_bottle_on_the_rack\\\": 0.8984,\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.5788,\\n        \\\"turn_on_the_stove\\\": 0.1337\\n      },\\n      \\\"A_with_euc_act\\\": 0.5393,\\n      \\\"B_with_cos_act\\\": 0.5209,\\n      \\\"C_crosstask_full_euc\\\": 0.7074,\\n      \\\"C_crosstask_full_cos\\\": 0.6595\\n    },\\n    \\\"siglip_projector\\\": {\\n      \\\"method_A\\\": 0.4509,\\n      \\\"method_A_phases\\\": {\\n        \\\"early\\\": 0.4406,\\n        \\\"mid\\\": 0.5239,\\n        \\\"late\\\": 0.3883\\n      },\\n      \\\"method_B\\\": 0.5645,\\n      \\\"method_B_per_task\\\": {\\n        \\\"open_the_middle_drawer_of_the_cabinet\\\": 0.3456,\\n        \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.804,\\n        \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.898,\\n        \\\"put_the_bowl_on_the_plate\\\": 0.53,\\n  \\n\\n... [截断: 输出过长，省略 2646 字符] ...\\n\\ntask + full trajectory + cosine (isolates phase effect from A)\\\"\\n  },\\n  \\\"scripts_compared\\\": {\\n    \\\"method_A_script\\\": \\\"rsa_analysis.py (line 1-486, /root/vla-ssd/rsa_analysis.py)\\\",\\n    \\\"method_B_script\\\": \\\"rsa_siglip_only.py + rsa_clip.py (/root/vla-ssd/scripts/)\\\"\\n  },\\n  \\\"three_differences\\\": {\\n    \\\"1_rdm_scope\\\": {\\n      \\\"method_A\\\": \\\"Cross-task: single 100x100 RDM (10 tasks x 10 demos), includes cross-task pairs\\\",\\n      \\\"method_B\\\": \\\"Per-task: 10 separate ~10x10 RDMs, one per task, average across tasks\\\",\\n      \\\"impact\\\": \\\"DOMINANT (~66% of DINO gap). Cross-task dilutes DINO RSA because DINO features across tasks are similar (shared LIBERO-Goal scene) but actions differ greatly.\\\",\\n      \\\"code_location\\\": \\\"rsa_analysis.py:main() builds flat dict with (task,did) keys vs rsa_siglip_only.py iterates tasks independently\\\"\\n    },\\n    \\\"2_temporal\\\": {\\n      \\\"method_A\\\": \\\"Split trajectory into 3 phases (early 0-33%, mid 33-67%, late 67-100%), compute RSA per phase, average\\\",\\n      \\\"method_B\\\": \\\"Full trajectory, uniformly subsample to N_SAMPLE=20 timesteps\\\",\\n      \\\"impact\\\": \\\"MODERATE (~24% of DINO gap). DINO late-phase RSA=0.26 drags average down.\\\",\\n      \\\"code_location\\\": \\\"rsa_analysis.py:TEMPORAL_BINS + get_temporal_indices() vs rsa_siglip_only.py:subsample_to_length()\\\"\\n    },\\n    \\\"3_action_distance\\\": {\\n      \\\"method_A\\\": \\\"Cosine distance on action vectors (7-dim), via build_dissimilarity_matrix()\\\",\\n      \\\"method_B\\\": \\\"Euclidean distance on action vectors, via mean_action_distance()\\\",\\n      \\\"impact\\\": \\\"MINOR (~10% of DINO gap). Cosine on small action vectors has different sensitivity than euclidean.\\\",\\n      \\\"code_location\\\": \\\"rsa_analysis.py:build_dissimilarity_matrix() uses compute_mean_cosine_distance() for both features AND actions; rsa_siglip_only.py has separate mean_action_distance() using np.linalg.norm\\\"\\n    }\\n  },\\n  \\\"fourth_difference_n_demos\\\": {\\n    \\\"description\\\": \\\"rsa_analysis.py uses --n_demos=10 (default), rsa_siglip_only.py/rsa_clip.py load ALL demos (~50/task)\\\",\\n    \\\"effect\\\": \\\"More demos -> more pairs -> slightly different RSA. DINO cls 10demos=0.641 vs 50demos=~0.692.\\\",\\n    \\\"not_root_cause\\\": \\\"This explains the residual gap between our 10-demo Method B (0.641) and previously reported 50-demo (0.692), but is NOT the main methodology issue.\\\"\\n  },\\n  \\\"critical_finding\\\": \\\"The originally reported comparison (SigLIP=0.615 vs VLA_trained=0.488 vs DINO=0.388) mixed Method A and Method B: SigLIP=0.615 was Method B (per-task, 50 demos), while VLA=0.488 and DINO=0.388 were Method A (cross-task, 10 demos, phase split). This is an apples-to-oranges comparison and must be corrected in the paper.\\\",\\n  \\\"unified_table_method_B_10demos\\\": {\\n    \\\"description\\\": \\\"All models computed with Method B (per-task + full trajectory + euclidean action), 10 demos/task\\\",\\n    \\\"results\\\": {\\n      \\\"dino_cls\\\": 0.6412,\\n      \\\"dino_patch_mean\\\": 0.5675,\\n      \\\"clip_cls\\\": 0.4818,\\n      \\\"clip_patch_mean\\\": 0.5408,\\n      \\\"siglip_projector\\\": 0.5645,\\n      \\\"vla_trained_L9\\\": 0.499,\\n      \\\"vla_untrained_L9\\\": 0.5767\\n    },\\n    \\\"ranking\\\": \\\"DINO_cls(0.641) > VLA_untrained(0.577) > DINO_pm(0.568) > SigLIP(0.565) > CLIP_pm(0.541) > VLA_trained(0.499) > CLIP_cls(0.482)\\\"\\n  },\\n  \\\"recommendation\\\": {\\n    \\\"method\\\": \\\"Method B (per-task + full trajectory + euclidean action distance)\\\",\\n    \\\"n_demos\\\": \\\"Use ALL demos (50/task) for maximum statistical power, OR use 10/task for all models consistently\\\",\\n    \\\"rationale\\\": [\\n      \\\"Per-task RSA is standard: measures feature discriminability for execution variants of SAME task\\\",\\n      \\\"Full trajectory avoids arbitrary phase boundaries\\\",\\n      \\\"Euclidean is natural for continuous 7-dim action space\\\",\\n      \\\"SigLIP was already Method B, so Method B achieves backward compatibility\\\"\\n    ],\\n    \\\"action_items\\\": [\\n      \\\"Re-run all models with unified Method B + consistent N_DEMOS\\\",\\n      \\\"Replace all RSA numbers in the paper with unified results\\\",\\n      \\\"DINO is NOT low-RSA baseline (0.641), it is actually HIGHEST RSA \\\\u2014 this changes the narrative\\\"\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 298_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01TRQHsBLGf1kyzrs7TsuRMz`</summary>

```json
{
  "name": "RSA Method Audit Report",
  "type": "report",
  "description": "Systematic audit of RSA methodology discrepancy (DINO 0.388 vs 0.692). Identifies 3 root causes and includes unified comparison table with factor isolation.",
  "project": "vla-ssd",
  "content_filename": "rsa_method_audit.json",
  "content": "See /root/autodl-tmp/vla-ssd/results/rsa/rsa_method_audit.json on westd-19183",
  "tags": [
    "rsa",
    "methodology",
    "audit",
    "blocking"
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
  "session_id": "76ab8e7d-57e0-4fff-8ef0-f0a9a442867b",
  "uuid": "2085afba-7652-4342-b35b-1ecd04a07116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDUqCZDfwbcz9BqcFrYzTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4298,
      "cache_read_input_tokens": 133532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4298
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

_source line 299 · 2026-05-16T02:52:57.761Z_

<details><summary>↩ Tool result · `toolu_01TRQHsBLGf1kyzrs7TsuRMz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_2ea075\", \"name\": \"RSA Method Audit Report\", \"type\": \"report\", \"description\": \"Systematic audit of RSA methodology discrepancy (DINO 0.388 vs 0.692). Identifies 3 root causes and includes unified comparison table with factor isolation.\", \"path\": \"projects/vla-ssd/artifacts/_project/report/rsa_method_audit.json\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:52:57.523226+00:00\", \"tags\": [\"rsa\", \"methodology\", \"audit\", \"blocking\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ab8e7d-57e0-4fff-8ef0-f0a9a442867b",
  "uuid": "24567eb6-edee-4936-9a47-5be73d33dc6d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_2ea075\\\", \\\"name\\\": \\\"RSA Method Audit Report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Systematic audit of RSA methodology discrepancy (DINO 0.388 vs 0.692). Identifies 3 root causes and includes unified comparison table with factor isolation.\\\", \\\"path\\\": \\\"projects/vla-ssd/artifacts/_project/report/rsa_method_audit.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"vla-ssd\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T02:52:57.523226+00:00\\\", \\\"tags\\\": [\\\"rsa\\\", \\\"methodology\\\", \\\"audit\\\", \\\"blocking\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_2ea075\", \"name\": \"RSA Method Audit Report\", \"type\": \"report\", \"description\": \"Systematic audit of RSA methodology discrepancy (DINO 0.388 vs 0.692). Identifies 3 root causes and includes unified comparison table with factor isolation.\", \"path\": \"projects/vla-ssd/artifacts/_project/report/rsa_method_audit.json\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:52:57.523226+00:00\", \"tags\": [\"rsa\", \"methodology\", \"audit\", \"blocking\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 300_

---

## RSA 方法论审计结果

### 1. 方法论差异（3 个脚本对比）

| 因素 | Method A (`rsa_analysis.py`) | Method B (`rsa_siglip_only.py` / `rsa_clip.py`) |
|------|-----|-----|
| **RDM 范围** | 跨任务 100×100 矩阵 | 逐任务 10×10，跨任务取平均 |
| **时间处理** | 三阶段切分 (early/mid/late) 各自计算 RSA 后取平均 | 全轨迹均匀下采样到 20 步 |
| **Action 距离** | cosine distance（`build_dissimilarity_matrix` 对 action 也用 cosine） | euclidean distance（`mean_action_distance` 用 `np.linalg.norm`） |
| **Demo 数量** | 10/task (默认) | 全部 (~50/task) |

### 2. 统一重算结果（全部用 Method B, 10 demos/task）

| Model | Method A | Method B | A-B gap |
|-------|---------|---------|---------|
| **DINO cls** | **0.388** | **0.641** | -0.253 |
| DINO patch_mean | 0.371 | 0.568 | -0.196 |
| CLIP cls | 0.457 | 0.482 | -0.025 |
| CLIP patch_mean | 0.479 | 0.541 | -0.062 |
| SigLIP projector | 0.451 | 0.565 | -0.114 |
| VLA trained L9 | **0.488** | 0.499 | -0.011 |
| VLA untrained L9 | 0.480 | 0.577 | -0.097 |

Method A 完美复现原始数字（DINO=0.3881≈0.388, VLA_trained=0.4876）。

### 3. 根因分解（以 DINO cls 为例，总 gap=0.253）

| 因素 | 贡献 | 占比 |
|------|------|-----|
| **RDM 范围**（跨任务→逐任务）| +0.167 | **66%** |
| **时间处理**（三阶段→全轨迹）| +0.064 | 24% |
| **Action 距离**（cosine→euclidean）| +0.027 | 10% |

跨任务 RDM 对 DINO 伤害最大，因为 LIBERO-Goal 所有 task 共享初始场景，DINO 的跨任务特征相似但 action 完全不同。

### 4. CRITICAL 发现

**原始论文比较（SigLIP=0.615 vs VLA=0.488 vs DINO=0.388）混用了两种方法：**
- SigLIP=0.615 是 Method B（逐任务, 50 demos）
- VLA=0.488 和 DINO=0.388 是 Method A（跨任务, 10 demos, 三阶段）

这是 apples-to-oranges 比较，**必须纠正**。

### 5. 建议

**统一使用 Method B**（逐任务 + 全轨迹 + euclidean action），所有模型用相同 N_DEMOS。

用统一方法后的 ranking：`DINO_cls(0.641) > VLA_untrained(0.577) > DINO_pm(0.568) > SigLIP(0.565) > CLIP_pm(0.541) > VLA_trained(0.499) > CLIP_cls(0.482)`

**DINO 不是 "low-RSA baseline"——它实际上是 RSA 最高的模型。** 这会改变论文叙事。

完整结果：`/root/autodl-tmp/vla-ssd/results/rsa/rsa_method_audit.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ab8e7d-57e0-4fff-8ef0-f0a9a442867b",
  "uuid": "4994330e-abb0-4e04-ab94-b112499d0bb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8EAWYpRzDGu1uPE8cjerV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 137830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 547
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


### Task result

_source line 301_

---

## RSA 方法论审计结果

### 1. 方法论差异（3 个脚本对比）

| 因素 | Method A (`rsa_analysis.py`) | Method B (`rsa_siglip_only.py` / `rsa_clip.py`) |
|------|-----|-----|
| **RDM 范围** | 跨任务 100×100 矩阵 | 逐任务 10×10，跨任务取平均 |
| **时间处理** | 三阶段切分 (early/mid/late) 各自计算 RSA 后取平均 | 全轨迹均匀下采样到 20 步 |
| **Action 距离** | cosine distance（`build_dissimilarity_matrix` 对 action 也用 cosine） | euclidean distance（`mean_action_distance` 用 `np.linalg.norm`） |
| **Demo 数量** | 10/task (默认) | 全部 (~50/task) |

### 2. 统一重算结果（全部用 Method B, 10 demos/task）

| Model | Method A | Method B | A-B gap |
|-------|---------|---------|---------|
| **DINO cls** | **0.388** | **0.641** | -0.253 |
| DINO patch_mean | 0.371 | 0.568 | -0.196 |
| CLIP cls | 0.457 | 0.482 | -0.025 |
| CLIP patch_mean | 0.479 | 0.541 | -0.062 |
| SigLIP projector | 0.451 | 0.565 | -0.114 |
| VLA trained L9 | **0.488** | 0.499 | -0.011 |
| VLA untrained L9 | 0.480 | 0.577 | -0.097 |

Method A 完美复现原始数字（DINO=0.3881≈0.388, VLA_trained=0.4876）。

### 3. 根因分解（以 DINO cls 为例，总 gap=0.253）

| 因素 | 贡献 | 占比 |
|------|------|-----|
| **RDM 范围**（跨任务→逐任务）| +0.167 | **66%** |
| **时间处理**（三阶段→全轨迹）| +0.064 | 24% |
| **Action 距离**（cosine→euclidean）| +0.027 | 10% |

跨任务 RDM 对 DINO 伤害最大，因为 LIBERO-Goal 所有 task 共享初始场景，DINO 的跨任务特征相似但 action 完全不同。

### 4. CRITICAL 发现

**原始论文比较（SigLIP=0.615 vs VLA=0.488 vs DINO=0.388）混用了两种方法：**
- SigLIP=0.615 是 Method B（逐任务, 50 demos）
- VLA=0.488 和 DINO=0.388 是 Method A（跨任务, 10 demos, 三阶段）

这是 apples-to-oranges 比较，**必须纠正**。

### 5. 建议

**统一使用 Method B**（逐任务 + 全轨迹 + euclidean action），所有模型用相同 N_DEMOS。

用统一方法后的 ranking：`DINO_cls(0.641) > VLA_untrained(0.577) > DINO_pm(0.568) > SigLIP(0.565) > CLIP_pm(0.541) > VLA_trained(0.499) > CLIP_cls(0.482)`

**DINO 不是 "low-RSA baseline"——它实际上是 RSA 最高的模型。** 这会改变论文叙事。

完整结果：`/root/autodl-tmp/vla-ssd/results/rsa/rsa_method_audit.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1006313,
  "duration_api_ms": 877687,
  "num_turns": 120,
  "stop_reason": "end_turn",
  "session_id": "76ab8e7d-57e0-4fff-8ef0-f0a9a442867b",
  "total_cost_usd": 6.599776500000001,
  "usage": {
    "input_tokens": 103,
    "cache_creation_input_tokens": 126536,
    "cache_read_input_tokens": 9217113,
    "output_tokens": 47893,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 126536,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1123,
        "cache_read_input_tokens": 137830,
        "cache_creation_input_tokens": 547,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 547
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2445,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00253,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 103,
      "outputTokens": 47893,
      "cacheReadInputTokens": 9217113,
      "cacheCreationInputTokens": 126536,
      "webSearchRequests": 0,
      "costUSD": 6.597246500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0250b774-8415-4d3b-8d3e-678d18377fb3"
}
```

</details>

---
