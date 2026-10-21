# ops cqa1 xvla seed43 oft cv

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-xvla-seed43-oft-cv_20260520T112951_result.json`
- **Structured JSON:** [`193fe4e68c2e99b6f7da.json`](../../sessions/19/193fe4e68c2e99b6f7da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three tasks are running on cqa1:

| GPU | Task | PID | Status |
|-----|------|-----|--------|
| 1 (4.5GB) | X-VLA k=0.9, seed=43, 50eps/task | 866917 | Running — task 0, ep 14/50, all SUCCESS so far |
| 2 (4.1GB) | X-VLA k=0.7, seed=43, 50eps/task | 868188 | Running — task 0, ep 7/50, all SUCCESS so far |
| 3 (14.8GB) | OFT 7B CV computation | 869442 | Running — model loaded, loading LIBERO frames |

**Issues encountered and fixed:**
- X-VLA model downloaded from HuggingFace (3.5GB, `2toINF/X-VLA-Libero`)
- Converted relative imports to absolute in X-VLA model files
- Installed missing deps: `timm<1.0`, `fastapi`, `uvicorn`, `json_numpy`
- OFT CV script: bypassed action mask processing by running vision backbone + projector + LLM manually; fixed fp16 dtype mismatch

**Estimates:**
- X-VLA evals: ~6-7 sec/episode × 500 episodes (10 tasks × 50 eps) = ~1 hour each
- OFT CV: 260 frames forward pass through 7B model = ~20-30 min

---
