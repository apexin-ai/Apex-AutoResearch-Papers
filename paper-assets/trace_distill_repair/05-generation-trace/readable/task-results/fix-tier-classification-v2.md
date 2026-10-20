# fix tier classification v2

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tier_classification_v2_20260515T123220_result.json`
- **Structured JSON:** [`0ce15a082053080b3a84.json`](../../sessions/0c/0ce15a082053080b3a84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重新生成结果与直接修复一致。汇总：

| Tier | 数量 | 实例 |
|------|------|------|
| **1** | **15** | black_1, cookiecutter_1/2/3, fastapi_2, **httpie_2**, luigi_5, sanic_2, scrapy_2/7, tornado_2, youtube-dl_1/2/5/20 |
| **2** | **1** | **fastapi_1** (5 files, multi-file patch) |
| **3** | **17** | httpie_1, luigi_1/2/10/14, sanic_1, scrapy_1/3/4, thefuck_1/2/4, tornado_1/4/5/7, youtube-dl_10 |

确认项：
- httpie_2 在 Tier 1（D022 override）
- fastapi_1 在 Tier 2（5 文件，LLM 定位困难）
- 除 httpie_2 外所有 Tier 1 实例均为 n_changed_files=1，无其他多文件实例误归 Tier 1
- `generate_tiers.py` 已修复分类逻辑，重新运行产出一致

---
