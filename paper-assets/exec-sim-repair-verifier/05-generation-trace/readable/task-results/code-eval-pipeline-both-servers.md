# code eval pipeline both servers

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-both-servers_20260512T210238_result.json`
- **Structured JSON:** [`cef4fe48662b698a6699.json`](../../sessions/ce/cef4fe48662b698a6699.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。两台服务器的 pipeline 状态：

**Home (home-1x5090)**:
- `run_repo_eval.sh` — 调用 `eval_repo_level.py --mode cls|cwm`
- `paired_bootstrap_repo.py` — 原有脚本，无需修改
- 全部语法检查通过

**Seetacloud (seetacloud-westd-4x5090)**:
- `run_repo_eval.sh` — CLS 调用 `eval_repo_verifier.py`，CWM 调用 `eval_repo_cwm.py`
- `eval_repo_verifier.py` — 已修改：`"prediction"` → `"pred"`，输出格式 JSON → JSONL
- `eval_repo_cwm.py` — 已添加 `--save_predictions` + `per_sample` 追踪 + JSONL 输出
- `paired_bootstrap_repo.py` — 从 Home 部署
- 全部语法检查通过

**用法**:
```bash
# 先跑 CLS
./run_repo_eval.sh --mode cls --checkpoint_dir &lt;cls_ckpt_path> --device cuda:0

# 再跑 CWM（自动触发 paired bootstrap）
./run_repo_eval.sh --mode cwm --checkpoint_dir &lt;cwm_ckpt_path> --device cuda:0
```

---
