#!/bin/bash

echo "📊 상위 CPU 점유 프로세스 확인 중..."
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 10

echo ""
echo "🛑 python/pyinstaller/make/gcc 관련 프로세스 종료 중..."
for PROC in python pyinstaller make gcc; do
    PIDS=$(pgrep -f $PROC)
    for PID in $PIDS; do
        echo "→ 종료: $PROC (PID $PID)"
        kill -9 $PID 2>/dev/null
    done
done

echo ""
echo "✅ 정리 완료. 현재 상위 CPU 프로세스:"
ps -eo pid,cmd,%cpu --sort=-%cpu | head -n 10
