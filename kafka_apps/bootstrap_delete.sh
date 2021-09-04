#!/bin/bash
# Deploy Producer app
echo "[TASK 1 ] Deploy Producer app"
kubectl delete -f producer/


# Deploy Consumer app
echo -e "\n[TASK 2 ] Deploy Consumer app"
kubectl delete -f consumer/

# Deploy Frontend app
echo -e "\n[TASK 2 ] Create frontent app"
kubectl delete -f front/