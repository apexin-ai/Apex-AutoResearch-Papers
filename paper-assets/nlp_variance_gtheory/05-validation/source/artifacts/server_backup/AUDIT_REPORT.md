# Server Audit & Backup Report
Date: 2026-05-23

---

## Part 1: westd-32570 Audit

### GPU Status
| GPU | Utilization | VRAM Used | VRAM Total |
|-----|-------------|-----------|------------|
| 0   | 0%          | 0 MiB     | 97887 MiB  |
| 1   | 0%          | 0 MiB     | 97887 MiB  |
| 2   | 0%          | 0 MiB     | 97887 MiB  |
| 3   | 0%          | 0 MiB     | 97887 MiB  |

### Running Processes
- **No Python/training processes running**
- System services only: supervisord, jupyter-lab, tensorboard, proxy, sshd
- One idle HTTP server on port 18999

### Disk Usage
| Directory | Size |
|-----------|------|
| data/     | 36 MB  |
| results/  | 3.8 GB |
| artifacts/| 8 KB   |
| figures/  | 292 KB |
| **Total** | **~3.9 GB** |

### Results Breakdown
| Subdirectory | Size | Contents |
|--------------|------|----------|
| analysis/ | 746 MB | G-study JSONs + large CSV/JSONL intermediate files |
| exp001_llama/ | 149 MB | 4 JSONL shards (59800 lines each) + fp32 backfill |
| exp001_gemma/ | 45 MB | 4 shards (~21K lines each) |
| exp001_gemma_fp32/ | 42 MB | 4 shards (21600 lines each) |
| exp001_mistral/ | 134 MB | 4 shards (64800 lines each) |
| exp001_qwen/ | 233 MB | 4 shards + resume/patch files |
| exp001b/ | 305 MB | 3 sample sets, 4 shards each |
| exp002/ | 1.9 GB | 8 models x 5 benchmarks (57600 lines each) |
| exp002_pilot/ | 8.8 MB | Pilot runs |
| exp003_scale_*.jsonl | ~105 MB | 3b/7b/72b scale study (57600 lines each) |
| exp004_8model_analysis/ | 852 KB | Analysis JSONs + figures |
| exp004_ff_residual/ | 1.1 MB | Regression + item features |
| partial_credit_multimodel/ | 188 MB | GSM8K partial credit (460800 lines) |

---

## Part 2: westd-15695 Audit

### GPU Status
| GPU | Utilization | VRAM Used | VRAM Total |
|-----|-------------|-----------|------------|
| 0   | 100%*       | 0 MiB     | 97887 MiB  |

*GPU shows 100% utilization but 0 MiB memory used - likely monitoring artifact, no training running.

### Running Processes
- **No Python/training processes running**
- System services only (same as westd-32570)

### Unique Data (not on westd-32570)
| File | Size | Lines | MD5 |
|------|------|-------|-----|
| exp001_yi/yi_mmlu.jsonl | 50 MB | 86400 | eb615a348e299c8480ea08f5ab573871 |
| exp001_yi/yi_arc.jsonl | 49 MB | 86400 | c2584a1917bdf9d998506255125f3064 |
| exp001_yi/yi_gsm8k.jsonl | 110 MB | 86400 | fa49c746d329e2feeac6d56593a68043 |
| exp001_olmo/olmo_mmlu.jsonl | 48 MB | 86400 | b6c1e387f613a6a7cc6874db7b40d146 |
| exp001_olmo/olmo_arc.jsonl | 49 MB | 86400 | 86652d2b66eb1cd745ff6bf91066d6e0 |
| exp001_olmo/olmo_gsm8k.jsonl | 88 MB | 86400 | b9706a050583987fff57304f8385e3bc |

---

## Part 3: westd-13176 / westd-19912

- **westd-19912**: Not in server list (may have been decommissioned)
- **westd-13176**: Connection failed (port 13176 unreachable - instance may be stopped or port changed)

---

## Part 4: Backup Status

### Tar Archives on Servers (ready for scp)

| Server | Path | Size | MD5 |
|--------|------|------|-----|
| westd-32570 | /tmp/nlp_vg_full_backup.tar.gz | 476 MB | 48f92bfe44a3b56c48c908eb0c8100ab |
| westd-15695 | /tmp/nlp_vg_15695_backup.tar.gz | 67 MB | 4a9bda6ff73553cbbc6269be75a9d61f |

### SCP Commands
```bash
scp connect.westd.seetacloud.com:/tmp/nlp_vg_full_backup.tar.gz ./
scp westd-15695:/tmp/nlp_vg_15695_backup.tar.gz ./
```

### Analysis JSONs Backed Up Locally
Location: `artifacts/server_backup/westd-32570/`
- data_json/exp_llama70b/llama70b_mmlu_gstudy.json
- (Additional files being backed up by background agent)

---

## Part 5: Key File MD5 Checksums

### data/ (westd-32570)
| File | MD5 |
|------|-----|
| exp_llama70b/llama70b_mmlu.jsonl (57600 lines, 35MB) | cfedd6898d278ba6a957b8302bd51c7c |
| exp_llama70b/llama70b_mmlu_gstudy.json | fb73b882b75508aa5a26c4c87918e291 |
| exp_llama70b/design_llama70b_mmlu.csv | 998aef0802c5f4c6bdeb806eae4f835b |
| exp_llama70b/design_llama70b_gsm8k.csv | ff714214c66cd583018cb5566ac52d78 |

