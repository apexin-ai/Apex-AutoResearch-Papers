# code d066 seed variance prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d066_seed_variance_prep_20260519T151226_result.json`
- **Structured JSON:** [`230cb0afb49a86bc8147.json`](../../sessions/23/230cb0afb49a86bc8147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成：**
1. **脚本编写并部署到两台服务器**（westd-16980, westd-21461）：
   - `scripts/d067_seed_variance.sh` — 单配置单 seed 推理（unconstrained + full_s1 + violation check）
   - `scripts/d067_run_all.sh` — 批量运行，2 GPU 并行 nohup

2. **验证通过**：语法检查、参数校验、checkpoint/数据路径确认

3. **Seed 机制**：`run_constrained_extraction.py` 已支持 `--seed`，greedy decoding 下理论确定性，LoRA 模型是否有差异正是实验目标

4. **报告**：`artifacts/_project/report/d067_seed_variance_prep.md`

**启动方式**（GPU 释放后）：
```bash
# 在任一服务器上
bash scripts/d067_run_all.sh
# 或单独跑
bash scripts/d067_seed_variance.sh 0 qwen_scierc 123
```

预估单服务器全量运行 ~4.5 小时（2 GPU 并行）。

---
