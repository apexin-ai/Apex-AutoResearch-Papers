# S3 Backup Report — irt_personfit_contam

**Date:** 2026-05-26 05:50 UTC

## Tarball

- **File:** `irt_personfit_contam-final-20260525T205541Z.tar.gz`
- **Size:** 13,973,282,863 bytes (13.0 GB compressed)
- **Location on server:** `/root/autodl-tmp/irt_personfit_contam-final-20260525T205541Z.tar.gz`

## S3 Upload

- **S3 URI:** `s3://agent-ml-manager-backups-emnlp/manager-backup/backends/irt_personfit_contam/project-archive/irt_personfit_contam-final-20260525T205541Z.tar.gz`
- **Upload time:** 787.6s
- **Upload rate:** 16.9 MB/s
- **Method:** Direct server-to-S3 via boto3 multipart upload (bypassed BE due to insufficient local disk)

## Backup Contents

| Component | Size |
|-----------|------|
| Code | 111M |
| Checkpoints | 20G |
| Data | 111M |
| Results | 40M |
| Paper | 712K |

## Notes

- Original tar to `/tmp` failed due to root partition full (30G, 100% used). Used pre-existing tarball from `/root/autodl-tmp/` (created 2026-05-25T20:55:41Z).
- Upload executed directly from server to S3 (server -> AWS ap-northeast-1) since BE local disk was too small to stage the 13G file.
- Temporary SSH key and upload scripts cleaned up after completion.
