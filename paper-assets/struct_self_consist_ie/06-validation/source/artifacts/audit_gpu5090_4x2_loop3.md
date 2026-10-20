# Audit: gpu-5090-4x-2 Orphan Experiments

**Date**: 2026-05-14
**Server**: gpu-5090-4x-2
**Status**: SERVER UNREACHABLE — not registered in available server list (only autodl-5090, bjb1-21071 available)

## Conclusion

gpu-5090-4x-2 is not accessible via SSH tools. The server was likely released or was never added to the current project's resource configuration. All experiments listed below are confirmed dead.

## PID Status

| exp_id | PID | GPU | Status |
|--------|-----|-----|--------|
| exp_001_n16_seed123_full | 61812 | cuda:0 | **DEAD** (server unreachable) |
| exp_001_n16_seed456_full | 62170 | cuda:1 | **DEAD** (server unreachable) |
| exp001_seed123 | 48530 | cuda:0 | **DEAD** (server unreachable) |
| exp001_seed456 | 50302 | cuda:1 | **DEAD** (server unreachable) |
| exp008_re_n16 | 53600 | cuda:2 | **DEAD** (server unreachable) |
| exp_008_re_n16_full | 62585 | cuda:2 | **DEAD** (server unreachable) |

## Output Check

Unable to inspect output directories — server not accessible.

## Recommendations

1. **Mark all 6 experiments as KILLED** in registry — server is gone, processes cannot be alive
2. **Output data is lost** unless the server can be re-registered or files were synced elsewhere
3. **Remove gpu-5090-4x-2 from registry** as a valid server if it has been permanently released
