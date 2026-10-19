"""Bounded, verified reads of a single S3 object through a presigned URL."""
import hashlib
import io
import time
import urllib.request


class RangedReader(io.RawIOBase):
    def __init__(self, item):
        self.url = item['url']
        self.size = item['metadata']['bytes']
        self.etag = item['metadata']['etag']
        self.offset = 0
        self.buffer = b''
        self.cursor = 0
        self.hash = hashlib.sha256()
        self.md5 = hashlib.md5()
        self.parts = []

    def readable(self):
        return True

    def read(self, n=-1):
        if n < 0:
            n = 16384
        while len(self.buffer) - self.cursor < n and self.offset < self.size:
            end = min(self.size - 1, self.offset + 8 * 1024**2 - 1)
            for attempt in range(5):
                try:
                    request = urllib.request.Request(
                        self.url,
                        headers={'Range': f'bytes={self.offset}-{end}', 'If-Match': self.etag},
                    )
                    with urllib.request.urlopen(request, timeout=120) as response:
                        if response.status != 206:
                            raise IOError('S3 did not honor byte range')
                        data = response.read()
                    if len(data) != end - self.offset + 1:
                        raise IOError('Short S3 range')
                    break
                except Exception:
                    if attempt == 4:
                        raise
                    time.sleep(2)
            self.offset += len(data)
            self.hash.update(data)
            self.md5.update(data)
            self.parts.append(hashlib.md5(data).digest())
            self.buffer = self.buffer[self.cursor:] + data
            self.cursor = 0
        result = self.buffer[self.cursor:self.cursor + n]
        self.cursor += len(result)
        return result

    def finish(self):
        while self.read(8 * 1024**2):
            pass
        expected = self.etag.strip('"')
        if '-' in expected:
            actual = hashlib.md5(b''.join(self.parts)).hexdigest() + '-' + str(len(self.parts))
        else:
            actual = self.md5.hexdigest()
        if actual != expected:
            raise IOError('Source ETag checksum mismatch')
        return self.hash.hexdigest()
