FROM mcr.microsoft.com/windows/nanoserver:20H2

COPY python .
COPY test_package.py test_package.py
