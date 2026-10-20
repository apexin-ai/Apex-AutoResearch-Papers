# analysis anova prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_anova_prep_20260526T060836_result.json`
- **Structured JSON:** [`0d4e89e305ad5a718ac9.json`](../../sessions/0d/0d4e89e305ad5a718ac9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，mock 数据测试通过。

**路径**: `artifacts/anova_2x2_factorial.py`

**用法**:
```bash
# JSON 字符串
python anova_2x2_factorial.py --json '{"full_occ_bn": [...], "full_occ_ln": [...], "detach_bn": [...], "detach_ln": [...]}'

# JSON 文件
python anova_2x2_factorial.py --input data.json --output results.json
```

**输出内容**: descriptive stats、Type II ANOVA (gradient_flow / norm_type / interaction)、partial η²、Tukey HSD post-hoc、decision helper (Plan A/B 建议)，同时写 JSON 到 `--output`。n<5 时自动打印 underpowered warning。

---
