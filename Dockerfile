#FROM mcr.microsoft.com/windows/servercore:ltsc2019
ARG BASE_IMAGE=mcr.microsoft.com/windows/nanoserver:20H2
FROM $BASE_IMAGE

COPY python .
