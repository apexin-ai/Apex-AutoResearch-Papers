# infra install vllm and sanity

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_install_vllm_and_sanity_20260520T180418_result.json`
- **Structured JSON:** [`7b11bdedb0cc78f59192.json`](../../sessions/7b/7b11bdedb0cc78f59192.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总产出：

---

### 产出汇总

**1. vLLM 版本 + import 验证**
- vLLM **0.9.2** OK（兼容 torch 2.7.0+cu128）
- 需 patch ovis.py 解决 transformers 4.57.6 的 `aimv2` 注册冲突

**2. 模型路径确认**
- `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`（15 GB safetensors，via ModelScope）

**3. sanity_check.json summary**
```json
{
  "greedy_deterministic": false,
  "phase1_seed_control": true,
  "phase2_sampling_diversity": 9.2,
  "sanity_check_pass": false
}
```

- **greedy_deterministic: false** — greedy (T=0) 在 5 items 中有 3 个出现了 2 种不同输出（首次推理与后续不同，答案字母一致但生成的后续文本不同）
- **phase1_seed_control: true** — 同 seed + T=0.5 的 10 次重复完全一致
- **phase2_sampling_diversity: 9.2** — 不同 seed 平均产生 9.2 种不同输出（10 seeds），多样性充分
- **sanity_check_pass: false** — 因 greedy 不完全确定而 FAIL

**4. 根分区剩余空间**: 3.1 GB

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "greedy_deterministic": false,
    "phase1_seed_control": true,
    "phase2_sampling_diversity": 9.2,
    "sanity_check_pass": false
  }
}
```

</details>

---
