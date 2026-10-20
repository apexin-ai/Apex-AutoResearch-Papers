#!/bin/bash
# Sync local paper files to westd-22162 for compilation
# Usage: bash sync_paper_to_remote.sh

LOCAL_DIR="/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/"
REMOTE_HOST="connect.westd.seetacloud.com"
REMOTE_PORT="22162"
REMOTE_USER="root"
REMOTE_DIR="/root/autodl-tmp/pacs/paper/"

# Decrypt password from resources.yaml
PW=$(cd /home/ubuntu/agent-ml-research && python3 -c "
from core.crypto import decrypt
print(decrypt('gAAAAABqBLojJSfDLeJYnWF7isT8Im1eLJ6VtSur5USVPqzDVrD2F-Kzs6Wuwk8suiwewsjB_KZHrMRcGcH53meaEM7F9g8L1Q=='))
")

sshpass -p "$PW" rsync -avz \
    -e "ssh -p $REMOTE_PORT -o StrictHostKeyChecking=no" \
    --include='*.tex' \
    --include='*.bib' \
    --include='*.sty' \
    --include='*.cls' \
    --include='*.bst' \
    --include='figures/' \
    --include='figures/**' \
    --exclude='*' \
    "$LOCAL_DIR" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}"

echo "Sync complete. To compile on remote:"
echo "  cd ${REMOTE_DIR} && latexmk -pdf main.tex"
