# S3 Backup Report (2026-05-25)

## Tarball
- **Path on server**: `/root/autodl-tmp/irt_personfit_contam-final-20260525T205541Z.tar.gz`
- **Size**: 13,973,282,863 bytes (13.01 GB compressed, from 20 GB source)
- **Compression ratio**: 65% (tar.gz)

## S3 Upload
- **S3 URI**: `s3://agent-ml-manager-backups-emnlp/manager-backup/backends/irt_personfit_contam/project-archive/irt_personfit_contam-final-20260525T205541Z.tar.gz`
- **Upload time**: 873.8s
- **Upload speed**: 15.3 MB/s
- **Method**: Direct upload from westd-35694 via boto3 (bypassed BE local SCP)

## Archive Contents
| Component | Size |
|-----------|------|
| code | 111M |
| checkpoints | 20G |
| data | 111M |
| results | 40M |
| paper | 712K |
| **Total (uncompressed)** | **~20G** |

## Notes
- Tarball written to data disk `/root/autodl-tmp/` (root partition had insufficient space)
- Uploaded directly from GPU server to S3 ap-northeast-1 (BE has no SSH access to GPU server for SCP)
