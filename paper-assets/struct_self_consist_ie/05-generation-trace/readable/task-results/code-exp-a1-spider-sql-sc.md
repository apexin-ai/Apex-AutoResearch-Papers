# code exp a1 spider sql sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_a1_spider_sql_sc_20260520T181611_result.json`
- **Structured JSON:** [`88531c6f67701e93b219.json`](../../sessions/88/88531c6f67701e93b219.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出报告：

---

**Spider SQL SC Pilot 实验准备状态**

| 项 | 状态 |
|---|---|
| 脚本 | `run_spider_sc.py` (470行) 已部署到 autodl-5090-b |
| 合成数据库生成器 | `generate_spider_dbs.py` — 已执行，166 个数据库就绪 |
| 模型 | Qwen2.5-7B-Instruct — 已在 HF 缓存 |
| GPU | cuda:2 — 32GB 空闲 |
| vLLM | 0.18.1 — import 测试通过 |
| Spider 数据 | `xlangai/spider` HF 数据集 — validation 1034 例 → 随机抽 200 |
| 数据库文件 | **合成数据库**（原版 Google Drive 被 AutoDL Squid 代理阻断） |
| Registry | `exp_spider_sc_pilot` — PENDING |

**运行命令：**
```
source /root/autodl-tmp/struct_self_consist_ie/env.sh && CUDA_VISIBLE_DEVICES=2 python3 /root/autodl-tmp/struct_self_consist_ie/code/run_spider_sc.py
```

**数据库说明：** Spider 原版数据库仅通过 Google Drive 分发，AutoDL 代理完全阻断 Google 域名。已用 `tables.json` 的 schema 信息生成 166 个合成 SQLite 数据库（每表 15 行），gold query 执行测试 78% 返回非空结果。对 SC 诊断性指标（degeneracy rate、agreement pattern、LP gap）有效；绝对 execution accuracy 为近似值。如需精确数值，后续可从 VPN 环境下载原版数据库替换。

**预计时长：** ~15-20 分钟（200 examples × 9 次推理 on 5090）

---
