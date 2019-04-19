import os

ARCH_TYPES = ['amd64', 'arm64', 'armel', 'armhf', 'i386',
              'mips', 'mips64el', 'mipsel', 'ppc64el', 's390x']

MIRROR_DOMAIN = os.environ.get(
    'MIRROR_DOMAIN', 'http://ftp.uk.debian.org/debian/dists/stable/main/')
