#!/bin/bash
# Deploy Producer app
echo "[TASK 1 ] Deploy Producer app"
kubectl apply -f producer/


# Deploy Consumer app
echo -e "\n[TASK 2 ] Deploy Consumer app"
kubectl apply -f consumer/