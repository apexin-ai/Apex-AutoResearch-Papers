# prep d112 rsft no evidence eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_d112_rsft_no_evidence_eval_r3_20260519T154416_result.json`
- **Structured JSON:** [`e63085a28299e19e6b87.json`](../../sessions/e6/e63085a28299e19e6b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Ready to submit.** 全部验证通过：

- 脚本存在：`scripts/seed_expansion/eval_4b_rsft_no_evidence.sh`
- 4 个依赖路径（RSFT adapter、SFT adapter、base model、data）全部存在
- `--no_evidence` 参数已设置（C005）
- cuda:1 显存 0 MiB，完全空闲（C001）
- 磁盘 65G 可用

提交命令：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/freige/scripts/seed_expansion/eval_4b_rsft_no_evidence.sh
```

报告已写入 `artifacts/d112_rsft_no_evidence_eval_r3_prep.md`。

---
