# deploy westd38929 gpu0 xvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929-gpu0-xvla_20260524T032825_result.json`
- **Structured JSON:** [`3e0e5a569e6e9919a7da.json`](../../sessions/3e/3e0e5a569e6e9919a7da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署并注册。

**总结**:
- **已部署**: `eval_xvla_random_k085_long_seed42` on westd-38929 GPU 0, PID=316561
- **实验**: X-VLA Random k=0.85 Long (libero_10), seed=42, 50 tokens → keep 42
- **原因**: Table 2 主数据(k=0.5/0.7/0.9/0.95)的 X-VLA 部分在 registry 中已全部有数据（tex 文件未更新）。用户建议的两个优先实验也已有数据。部署了 k=0.85 Random Long — 这是 k=0.85 跨 suite Random 数据的最后缺口（Object=65.0%, Spatial=68.2%, Goal=60.4%, Long=?），补全 D196 RoPE disruption hypothesis 分析。
- **westd-38929 GPU 分布**: GPU 0=本实验, GPU 1=L2norm k=0.5 Spatial v2, GPU 2=L2norm k=0.3 Goal v3, GPU 3=L2norm k=0.7 Goal v2
- **预计时长**: ~90 min（Long suite 通常较慢）

---
