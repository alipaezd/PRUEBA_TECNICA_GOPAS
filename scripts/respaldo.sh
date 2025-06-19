#!/bin/bash

FECHA=$(date +"%Y%m%d")
DESTINO="/backups/usuario1_backup_${FECHA}.tar.gz"
tar -czvf "$DESTINO" /home/usuario1
