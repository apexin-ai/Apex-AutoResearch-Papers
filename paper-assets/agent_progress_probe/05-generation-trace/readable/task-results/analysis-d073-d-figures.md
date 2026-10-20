# analysis d073 d figures

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-d-figures_20260516T024507_result.json`
- **Structured JSON:** [`4060a71e82fcb75803bf.json`](../../sessions/40/4060a71e82fcb75803bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Files are on the remote server (register_artifact expects local paths). All three figures generated successfully:

**B3: Pareto Curve** — `artifacts/d072/pareto_curve.pdf` (20 KB)
- Compute Saved (%) vs Task Success Preserved (%) for 4 models (3-LF GB, 2-LF RF, Oracle, Random) across k=1,2,3,5,7,10
- Error bars from 3-seed simulation
- k-value annotations on each point

**D1: SHAP Feature Importance** — `artifacts/d073/shap_feature_importance.pdf` (230 KB)
- Beeswarm plot of top 20 features from GB classifier (200 trees, lr=0.05, depth=5)
- Trained on 15,401 SWE conf≥2 windows (5,846 stag / 9,555 prog)
- Feature names colored: **blue bold** = LF-overlap (11), **red** = structural (19)
- Dot color = feature value (RdBu colormap, low→high)
- Colorbar + group legend

**D2: Trajectory Visualization** — `artifacts/d073/trajectory_visualization.pdf` (26 KB)
- Selected trajectory: `keras-team__keras-nlp-131__swe-agent-llama-70b__r161` (57 steps, 13 windows)
- Upper panel: 3-row binary LF activation heatmap (Cmd Repetition, File Diff Delta, Outcome BP)
- Lower panel: GB P(progress) curve with decision boundary at 0.5
- Annotated: stagnation onset (green), model detection (orange), early termination k=3 (red)

---
