@echo off
git add .
git commit -m "%*"
git pull origin main
git push origin main