### results/ JSONL files (westd-32570) - Raw Inference Data
| File | Lines | MD5 |
|------|-------|-----|
| all_results.jsonl | 5400 | da759561e0d2b665ad2d70bb40186de2 |
| float32_results.jsonl | 1800 | 8ec36abee7ea5162ac8d8a8f272e0774 |
| bf16_eager_results.jsonl | 1800 | bb922b631591e56dfb27a1e2200f9f63 |
| exp001_llama/llama_shard_0.jsonl | 59800 | a6ca4ca6b9ace48373f0526dcb095f36 |
| exp001_llama/llama_shard_1.jsonl | 59800 | bcaae2747b8a29df10ff4299f84fe28c |
| exp001_llama/llama_shard_2.jsonl | 59800 | 8fb22bd85a762cd588eff84b893cdedd |
| exp001_llama/llama_shard_3.jsonl | 59800 | 5723334bb06cf1ef0b47ba170dd5e66b |
| exp001_llama/llama_fp32_t0_backfill.jsonl | 20000 | afbdb5cbb0c242025d8970b3faeaf86b |
| exp001_gemma/shard_0.jsonl | 23200 | 12bc3a0a3bde1ee793c8aa32d065e3d3 |
| exp001_gemma/shard_1.jsonl | 20400 | 89aa1f5313c5d746720913e51a0cc578 |
| exp001_gemma/shard_2.jsonl | 21400 | 74579361051ac8047a9021304ee32aec |
| exp001_gemma/shard_3.jsonl | 21400 | ffa155f769c1a8b5e34af661ed06cbea |
| exp001_mistral/shard_{0-3}.jsonl | 64800 each | (see full list above) |
| exp001_gemma_fp32/shard_{0-3}.jsonl | 21600 each | (see full list above) |
| exp001_qwen/shard_{0-3}.jsonl | 64800 each | (see full list above) |
| exp001b/sample{1-3}/all_results.jsonl | 86400 each | (3 sample sets) |
| exp002/{model}_{benchmark}.jsonl | 57600 each | 8 models x 5 benchmarks = 40 files |
| exp003_scale_7b_mmlu.jsonl | 57600 | 5e220653dfd84e0539e6e8f352b46582 |
| exp003_scale_3b_mmlu.jsonl | 57600 | 756839c2ca15000868ce3d0f0fc9bafb |
| exp003_scale_72b_mmlu.jsonl | 57600 | 0d0d6da83f7bf47807553a01f6fd6452 |
| partial_credit_multimodel/gsm8k_8model_partial_scored.jsonl | 460800 | f8fc018d9003e132f5ae7c74ab643741 |

### results/ Analysis JSONs (westd-32570) - Key Results
| File | MD5 |
|------|-----|
| variance_components.json | 7706804c70ec938e2b00889ef0e35b90 |
| d_study_results.json | fb6bbc4db8bad6b69d9af1c157bc375a |
| variance_components_text.json | 0bf1316bb54d4f59b15f187d6911372e |
| d_study_results_text.json | f04805570664817d091da5e031158b86 |
| exp001_bf16_2temp_comparison.json | 8287f5c898d04773e9b04b6c07397269 |
| exp003_scale_gstudy.json | d3172fdca597b966aadaf4e2bae8a746 |
| exp003_72b_single_gstudy.json | 39c78b1edc0beb20238231417006f054 |
| exp003_scale_crossed_3model.json | 1ed30538a965f8c837c3132b91540420 |
| exp003_scale_crossed_gstudy_test.json | 889500ed01f567f7da1eb4367b4eba0f |
| partial_credit_multimodel_gstudy.json | f704ad037f182ad4807386dfebef7595 |

### results/analysis/ (30+ JSON files)
(Full MD5 list in separate md5_manifest.txt)

### results/exp004_8model_analysis/ (20+ JSON files)
(Full MD5 list in separate md5_manifest.txt)

---

## Part 6: Classification Recommendation

| Server | Classification | Reason |
|--------|---------------|--------|
| **westd-32570** | **B → C** | No running processes, all GPUs idle. Tar backup (476MB) created at `/tmp/nlp_vg_full_backup.tar.gz`. After user pulls tar via scp and verifies MD5, can be released. |
| **westd-15695** | **B → C** | No running processes, GPU idle. Contains unique Yi/OLMo exp001 data not on westd-32570. Tar backup (67MB) at `/tmp/nlp_vg_15695_backup.tar.gz`. After scp + MD5 verify, can be released. |
| **westd-13176** | **B** | Connection failed. Cannot assess. User should check AutoDL console for status/port change. |

### Action Items
1. **Pull tar backups via scp** (critical before release):
   ```bash
   scp connect.westd.seetacloud.com:/tmp/nlp_vg_full_backup.tar.gz /path/to/local/backup/
   scp westd-15695:/tmp/nlp_vg_15695_backup.tar.gz /path/to/local/backup/
   ```
2. **Verify MD5** after download:
   - westd-32570 tar: `48f92bfe44a3b56c48c908eb0c8100ab`
   - westd-15695 tar: `4a9bda6ff73553cbbc6269be75a9d61f`
3. **Check westd-13176** status in AutoDL console
4. After verification, both westd-32570 and westd-15695 can be released
