# ops eval server prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-server-prep_20260521T191017_result.json`
- **Structured JSON:** [`409871d7690a02ae90be.json`](../../sessions/40/409871d7690a02ae90be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 就绪状态汇报

### 关键发现：无需 git pull
两台服务器 `src/evaluate.py` / `pi05_wrapper.py` / `crm.py` 的 **md5 完全一致**，代码状态相同。任务前提（bjb2 旧于 bjb1）不成立。
- bjb1-32546：`/root/acr-vla-conformal-refinement` 不是 git 仓库（无 .git），项目以 rsync 同步而非 git
- bjb2-28827：是本地 git repo 但**未配置 origin remote**，git pull 也不可行（且有大量未提交本地改动 + 未跟踪文件）

### bjb1-32546 ✅ 完全就绪
- torch=2.10.0+cu128，CUDA OK，6× RTX 4090（24GB）
- pi05 模型完整（model.safetensors 7.47GB，全部配置文件齐全）
- evaluate.py 存在（33058 bytes，2026-05-21 23:49 更新）
- **GPU 全部空闲**（6/6 显存 1 MiB，利用率 0%）

### bjb2-28827 ⚠️ 部分占用
- torch=2.10.0+cu128，CUDA OK，6× RTX 4090（24GB）
- pi05 模型完整（注意：`policy_preprocessor.json` 1937 bytes，比 bjb1 多 34 字节，时间戳 14:31——可能是某次调试改动，但 md5 未对比，若 eval 报 normalizer 异常需排查）
- evaluate.py 存在（与 bjb1 完全相同）
- **GPU 0/1/3/5 被占用**（各 9.8GB，20-43% 利用率，疑似 CRM training）；GPU 2/4 空闲

### 部署建议
- bjb1-32546 可立即跑 3 个 seed（GPU 0/1/2）
- bjb2-28827 需等 CRM training 完成腾出 GPU 0/1/3/5，或仅用空闲的 GPU 2/4 跑 2 个 seed
- 若 bjb2 的 `policy_preprocessor.json` 差异引发问题，从 bjb1 同步过去即可

---
