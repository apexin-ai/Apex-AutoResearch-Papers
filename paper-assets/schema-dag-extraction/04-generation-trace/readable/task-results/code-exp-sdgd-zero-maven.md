# code exp sdgd zero maven

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_sdgd_zero_maven_20260519T114328_result.json`
- **Structured JSON:** [`cac6795411422f19b5f5.json`](../../sessions/ca/cac6795411422f19b5f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已清理，无残留进程。

实验准备完成。总结：

**已完成：**
1. 读取了 SDGD 全模块（decompose, graph, merge, evaluate, similarity）和 run_sdgd_experiment.py
2. 验证了 MAVEN 数据（8042 samples, 168 types, parquet 格式）和 SCS matrix（168x168 .pt）
3. 创建了 `/root/schema-dag-extraction/src/run_sdgd_maven.py`：
   - 单次加载 vLLM，复用跑三臂
   - single_pass (168 types) → sdgd_zero (18 batches) → random_batch (3 seeds × 18 batches)
   - 包含 merge 统计（raw vs merged predictions, expansion ratio）
   - 输出 summary.json + per-mode results/predictions
4. 创建了 `launch_sdgd_maven.sh` 启动脚本
5. Dry-run 通过：5 samples, F1=0.200, pipeline 端到端正常
6. 更新了 registry（hypothesis + notes）

**MAVEN 分解特征：**
- tau=0.3191（Few-NERD 为 0.8676，低很多因为 SCS 分布不同）
- 18 batches（Few-NERD 8 batches），sizes=[39,20,16,12,12,10,10,8,8,6,6,6,5,4,2,2,1,1]
- 更多 batches 意味着 merge amplification 效应可能更强

**待执行：**
- 等 exp_docred_bcs_expanded 完成后，运行 `bash /root/schema-dag-extraction/src/launch_sdgd_maven.sh`
- 预计 3-4 GPU 小时

---
