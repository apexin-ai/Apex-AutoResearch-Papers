# LeRobot Official Eval: SmolVLA on LIBERO-Object

## Summary
- **Model**: /root/autodl-tmp/models/smolvla_libero (pepijn223/smolvla_libero)
- **Eval**: lerobot v0.5.2, 200 episodes (10 tasks × 20 episodes each)
- **Overall success rate**: 66.5%
- **Total eval time**: 1540s (~25.7 min)

## Per-Task Success Rates
| Task ID | Success Rate |
|---------|-------------|
| 0 | 60% |
| 1 | 75% |
| 2 | 45% |
| 3 | 70% |
| 4 | 60% |
| 5 | 45% |
| 6 | 85% |
| 7 | 70% |
| 8 | 70% |
| 9 | 85% |

## Comparison
| Method | Success Rate |
|--------|-------------|
| Paper reported | 96% |
| lerobot official eval (this run) | 66.5% |
| Our wrapper (evaluate.py) | 10.8% |

## Key Observations
1. Our wrapper has severe implementation bugs (10.8% vs 66.5%)
2. This model (pepijn223/smolvla_libero, trained on libero_spatial) achieves 66.5%, far below 96%
3. The 96% claim may refer to a different checkpoint (HuggingFaceVLA/smolvla_libero on HF Hub) or different eval protocol

## Eval Command
```bash
python -m lerobot.scripts.lerobot_eval \
    --policy.path=/root/autodl-tmp/models/smolvla_libero \
    --env.type=libero \
    --env.task=libero_object \
    --eval.n_episodes=20 \
    --eval.batch_size=1 \
    --policy.device=cuda \
    --policy.empty_cameras=1 \
    --rename_map='{"observation.images.image": "observation.images.camera1", "observation.images.image2": "observation.images.camera2"}'
```

## Notes
- Required --rename_map to map LIBERO camera names (image, image2) to policy expected names (camera1, camera2)
- Required --policy.empty_cameras=1 because policy expects 3 cameras but LIBERO only has 2
- Model config shows observation.state shape [6], not [8] as previously assumed
- Model has chunk_size=50, n_action_steps=50 (open-loop 50-step action replay)
