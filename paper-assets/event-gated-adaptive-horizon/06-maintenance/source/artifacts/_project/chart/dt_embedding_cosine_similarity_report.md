Worker C: dt_embedding cosine similarity analysis

Cosine Similarity (dt=1 vs dt=2):
- Trained Walker: -0.655 to -0.903
- Trained Cheetah: -0.684 to -0.803
- Frozen Walker: -0.150 to 0.203
- Frozen Cheetah: 0.069
- Untrained (008a): 0.024

Training dynamics: cosine drops to -0.9 in first 25K steps, then slowly recovers to -0.65~-0.85.

Charts: artifacts/dt_embedding_cosine_similarity.png (local), /root/autodl-tmp/event-gated-adaptive-horizon/artifacts/dt_embedding_cosine_similarity.pdf (server)