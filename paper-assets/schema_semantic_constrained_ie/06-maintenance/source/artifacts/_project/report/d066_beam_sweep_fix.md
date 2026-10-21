# d066 Beam Sweep Script Modification Report

## 验证：westd-21461 SciERC 脚本
- 脚本 `d066_beam_sweep_scierc.sh` 已验证正确，无需修改
- 全量 SciERC 100 docs, beam k=1,2,4,8, unconstrained + full_s1
- 双卡并行：GPU0=Llama, GPU1=Qwen

## 修改：westd-16980 DocRED 脚本

### 变更内容
1. **BEAMS**: `(1 2 4 8)` → `(2 8)` — k=1/4 复用 d064 全量数据
2. **--max_docs 200**: 利用已有的 `--max_docs` 参数截取前 200 docs（无需生成子集文件）
3. **输出路径**: `{model}_docred_beam{k}_{mode}` → `{model}_docred_200_beam{k}_{mode}`
4. **完成检查阈值**: `n_lines >= 998` → `n_lines >= 200`
5. **注释**: 更新为反映 200-doc subset 和 k=2,8

### 输出文件列表
```
d066_beam_sweep/llama_docred_200_beam2_unconstrained.jsonl
d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl
d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl
d066_beam_sweep/llama_docred_200_beam8_full_s1.jsonl
d066_beam_sweep/qwen_docred_200_beam2_unconstrained.jsonl
d066_beam_sweep/qwen_docred_200_beam2_full_s1.jsonl
d066_beam_sweep/qwen_docred_200_beam8_unconstrained.jsonl
d066_beam_sweep/qwen_docred_200_beam8_full_s1.jsonl
```

### 预估运行时间
- 原方案：2 models × 4 beams × 2 modes × 998 docs = 约 32 小时/GPU
- 新方案：2 models × 2 beams × 2 modes × 200 docs = 约 3-4 小时/GPU（双卡并行，wall time ~3-4h）
- 缩减约 90%

### 启动命令
```bash
# 在 westd-16980 上（GPU 空闲后）
cd /root/schema_semantic_constrained_ie
nohup bash scripts/d066_beam_sweep_docred.sh > /root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_docred_main.log 2>&1 &
```

## 语法验证
`bash -n` 通过，无语法错误。
